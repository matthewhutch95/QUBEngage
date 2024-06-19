require 'webrick'
require 'net/http'
require 'json'
require_relative 'RiskOfStudentFailure'

class StudentEngagementServlet < WEBrick::HTTPServlet::AbstractServlet
  def do_GET(request, response)
    begin
      validate_params(request.query)
      lecture = validate_integer_param(request.query['lecture'], 'lecture')
      lab = validate_integer_param(request.query['lab'], 'lab')
      support_sessions = validate_integer_param(request.query['support_sessions'], 'support_sessions')
      canvas_activities = validate_integer_param(request.query['canvas_activities'], 'canvas_activities')
      cutoff = validate_integer_param(request.query['cutoff'], 'cutoff')

      student_engage_url = URI.parse("http://studentengagmentscore.40112152.qpc.hal.davecutting.uk/?lecture=#{lecture}&lab=#{lab}&support_sessions=#{support_sessions}&canvas_activities=#{canvas_activities}")
      returned_response = Net::HTTP.get(student_engage_url)

      json_format = JSON.parse(returned_response)
      total_engagement = json_format['total_engagement']

      validate_integer_result(total_engagement, 'total_engagement')
      validate_integer_result(cutoff, 'cutoff')

      result = RiskOfStudentFailure.check_for_failure((total_engagement * 100), cutoff)
      result_json = { risk_of_student_failure: result }

      response.status = 200
      response.content_type = 'application/json'
      response.body = result_json.to_json

    rescue StandardError => e
      response.status = 400
      response.body = { error: e.message }.to_json
    end
  end

  private

  def set_cors_headers(response)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
  end

  def validate_params(query_params)
    required_params = %w[lecture lab support_sessions canvas_activities cutoff]
    missing_params = required_params - query_params.keys.map(&:to_s)

    raise ArgumentError, "Missing query parameters: #{missing_params.join(', ')}" unless missing_params.empty?
  end

  def validate_integer_param(param, param_name)
    raise ArgumentError, "#{param_name} only integers from 0-9 are to be used" unless param =~ /^\d+$/
    param.to_i
  end

  def validate_integer_result(result, result_name)
    raise ArgumentError, "#{result_name} only integers from 0-9 are to be used" unless result.to_i >= 0
  end
end

server = WEBrick::HTTPServer.new(:Port => 4567)
server.mount('/', StudentEngagementServlet)

trap('INT') { server.shutdown }

server.start

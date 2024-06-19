require 'test-unit'
require 'webrick'
require 'json'
require 'net/http'
require_relative 'RiskOfStudentFailure'

class TestRiskOfStudentFailure < Test::Unit::TestCase
  def test_failure
    assert_equal("Student is not at risk", RiskOfStudentFailure.check_for_failure(50, 40))
    assert_equal("Student is at risk", RiskOfStudentFailure.check_for_failure(30, 50))
  end
end

class TestMainApp < Test::Unit::TestCase
  def test_request
    uri = URI.parse("http://localhost:4567/?cutoff=101&lecture=33&lab=22&support_sessions=44&canvas_activities=55")
    response = Net::HTTP.get_response(uri)
    assert_equal(200, response.code.to_i)
  end
end

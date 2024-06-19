from flask import Flask, request, jsonify
from flask_cors import CORS
from StudentEngagementScore import student_engagement_calc

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def calculate_engagement():
    try:
        lt = request.args.get('lecture')
        lb = request.args.get('lab')
        supp = request.args.get('support_sessions')
        canv = request.args.get('canvas_activities')

        if not all(value.isdigit() for value in [lt, lb, supp, canv]):
            raise ValueError("Invalid input. Please do not leave values blank and only input valid integers 0-9.")

        lt = int(lt)
        lb = int(lb)
        supp = int(supp)
        canv = int(canv)

        result = student_engagement_calc(lt, lb, supp, canv)

        response = {'total_engagement': result}
        return jsonify(response), 200

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

def is_valid_url(url):
    # Basic URL validation to check if it starts with "http://" or "https://"
    return url.startswith("http://") or url.startswith("https://")

@app.route('/info', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    github_file_url = request.args.get('https://github.com/Anthonyogar/HNG-X/blob/main/app.py')
    github_repo_url = request.args.get('https://github.com/Anthonyogar/HNG-X/tree/main')

    # Input validation
    # if not slack_name or not track or not github_file_url or not github_repo_url:
    #     return jsonify({"error": "All query parameters are required."}), 400

    # if not is_valid_url(github_file_url) or not is_valid_url(github_repo_url):
    #     return jsonify({"error": "Invalid GitHub URL format."}), 400

    try:
        current_day = datetime.now(pytz.utc).strftime('%A')
        utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%S')
        status_code = 200

        response_data = {
            'slack_name': slack_name,
            'current_day': current_day,
            'utc_time': utc_time,
            'track': track,
            'github_file_url': 'https://github.com/Anthonyogar/HNG-X/blob/main/app.py',
            'github_repo_url': 'https://github.com/Anthonyogar/HNG-X/tree/main',
            'status_code': status_code
        }

        return jsonify(response_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

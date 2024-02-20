from flask import Flask, render_template, jsonify

app = Flask(__name__)

SKILLS = [
    {
        'skill': 'Python',
        'type': 'Programming Languages',
        'main uses': 'Application development and automation'
    },
    {
        'skill': 'Powershell',
        'type': 'Programming/Scripting Languages',
        'main uses': 'Automation and scripting'
    },
    {
        'skill': 'Microsoft Azure',
        'type': 'Public Cloud Platform',
        'main uses': 'Architecting and infrastructure deployment and management'
    },
    {
        'skill': 'Oracle Cloud Infrastructure',
        'type': 'Public Cloud Platform',
        'main uses': 'Architecting and infrastructure deployment and management'
    },
    {
        'skill': 'Linux',
        'type': 'Operational System',
        'main uses': 'Infrastructure and support operations'
    },
    {
        'skill': 'SQL',
        'type': 'Programming Language',
        'main uses': 'Database operations and scripting'
    }
]

@app.route("/")
def portfolio_website():
    return render_template('home.html')

@app.route("/api/mainSkills")
def main_skills():
    return jsonify(SKILLS)

#Comment the line below when using Gunicorn as WSGI
app.run(host='0.0.0.0', port=5000, debug=True)
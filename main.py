# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_render_template]
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/cloudmyip-project')
def cloudmyipproject():
    return render_template('cloudmyip-project.html')

@app.route('/contactx-project')
def contactxproject():
    return render_template('contactx-project.html')

@app.route('/custom-smart-light-switch-project')
def customsmartlightswitchproject():
    return render_template('custom-smart-light-switch-project.html')

@app.route('/diy-smart-thermostat-project')
def diysmartthermostatproject():
    return render_template('diy-smart-thermostat-project.html')
    
@app.route('/home-automation-project')
def homeautomationproject():
    return render_template('home-automation-project.html')
    
@app.route('/personal-website-project')
def personalwebsiteproject():
    return render_template('personal-website-project.html')
    
@app.route('/projects-grid')
def projectsgridcards():
    return render_template('projects-grid-cards.html')
    
@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python37_render_template]

from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story1

app = Flask(__name__)
app.config['SECRET_KEY'] = "password1"

debug = DebugToolbarExtension(app)

@app.route('/')
def view_homepage():
    '''Show home page with madlib question form'''

    prompts = story1.prompts

    return render_template('home.html', questions = prompts)


@app.route('/story')
def view_story_result():
    '''Show madlib story result'''

    answers = story1.generate(request.args)

    return render_template('story.html', reply = answers)

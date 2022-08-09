from flask import Flask, render_template, request
import stories
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

my_story = None

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    """Select a MadLib or create your own."""
    options = stories.stories

    return render_template('home.html', stories=options)

@app.route('/form')
def form():
    """Fill in your MadLib variables."""
    story_title = request.args.get('my_story')
    global my_story
    my_story = stories.get_story(story_title)

    return render_template('form.html', prompts=my_story.prompts)

@app.route('/story')
def story():
    """Display final MadLib on page!"""
    dictionary = {}
    for prompt in request.args:
        dictionary[f"{prompt}"] = request.args.get(f"{prompt}")
    story_text = my_story.generate(dictionary)

    return render_template('story.html', story=story_text)

@app.route('/submit_story')
def submit_story():
    """This form takes your MadLib story title and your raw Mad lib story text (with {variables})"""
    return render_template('submit_story.html')

@app.route('/create_story', methods=['POST'])
def create_story():
    """creates new Story() instance then redirects user back to home page."""
    title = request.form['title']
    raw_text = request.form['story']

    words = raw_text.split()
    keyword_list = [word[1:-1] for word in words if word.startswith('{') and word.endswith('}')]

    stories.stories.append(stories.Story(title, keyword_list, raw_text))

    return render_template('home.html', stories=stories.stories)
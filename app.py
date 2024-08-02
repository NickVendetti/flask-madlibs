from flask import Flask, render_template, request, redirect, url_for
from stories import story

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        answers = {prompt: request.form[prompt] for prompt in story.prompts}
        return redirect(url_for('show_story', **answers))
    return render_template('form.html', prompts=story.prompts)

@app.route('/story')
def show_story():
    """Show the resulting story."""
    answers = {key: request.args[key] for key in story.prompts}
    generated_story = story.generate(answers)
    return render_template("story.html", story=generated_story)

if __name__ == '__main__':
    app.run(debug=True)
    


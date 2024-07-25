from flask import Flask, request, redirect, render_template, url_for, flash
from forms import URLForm
import string, random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# In-memory storage for URLs
url_mapping = {}

def generate_short_id(num_of_chars: int):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=num_of_chars))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        original_url = form.original_url.data
        short_id = generate_short_id(6)
        while short_id in url_mapping:
            short_id = generate_short_id(6)
        url_mapping[short_id] = original_url
        short_url = url_for('redirect_to_url', short_id=short_id, _external=True)
        return render_template('index.html', form=form, short_url=short_url)
    return render_template('index.html', form=form)

@app.route('/<short_id>')
def redirect_to_url(short_id):
    original_url = url_mapping.get(short_id)
    if original_url:
        return redirect(original_url)
    else:
        flash('Invalid URL')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

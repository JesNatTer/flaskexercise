from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<name>')
def home(name):
    return render_template('homepage.html', name=name)


@app.route('/looping/<int:number>')
def looppage(number):
    return render_template('theloopfile.html', number=number)


@app.route('/image')
def image():
    return render_template('theimage.html')


if __name__ == "__main__":
    app.debug = True
    app.run()

import os 
from google_images_download import google_images_download
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)



def my_function(imgChoose):

    response = google_images_download.googleimagesdownload()
    response.download({ "keywords": imgChoose, "limit": 20})

    dirname = os.path.dirname(os.path.realpath(__file__)) + "\downloads\\" + imgChoose

    i=0

    for name in os.listdir(dirname):

        dst = imgChoose + str(i) + ".jpg"
        src = dirname + '\\' + name
        dst = dirname + '\\'+dst
        
        os.rename(src,dst)
        i+=1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
    return 'finish grabing %s' % name

@app.route('/login',methods = ['POST'])
def login():
    imgChoose = request.form['name']
    my_function(imgChoose)
    #return redirect(url_for('success',name = imgChoose))
    return 'test'

if __name__ == '__main__':
    app.run(debug = True)


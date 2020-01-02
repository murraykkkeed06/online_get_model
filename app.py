import os 
import asyncio
from flask import Flask, render_template, request
from google_images_download import google_images_download
from fastai.vision import *
from fastai.imports import *
import train

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train')
def train():
    os.system('python train.py')

    return render_template('index.html')

@app.route('/name',methods = ['POST'])
def name():

    
    imgChoose = request.args.get('name')

    

    return my_function(imgChoose)

@app.route('/get_num',methods=['POST'])
def get_num():
    choose= request.args.get('name')

    dirname = os.path.dirname(os.path.realpath(__file__)) + "\\static\\downloads\\" + choose
    i=0
    for filename in os.listdir(dirname):
        print(i)
        i+=1

    return str(i)


@app.route('/delete',methods = ['POST'])
def delete():
    choose = request.args.get('name')

    download_dirname = os.path.dirname(os.path.realpath(__file__)) + "\\static\\downloads" 

    dirname = os.path.dirname(os.path.realpath(__file__)) + "\\static\\downloads\\" + choose

    for filename in os.listdir(dirname):
        if filename.endswith('.jpg'):
            os.remove(dirname +"\\" + filename)

   
    os.rmdir(download_dirname+"\\"+choose)

    return "delete done!"



def my_function(imgChoose):

    origin_dirname = os.path.dirname(os.path.realpath(__file__))
    static_dirname = os.path.dirname(os.path.realpath(__file__)) + "\\static" 
    download_dirname = os.path.dirname(os.path.realpath(__file__)) + "\\static\\downloads" 
    img_dirname = os.path.dirname(os.path.realpath(__file__)) + "\\static\\downloads\\" + imgChoose
    

    os.chdir(static_dirname)
    
    try:
        response = google_images_download.googleimagesdownload()
        response.download({"keywords":imgChoose,"limit":3})
    except:
        return "error"

    os.chdir(origin_dirname)
    print(origin_dirname)
    
    
    if len(os.listdir(img_dirname)) == 0:
        return "error"

    path = Path('static\\downloads')
    try:
        for name in os.listdir(download_dirname):
            print(path/name)
            verify_images(path/name, delete=True, max_size=500)
    except:
        return "error"


    try:
        i=0
        
        for name in os.listdir(img_dirname):

            dst = imgChoose + str(i) + ".jpg"
            src = img_dirname + '\\' + name
            dst = img_dirname + '\\'+ dst
            
            os.rename(src,dst)
            i+=1
    except:
        return "error"

    return imgChoose

if __name__ == '__main__':
    app.run(debug = True)
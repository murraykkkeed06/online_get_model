import os 
import asyncio
from flask import Flask, render_template, request
from google_images_download import google_images_download
app = Flask(__name__)

loop = asyncio.get_event_loop()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/name',methods = ['GET'])
def name():

    
    imgChoose = request.args.get('name')

    loop.run_until_complete(my_function(imgChoose))

    return imgChoose


async def my_function(imgChoose):
    
    response = google_images_download.googleimagesdownload()
    response.download({"keywords":imgChoose,"limit":10})
    
    dirname = os.path.dirname(os.path.realpath(__file__)) + "\downloads\\" + imgChoose

    i=0

    for name in os.listdir(dirname):

        dst = imgChoose + str(i) + ".jpg"
        src = dirname + '\\' + name
        dst = dirname + '\\'+ dst
        
        os.rename(src,dst)
        i+=1

if __name__ == '__main__':
    app.run(debug = True)
import os
import numpy as np 
from flask import Flask,request,render_template 
from tensorflow.keras.models import load_model 
from tensorflow.keras.preprocessing import image



app=Flask(__name__)
model=load_model(r'../model/model.h5')

@app.route("/") 
def about():
    return render_template("about.html")

@app.route("/about")
def home():
    return render_template("about.html")

@app.route("/info") 
def information():
    return render_template("info.html")

@app.route("/upload")
def test():
    return render_template("index6.html")

@app.route("/predict",methods=["GET","POST"]) 
def upload():
    if request.method=='POST':
        f=request.files['file'] 
        print(f)
        basepath=os.path.dirname('__file__')
        print(basepath)
        filepath=os.path.join(basepath,"uploads",f.filename)
        f.save(filepath)
        print(filepath)
        
        img=image.load_img(filepath,target_size=(64,64)) 
        x=image.img_to_array(img)
        x=np.expand_dims(x,axis=0)
        pred=model.predict(x)
        print(pred[0][0])
        print("prediction",pred)
        if(pred==0):
            result="Uninfected"
        else:
            result="Infected"
        return result
    return None

if __name__=="__main__":
    app.run(debug=False)
            
            
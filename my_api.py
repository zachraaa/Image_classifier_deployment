from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import time

app = Flask(__name__)

dic = {0 : 'Paper', 1 : 'Rock', 2 : 'Scissors'}

model = load_model('F:\kuliah\semester 7\praktikum pembelajaran mesin\coba\image_classification.h5')

model.make_predict_function()

@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Please subscribe  Artificial Intelligence Hub..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        start_time = time.time()
        img = request.files['my_image']
        img_path = "static/" + img.filename	
        img.save(img_path)
        img_array = image.img_to_array(image.load_img(img_path, target_size=(150, 150))) / 255.0
        img_array = img_array.reshape(1,150,150,3)
        p = model.predict(img_array)
        predicted_class = np.argmax(p)
        prediction = dic[predicted_class]
        confidence = np.round(float(p[0][predicted_class])*100,2)
        end_time = time.time()
        runtime = round(end_time - start_time, 4)
        return render_template("index.html", prediction = prediction,  img_path = img_path, runtime=runtime, confidence=confidence)
    return render_template("index.html", prediction=None, img_path=None, runtime=None, confidence=None)

if __name__ =='__main__':
	app.run(debug = True)
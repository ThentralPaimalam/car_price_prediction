from flask import Flask,render_template,request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load(open('dt_music.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])

def predict():

    prediction = model.predict([[request.form.get('age',type = int),request.form.get('gender', type=int)]])
    # output = prediction[0]

    return render_template('index.html' , prediction_text = f"the genre the person like is {prediction[0]}")

if __name__ == "__main__":
    app.run(debug = True)



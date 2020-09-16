from flask import Flask,render_template,request
import joblib
import pandas as pd

 

app = Flask(__name__)

# from sklearn.externals import joblib
model = joblib.load("finalmodel1.pkl")

@app.route('/',methods = ['GET','POST'])
def pred():
    if request.method == 'POST':
        # try:
            params = request.form


            duration = int(params['duration'])
            color = int(params['color'])
            breed = float(params['breed'])
            x1 = int(params['x1'] )  
            x2 = int(params['x2'])
            condition = int(params['condition'])
            height = int(params['height'])
            length = float(params['width'])


            # length, height = 0, 0
            rdf=pd.DataFrame([[condition,color, length, height,x1, x2,breed,duration]], columns=['f0','f1','f2','f3','f4','f5','f6','f7'])
            result = model.predict(rdf)
            #result = model.predict([[condition,color, length, height,x1, x2,breed,duration]])
            return render_template('result.html',result = result)
        # except:
        #     return render_template('index.html')

    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug = True)
import pandas as pd
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request, template_rendered
from xgboost import XGBRegressor
from sklearn import linear_model
from sklearn import metrics

app=Flask(__name__)

@app.route('/')
def web1():
   return render_template("ind.html")
@app.route('/',methods=['POST'])
def web2():
   m=request.form['name']
   m=int(m)
   c=request.form['b']
   c=int(c)
   k={'AREA':[m],'BHK':[c]}
   df2=pd.DataFrame(k)
   l=request.form['se']
   f=l+".csv"
   
   data=pd.read_csv(f)
   #print(data)
   #print(data.values)
   New={'AREA':data['Area'],'BHK':data['bhk'],'PRICE':data['Price']}
   df1=pd.DataFrame(New)

   #print(df1)
   Y=df1['PRICE']
   X=df1.drop(['PRICE'],axis=1)

   X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2, random_state=2)
   #print(X.shape,X_train.shape,X_test.shape)
   model=XGBRegressor()
   model.fit(X_train,Y_train)
   
   model2=linear_model.LinearRegression()
   model2.fit(X_train,Y_train)
   
   t=model.predict(df2)
   t=int(t)
   # t1=model.predict(X_test)
   # score_2=metrics.r2_score(Y_test,t1)
   # print(score_2)
   
   e=model2.predict(df2)
   e=int(e)
   minim=min(t,e)
   maxim=max(t,e)

   return render_template("web2.html",name=minim,name2=maxim,city=l,d=c,z=m)


if __name__ == '__main__':

   app.run(debug=True,port=5001)


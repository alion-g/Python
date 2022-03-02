import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as mp
import tensorflow as tf
from tensorflow.keras.layers import Dense


dataFrame=pd.read_excel("bisiklet_fiyatlari.xlsx")
y=dataFrame["Fiyat"].values
x=dataFrame[["BisikletOzellik1","BisikletOzellik2"]].values

#Preparing train and test values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=15)

#Scaling

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(x_train)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)

#Adding model and perceptron

model=tf.keras.models.Sequential()
model.add(Dense(5,activation="relu"))
model.add(Dense(5,activation="relu"))
model.add(Dense(5,activation="relu"))
model.add(Dense(1)) #output perceptron
model.compile(optimizer="rmsprop",loss="mse")

#Training

model.fit(x_train,y_train,epochs=250)
loss=model.history.history["loss"]
sbn.lineplot(x=range(len(loss)),y=loss)

train_loss=model.evaluate(x_train,y_train,verbose=0)
test_loss=model.evaluate(x_test,y_test,verbose=0)
print(train_loss,test_loss)

test_predict=model.predict(x_test)
test_predict=pd.Series(test_predict.reshape(330,))
realDf=pd.DataFrame(y_test,columns=["Real"])
predictDf=pd.DataFrame(test_predict,columns=["Predict"])

newDf=pd.concat([realDf,predictDf],axis=1)
print(newDf)

sbn.scatterplot(x="Real",y="Predict",data=newDf)

#if we want to see mean value of error
from sklearn.metrics import mean_absolute_error
meanError=mean_absolute_error(newDf["Real"],newDf["Predict"])
print(meanError)

#Now we can describe new data and compare the solution
print(dataFrame.describe())
newBike=[[1751,1750]]
newBike=scaler.transform(newBike)
value=model.predict(newBike)
print(value)

#Saving Model
from tensorflow.keras.models import load_model
model.save("bikes_model.h5")







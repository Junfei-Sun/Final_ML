import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score#R square
from sklearn.metrics import mean_squared_error #均方误差
from sklearn.metrics import mean_absolute_error #平方绝对误差
import matplotlib.pyplot as plt
import bike_data
#print(bike_data.trainset)
train_x = bike_data.trainset.drop(['cnt'],axis=1)
#print(train_x)
train_y = bike_data.trainset['cnt']
#print(train_y.head())
lr=LinearRegression()
test=lr.fit(train_x,train_y) #训练模型

test_x = bike_data.testset.drop(['cnt'],axis=1)
#print(test_x.head())
print(bike_data.testset)
test_y = bike_data.testset['cnt']
print(test_y)

test_y=test_y.values.tolist()
#回归预测
result=lr.predict(test_x)
result_arr=np.array(result)
print(result)
print(result_arr[0])
print(test_y)
print(test_y[0])
temp=test_y[0]-result_arr[0]
print(temp)
add=0
ad=0


for row in range(146):
    ad=ad+1

    if ((1-(np.abs(test_y[row]-result_arr[row])/test_y[row]))>0.8):
    # if(np.abs(test_y[row]-result_arr[row])<3000):
        add=add+1
accuary=add/ad
print("the accuary is accuacy",accuary)
# score=lr.score(test_x,test_y)
# print(score)
# #线性回归 得到的coef
# axes=plt.subplot(221)
# axes.plot(lr.coef_)
# axes.set_title('lrg_coef')
# plt.show()
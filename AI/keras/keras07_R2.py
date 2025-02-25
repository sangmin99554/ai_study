import numpy as np

#1. 훈련 데이터 
x_train = np.array([1,2,3,4,5,6,7,8,9,10])
y_train = np.array([1,2,3,4,5,6,7,8,9,10])

x_test = np.array([11,12,13,14,15,16,17,18,19,20])
y_test = np.array([11,12,13,14,15,16,17,18,19,20])

x3= np.array([101, 102, 103, 104, 105, 106])
x4= np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
x5= np.array(range(30, 50))
#열이 우선이다 행은 무시된다

#2. 모델 구성
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()


model.add(Dense(30000, input_shape = (1, ), activation ='relu'))
#model.add(Dense(12))
model.add(Dense(4))
model.add(Dense(40))
model.add(Dense(666))
model.add(Dense(55))
model.add(Dense(60))
model.add(Dense(55))
model.add(Dense(10000))
model.add(Dense(55))
model.add(Dense(80))
model.add(Dense(10000))
model.add(Dense(5))
model.add(Dense(1))

#model.summary()
# #model.summary() # param은 dense 가 5와 3일떄는 input weight 5, bias 1, x 3

#3. 훈련
me', optimizer='adam', metrics=['mse'])odel.compile(loss='ms
#model.fit(x, y, epochs=100, batch_size=11)
model.fit(x_train, y_train, epochs=220, batch_size=1)

#4. 평가 예측
# loss, acc = model.evaluate(x_test, y_test, batch_size=3)
# print('acc:', acc)


print(x5)
y_predict = model.predict(x_test)
print(y_predict)

#RMSE 구하기
from sklearn.metrics import mean_squared_error

def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

print("RMSE: ", RMSE(y_test, y_predict))

#R2 구하기
from sklearn.metrics import r2_score

r2_y_predict = r2_score(y_test, y_predict)
print("R2: ", r2_y_predict)

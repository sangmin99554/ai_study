import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical
#데이터 읽어들이기
wine = pd.read_csv("./data/winequality-white.csv", sep=';', encoding='utf-8')

#데이터를 레이블과 데이터로 분리하기
y = wine["quality"]
# x = wine.iloc[:, 0:4]
x = wine.drop(["quality"], axis=1)
y = to_categorical(y)
print(np.argmax(y))
# print(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=66)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

print(x_train)
#학습하기
model = Sequential()
model.add(Dense(512, input_dim=11, activation='relu'))
model.add(Dense(128))
model.add(Dense(64))
model.add(Dense(32))
model.add(Dense(13))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=100, batch_size=64, validation_data=(x_test, y_test))
#평가하기
y_pred = model.predict(x_test)
# print(classification_report(y_test, y_pred))
# print("정답률=", accuracy_score(y_test, y_pred))
# print(aaa)
# print(np.argmax(y_pred))
acc = model.evaluate(x_test, y_test, batch_size=64)
print(acc[1])
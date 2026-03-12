# import lib 
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# read data
train_data = 'module 2 /w5/T4/2cls_spam_text_cls.csv'
df = pd.read_csv(train_data)

# change data to list 
# .values return to numpy array 
messages = df['Message'].values.tolist() 
labels = df['Category'].values.tolist() 

# label data 
# LabelEncoder() dùng để đổi nhãn phân loại từ text -> số 
# fit_transform() để chuyển đổi dữ liệu 
le = LabelEncoder()
y = le.fit_transform(labels)

# pre processing data 
def lower(text) : 
    return text.lower() 

def remove_punctuation(text) : 
    translator = str.maketrans('' , '', string.punctuation)
    return text.translate(translator)

def tokenize(text) : 
    return nltk.word_tokenize(text) 

def remove_stopword(text):
    stop_word = nltk.corpus.stopwords.words('english')
    return [token for token in text if token not in stop_word]

def stemming(text):
    stemmer = nltk.PorterStemmer()
    return [stemmer.stem(token) for token in text ]

def processing_text(text) : 
    text = lower(text) 
    text = remove_punctuation(text)
    tokens = tokenize(text)
    tokens = remove_stopword(tokens)
    tokens = stemming(tokens)
    return tokens 

messages = [processing_text(message) for message in messages]

# create dic 
def dictionary(messages) : 
    dict = []
    for message in messages : 
        for token in message : 
            if token not in dict : 
                dict.append(token)
    return dict 

def create_features(tokens , dict) : 
    features = np.zeros(len(dict))
    for token in tokens : 
        if token in dict : 
            features[dict.index(token)] += 1 
    return features 

dict = dictionary(messages)
X = np.array([create_features(token , dict) for token in messages])

VAL_SIZE = 0.2
TEST_SIZE = 0.125
SEED = 0
# bước 1 : lấy text = 20% 
X_train, X_val, y_train, y_val = train_test_split(X, y,
                                                  test_size=VAL_SIZE,
                                                  shuffle=True,
                                                  random_state=SEED)
# bước 2 : lấy text = 12.5% 
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train,
                                                    test_size=TEST_SIZE,
                                                    shuffle=True,
                                                    random_state=SEED)

model = GaussianNB()
print('Start training...')
model = model.fit(X_train, y_train)
print('Training completed!')                               

y_val_pred = model.predict(X_val)
y_test_pred = model.predict(X_test)
val_accuracy = accuracy_score(y_val, y_val_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)
print(f'Val accuracy: {val_accuracy}')
print(f'Test accuracy: {test_accuracy}')

def predict(text, model, dictionary):
    processed_text = processing_text(text)
    features = create_features(text, dictionary)
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    prediction_cls = le.inverse_transform(prediction)[0]

    return prediction_cls

test_input = 'I am actually thinking a way of doing something useful'
prediction_cls = predict(test_input, model, dictionary)
print(f'Prediction: {prediction_cls}')


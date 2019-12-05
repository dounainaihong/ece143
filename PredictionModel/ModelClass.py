import os
import tensorflow as tf
from tensorflow.keras import layers
from keras.models import load_model

class PredictModel(object):
    
    def __init__(self, input_size, lr=0.01, model_path=None):
        # Initialize the deep learning model.
        self.input_size = input_size
        self.lr = lr
        if not model_path:
            self.model_path = './model'
            self.model = self.InitialModel()
            if not os.path.exists(self.model_path):
                os.mkdir(self.model_path)
        else:
            self.model = load_model(model_path)
        
    def InitialModel(self):
        model = tf.keras.Sequential([
            layers.Dense(256, activation='relu', input_shape=(self.input_size,)),
            layers.Dense(1024, activation='relu'),
            layers.Dense(512, activation='relu'),
            layers.Dense(2, activation='softmax')
        ])
        model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
        return model
    
    def TrainModel(self, train_set, train_label, model_id, sub_epochs=10):
        self.model.fit(train_set, train_label, epochs=sub_epochs,validation_split=0.2)
        model_name = self.model_path+'/model_'+str(model_id)
        self.model.save(model_name)
    
    def Predict(self, input_data):
        return self.model.predict(input_data)
    
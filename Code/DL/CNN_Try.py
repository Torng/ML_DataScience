import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import glob
datas = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test)= datas.load_data()
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="ML", histogram_freq=1)  # 定義TensorBoard物件


x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5,callbacks=tensorboard_callback)
model.evaluate(x_test, y_test, verbose=2)




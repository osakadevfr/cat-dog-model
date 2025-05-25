import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import time

# ----- SETTINGS -----
IMG_SIZE = (128, 128)
BATCH_SIZE = 32
EPOCHS = 10
DATA_DIR = os.getcwd()

# ----- DATA -----
datagen = ImageDataGenerator(
    rescale=1. / 255,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    DATA_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='training',
    classes=['cat', 'dog']
)

val_data = datagen.flow_from_directory(
    DATA_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='validation',
    classes=['cat', 'dog']
)

# ----- MODEL -----
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# ----- TIMER CALLBACK -----
class TimeHistory(tf.keras.callbacks.Callback):
    def on_train_begin(self, logs=None):
        self.epoch_times = []

    def on_epoch_begin(self, epoch, logs=None):
        self.epoch_start = time.time()

    def on_epoch_end(self, epoch, logs=None):
        epoch_duration = time.time() - self.epoch_start
        self.epoch_times.append(epoch_duration)

        avg = sum(self.epoch_times) / len(self.epoch_times)
        remaining = avg * (EPOCHS - (epoch + 1))
        mins, secs = divmod(remaining, 60)
        print(f"⏱️  Estimated time remaining: {int(mins):02d}:{int(secs):02d}")

# ----- TRAIN -----
print("🚀 Training started...\n")
timer_callback = TimeHistory()
model.fit(
    train_data,
    epochs=EPOCHS,
    validation_data=val_data,
    callbacks=[timer_callback]
)

model.save("cat_and_dog_vision.h5")
print("✅ Model done.")

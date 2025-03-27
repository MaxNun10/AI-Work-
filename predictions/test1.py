import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


with open(r"C:\Users\Max\PycharmProjects\predictions", 'r', encoding='utf-8') as file:
    texts = file.readlines()


labels = np.array([1, 0, 1, 0])


if len(texts) != len(labels):

    labels = np.tile(labels, int(np.ceil(len(texts) / len(labels))))[:len(texts)]


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts).toarray()


model = Sequential([
    Dense(64, activation='relu', input_shape=(X.shape[1],)),
    Dense(1, activation='sigmoid')
])


model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


history = model.fit(X, labels, epochs=10, verbose=1)


plt.plot(history.history['loss'])
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.savefig(r'C:\Users\ACER\Desktop\training_loss_plot.png', dpi=300, bbox_inches='tight')
plt.show()
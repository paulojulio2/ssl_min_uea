# -*- coding: utf-8 -*-
"""Com 17 atributos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZBpF-Xedf0ymVSGQsygRIn6dlcvsYwW5
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

# Carregar o dataset
df = pd.read_csv('music_lyrics_dataset.csv')

# 17 atributos originais
X = df[[ 'attr4', 'attr4', 'attr4', 'attr4']]
y = df['genre']

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar e avaliar os modelos de classificação
models = {
    'SVM': SVC(),
    'Random Forest': RandomForestClassifier(),
    'Naive Bayes': GaussianNB()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='macro')
    print(f"{name} - Acurácia: {accuracy:.2f}, Macro-F1: {f1:.2f}")

    # Visualizar a matriz de confusão
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 8))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title(f'Matriz de Confusão - {name}')
    plt.colorbar()
    tick_marks = np.arange(len(df['genre'].unique()))
    plt.xticks(tick_marks, df['genre'].unique(), rotation=90)
    plt.yticks(tick_marks, df['genre'].unique())
    plt.xlabel('Previsto')
    plt.ylabel('Real')
    plt.show()

# Visualizar a distribuição dos gêneros musicais
plt.figure(figsize=(10, 6))
df['genre'].value_counts().plot(kind='bar')
plt.title('Distribuição de Gêneros Musicais')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.show()

# Recomendações
print("Recomendações:")
print("1. Considerar a adição de mais atributos específicos para a classificação de gêneros musicais, como features relacionadas à estrutura musical, instrumentação, entre outros.")
print("2. Explorar técnicas de seleção e engenharia de atributos para identificar as características mais relevantes para a tarefa de classificação.")
print("3. Investigar o uso de modelos de aprendizado de máquina mais avançados, como redes neurais profundas, que podem ter a capacidade de capturar padrões mais complexos nas letras de músicas.")
print("4. Avaliar o impacto da quantidade de dados disponíveis e do balanceamento entre os gêneros na eficácia dos modelos de classificação.")
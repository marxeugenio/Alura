import matplotlib.pyplot as plt
import numpy as np

# Definimos as constantes do pêndulo
g = 9.81
l = 1

# Definimos um array de tempos
t = np.arange(0, 10, 0.01)

# Calculamos a posição do pêndulo em cada instante
x = l * np.sin(t * np.pi)
y = -l * np.cos(t * np.pi)

# Plotamos o movimento do pêndulo
plt.plot(x, y)

# Definimos os rótulos dos eixos
plt.xlabel("x")
plt.ylabel("y")

# Definimos o título do gráfico
plt.title("Movimento de um pêndulo simples")

# Exibe o gráfico
plt.show()

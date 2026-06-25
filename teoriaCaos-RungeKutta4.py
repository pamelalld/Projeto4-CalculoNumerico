import numpy as np
import matplotlib.pyplot as plt
sigma = 10
rho = 28
beta = 8/3
def lorenz(t, state): 
    x, y, z = state 
    dx = sigma * (y - x) 
    dy = x * (rho - z) - y 
    dz = x * y - beta * z 
    return np.array([dx, dy, dz])

def rk4(f, y0, t0, tf, h): 
    n = int((tf - t0) / h) 
    t = np.linspace(t0, tf, n + 1) 
    y = np.zeros((n + 1, len(y0))) 
    y[0] = y0 
    for i in range(n): 
        k1 = f(t[i], y[i])

        k2 = f(
            t[i] + h / 2,
            y[i] + h * k1 / 2
        )

        k3 = f(
            t[i] + h / 2,
            y[i] + h * k2 / 2
        )

        k4 = f(
            t[i] + h,
            y[i] + h * k3
        )

        y[i + 1] = y[i] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t, y

t0 = 0
tf = 40
h = 0.01

t, sol1 = rk4(
    lorenz,
    [1, 1, 1],
    t0,
    tf,
    h
)

t, sol2 = rk4(
    lorenz,
    [1.000001, 1, 1],
    t0,
    tf,
    h
)

# -----------------------------------------------------
# Gráfico 1 - Evolução temporal
# -----------------------------------------------------
plt.figure(figsize=(12, 6))

plt.plot(t, sol1[:, 0], label='x(t)')
plt.plot(t, sol1[:, 1], label='y(t)')
plt.plot(t, sol1[:, 2], label='z(t)')

plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.title('Evolução Temporal do Sistema de Lorenz')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------------------------------
# Gráfico 2 - Atrator de Lorenz
# -----------------------------------------------------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

ax.plot(
    sol1[:, 0],
    sol1[:, 1],
    sol1[:, 2]
)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Atrator de Lorenz')

plt.tight_layout()
plt.show()

# -----------------------------------------------------
# Gráfico 3 - Comparação das trajetórias
# -----------------------------------------------------
plt.figure(figsize=(12, 6))

plt.plot(
    t,
    sol1[:, 0],
    label='x0 = 1'
)

plt.plot(
    t,
    sol2[:, 0],
    '--',
    label='x0 = 1.000001'
)

plt.xlabel('Tempo')
plt.ylabel('x(t)')
plt.title('Sensibilidade às Condições Iniciais')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------------------------------
# Gráfico 4 - Crescimento do erro
# -----------------------------------------------------
erro = np.abs(sol1[:, 0] - sol2[:, 0])

plt.figure(figsize=(10, 5))
plt.semilogy(t, erro)

plt.xlabel('Tempo')
plt.ylabel('|x1 - x2|')
plt.title('Crescimento da Diferença Entre Trajetórias')
plt.grid(True)

plt.tight_layout()
plt.show()

print("\\nSimulação concluída com sucesso!")
print(f"Número de passos: {len(t)}")
print(f"Passo de integração h = {h}")

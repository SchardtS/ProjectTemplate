import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(X, Y):

    Z = X[None,:] + Y[:,None] * 1j

    Z0 = Z.copy()
    iter_counts = np.zeros(Z.shape)

    for k in range(50):
        indices = np.abs(Z) < 1e3
        iter_counts[indices] += 1
        Z[indices] = Z[indices]**2 + Z0[indices]

    return iter_counts, Z

def plot_mandelbrot(X, Y):
   
    iter_counts, Z = mandelbrot(X, Y)

    indices = abs(Z) < 1e3
    iter_counts[indices] = 0

    iter_counts[~indices] = np.log(iter_counts[~indices])

    size_x = 12
    size_y = size_x * (Y[-1] - Y[0])/(X[-1] - X[0])

    plt.figure(figsize=(size_x, size_y))
    plt.imshow(iter_counts, cmap='magma', extent=[X.min(), X.max(), Y.min(), Y.max()])
    
    plt.savefig('Results/Figures/Mandelbrot.png')
    plt.savefig('Results/Figures/Mandelbrot.pdf')

    return

x = np.linspace(-2.4,1.4,2000)
y = np.linspace(-1.2,1.2,1000)

plot_mandelbrot(x, y)
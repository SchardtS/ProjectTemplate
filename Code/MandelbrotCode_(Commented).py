import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(X, Y):
    """
    Computes the Mandelbrot set for a given range of x and y values.

    Parameters
    ----------
    X : numpy.ndarray
        A 1D array of x values.
    Y : numpy.ndarray
        A 1D array of y values.

    Returns
    -------
    T : numpy.ndarray
        A 2D array of iteration counts for each point in the complex plane.
    Z : numpy.ndarray
        A 2D array of final values for each point in the complex plane.
    """
    # Create a 2D array of complex numbers
    Z = X[None,:] + Y[:,None] * 1j

    # Initialize arrays to store iteration counts and initial values
    Z0 = Z.copy()
    iter_counts = np.zeros(Z.shape)

    # Iterate over the complex plane
    for k in range(50):
        # Find indices where the absolute value of Z is less than 1e3
        indices = np.abs(Z) < 1e3
        # Increment the iteration count for points that satisfy the condition
        iter_counts[indices] += 1
        # Update the complex values for points that satisfy the condition
        Z[indices] = Z[indices]**2 + Z0[indices]

    # Return the iteration counts and final values
    return iter_counts, Z

def plot_mandelbrot(X, Y):
    """
    Plots the Mandelbrot set for a given range of x and y values.

    Parameters
    ----------
    X : numpy.ndarray
        A 1D array of x values.
    Y : numpy.ndarray
        A 1D array of y values.

    Returns
    -------
    None
    """
    # Compute the iteration counts and final values for the Mandelbrot set
    iter_counts, Z = mandelbrot(X, Y)

    # Set the iteration counts to 0 for points inside the Mandelbrot set
    indices = abs(Z) < 1e3
    iter_counts[indices] = 0

    # Scale the iteration count with the natural logarithm for points outside the Mandelbrot set
    iter_counts[~indices] = np.log(iter_counts[~indices])

    # Compute the aspect ratio of the plot based on the x and y ranges
    size_x = 12
    size_y = size_x * (Y[-1] - Y[0])/(X[-1] - X[0])

    # Create a plot of the iteration counts
    plt.figure(figsize=(size_x, size_y))
    plt.imshow(iter_counts, cmap='magma', extent=[X.min(), X.max(), Y.min(), Y.max()])
    
    # Save the plot as .png and .pdf files
    plt.savefig('Figures/Mandelbrot.png', facecolor=None)
    plt.savefig('Figures/Mandelbrot.pdf', facecolor=None)

    # Return None
    return

# Create a range of x and y values
x = np.linspace(-2.4,1.4,2000)
y = np.linspace(-1.2,1.2,1000)

# Plot the Mandelbrot set
plot_mandelbrot(x, y)
import numpy
import matplotlib.pyplot

def calculate(A, B):

    C = A[None,:] + B[:,None] * 1j

    C0 = C.copy()
    D = numpy.zeros(C.shape)

    for k in range(50):
        E = numpy.abs(C) < 1e3
        D[E] += 1
        C[E] = C[E]**2 + C0[E]

    return D, C

def plot(A, B):
   
    D, C = calculate(A, B)

    E = abs(C) < 1e3
    D[E] = 0

    D[~E] = numpy.log(D[~E])

    size_x = 12
    size_y = size_x * (B[-1] - B[0])/(A[-1] - A[0])

    matplotlib.pyplot.figure(figsize=(size_x, size_y))
    matplotlib.pyplot.imshow(D, cmap='magma', extent=[A.min(), A.max(), B.min(), B.max()])
    matplotlib.pyplot.show()

    return

p1 = numpy.linspace(-2.4,1.4,2000)
p2 = numpy.linspace(-1.2,1.2,1000)

plot(p1, p2)
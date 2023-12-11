import matplotlib.pyplot as plt
import numpy as np

def generate_sine_wave():
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)

    return x, y

def plot_sine_wave(x, y):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Sine Wave')
    plt.title('Sine Wave Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    x_values, y_values = generate_sine_wave()
    plot_sine_wave(x_values, y_values)

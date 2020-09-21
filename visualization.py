import matplotlib.pyplot as plt
import pandas as pd

def main():
    input = pd.read_csv('random_x.csv', header=None)
    x = input[0].tolist()
    output = pd.read_csv('output_y.csv', header=None)
    y=output[0].tolist()
    plt.plot(x, y)
    plt.grid(True)
    plt.title('y = 3x + 6')
    plt.savefig('plot_x_y.png')
    plt.show()

if __name__ == '__main__':
    main()
    print('plotting graph...')
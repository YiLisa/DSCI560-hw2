import random
import pandas as pd
def main():
    x = []
    for i in range(1000):
        x.append(int(random.random() * 100))
    df = pd.DataFrame(x)
    df.to_csv('random_x.csv', index=False, header=False)
if __name__ == '__main__':
    main()
    print('generating 1000 random numbers...')
import pandas as pd


def main():
    input = pd.read_csv('random_x.csv', header=None)
    x=input[0].tolist()
    y = []
    for n in x:
        y.append(3*int(n)+6)
    df = pd.DataFrame(y)
    df.to_csv('output_y.csv', index=False, header=False)

if __name__ == '__main__':
    main()
    print('generating y = 3x+6...')
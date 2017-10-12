import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("square", type=int, help="dsipkay the sqaure of this number")

    args = parser.parse_args()
    print(args.square**2)


if __name__ == '__main__':
    main()
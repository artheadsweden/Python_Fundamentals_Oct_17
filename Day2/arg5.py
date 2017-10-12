import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("square", type=int, help="display the square of this number")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")

    args = parser.parse_args()
    answer = args.square**2
    if args.verbose:
        print(f"the square of {args.square} equals {answer}")
    else:
        print(answer)


if __name__ == '__main__':
    main()
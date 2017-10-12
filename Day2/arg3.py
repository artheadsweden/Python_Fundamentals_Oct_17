import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("echo", help="String to be echoed back")
    args = parser.parse_args()

    print(args.echo)


if __name__ == '__main__':
    main()
import math
from math import sqrt
from math import sqrt as squareroot
# from math import * - Don't use this kind

def main():
    print(math.sqrt(9)) # Uses import math
    print(sqrt(9)) # Uses from math import sqrt
    print(squareroot(9)) # from math import sqrt as squareroot

if __name__ == '__main__':
    main()
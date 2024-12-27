import sys
import re

def find_degres(s: str) -> int:
    degres = 0
    res = re.findall(r'X\^\d+', s)
    if 'X' in s:
        degres = 1
    if res:
        result = [int(x[2:]) for x in res]
        print(result)
        degres = max(result)
    print (degres)
    return degres


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Bad arg")
        s = sys.argv[1]
        
        degres = find_degres(s)
        print(f'Polynomial degree = {degres}')
        
        if degres > 2:
            print("The polynomial degree is strictly greater than 2, I can't solve")
            return
        elif degres == 0:
            print("degree 0, there is no solution")
            return
    except ValueError as e:
        print(f"ValueError: bad exposant")
    except AssertionError as e:
        print(f"Assertion Error: {e}")


if __name__ == '__main__':
    main()
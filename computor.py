import sys
import re
from reduced import reduced_form

def find_degres(s: str) -> int:
    degres = 0
    res = re.findall(r'X\^\d+', s)
    if 'X' in s:
        degres = 1
    if res:
        result = [int(x[2:]) for x in res]
        degres = max(result)
    return degres

def result_degres_one(s: list[tuple])-> None:
    b = 0
    a = 0
    for coeff, exp in s:
        if exp == 1:
            a = coeff
        elif exp == 0:
            b = coeff * -1
    result = b / a
    print(result)

def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Bad arg")
        s = sys.argv[1].upper()
        degres = find_degres(s)

        new_s = reduced_form(s)
        print(f'Polynomial degree = {degres}')
        
        if degres == 2:
            print("degres2")
            return
        elif degres == 1:
            result_degres_one(new_s)
            return
        elif degres == 0:
            print("degree 0, there is no solution")
            return
        else:
            print("The polynomial degree is strictly greater than 2, I can't solve")
            return

    except ValueError as e:
        print(f"ValueError: bad exposant: {e}")
    except AssertionError as e:
        print(f"Assertion Error: {e}")


if __name__ == '__main__':
    main()
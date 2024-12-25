import sys

def find_degres(s: str) -> int:
    if '.' in s:
        raise AssertionError("Non whole number")
    degres = 0
    for i in range(len(s) -1):
        
        j = i +1
       
        if s[i] == '^' and s[j]:
            if int(s[j]) > degres:
                degres = int(s[j])

    return degres



def main():
    try:
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
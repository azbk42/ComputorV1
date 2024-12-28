import re

def add_sub_same_exp(matches: list[tuple])-> list[tuple]:
    i = 0
    while i < len(matches):
        j = i + 1
        while j < len(matches):
            if matches[i][1] == matches[j][1]:
                new_coeff = matches[i][0] + matches[j][0]
                exp = matches[i][1]
                matches[i] = (new_coeff, exp)
                del matches[j]
            else:
                j += 1
        i += 1

    return matches
    
def right_to_left(part1: list[tuple], part2: list[tuple])-> list[tuple]:
    for x in part2:
        part1.append([x[0]*(-1), x[1]])
    return part1

def print_reduced_form(s: list[tuple])-> None:
    print("reduced form: ", end="")
    first = 1
    for coeff, exp in s:
        if first:
            print(round(coeff), end="")
            first = 0
        else:
            if coeff >= 0:
                print("+ " + str(coeff), end="")
            else:

                print("- " + str(abs(coeff)), end="")
        print(" * X^", end="")
        print(exp, end=" ")
    print("= 0")

def reduced_form(s: str):
    print(s)
    s_plit = s.split("=")

    part1 = re.findall(r'([+-]?\s*\d+\.?\d*)\s*\*\s*X\^(\d+)', s_plit[0])
    part1 = [(coeff.replace(" ", ""), exp) for coeff, exp in part1]
    part1 = [(float(coeff), int(exp)) for coeff, exp in part1]

    part2 = re.findall(r'([+-]?\s*\d+\.?\d*)\s*\*\s*X\^(\d+)', s_plit[1])
    part2 = [(coeff.replace(" ", ""), exp) for coeff, exp in part2]
    part2 = [(float(coeff), int(exp)) for coeff, exp in part2]
    
    reduced = right_to_left(part1, part2)
    reduced = add_sub_same_exp(reduced)

    print_reduced_form(reduced)
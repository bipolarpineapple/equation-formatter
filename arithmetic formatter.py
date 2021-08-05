def arithmetic_arranger():
    problems = []
    answer = []

    def int_validation():
        try:
            first_num = int(input("Enter a number: "))
            other_num = int(input("Enter another number: "))
            return first_num, other_num

        except ValueError:
            print("Error: Numbers must only contain digits.")
            return int_validation()

    first_num, other_num = int_validation()

    ans = ""
    sum1 = ""
    sign = input("+ or - ? ")
    if sign == "+":
        ans = str(int(first_num) + int(other_num))
        sum1 = str(first_num) + " " + sign + " " + str(other_num)
    elif sign == "-":
        ans = str(int(first_num) - int(other_num))
        sum1 = str(first_num) + " " + sign + " " + str(other_num)
    else:
        print("Error: Operator must be '+' or '-'.")

    problems.append(sum1)
    answer.append(ans)

    def convert_vertical():
        first = ""
        second = ""
        lines = ""
        sumx = ""

        for problem in problems:
            first_number = problem.split(" ")[0]
            operator = problem.split(" ")[1]
            second_number = problem.split(" ")[2]

            length = max(len(first_number), len(second_number)) + 2
            top = str(first_number).rjust(length)
            bottom = operator + str(second_number).rjust(length - 1)
            line = ""
            res = str(ans).rjust(length)
            for s in range(length):
                line += "-"

            first += top
            second += bottom
            lines += line
            sumx += res

        print("\n")

        if not answer:
            string = str(first + "\n" + second + "\n" + lines)
        else:
            string = str(first + "\n" + second + "\n" + lines + "\n" + sumx)

        print(string)

    convert_vertical()

    def continue_enter():
        cont = input("\nDo you wish to enter more equations? [Yes/No] ")
        if cont == "Yes":
            arithmetic_arranger()
        elif cont == "No":
            print("Hope to see you soon!")
            exit()
        else:
            print("Invalid input, please try again.")
            arithmetic_arranger()

    continue_enter()


arithmetic_arranger()

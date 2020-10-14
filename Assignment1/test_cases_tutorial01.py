import tutorial01 as A1

actual_answers = [9, 12, 80, 5, -5]
student_answers = []

test_case_1 = A1.add(4, 5)
student_answers.append(test_case_1)

test_case_2 = A1.subtract(14, 2)
student_answers.append(test_case_2)


test_case_3 = A1.multiply(10, 8)
student_answers.append(test_case_3)

test_case_4 = A1.divide(10, 2)
student_answers.append(test_case_4)

test_case_5 = A1.power(-5, 10)
student_answers.append(test_case_5)

# Code for test case checking of GP
a = 10.2
r = 2
n = 5.0

test_case_6 =A1.printGP(a,r,n)
student_answers.append(list(test_case_6))


# Code for test case checking of AP
a = 10
d = 2
n = 7.0

test_case_7 =A1.printAP(a,r,n)
student_answers.append(list(test_case_7))

# Code for test case checking of HP
a = 10
d = 2
n = 7

test_case_7 =A1.printHP(a,r,n)
student_answers.append(list(test_case_7))



print(actual_answers)
print(student_answers)

total_test_cases = len(actual_answers)
count_of_correct_test_cases = 0

for x, y in zip(actual_answers, student_answers):
    if x == y:
        count_of_correct_test_cases += 1

print("Test Cases Passed = 'f{count_of_correct_test_cases}'  / 'f{total_test_cases}'")

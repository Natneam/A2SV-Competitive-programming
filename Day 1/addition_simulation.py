# Calculate a + b

def add(num1, num2):
    # casting the numbers to comfortable format
    strNum1, strNum2 = str(num1), str(num2)
    if len(strNum1) > len(strNum2):
        for i in range(len(strNum1)-len(strNum2)):
            strNum2 = '0' + strNum2
    elif len(strNum2) > len(strNum1):
        for i in range(len(strNum2)-len(strNum1)):
            strNum1 = '0' + strNum1

    carry = 0
    summation = ''
    for i in range(len(strNum1)):
        s = str(int(strNum1[-i-1]) + int(strNum2[-i-1]) + carry)
        # print(s)
        if len(s) == 2:
            carry = int(s[0])
        else:
            carry = 0
        summation = s[-1] + summation
    return summation



# print(add(15075390, 2500758275347))
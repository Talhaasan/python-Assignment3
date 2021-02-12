def decToHex(n):
    hexaDecimalNumber = ['0'] * 50
    i = 0
    try:
        while (int(n) != 0):
            temp = 0
            temp = int(n) % 16
            if (temp < 10):
                hexaDecimalNumber[i] = chr(temp + 48)
                i = i + 1
            else:
                hexaDecimalNumber[i] = chr(temp + 55)
                i = i + 1
            n = int(int(n) / 16)
        j = i - 1
        while (j >= 0):
            print((hexaDecimalNumber[j]), end="")
            j = j - 1
    except ValueError:
        print('The number is not a integer value.')

number = input("Enter a integer value :")
decToHex(number)
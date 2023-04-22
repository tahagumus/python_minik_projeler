import re

print("Hesap Makinesi")
print("Çıkış için 'çıkış' yazınız\n")

previous = 0
run = True


def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Değer Giriniz: ")
    else:
        equation = input(str(previous))

    if equation == 'çıkış':
        print("görüşmek üzere")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]',' ',equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) +  equation)


while run:
    performMath()
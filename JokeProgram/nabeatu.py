from time import sleep

def nabeatu(num):
    if num % 3 == 0 or "3" in str(num):
        return "((●˚⺣˚)<{0}!!".format(num)
    else:
        return "(・∀・)<{0}".format(num)

range_crazy = int(input("いくつまでアホになりたいですか?:"))
for num in range(1, range_crazy + 1):
    print(nabeatu(num))
    sleep(1)

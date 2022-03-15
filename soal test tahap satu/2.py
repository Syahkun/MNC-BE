total_belanja = input()
bayar = input()

arr = [total_belanja, bayar]
arr_res = []
for ex in arr:
    numbers = ex.split(": Rp ")
    numbers = numbers[-1].split(".")
    res = ""
    for numb in numbers:
        res += numb
    res = int(res)
    arr_res.append(res)
    


def moneyChanger(money):
    money = money[1] - money[0]

    if money < 0:
        print("False, kurang bayar")
    else:
        first_money = money
        money = money + 1
        changers = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
        mvp = 0
        arr = []
        for changer in changers:
            while money > changer:
                money = money - changer
                arr.append(changer)
                mvp += changer
        print("Kembalian yang harus diberikan kasir: %s, " % str(f'{first_money:,}').replace(",", "."))
        print("dibulatkan menjadi %s" % str(f'{mvp:,}').replace(",", "."))
        print("")
        print("Pecahan uang: ")

        money_detail = list(dict.fromkeys(arr))
        money_count = []
        for money in money_detail:
            if money == 200 or money == 100:
                print("%s koin %s" % (str(arr.count(money)), str(money)))
            else:
                print("%s lembar %s" % (str(arr.count(money)), str(money)))

    
moneyChanger(arr_res)

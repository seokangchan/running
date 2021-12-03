import tkinter as tk

price_meal = {"김밥": 3000, "라면": 3500,"떡볶이": 5000, "튀김": 4500, "쫄면": 7000}
price_drink = {"아메리카노": 3000, "카페라떼": 3500, "아이스티": 4000, "에이드": 4500, "스무디": 5000}
price_bread = {"마카롱": 3000, "초코조각케이크": 3500, "치즈조각케이크": 4000, "스콘": 4500, "허니브레드": 5000}

order_meal = {}
order_drink = {}
order_bread = {}

order_cash = {}
order_card = {}

total_price = 0

    

def show_meal():
    btn_meal.configure(bg="yellow")
    btn_drink.configure(bg="white")
    btn_bread.configure(bg="white")
    btn_cash.configure(bg="white")
    btn_card.configure(bg="white")
    frame4.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame2.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)

def show_drink():
    btn_meal.configure(bg="white")
    btn_drink.configure(bg="yellow")
    btn_bread.configure(bg="white")
    btn_cash.configure(bg="white")
    btn_card.configure(bg="white")
    frame4.pack_forget()
    frame2.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame3.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)

def show_bread():
    btn_meal.configure(bg="white")
    btn_drink.configure(bg="white")
    btn_bread.configure(bg="yellow")
    btn_cash.configure(bg="white")
    btn_card.configure(bg="white")
    frame4.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)

def show_cash():
    btn_meal.configure(bg="white")
    btn_drink.configure(bg="white")
    btn_cash.configure(bg="blue")
    btn_card.configure(bg="white")
    frame4.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame5.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)
  

def show_card():
    btn_meal.configure(bg="white")
    btn_drink.configure(bg="white")
    btn_cash.configure(bg="white")
    btn_card.configure(bg="blue")
    frame4.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()
    frame7.pack_forget()
    frame6.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)

    

def meal_add(m):
    global total_price, order_meal, order_drink, order_bread
    if m not in price_meal:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_price = price_meal.get(m)
    total_price += this_price

    if m in order_meal:
        order_meal[m] = order_meal.get(m) + 1
    else:
        order_meal[m] = 1
    print_order()
    print_price()

def drink_add(m):
    global total_price, order_meal, order_drink, order_bread
    if m not in price_drink:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_price = price_drink.get(m)
    total_price += this_price

    if m in order_drink:
        order_drink[m] = order_drink.get(m) + 1
    else:
        order_drink[m] = 1
    print_order()
    print_price()

def bread_add(m):
    global total_price, order_meal, order_drink, order_bread

    if m not in price_bread:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_price = price_bread.get(m)
    total_price += this_price

    if m in order_bread:
        order_bread[m] = order_bread.get(m) + 1
    else:
        order_bread[m] = 1
    print_order()
    print_price()
    
    


def print_order():
    global order_meal, order_drink, order_bread

    tmp = ""
    for i in order_meal:
        tmp = tmp + i + " x " + str(order_meal.get(i)) + "\n"
    for i in order_drink:
        tmp = tmp + i + " x " + str(order_drink.get(i)) + "\n"
    for i in order_bread:
        tmp = tmp + i + " x " + str(order_bread.get(i)) + "\n"

    text_1.delete('1.0', tk.END)
    text_1.insert(tk.INSERT, tmp)

def order_end():
    global total_price, order_meal, order_drink, order_bread
    print('결제가 완료되었습니다.')

    total_price = 0
    del order_meal
    del order_drink
    del order_bread

    order_meal = {}
    order_drink = {}
    order_bread = {}
    print_price()
    print_order()
    show_meal()
    

def print_price():
    global total_price
    label_price.configure(text=str(total_price) + " 원 ")





window = tk.Tk()
window.title("주문 프로그램")
window.geometry("1000x600+1000+300")
window.resizable(False, False)

frame1 = tk.Frame(window, width="600", height="10")
frame1.pack(fill="both")

frame2 = tk.Frame(window, width="600")
frame2.pack(fill="both", expand=True)

frame3 = tk.Frame(window, width="600")
# frame3.pack(fill="both", expand=True)

frame4 = tk.Frame(window, width="600", height="10")
frame4.pack(fill="both", expand=True)

frame5 = tk.Frame(window, width="600")
frame5.pack(fill="both", expand=True)

frame6 = tk.Frame(window, width="600")
frame6.pack(fill="both", expand=True)

frame7 = tk.Frame(window, width="600")
frame7.pack(fill="both", expand=True)


btn_meal = tk.Button(frame1, text="식사", padx="10", pady="10", bg="yellow", command=show_meal)
btn_meal.grid(row=0, column=0, padx=10, pady=10)

btn_drink = tk.Button(frame1, text="음료", padx="10", pady="10", bg="white", command=show_drink)
btn_drink.grid(row=0, column=1, padx=10, pady=10)

btn_bread = tk.Button(frame1, text="빵", padx="10", pady="10", bg="white", command=show_bread)
btn_bread.grid(row=0, column=2, padx=10, pady=10)

btn_end = tk.Button(frame1, text="주문종료", padx="10", pady="10", bg="white", command=order_end)
btn_end.grid(row=0, column=3, padx=10, pady=10)

btn_cash = tk.Button(frame1, text="현금", padx="10", pady="10", bg="white", command=show_cash)
btn_cash.grid(row=4, column=0, padx=10, pady=10)

btn_card = tk.Button(frame1, text="카드", padx="10", pady="10", bg="white", command=show_card)
btn_card.grid(row=4, column=1, padx=10, pady=10)



label_price = tk.Button(frame1, text="0 원", width="20", padx="10", pady="10", fg="blue", font= 'Arial 15')
label_price.grid(row=0, column="4", padx="10", pady="10")


#식사
btn_meal_1 = tk.Button(frame2, text="김밥\n(3000원)", padx="10", pady="10", width="10", command=lambda: meal_add('김밥'))
btn_meal_1.grid(row=0, column=0, padx=10, pady=10)

btn_meal_2 = tk.Button(frame2, text="라면\n(3500원)", padx="10", pady="10", width="10", command=lambda: meal_add('라면'))
btn_meal_2.grid(row=0, column=1, padx=10, pady=10)

btn_meal_3 = tk.Button(frame2, text="떡볶이\n(5000원)", padx="10", pady="10", width="10", command=lambda: meal_add('떡볶이'))
btn_meal_3.grid(row=0, column=2, padx=10, pady=10)

btn_meal_4 = tk.Button(frame2, text="튀김\n(4500원)", padx="10", pady="10", width="10", command=lambda: meal_add('튀김'))
btn_meal_4.grid(row=0, column=3, padx=10, pady=10)

btn_meal_5 = tk.Button(frame2, text="쫄면\n(7000원)", padx="10", pady="10", width="10", command=lambda: meal_add('쫄면'))
btn_meal_5.grid(row=0, column=4, padx=10, pady=10)


#음료
btn_drink_1 = tk.Button(frame3, text="아메리카노\n(3000원)", padx="10", pady="10", width="10", command=lambda: drink_add('아메리카노'))
btn_drink_1.grid(row=0, column=0, padx=10, pady=10)

btn_drink_2 = tk.Button(frame3, text="카페라떼\n(3500원)", padx="10", pady="10", width="10", command=lambda: drink_add('카페라떼'))
btn_drink_2.grid(row=0, column=1, padx=10, pady=10)

btn_drink_3 = tk.Button(frame3, text="아이스티\n(4000원)", padx="10", pady="10", width="10", command=lambda: drink_add('아이스티'))
btn_drink_3.grid(row=0, column=2, padx=10, pady=10)

btn_drink_4 = tk.Button(frame3, text="에이드\n(4500원)", padx="10", pady="10", width="10", command=lambda: drink_add('에이드'))
btn_drink_4.grid(row=0, column=3, padx=10, pady=10)

btn_drink_5 = tk.Button(frame3, text="스무디\n(5000원)", padx="10", pady="10", width="10", command=lambda: drink_add('스무디'))
btn_drink_5.grid(row=0, column=4, padx=10, pady=10)

#빵
btn_bread_1 = tk.Button(frame7, text="마카롱\n(3000원)", padx="10", pady="10", width="10", command=lambda: bread_add('마카롱'))
btn_bread_1.grid(row=0, column=0, padx=10, pady=10)

btn_bread_2 = tk.Button(frame7, text="초코조각케이크\n(3500원)", padx="10", pady="10", width="10", command=lambda: bread_add('초코조각케이크'))
btn_bread_2.grid(row=0, column=1, padx=10, pady=10)

btn_bread_3 = tk.Button(frame7, text="치즈조각케이크\n(4000원)", padx="10", pady="10", width="10", command=lambda: bread_add('치즈조각케이크'))
btn_bread_3.grid(row=0, column=2, padx=10, pady=10)

btn_bread_4 = tk.Button(frame7, text="스콘\n(4500원)", padx="10", pady="10", width="10", command=lambda: bread_add('스콘'))
btn_bread_4.grid(row=0, column=3, padx=10, pady=10)

btn_bread_5 = tk.Button(frame7, text="허니브레드\n(5000원)", padx="10", pady="10", width="10", command=lambda: bread_add('허니브레드'))
btn_bread_5.grid(row=0, column=4, padx=10, pady=10)

#현금 
btn_cash_1 = tk.Button(frame5, text="현금을 넣어 주세요 ", padx="20", pady="20", width="20",command=lambda: text_1.insert(1.0, "--------결제가 완료되었습니다.--------\n"))
btn_cash_1.grid(row=0, column=3, padx=10, pady=10)

#카드
btn_card_1 = tk.Button(frame6, text="카드를 넣어 주세요 ", padx="20", pady="20", width="20", command=lambda: text_1.insert(1.0, "--------결제가 완료되었습니다.--------\n"))
btn_card_1.grid(row=0, column=3, padx=10, pady=10)

#주문 리스트
text_1 = tk.Text(frame4, height="10")
text_1.pack()

window.mainloop()















        

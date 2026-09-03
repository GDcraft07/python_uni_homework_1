from fraction import *
from tkinter import *


def calculations(fraction_1: Fraction, fraction_2: Fraction, sign: str):
    result = None
    if sign == "+":
        result = fraction_1.sumFractions(fraction_2)

    elif sign == "-":
        result = fraction_1.subFractions(fraction_2)

    elif sign == "*":
        result = fraction_1.multiFractions(fraction_2)

    elif sign == "/":
        result = fraction_1.divFractions(fraction_2)

    else:
        raise ValueError("Неправильно введен знак!")

    if result:
        return result.getInfo()


def main():
    root = Tk()
    root.title("Калькулятор дробей")
    root.geometry("400x300")

    for c in range(3): root.columnconfigure(index=c, weight=1)
    for r in range(3): root.rowconfigure(index=r, weight=1)

    entry_numerator_1 = Entry(root)
    entry_numerator_1.grid(row=0, column=0, padx=10)
    
    entry_denominator_1 = Entry(root)
    entry_denominator_1.grid(row=1, column=0, padx=10)

    entry_numerator_2 = Entry(root)
    entry_numerator_2.grid(row=0, column=2, padx=10)

    entry_denominator_2 = Entry(root)
    entry_denominator_2.grid(row=1, column=2, padx=10)

    frame_radiobutton = Frame(root)
    frame_radiobutton.grid(row=0, column=1, rowspan=2)

    sign = StringVar(value="+")

    radio_sum = Radiobutton(frame_radiobutton, text="+", variable=sign, value="+")
    radio_sub = Radiobutton(frame_radiobutton, text="-", variable=sign, value="-")
    radio_multi = Radiobutton(frame_radiobutton, text="*", variable=sign, value="*")
    radio_div = Radiobutton(frame_radiobutton, text="/", variable=sign, value="/")

    radio_sum.grid(row=0, column=0)
    radio_sub.grid(row=1, column=0)
    radio_multi.grid(row=0, column=1)
    radio_div.grid(row=1, column=1)


    def doCalculations():
        try:
            result = calculations(Fraction(entry_numerator_1.get(), entry_denominator_1.get()), Fraction(entry_numerator_2.get(), entry_denominator_2.get()), sign.get())
            result = f"{result[0]}/{result[1]}"

            answer_window = Toplevel(root)
            answer_window.title("ОТВЕТ")
            answer_window.geometry(f"{30 * len(result)}x100")
            answer_window.columnconfigure(0, weight=1)
            answer_window.rowconfigure(0, weight=1)

            result_label = Label(answer_window, text=result, font=("Arial", 30))
            result_label.grid(row=0, column=0)


        except Exception as e:
            error = f"{e}"

            error_window = Toplevel(root)
            error_window.title("ОШИБКА")
            error_window.geometry(f"{30 * len(error)}x100")
            error_window.columnconfigure(0, weight=1)
            error_window.rowconfigure(0, weight=1)

            error_label = Label(error_window, text=error, font=("Arial", 30))
            error_label.grid(row=0, column=0)

        
        entry_list = [entry_numerator_1, entry_numerator_2, entry_denominator_1, entry_denominator_2]
        
        for i in entry_list:
            i.delete(0, END)


    button_submit = Button(root, text="SUBMIT", command=doCalculations)
    button_submit.grid(row=2, column=0, columnspan=3, ipadx=70, ipady=7, padx=1, pady=1)
    
    root.mainloop()


if __name__ == "__main__":
    main()


# def step():
#     numerator_1 = input("Введите числитель первого числа: ")
#     denominator_1 = input("Введите знаменатель первого числа: ")
#     fraction_1 = Fraction(numerator_1, denominator_1)

#     numerator_2 = input("Введите числитель второго числа: ")
#     denominator_2 = input("Введите знаменатель второго числа: ")
#     fraction_2 = Fraction(numerator_2, denominator_2)

#     sign = input("Введите операцию: ")

#     result = None

#     if sign == "+":
#         result = fraction_1.sumFractions(fraction_2)

#     elif sign == "-":
#         result = fraction_1.subFractions(fraction_2)

#     elif sign == "*":
#         result = fraction_1.multiFractions(fraction_2)

#     elif sign == "/":
#         result = fraction_1.divFractions(fraction_2)

#     else:
#         print("Введен неправильный символ операции.")

#     if result:
#         print(result)


# if __name__ == "__main__":
#     step()

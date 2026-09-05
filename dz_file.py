from tkinter import *


def gcd(number_1: int, number_2: int):
    while number_2:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1 if number_1 >= 0 else -number_1


is_digits = lambda str_number: str_number not in ["", "-"] and all(map(lambda x: x.isdigit(), list(str_number if str_number[0] != "-" else str_number[1:])))


def calculations(fraction_1: tuple[str, str], fraction_2: tuple[str, str], sign: str):    
    if (not is_digits(fraction_1[0])) or (not is_digits(fraction_1[1])) or (not is_digits(fraction_2[0])) or (not is_digits(fraction_2[1])):
        raise TypeError("Введите в полях числителей и знаменатилей целые числа!")

    fraction_1 = (int(fraction_1[0]), int(fraction_1[1]) * (-1 if fraction_1[1][0] == "-" else 1))
    fraction_2 = (int(fraction_2[0]), int(fraction_2[1]) * (-1 if fraction_2[1][0] == "-" else 1))

    if fraction_1[1] == 0 or fraction_2[1] == 0 or (sign == "/" and fraction_2[0] == 0):
        raise ZeroDivisionError("На ноль делить нельзя!")
    
    result = None
    if sign == "+":
        result = (fraction_1[0] * fraction_2[1] + fraction_2[0] * fraction_1[1], fraction_1[1] * fraction_2[1])

    elif sign == "-":
        result = (fraction_1[0] * fraction_2[1] - fraction_2[0] * fraction_1[1], fraction_1[1] * fraction_2[1])

    elif sign == "*":
        result = (fraction_1[0] * fraction_2[0], fraction_1[1] * fraction_2[1]) 

    elif sign == "/":
        if fraction_2[0] < 0:
            fraction_2 = (-fraction_2[0], -fraction_2[1])
            
        result = (fraction_1[0] * fraction_2[1], fraction_1[1] * fraction_2[0])

    fraction_gcd = gcd(result[0], result[1])

    return (result[0] // fraction_gcd, result[1] // fraction_gcd)


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
            result = calculations((entry_numerator_1.get(), entry_denominator_1.get()), (entry_numerator_2.get(), entry_denominator_2.get()), sign.get())
            result = f"{result[0]}/{result[1]}"

            answer_window = Toplevel(root)
            answer_window.title("ОТВЕТ")
            answer_window.geometry(f"{30 * len(result)}x100")
            answer_window.columnconfigure(0, weight=1)
            answer_window.rowconfigure(0, weight=1)

            result_label = Label(answer_window, text=result, font=("Arial", 30))
            result_label.grid(row=0, column=0)

            answer_window.grab_set()


        except Exception as e:
            error = f"{e}"

            error_window = Toplevel(root)
            error_window.title("ОШИБКА")
            error_window.geometry(f"{30 * len(error)}x100")
            error_window.columnconfigure(0, weight=1)
            error_window.rowconfigure(0, weight=1)

            error_label = Label(error_window, text=error, font=("Arial", 30))
            error_label.grid(row=0, column=0)

            error_window.grab_set()

        
        entry_list = [entry_numerator_1, entry_numerator_2, entry_denominator_1, entry_denominator_2]
        
        for i in entry_list:
            i.delete(0, END)


    button_submit = Button(root, text="SUBMIT", command=doCalculations)
    button_submit.grid(row=2, column=0, columnspan=3, ipadx=70, ipady=7, padx=1, pady=1)
    
    root.mainloop()


if __name__ == "__main__":
    main()
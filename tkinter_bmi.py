from tkinter import *

def nhap_du_lieu(entry):
    try:
        number = float(entry.get())
        if number > 0:
            return number
        else:
            return 0
    except ValueError:
        warning.config(text="THÔNG BÁO: SAI DỮ LIỆU ĐẦU VÀO")
        return 0

def interpretation(number):
    if number > 40:
        return "Béo phì cấp độ III"
    elif number >= 35:
        return "Béo phì cấp độ II"
    elif number >= 30:
        return "Béo phì cấp độ I"
    elif number >= 25:
        return "Thừa cân"
    elif number >= 18.5:
        return "Bình thường"
    elif number >= 17:
        return "Gầy cấp độ I"
    elif number >= 16:
        return "Gầy cấp độ II"
    else:
        return "Gầy cấp độ III"

def cal_bmi():
    weight = nhap_du_lieu(can_nang)
    height = nhap_du_lieu(chieu_cao)
    if weight * height == 0:
        warning.config(text= f"THÔNG BÁO: SAI DỮ LIỆU ĐẦU VÀO")
    else:
        result = weight / height ** 2
        bmi_result.config(text = f"Kết quả:   {result:.2f}")
        text = interpretation(result).upper()
        warning.config(text= f"THÔNG BÁO:   {text}")

window = Tk()
window.geometry("250x200")          # khung cửa sổ
window.title("BMI Calculation")      # tiêu đề của cửa sổ
window.config(background="light cyan")

# Tạo nhãn và entry cân nặng
can_nang = Entry(window)
can_nang.insert(0, "66")
can_nang.place(x = 100, y = 25)

Label(window,
      text = "Cân nặng (kg): ",
      font = ("Calibri", 11),
      bg = "light cyan").place(x = 5, y = 25)

# Tạo nhãn và entry chiều cao
chieu_cao = Entry(window)
chieu_cao.insert(0, "1.69")
chieu_cao.place(x = 100, y = 50)

Label(window,
      text = "Chiều cao (m): ",
      font = ("Calibri", 11),
      bg = "light cyan").place(x = 5, y = 50)

# Tạo nhãn thông báo điều kiện dữ liệu đầu vào và trả kết quả giải đoán
warning = Label(window,
                text = "THÔNG BÁO: ",
                font = ("Calibri", 11, "bold"),
                bg = "light cyan",
                fg = "red")
warning.place(x = 5, y = 130)

# Tạo nhãn kết quả tính toán giá trị BMI
bmi_result = Label(window,
                text = "Kết quả:   0",
                font = ("Calibri", 11),
                bg = "light cyan")
bmi_result.place(x = 85, y = 110)

# Tạo nút bấm BMI Calculate
Button(window,
       text = "BMI Calculate",
       command = cal_bmi).place(x = 85, y = 80)

window.mainloop()
from currency_converter import CurrencyConverter
import customtkinter as ct
import tkinter as tk


def button_function():
    amount = float(amountEntry.get())
    currency_from = str(currencyCombobox.get())
    currency_too = str(currencyCombobox2.get())
    c = CurrencyConverter()
    text_var.set(c.convert(amount, currency_from, currency_too))


ct.set_appearance_mode("system")  # Can be set light, dark, system
ct.set_default_color_theme("blue")

app = ct.CTk()  # Window name and size
app.title("Currency Converter")
app.geometry("700x500")
app.iconbitmap("currency.ico")

frame = ct.CTkFrame(master=app, width=700, height=500, corner_radius=10, bg_color="silver",
                    fg_color="grey")  # frame created
frame.pack(padx=20, pady=20, fill="both", expand=True)

label1 = ct.CTkLabel(master=frame, text="Enter the Amount to be Converted", font=("Roboto", 18))
label1.pack(pady=10, padx=10)

amountEntry = ct.CTkEntry(master=frame, placeholder_text="Amount", width=150, height=35, border_width=2,
                          corner_radius=8)
amountEntry.pack(padx=10, pady=2)

label2 = ct.CTkLabel(master=frame, text="Select the currency", font=("Roboto", 18))
label2.pack(pady=1, padx=10)

currencyCombobox = ct.CTkComboBox(master=frame,
                                  values=["USD", "JPY", "BGN", "CYP", "CZK", "DKK", "EEK", "GBP", "HUF", "LTL", "LVL",
                                          "MTL", "PLN", "ROL", "RON", "SEK", "SIT", "SKK", "CHF", "ISK", "NOK", "HRK",
                                          "RUB", "TRL", "TRY", "AUD", "BRL", "CAD", "CNY", "HKD", "IDR", "ILS", "INR",
                                          "KRW", "MXN", "MYR", "NZD", "PHP", "SGD", "THB", "ZAR"], )
currencyCombobox.pack(pady=1, padx=10)

label3 = ct.CTkLabel(master=frame, text="Desired currency", font=("Roboto", 18))
label3.pack(pady=10, padx=10)

currencyCombobox2 = ct.CTkComboBox(master=frame,
                                   values=["USD", "JPY", "BGN", "CYP", "CZK", "DKK", "EEK", "GBP", "HUF", "LTL", "LVL",
                                           "MTL", "PLN", "ROL", "RON", "SEK", "SIT", "SKK", "CHF", "ISK", "NOK", "HRK",
                                           "RUB", "TRL", "TRY", "AUD", "BRL", "CAD", "CNY", "HKD", "IDR", "ILS", "INR",
                                           "KRW", "MXN", "MYR", "NZD", "PHP", "SGD", "THB", "ZAR"], )
currencyCombobox2.pack(pady=10, padx=10)

convertButton = ct.CTkButton(master=frame, text="Convert", command=button_function, width=250, height=35,
                             corner_radius=10, hover_color="grey", font=("Roboto", 18))  # convert button
convertButton.pack(pady=10, padx=10)

text_var = tk.StringVar()

label4 = ct.CTkLabel(master=frame, textvariable=text_var, font=("Roboto", 18))
label4.pack(pady=10, padx=10)

label5 = ct.CTkLabel(master=frame, text=" ", font=("Roboto", 4))
label5.pack(pady=10, padx=10)


label7 = ct.CTkLabel(master=frame, text="By- Amitesh Singh", font=("Roboto",8,))
label7.pack(pady=10, padx=10)
app.mainloop()

import tkinter as tk
from tkinter import messagebox

# Currency Conversion Function with predefined exchange rates
def currency_converter(frc, fva, trc):
    # Exchange rates (from one currency to another)
    exchange_rates = {
        "USD-JPY": 153.01, "EUR-JPY": 165.77, "HKD-JPY": 19.6716, "USD-HKD": 7.7772,
        "USD-SGD": 1.3261, "AUD-JPY": 100.35, "AUD-USD": 0.6559, "NZD-USD": 0.5963,
        "USD-TWD": 31.93, "USD-KRW": 1378.21, "USD-PHP": 58.409, "USD-IDR": 15732.00,
        "USD-INR": 84.085, "USD-CNY": 7.1283, "USD-MYR": 4.3807, "USD-THB": 33.965,
        "JPY-MYR": 2.8634
    }
    
    try:
        # If currencies are the same, return the same value
        if frc == trc:
            return fva
        
        # Prepare the currency pair for conversion
        currency_pair = f"{frc}-{trc}"
        
        if currency_pair in exchange_rates:
            rate = exchange_rates[currency_pair]
            converted_value = fva * rate
            return round(converted_value, 2)
        else:
            # Reverse the currency pair if the conversion direction is not found
            reverse_pair = f"{trc}-{frc}"
            if reverse_pair in exchange_rates:
                rate = 1 / exchange_rates[reverse_pair]  # Reverse the rate for inverse conversion
                converted_value = fva * rate
                return round(converted_value, 2)
            else:
                return None
    except KeyError:
        return None

# Function for Currency Conversion
def convert_currency():
    from_currency = from_currency_var.get().strip().upper()
    amount = amount_entry.get().strip()
    to_currency = to_currency_var.get().strip().upper()

    try:
        amount_value = float(amount)
        converted_amount = currency_converter(from_currency, amount_value, to_currency)
        
        if converted_amount is not None:
            result_label.config(text=f"Converted Amount: {converted_amount} {to_currency}")
        else:
            messagebox.showerror("Error", f"Conversion from {from_currency} to {to_currency} is not available.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the amount.")

# Number System Conversion Function
def convert_number_system():
    num_value = entry_value.get().strip()
    from_base = from_base_var.get()
    to_base = to_base_var.get()
    
    try:
        if from_base == "Binary":
            decimal_value = int(num_value, 2)
        elif from_base == "Octal":
            decimal_value = int(num_value, 8)
        elif from_base == "Decimal":
            decimal_value = int(num_value)
        elif from_base == "Hexadecimal":
            decimal_value = int(num_value, 16)
        
        if to_base == "Binary":
            result_value = bin(decimal_value)[2:]
        elif to_base == "Octal":
            result_value = oct(decimal_value)[2:]
        elif to_base == "Decimal":
            result_value = str(decimal_value)
        elif to_base == "Hexadecimal":
            result_value = hex(decimal_value)[2:].upper()
        
        result_label.config(text=f"Converted Value: {result_value}")
    except ValueError:
        messagebox.showerror("Error", "Invalid number or base selected. Please try again.")

# Unit Conversion Function
length_conversion_factors = {
    "mm": 0.001, "cm": 0.01, "dm": 0.1, "dam": 10, "hm": 100, "km": 1000,
    "inch": 0.0254, "foot": 0.3048, "mile": 1609.344
}
        
def unit_converter(quantity_type, from_unit, value, to_unit):
    if quantity_type == "Length":
        conversion_factors = length_conversion_factors
    else:
        return None  # Invalid quantity type
    
    try:
        value_in_base = value * conversion_factors[from_unit]
        reverse_conversion_factor = 1 / conversion_factors[to_unit]
        result = value_in_base * reverse_conversion_factor
        return round(result, 4)
    except KeyError:
        return None

def on_convert_button_click():
    quantity_type = quantity_type_var.get().strip()
    from_unit = from_unit_var.get().strip().lower()
    to_unit = to_unit_var.get().strip().lower()
    value = value_entry.get().strip()
    
    try:
        value = float(value)
        if quantity_type == "Temperature":
            converted_value = temperature_converter(from_unit, value, to_unit)
        else:
            converted_value = unit_converter(quantity_type, from_unit, value, to_unit)
        
        if converted_value is not None:
            result_label.config(text=f"Converted Value: {converted_value} {to_unit.capitalize()}")
        else:
            messagebox.showerror("Error", f"Invalid unit: {from_unit} or {to_unit} for {quantity_type}.")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the value.")

# Main Application Window
root = tk.Tk()
root.title("Multi Converter")

# Available converter types
converter_types = ["Currency Converter", "Number System Converter", "Unit Converter"]

# Function to switch between converters
def select_converter(*args):
    selected_converter = converter_var.get()
    
    # Hide all widgets and show only the selected converter
    if selected_converter == "Currency Converter":
        currency_converter_frame.grid(row=1, column=0, padx=10, pady=10)
        number_system_converter_frame.grid_forget()
        unit_converter_frame.grid_forget()
    elif selected_converter == "Number System Converter":
        number_system_converter_frame.grid(row=1, column=0, padx=10, pady=10)
        currency_converter_frame.grid_forget()
        unit_converter_frame.grid_forget()
    elif selected_converter == "Unit Converter":
        unit_converter_frame.grid(row=1, column=0, padx=10, pady=10)
        currency_converter_frame.grid_forget()
        number_system_converter_frame.grid_forget()

# Drop down menu for selecting converter
converter_var = tk.StringVar(root)
converter_var.set(converter_types[0])  # Default selection
converter_menu = tk.OptionMenu(root, converter_var, *converter_types, command=select_converter)
converter_menu.grid(row=0, column=0, padx=10, pady=10)

# Currency Converter Frame
currency_converter_frame = tk.Frame(root)

tk.Label(currency_converter_frame, text="From Currency:").grid(row=0, column=0, padx=10, pady=10)
from_currency_var = tk.StringVar(currency_converter_frame)
from_currency_var.set("USD")
from_currency_menu = tk.OptionMenu(currency_converter_frame, from_currency_var, *["USD", "EUR", "HKD", "JPY", "AUD", "NZD", "TWD", "KRW", "PHP", "IDR", "INR", "CNY", "MYR", "THB", "SGD"])
from_currency_menu.grid(row=0, column=1, padx=10, pady=10)

tk.Label(currency_converter_frame, text="Amount to Convert:").grid(row=1, column=0, padx=10, pady=10)
amount_entry = tk.Entry(currency_converter_frame)
amount_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(currency_converter_frame, text="To Currency:").grid(row=2, column=0, padx=10, pady=10)
to_currency_var = tk.StringVar(currency_converter_frame)
to_currency_var.set("JPY")
to_currency_menu = tk.OptionMenu(currency_converter_frame, to_currency_var, *["USD", "EUR", "HKD", "JPY", "AUD", "NZD", "TWD", "KRW", "PHP", "IDR", "INR", "CNY", "MYR", "THB", "SGD"])
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

convert_currency_button = tk.Button(currency_converter_frame, text="Convert", command=convert_currency)
convert_currency_button.grid(row=3, column=0, columnspan=2, pady=10)

# Number System Converter Frame
number_system_converter_frame = tk.Frame(root)

tk.Label(number_system_converter_frame, text="From Base:").grid(row=0, column=0, padx=10, pady=10)
from_base_var = tk.StringVar(number_system_converter_frame)
from_base_var.set("Decimal")
from_base_menu = tk.OptionMenu(number_system_converter_frame, from_base_var, "Binary", "Octal", "Decimal", "Hexadecimal")
from_base_menu.grid(row=0, column=1, padx=10, pady=10)

tk.Label(number_system_converter_frame, text="Number to Convert:").grid(row=1, column=0, padx=10, pady=10)
entry_value = tk.Entry(number_system_converter_frame)
entry_value.grid(row=1, column=1, padx=10, pady=10)

tk.Label(number_system_converter_frame, text="To Base:").grid(row=2, column=0, padx=10, pady=10)
to_base_var = tk.StringVar(number_system_converter_frame)
to_base_var.set("Decimal")
to_base_menu = tk.OptionMenu(number_system_converter_frame, to_base_var, "Binary", "Octal", "Decimal", "Hexadecimal")
to_base_menu.grid(row=2, column=1, padx=10, pady=10)

convert_number_button = tk.Button(number_system_converter_frame, text="Convert", command=convert_number_system)
convert_number_button.grid(row=3, column=0, columnspan=2, pady=10)

# Unit Converter Frame
unit_converter_frame = tk.Frame(root)

tk.Label(unit_converter_frame, text="Quantity Type:").grid(row=0, column=0, padx=10, pady=10)
quantity_type_var = tk.StringVar(unit_converter_frame)
quantity_type_var.set("Length")
quantity_type_menu = tk.OptionMenu(unit_converter_frame, quantity_type_var, "Length",)
quantity_type_menu.grid(row=0, column=1, padx=10, pady=10)

tk.Label(unit_converter_frame, text="From Unit:").grid(row=1, column=0, padx=10, pady=10)
from_unit_var = tk.StringVar(unit_converter_frame)
from_unit_var.set("mm")
from_unit_menu = tk.OptionMenu(unit_converter_frame, from_unit_var, *length_conversion_factors.keys())
from_unit_menu.grid(row=1, column=1, padx=10, pady=10)

tk.Label(unit_converter_frame, text="Value to Convert:").grid(row=2, column=0, padx=10, pady=10)
value_entry = tk.Entry(unit_converter_frame)
value_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(unit_converter_frame, text="To Unit:").grid(row=3, column=0, padx=10, pady=10)
to_unit_var = tk.StringVar(unit_converter_frame)
to_unit_var.set("cm")
to_unit_menu = tk.OptionMenu(unit_converter_frame, to_unit_var, *length_conversion_factors.keys())
to_unit_menu.grid(row=3, column=1, padx=10, pady=10)

convert_unit_button = tk.Button(unit_converter_frame, text="Convert", command=on_convert_button_click)
convert_unit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="Result will be shown here.")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Initialize with the first converter (Currency Converter)
select_converter(converter_types[0])

root.mainloop()

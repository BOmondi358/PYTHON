def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = (discount_percentage/100)*price
        final_price = price - discount_amount
        return final_price
    return price
try:
    price = float(input("Enter the price: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(price, discount_percentage)
    print(f"The final price after applying the discount is: {final_price}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
       
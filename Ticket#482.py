payment_method = input("Payment method? (card/cash):").strip().lower()
if payment_method == "card":
    print("processing...")
else:
    print("cash accepted")



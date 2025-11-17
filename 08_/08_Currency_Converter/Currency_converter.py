print("Currency Converter")

usd_to_inr = 84      
eur_to_inr = 91       
inr_to_usd = 1 / usd_to_inr
inr_to_eur = 1 / eur_to_inr

print("\nChoose conversion:")
print("1) USD → INR")
print("2) INR → USD")
print("3) EUR → INR")
print("4) INR → EUR")

choice = input("Enter your choice (1-4): ")

amount = float(input("Enter amount: "))

if choice == "1":
    result = amount * usd_to_inr
    print("INR:", result)

elif choice == "2":
    result = amount * inr_to_usd
    print("USD:", result)

elif choice == "3":
    result = amount * eur_to_inr
    print("INR:", result)

elif choice == "4":
    result = amount * inr_to_eur
    print("EUR:", result)

else:
    print("Invalid choice")

print("Thank you for using Currency Converter!")

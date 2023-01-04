high_income = True
good_credit = True
has_criminalRecord =False

if high_income and good_credit:
    print("You are eligible for Loan")
else:
    print("You are not eligible for Loan")


if good_credit and not has_criminalRecord:
    print("You are eligible for Loan")
else:
    print("You are not eligible for Loan")

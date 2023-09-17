userAge = int(input("how old r u ?: "))
vacationDays = []

if 18 <= userAge < 55:
    vacationDays.append(30)
elif userAge < 18:
    vacationDays.append(35)
else:
    vacationDays.append(32)

userDisabilityGrade = int(input("how high is you disability grading?(null for none): "))
if userDisabilityGrade >= 50:
    vacationDays.append(5)

vacationDaysAll = sum(vacationDays)
print("your have ", vacationDaysAll, " days per year enjoy it")

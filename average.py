#program for calculating grades
print("enter marks for 3 subjects")
subject_m =int(input("enter marks for maths"))
subject_p =int(input("enter marks for physics"))
subject_e =int(input("enter marks for english"))
total = subject_m + subject_p + subject_e
average = total/3
print("your total marks:",total)
print("your average marks:",average)

if average>=70 and average <=100:
    print("Grade A")
elif average>=60 and average <=69:
    print("Grade B")
elif average>=50 and average <=59:
    print("Grade C")
elif average>=40 and average <=49:
    print("Grade D")
elif average>=0 and average <=39:
    print("FAIL")

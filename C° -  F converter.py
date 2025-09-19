unit= input("please enter the degree C/F : ")
temp = float(input("plese enter the tempreature as a number: "))

if unit.lower() == "c":
    temp= temp*9/5 +32
    print(f"your tempreature if {temp}°F")

elif unit.lower()=="f":
    temp = (temp-32)*5/9
    print(f"your tempreature is {temp}°C")
else :
    pass

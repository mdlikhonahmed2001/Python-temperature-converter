#############################################
#                                           #
#  Python temperature converter system by   #
#          Likhon Ahmed            #
#                                           #
#############################################
# Banner
print("#############################################")
print("#                                           #")
print("#  Python temperature converter system by   #")
print("#          Likhon Ahmed            #")
print("#                                           #")
print("#############################################")
print("Type 1 to convert celsius to fahrenheit")
print("Type 2 to convert fahrenheit to celsius")

# Start main programme

op = int(input("What's your choice?: "))

if op == 1:

    c = float(input("Enter the value of Celsius temperature: "))
    f = (1.8 * c) + 32
    print("The Fahrenheit value is", f)

elif op == 2:

    f = float(input("Enter the value of Fahrenheit temperature: "))
    c = (f - 32) / 1.8
    print("The Celsius value is", c)
else:
    print("you entered the wrong key")



echo "# Python-temperature-converter" >> README.md
git init
git add --all
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mdlikhonahmed2001/Python-temperature-converter.git
git push -u origin main
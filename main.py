try:
    a = int(input("Enter the first number: "))

    b= int(input("Enter the second number: "))

    print("what kind of operation do u want to perform.\n Press + for (add)\n press - for (sub)\n press * for (mul)\n press / for (div)")

    o = input("Enter Operation: ")
    match o:
        case "+":
            print(f"the result is : {a+b}")
    
        case "-":
            print(f"the result is : {a-b}")
    
        case "*":
            print(f"the result is : {a*b}")
    
        case "/":
            print(f"the result is : {a/b}")
        case default:
            print("There was an error")
except Exception as e:
    print("Enter a valid value of a and b")
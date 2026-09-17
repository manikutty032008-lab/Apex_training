while True:
    print("\n1. Area of Circle")
    print("2. Area of Square")
    print("3. Area of Rectangle")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        r = int(input("Enter radius: "))
        area = int(3.14 * r * r)
        print("Area of Circle =", area)

    elif choice == 2:
        side = int(input("Enter side: "))
        area = side * side
        print("Area of Square =", area)

    elif choice == 3:
        length = int(input("Enter length: "))
        breadth = int(input("Enter breadth: "))
        area = length * breadth
        print("Area of Rectangle =", area)

    elif choice == 4:
        print("Program ended")
        break

    else:
        print("Invalid choice")

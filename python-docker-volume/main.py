try:
    name = input("Enter your name: ")

    if name:
        with open("user-name.txt", "a") as file:
            file.write(name + "\n")

        print("Name saved successfully!")

        show = input("Do you want to see all names? (y/n): ")

        if show.lower() == "y":
            with open("user-name.txt", "r") as file:
                names = file.read()

            print("\nAll Names:")
            print(names)

    else:
        print("\nNo new name entered.")
        print("Showing old names...\n")

        with open("user-name.txt", "r") as file:
            names = file.read()

        print("Old Name List:")
        print(names)
        

except Exception as e:
    print("Error:", e)
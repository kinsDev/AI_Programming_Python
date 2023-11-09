"""
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("This is not a valid number: ")
except KeyboardInterrupt:
    print("\nNo Input Taken\n")
else:
    print(x + 20)
finally:
    print("Didn't see an error? You've passed.\nOtherwise not")

"""

while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("This is not a valid number: ")
        break
    except KeyboardInterrupt:
        print("\nNo Input Taken\n")
        break
    else:
        print(x + 20)
        break
    finally:
        print("Didn't see an error? You've passed.\nOtherwise not")
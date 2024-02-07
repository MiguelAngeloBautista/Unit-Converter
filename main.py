import dist
import temp


def main():
  while True:
    print("1. Length/Distance")
    print("2. Temperature")
    print("3. Speed")
    print("4. Weight")
    print("0. Quit")

    # get input from user
    choice = input("\nEnter your choice: ")

    if choice == "0":
      print("Goodbye!")
      break

    match (choice):
      case "1":
        result = dist.main()
      case "2":
        result = temp.main()
      case "3":
        print("Speed")
      case "4":
        print("Weight")
      case _:
        print("Invalid choice\n")
    
    if result is not None:
      print("The final value is {:.2f}".format(result[0]), "|", "{:.2f}".format(result[1]), "\n")

if __name__ == "__main__":
  main()
# end main
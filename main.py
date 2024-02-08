# pylint: disable=W0311,C0301
import dist
import temp
import speed
import weight

def main():
  while True:
    print("1. Length/Distance")
    print("2. Temperature")
    print("3. Speed")
    print("4. Weight")
    print("q. Quit")

    # get input from user
    choice = input("\nEnter your choice: ")

    if choice.lower() == "q":
      print("Goodbye!")
      break

    match (choice):
      case "1":
        result = dist.main()
      case "2":
        result = temp.main()
      case "3":
        result = speed.main()
      case "4":
        result = weight.main()
      case _:
        print("Invalid choice\n")
    
    if result is not None:
      print("{:.2f}".format(result[0]), "is equal to", "{:.2f}".format(result[1]), "\n")


if __name__ == "__main__":
  main()
# end main
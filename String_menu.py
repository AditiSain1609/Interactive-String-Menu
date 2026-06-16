
string = input("Enter a string: ")

while True:
  print("\n===== STRING MENU =====")
  print("1. Strip Spaces ")
  print("2. Find a Substring ")
  print("3. Capitalize String ")
  print("4. Convert to Uppercase ")
  print("5. Convert to Lowercase")
  print("6. Convert to Title Case ")
  print("7. Replace a Word ")
  print("8. Count Occurrences ")
  print("9. Check Starts With ")
  print("10. Check Ends With")
  print("11. Split String ")
  print("12. Enter new String : ")
  print("13. Exit")
  
  choice = int(input("Enter your Choice : "))
  
  if(choice== 1):
    print(string.strip())
    
  elif(choice== 2 ):
    word = input("Enter the word to find: ")
    if string.find(word) != -1:
     print("Substring is found!")
    else:
     print("Substring is not found!")
     
  elif(choice== 3 ):
    print(string.capitalize())
    
  elif(choice== 4):
    print(string.upper())
    
  elif(choice== 5 ):
    print(string.lower())
    
  elif(choice== 6 ):
    print(string.title())
    
  elif(choice== 7):
    word = input("Enter the word that you replace : " )
    replace_to = input("Enter the word that enter : " )
    result = string.replace(word,replace_to)
    print("Updated String : " , result)
    
  elif(choice== 8):
    counts = input("Enter the string or word that to be count : ")
    print(string.count(counts))
    
  elif(choice == 9):
    start_word = input("Enter the check start word : ")
    if string.startswith(start_word):
        print("String start with", start_word)
    else:
        print("String does not start with", start_word)
        
  elif(choice == 10):
    end_word = input("Enter the check end word: ")
    if string.endswith(end_word):
        print("String ends with", end_word)
    else:
        print("String does not end with", end_word)
        
  elif(choice== 11):
    separator = input("Enter separator : " )
    print(string.split(separator))
    
  elif choice == 12:
    string = input("Enter New String: ")
    
  elif(choice== 13):
    print("Thank You for using String Menu!")
    break
  
  else:
    print("Invalid choice,please try again!")
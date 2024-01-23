def palindrome(sen):
    if len(sen) == 0:
        return True
    if sen[0] == sen[-1]:  
        return palindrome(sen[1:len(sen)-1])    
    else:
        return False
    
def main():
    sen = input("Enter a string:\n")
    if palindrome(sen) == True:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
        
main()
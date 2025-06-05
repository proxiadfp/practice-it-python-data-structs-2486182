from collections import deque
def check_palindrome (word):
    my_deque = deque(word)
    
    if my_deque.popleft() == my_deque.pop():
        print ('palindrome')
    else :
        print ('not palindrome')
    

def main():
    #add code here
    word = 'tacocat'
    check_palindrome(word)
     
if __name__ == "__main__":
    main()
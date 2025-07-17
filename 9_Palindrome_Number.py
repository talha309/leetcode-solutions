
#  String Methon- (easy way) 

class Solution(object):
    def isPalindrome(x):
        x_str = str(x)
        return x_str == x_str[::-1]  # Compare string with its reverse

    x = input("Enter any: ")
    print("Is Palindrome:", isPalindrome(x))


    def isPladinrom (y):
        y_str = str(y)
        return y_str == y_str [::-1]

    y = 1221
    print ("is Palidrome:", isPalindrome(y))


#  step by step explanation (math method-without string)

class Solution (object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        original = x
        reversed_sum = 0
        while x != 0:
            digit = x%10
            reversed_sum = reversed_sum * 10 + digit
            x = x // 10 
            return original ==  reversed_sum
        

sol = Solution()
print (sol.isPalindrome(121))

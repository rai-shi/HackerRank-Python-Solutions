# challange : check if the number is palindrome without turning it to string 
def isPalindrome(x: int) -> bool:
        """
        15851 : 10000 + 5000 + 800 + 50 + 1
        
        15851 // 10 = 1585
        15851 % 10 = 1
        """
        number_list = []
        if (type(x)==int):
            if not (x < 0):
                while(True):
                    number_list.append(x % 10)
                    x //= 10
                    if x == 0:
                        break 
                half_length = len(number_list) // 2
                for idx in range(half_length):
                    end_idx = 0 - (idx + 1)
                    if number_list[idx] != number_list[end_idx]:
                        return False 
                return True 
            return False
        return False
            

print(isPalindrome(-15851))

# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("qabel@calpoly.edu")
print(message)



def smallest(n: float, m: float) -> float:
   if n < m:
      return n  #For which calls below is this statement evaluated? first
   else:
      return m


first = smallest(3, 2)  #What is the value of first? 2
second = smallest(2, 2)  #What is the value of second? Is this a reasonable result? Why or why not? 2, No because the two values are the same.
print(first, second)


def function2(a:int, b:int, c:int) -> int:
   if a > b and a > c:
      return a - b  #In general, when will a call to this function evaluate this statement? When a is greater than both b and c
   elif b > c:
      return b + c  #In general, when will a call to this function evaluate this statement? When a is less than b and c but b is greater than c
   else:
      return 2 * c  #In general, when will a call to this function evaluate this statement? When a is not greater than b and c and b is not greater than c.

answer1 = function2(3, 2, 1)  #What is the value of answer1? 1
answer2 = function2(2, 3, 1)  #What is the value of answer2? 4
answer3 = function2(2, 1, 3)  #What is the value of answer3? 6
print (answer1, answer2, answer3)


from typing import Optional  #gain access to the Optional [X] type hint

def checked_access(L:list[int], idx:int) -> Optional[int]:
   test = idx >= 0 and idx < len(L)  #What is the value of test on each call? Test is False on first call and test is True on second call
   if test:       #What is this check preventing? an Index Error
      return L[idx]
   else:
      return None

first = checked_access ([1, 0, 1], 9)  #What is the value of first? None
second = checked_access([1, 0, 1], 2)  #What is the value of second? 1
print(first)
print(second)


def length_sum(L:list[str]) -> int:
   if len(L) > 2:
      result = len(L[0]) + len(L[1]) + len(L[2])  #For which call below is this statement evaluated? First
   elif len(L) > 1:  #and what are the values being added? This + Is + The, 4+2+3
      result = len(L[0]) +len(L[1])  #For which call below is this statement evaluated? Second
   elif len(L)>0:  #and what are the values being added? Second + _ + call, 6+1+4
      result = len(L[0])  #For which call below is this statement evaluated? Third
   else:  #and what are the values being added? Another + Call, 7+4
      result = 0
   return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print(first)
print(second)
print(third)


def surprising(L:list[str], other:str) -> list[str]:
   L.append(other.upper())
   return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
  #What is the value of words at this point? ['this', 'is', 'confusing', 'code', 'AVOID', 'SUCH.']]
  #What are the values of first and second at this point? ['this', 'is', 'confusing', 'code.' 'AVOID', 'SUCH.'], ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
  #What happened? Avoid and such were turned into uppercase and added to words. The original list was changed.
print(first)
print(second)
# 1________
# print('Hello World')

# 2_________
# str = 'Hello World'
# print(str)

# 3_________
# print(int(input())*2)

# 4__________
# print(int(input())*int(input()))

# 5_________
# name = input()
# surname = input()
# age = input()
# strin = f"My name is {name}, surname is {surname}, age is{age}"
# print(strin)

# 6)
# print("First Number")
# num1 = int(input())
# print("Second Number")
# num2 = int(input())
# print("+ or - or / or *")
# char = input()
# if char == '+':
#     print(num1+num2)
# elif char == '/':
#     print(num1/num2)
# elif char == '*':
#     print(num1*num2)
# elif char == '-':
#     print(num1*num2)

# 7)
# def cubePrinter():
#     num = int(input())
#     print(num * num * num)
# cubePrinter()

# 8)
# def perimeterCalculator():
#     length = int(input())
#     width =  int(input())
#     print(2*(length + width))
# perimeterCalculator()

# 9)
# def triangleAngleFinder():
#     print("\n \n Enter 1st degree")
#     deg1 = int(input())
#     print("Enter 2nd degree")
#     deg2 = int(input())
#     if (deg1 + deg2)>180:
#         return triangleAngleFinder()
#     else:
#         print(180 - (deg1 + deg2))

# triangleAngleFinder()

# 10)
# l = {45, 67, 89, 23, 55, 88, 93}
# print("Enter your number")
# number = int(input())
# exist = False
# for e in l:
#     if e == number:
#         exist = True
#     else:
#         continue
# print(exist)

# 11)
# num = int(input())
# print((8*num +45)/25-9)

# 12)
# print(int(int(input()) * int(input()) / 100))
# print(int(int(input()) / int(input()) * 100))

##################################################################################################
##################################################################################################
##################################################################################################
# arr = [678, 4511, 67, 89, 23, 545, 188, 293]
# 13)
# def Sum(arr):
#     x = 0
#     for e in arr:
#         x = x + e
#     return x
# print(Sum(arr))

# 14)
def Average(arr):
    x = 0
    for e in arr:
        x = x + e
    return x/len(arr)

# 15)
# def Counter(arr):
#     x = 0
#     for e in arr:
#         x += 1
#     return x
# print(Counter(arr))

# 16)
# def Counter100200(arr):
#     x = 0
#     for e in arr:
#         if e > 100 and e < 200:
#             x = x + 1
#     return x
# print(Counter100200(arr))

# 17)
# def CounterEven(arr):
#     x = 0
#     for e in arr:
#         if e % 2 == 0:
#             x = x + 1
#     return x
# print(CounterEven(arr))

# 18)
# def Biggest(arr):
#     x = arr[0]
#     for e in arr:
#         if e > x:
#             x = e
#     return int(x)


# 19)
# def Smallest(arr):
#     x = arr[0]
#     for e in arr:
#         if e < x:
#             x = e
#     return int(x)

# 20)
# def BigMinusSmal(arr):
#     print(Biggest(arr) - Smallest(arr))

# List = [678, 'Freelance', 45, 67, 89, 'Raymond',
#         23, True, 'Michael', 'Joseph', 545, 188, 293]
# 21)
# x = 0
# for e in List:
#     # if(isinstance(e, str) == True):
#     if(type(e) == str):
#         x += 1
# print(x)

# 22)
# x = 0
# for e in List:
#     # if(isinstance(e, str) == True):
#     if(type(e) == str):
#         x += 1
#         print(e + f"\n Letter Count:{len(e)}")
# print(x)

# 23)
# for e in List:
#     # if(isinstance(e, str) == True):
#     if(type(e) == str):
#         new_str = str()
#         i = len(e)-1   # LengthWord
#         while(i >= 0):  # Condition
#             new_str += e[i]
#             i -= 1  # OperationOnEachIteration
#         print(new_str)

# 24)
# for e in List:
#     if(type(e) == str):
#         vowels = set()
#         for l in range(len(e)):
#              if (e[l] in {"e","u","i","o","a"}):
#                  vowels.add(e[l])
#         print(vowels)

# 25)
# for e in List:
#     if(type(e) == str):
#         new_str = str()
#         for l in range(len(e)):
#             if (e[l].islower()):
#                 new_str = new_str+e[l].upper()
#             else:
#                 new_str = new_str+e[l].lower()
#         print(new_str)

# 26)
# name = input("Type your name")
# new_str = str()
# for l in name:
#     new_str = new_str + str(ord(l))
# print(new_str)

# 27)
# str1 = 'Senan'
# str2 = 'Hellas'
# l = 0
# while (l < len(str1)):
#     if int(ord(str1[l])) > int(ord(str2[l])):
#         print('str1 is bigger')
#         break
#     if int(ord(str1[l])) < int(ord(str1[l])):
#         print('str2 is bigger')
#         break
#     l += 1

# 28)
# def checkContain(word, phrase):
#     if type(word) != str or type(phrase) != str or len(word) < 1 or len(phrase) < 1:
#         return False

#     found = False

#     for i in range(len(word)):
#         if word[i] == phrase[0]:
#             j = 0
#             while(i < len(word) and j < len(phrase)):
#                 if word[i] != phrase[j]:
#                     found = False
#                 else:
#                     found = True
#                 i += 1
#                 j += 1
#             if found == True:
#                 break
#         else:
#             continue
#     return found

# 29)


# def startsWith(word, phrase):
#     if type(word) != str or type(phrase) != str or len(word) < 1 or len(phrase) < 1 or len(word) < len(phrase):
#         return False

#     starts = False
#     i = 0
#     while (i < len(phrase) and i < len(word)):
#         if word[i] == phrase[i]:
#             starts = True
#         else:
#             starts = False
#             break
#         i += 1
#     return starts


# print(startsWith("Azerbaijan", "Az"))

# 30)
# def endsWith(word, phrase):
#     if type(word) != str or type(phrase) != str or len(word) < 1 or len(phrase) < 1 or len(word) < len(phrase):
#         return False

#     ends = False
#     i = len(word) - 1#last index Word
#     j = len(phrase) - 1#last index Phrase
#     while (i > -1 and j > -1):
#         if word[i] == phrase[j]:
#             ends = True
#             print(word[i])
#         else:
#             ends = False
#             break
#         i -= 1
#         j -= 1
#     return ends
# print(endsWith("Azerbaijan","a"))

# 31)
# def checkContainİndex(word, phrase):
#     if type(word) != str or type(phrase) != str or len(word) < 1 or len(phrase) < 1 or len(word) < len(phrase):
#         return False
#     found = False
#     found_index = -1
#     for i in range(len(word)):
#         if word[i] == phrase[0]:
#             found_index = i
#             j = 0
#             while(i < len(word) and j < len(phrase)):
#                 if word[i] != phrase[j]:
#                     found = False
#                 else:
#                     found = True
#                 i += 1
#                 j += 1
#             if found == True:
#                 break
#         else:
#             continue
#     if found:
#         return found_index
#     else:
#         return -1

# print(checkContainİndex("Senan","aaa"))


# 32)
# Senan SeNAnan
# def addPhraseToIndex(word, phrase, index):
#     new_word = str()
#     for i in range(index):
#         new_word += word[i]
#     for i in range(len(phrase)):
#         new_word += phrase[i]
#     j = index
#     while(j < len(word)):
#         new_word += word[j]
#         j += 1
#     return new_word

# print(addPhrase('senan', '123456', 2))

# 33)
# def splice(word, index, delete_count):
#     if delete_count > len(word) - index:
#         return False
#     new_word = str()
#     for i in range(index):
#         new_word += word[i]

#     j = len(word) - (index + delete_count) #How many times to add
#     k = index + delete_count #Where to start
#     i=0
#     while i < j:
#         new_word += word[k]
#         k += 1
#         i += 1
#     return new_word


#     j = len(word) - (index + delete_count)
#     for i in range(j):
#         new_word += word[j]

# 34)
#################################
### Most Difficult Why? #########
#################################
# def replace(word, searching, defining):
#     new_string = str()
#     founded_indexes = set()
#     for l in range(len(word)):
#         founded = False
#         if word[l] == searching[0]:
#             k = l
#             j = 0
#             while k < len(word) and j < len(searching):
#                 if word[k] == searching[j]:
#                     founded = True
#                 else:
#                     founded = False
#                 k += 1
#                 j += 1

#         if founded:
#             founded_indexes.add(l)
#     start_paste_index = int(0)
#     while(start_paste_index < len(word)):
#         if start_paste_index in founded_indexes:
#             new_string += defining
#             start_paste_index += len(searching)
#         else:
#             new_string += word[start_paste_index]
#             start_paste_index += 1
#     return new_string


# 35)
# def split(word, index):
#     new_string = str()
#     for l in range(len(word)):
#         if l < index:
#             continue
#         else:
#             new_string += word[l]
#     return new_string


#####################################################
#####################################################
###### Pre-Intermediatee  Level questions ###########
#####################################################
lastArr = [678, "Freelance", [99, 21, [99, 12, 456, ["Simon", "Holly"], 78, 34],
                              45, 67], 45, 67, 89, "Raymond", 23, True, "Michael", "Joseph", 545, 188, 293]
numbers = [678, 99, 21, 99, 12, 456, 78, 34,
           45, 67, 45, 67, 89, 23, 545, 188, 293]

# 36)
# def recursiveSum(arr):
#     sum_new = 0
#     for element in arr:
#         if type(element) == int:
#             sum_new += element
#         elif type(element) == dict or type(element) == set or type(element) == tuple or type(element) == list:
#             foo = recursiveSum(element)
#             sum_new += foo
#     return sum_new

# JustForFun

# 37)

# class AverageUnits:
#     def __init__(self, sum, count):
#         self.sum = sum
#         self.count = count

#     def Sum(self):
#         return self.sum

#     def Count(self):
#         return self.count

#     def Average(self):
#         return self.sum/self.count
# def recursiveAverage(arr):  # 167 should be
#     if len(arr) < 1:
#         return 0
#     sum_new = 0
#     int_count = 0
#     for element in arr:
#         if type(element) == int:
#             sum_new += element
#             int_count += 1
#         elif type(element) == dict or type(element) == set or type(element) == tuple or type(element) == list:
#             foo = recursiveAverage(element).Sum()
#             int_count += recursiveAverage(element).Count()
#             sum_new += foo
#     return AverageUnits(sum_new, int_count)

# 38)
# AverageUnit.Count() already created clas

# 39)
# def recursiveStringFinder(arr):
#     string_count = 0
#     for element in arr:
#         if type(element) == str:
#             string_count += 1
#         elif type(element) == dict or type(element) == set or type(element) == tuple or type(element) == list:
#             sub_array_count = recursiveStringFinder(element)
#             string_count += sub_array_count
#     return string_count

# 40)
# def recursiveStringWordCountFinder(arr):
#     string_dictionary = dict()
#     for element in arr:
#         if type(element) == str:
#             string_dictionary[element] = len(element)
#         elif type(element) == dict or type(element) == set or type(element) == tuple or type(element) == list:
#             string_sub_dictionary = recursiveStringWordCountFinder(element)
#             for key in string_sub_dictionary:
#                 string_dictionary[key] = string_sub_dictionary[key]
#     return string_dictionary

# 41)
# def recursiveStringHexFinder(arr):
#     string_dictionary = dict()
#     for element in arr:
#         if type(element) == str:
#             hexed_value = str()
#             for l in range(len(element)):
#                 hexed_value = hexed_value + str(ord(element[l]))
#             string_dictionary[element] = hexed_value
#         elif type(element) == dict or type(element) == set or type(element) == tuple or type(element) == list:
#             string_sub_dictionary = recursiveStringWordCountFinder(element)
#             for key in string_sub_dictionary:
#                 string_dictionary[key] = string_sub_dictionary[key]
#     return string_dictionary

# 42)
# def recursiveWordInverter(arr):
#     string_dictionary = dict()
#     for element in arr:
#         if type(element) == str:
#             inverse_string = str()
#             j = len(element) - 1
#             while j > -1:
#                 inverse_string += element[j]
#                 j -= 1
#             string_dictionary[element] = inverse_string
#         elif type(element) == dict or type(element) == set or type(element) == tuple or type(element) == list:
#             string_sub_dictionary = recursiveWordInverter(element)
#             for key in string_sub_dictionary:
#                 string_dictionary[key] = string_sub_dictionary[key]
#     return string_dictionary

# 43)
# def recursiveWordUpLower(arr):
#     string_dictionary = dict()
#     for element in arr:
#         if type(element) == str:
#             up_low_string = str()
#             for l in element:
#                 if l.islower():
#                     up_low_string += l.upper()
#                 else:
#                     up_low_string += l.lower()
#             string_dictionary[element] = up_low_string
#         elif type(element) == dict or type(element) == set or type(element) == tuple or type(element) == list:
#             string_sub_dictionary = recursiveWordUpLower(element)
#             for key in string_sub_dictionary:
#                 string_dictionary[key] = string_sub_dictionary[key]
#     return string_dictionary

# 43) Recursive Factorial
# def Factorial(target_number, current_number=1, current_value=1,):
#     if target_number == 0:
#         return 1

#     current_value = current_value * (current_number + 1)
#     current_number += 1
#     if current_number == target_number:
#         return current_value
#     else:
#         return Factorial(target_number, current_number , current_value)

# 43) Iterative Factorial
# def Factorial(target_number):
#     if target_number == 0:
#         return 1

#     current_value = 1
#     i = 1
#     while i <= target_number:
#         current_value = current_value * i
#         i+=1
#     return current_value



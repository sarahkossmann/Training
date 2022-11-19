data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

# print (new_list)

def reverse(string):
    string = list(string)
    string.reverse()
    return "".join(string)


s = "Geeksforgeeks"


# print("The reversed string(using reversed) is : ", reverse(s))


for num in range(2,51):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)

def swap_list(list, position_a, position_b):
    temp = list[position_a]
    list[position_a] = list[position_b]
    list[position_b] = temp
    print(list)


def count_vowels(text):
    letters = set(text.lower())

    count = 0
    for vowel in 'aeiou':
        if vowel in letters:
            count += 1
    return count


print(count_vowels("Aaa aeeE"))  # Prints 2
print(count_vowels("eiOuayOI j_#Ra"))

# Print First 10 natural numbers using while loop
number = 1

while number < 11:
    print(number)
    number = number + 1

# Write a program to print the following number pattern using a loop

for i in range(7):
    for j in range(1, i):
        print(j, end=" ")
    print("")

# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

user_number = int(input("Enter a number: "))
sum = 0

for i in range(1, user_number+1):
    sum += i
print(sum)

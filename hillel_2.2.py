
numbers = int(input("Enter a 5-digit integer : "))

revers_number_type_str = str(numbers % 10) + str(numbers // 10%10) + str(numbers // 100%10) + str(numbers // 1000%10) + str(numbers // 10000)

change_type_to_int = int(revers_number_type_str)
# Якщо необхідний тип 'Str'
print(type(revers_number_type_str))
print(revers_number_type_str)
print("---------------------")
# В разі необхідно тип 'Int'
print(type(change_type_to_int))
print(change_type_to_int)

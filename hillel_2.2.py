
numbers = int(input("Enter a 5-digit integer : "))
n1=numbers%10*10000
n2=numbers%100//10*1000
n3=numbers%1000//100*100
n4=numbers//1000%10*10
n5 = numbers//10000
answer = n1 + n2 + n3 + n4 + n5
print("Перевернута цифра: ", answer)
print(n1,n2,n3,n4,n5)


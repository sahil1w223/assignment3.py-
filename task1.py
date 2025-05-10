dic = {'alice' : 60 , 'bob' : 70 , 'charlie' : 80 , 'dave' : 90}
enter_name = input("Enter name: ")
if enter_name in dic:
    print(enter_name + "'s marks : ", dic[enter_name])    
else:
    print("student not found")
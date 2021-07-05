#We know that we can perform list comprehension like this

list_Ex1 = [i for i in range(0,10)]
list_Ex2 = [chr(i+65) for i in range(0,10)]

#But do you know you can do comprehension like this in dictionary also?
#We can do so like :
dict_comp_example = {key:value for key, value in zip(list_Ex1,list_Ex2)}
print(dict_comp_example)


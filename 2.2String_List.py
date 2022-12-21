'''
2.2	String List
Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators. 
'''
l=[]
wrd_list = []
sep_list = []
final_list = []

print("Enter a string : ")
strg=str(input())                                     
wrd_list=strg.split(", ")
for i in range(len(wrd_list)):
    spaces=wrd_list[i].count(" ")
    l+=wrd_list[i].split(" ")
    for j in range(spaces) :
        sep_list.append(" ")
    if i!=len(wrd_list)-1:sep_list.append(",")
final_list.append(l)
final_list.append(sep_list)
print(final_list)
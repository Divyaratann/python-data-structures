#list
#collection of item
marks=[98,67,45,78,90]
print(marks,type (marks))
mark =[98,67,45,78,90,'A',92.6]
print(mark,type (mark))


#length of list
print(len(mark)) #7

# index
print(mark[0]) #98  
print(mark[1]) #67
print(mark[2]) #45
print(mark[-1]) #92.6
print(mark[-2]) #A


#slicing     ------------------------list[st:end]
print(mark[0:3]) #[98,67,45]
print(mark[-3:])
print(mark[:])
print(mark[:3])

for score in marks: #loop through list
    print(score)

# list is mutable
marks.append(100) #add 100 at the end of list
print(marks)

#insert in list
marks.insert(1,23)
print(marks)

#check if 98 is in marks list or not
print(98 in marks) #True
print(98 in marks) #True
print(100 in marks) #False

###################
marks.clear () #clear the list
print(marks,len(marks))
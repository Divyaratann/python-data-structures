#dictionary
# isme key value pair hota hai

marks={"maths":99,"Physics":88,"Chemistry":90}
print(marks,type(marks))
print(marks["Physics"])


marks["English"]=97

print(marks["English"])



#loops
for key in marks:
    print(key,marks[key])

    
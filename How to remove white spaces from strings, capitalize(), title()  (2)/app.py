name = str(input("Please enter your name: "))
print("hello, ", name)

# result:
#     Please enter your name:           sepehr
#     Hello,            sepehr
    
# as you see, if a user write many spacelines 
# system should remove it 


name = name.strip()
name = name.title()#capitalize every single word
# name = name.capitalize()#for capitlize the first letter
print("hello, ", name)

# name = input().strip.title 
#better way
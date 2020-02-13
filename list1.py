students =["Leroy", "Julius", "Collins", "Alex","Jacob"] #The list must have a title i.e Students
print (students[1]) # with indexing, starting from 0, the name printed is Julius as it is number 1 on the index
print (students [0]) # Leroy is printed as it is number 0 on the index scale
print (students [2:5])
students [3] = "Richard" # Changes the value/Name in the list
print (students)
students [2] = "Jake"
print (students)
for student in students: # This will give you a list of all students
  print (students)
if "Leroy" in students:
  print ("Leroy is there") # If a name is in the list, it will be printed
print (len (students)) #prints out the length of the list
students.append ("Kate") #adds a name/value to the list
print (students)
students.insert (1, "Cassandra") #will add a name/value to the list at the specified index point
print (students)
students.remove ("Cassandra") # Removes the specified name/value from the list
print (students)
students.pop(2) # Removes the specified index and the name it represents
print (students)
students.reverse() # Reverses the way the list is outputed/read
print (students)
students.sort() #Sorts the list according to specifications
print (students)
students.copy()n #makes a copy of the list
print (students)
contacts={ "greg": 7235591, "Mary": 3841212, "Bob": 3841212, "Susan": 2213278}
# print content of dictionary
print("Dictionary content are: \n", contacts)
#printing the value of a dictionary key
print("Phone number for Susan is:", contacts["Susan"])
#print out how many keys are in the dictionary
print("Lenght of dictionary is:", len(contacts))
#adding two keys in the dictionary
contacts["John"]=4440001
contacts["Fred"]=5550001
#deleting the contact calle "bob"
contacts.pop("Bob")
print("Contents of contacts after deleting entry for bob is:\n", contacts)
print("lenght of dictionary is now:", len(contacts))


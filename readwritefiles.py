#! /bin/python3/

# Write Mode ("w"):  Overwrites the exisitng data

months=open("Months.txt","w") 

months.write("Jan\n")
months.write("Feb\n")
months.write("Mar\n")
months.write("Apr\n")
months.write("May\n")

print(months)# Prints -  <_io.TextIOWrapper name='Months.txt' mode='w' encoding='UTF-8'> 

#print(months.readlines())

months.close()

#*************************************************************************************

# Append Mode ("a"):  Overwrites the exisitng data

months=open("Months.txt","a")

months.write("Jun\n")
months.write("Jul\n")
months.write("Aug\n")
months.write("Sep\n")
months.write("Oct\n")

print(months)# Prints -  <_io.TextIOWrapper name='Months.txt' mode='a' encoding='UTF-8'> 

#print(months.readlines())

months.close()

#*************************************************************************************

# Read Mode ("r")

months=open("Months.txt","r")

print(months)# Prints -  <_io.TextIOWrapper name='Months.txt' mode='r' encoding='UTF-8'> 

print(months.mode) # Prints- r
print(months.readable()) # Prints- True

print(months.read()) # Reads full content of the file
print(months.readline()) # Originally Reads line by line; but here it prints blank lines as the read handle has already reached the end of the file

print(months.readlines()) # Originally Read the full content in the form of a list; but here it prints blank lines as the read handle has already reached the end of the file. Use months.seek(0) to go back to the first line

months.seek(0) # To go back to the first line

for month in months:
	print(month)



months.close() 

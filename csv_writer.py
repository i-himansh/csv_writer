with open("csv_data.txt" , "r") as my_file:
    lines = my_file.readlines()
    lines = [line.strip() for line in lines[1:]]
print (lines)
for line in lines:
    personal_data = line.split(",")
    name = personal_data[0].title()
    age = personal_data[1]
    college = personal_data[2].capitalize()
    subject = personal_data[3].capitalize()

    print(f"{name} is {age} studing {subject} at {college}")
save_in_csv = ','.join(['rolf','23',"MIT","computer science"]) # this is how to write back in csv
print(save_in_csv)

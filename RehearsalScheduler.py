rooms = {"Room A" : {"Monday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None}, 
					"Tuesday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None},
					"Wednesday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None},
					"Thursday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None}, 
					"Friday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None}}, 
		
		"Room B" : {"Monday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None}, 
					"Tuesday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None},
					"Wednesday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None},
					"Thursday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None}, 
					"Friday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None}},  
		
		"Room C" : {"Monday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None}, 
					"Tuesday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None},
					"Wednesday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None},
					"Thursday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None}, 
					"Friday" : {"3:00 pm" : None, "4:00 pm" : None, "5:00 pm" : None}}, 
					} 

# Mailgun API 
# Flask

def show_particular_room():
	choice = raw_input("What room would you like to view?")
	if choice == "Room A":
		print rooms["Room A"]

def main():
	print rooms
	print show_particular_room()

if __name__ == '__main__':
	main()






							
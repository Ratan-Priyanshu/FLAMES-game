# import all functions from the tkinter
from tkinter import *
from pygame import mixer 
from PIL import ImageTk, Image

#for background music
def bgsound():
    mixer.init()
    mixer.music.load("bgsound.mp3")
    mixer.music.play(-1)

# function for removing common characters
# with their respective occurrences
def remove_match_char(list1, list2):

	for i in range(len(list1)) :
		for j in range(len(list2)) :

			# if common character is found
			# then remove that character
			# and return list of concatenated
			# list with True Flag
			if list1[i] == list2[j] :
				c = list1[i]

				# remove character from the list
				list1.remove(c)
				list2.remove(c)

				# concatenation of two list elements with *
				# * is act as border mark here
				list3 = list1 + ["*"] + list2

				# return the concatenated list with True flag
				return [list3, True]

	# no common characters is found
	# return the concatenated list with False flag
	list3 = list1 + ["*"] + list2
	return [list3, False]


# function for telling the relationship status
def tell_status() :
	
	# take a 1st player name from Player1_field entry box
	p1 = Player1_field.get()

	# converted all letters into lower case
	p1 = p1.lower()

	# replace any space with empty string
	p1.replace(" ", "")

	# make a list of letters or characters
	p1_list = list(p1)

	# take a 2nd player name from Player2_field entry box
	p2 = Player2_field.get()
	p2 = p2.lower()
	p2.replace(" ", "")
	p2_list = list(p2)

	# taking a flag as True initially
	proceed = True
	
	# keep calling remove_match_char function
	# until common characters is found or
	# keep looping until proceed flag is True
	while proceed :

		# function calling and store return value
		ret_list = remove_match_char(p1_list, p2_list)

		# take out concatenated list from return list
		con_list = ret_list[0]

		# take out flag value from return list
		proceed = ret_list[1]

		# find the index of "*" / border mark
		star_index = con_list.index("*")

		# list slicing perform
		
		# all characters before * store in p1_list
		p1_list = con_list[ : star_index]

		# all characters after * store in p2_list
		p2_list = con_list[star_index + 1 : ]


	# count total remaining characters
	count = len(p1_list) + len(p2_list)

	# list of FLAMES acronym
	result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

	# keep looping until only one item
	# is not remaining in the result list
	while len(result) > 1 :

		# store that index value from
		# where we have to perform slicing.
		split_index = (count % len(result) - 1)

		# this steps is done for performing
		# anticlock-wise circular fashion counting.
		if split_index >= 0 :

			# list slicing
			right = result[split_index + 1 : ]
			left = result[ : split_index]

			# list concatenation
			result = right + left

		else :
			result = result[ : len(result) - 1]

	# insert method inserting the
		# value in the text entry box.
	Status_field.insert(10, result[0])


# Function for clearing the
# contents of all text entry boxes
def clear_all() :
	Player1_field.delete(0, END)
	Player2_field.delete(0, END)
	Status_field.delete(0, END)

	# set focus on the Player1_field entry box
	Player1_field.focus_set()

# Driver code
if __name__ == "__main__" :

	# Create a GUI window
	root = Tk()
	
	# Set the background colour of GUI window
	root.configure(background = 'pink')

	# Set the configuration of GUI window
	root.geometry("500x400")

	bg = ImageTk.PhotoImage(Image.open("bgimg.png"))
	#bg = PhotoImage(file = "bgimg.png")
  
	# Show image using label
	label12 = Label( root, image = bg)
	label12.place(x = 0, y = 0)

	# set the name of tkinter GUI window
	root.title("Flames Game")
	bgsound()
	
	
	# Create a Player 1 Name: label
	label1 = Label(root, text = "Player 1 Name: ",font=("Arial",8,"bold"),fg = 'black', bg = 'purple')

	# Create a Player 2 Name: label
	label2 = Label(root, text = "Player 2 Name: ",font=("Arial",8,"bold"),fg = 'black', bg = 'purple')
	
	# Create a Relation Status: label
	label3 = Label(root, text = "Relationship Status: ",font=("Arial",9,"bold"),fg = 'black', bg = 'purple')

	# grid method is used for placing
	# the widgets at respective positionswq
	# in table like structure .
	label1.place(relx=0.25,rely=0.2)
	label2.place(relx=0.25,rely=0.3)
	label3.place(relx=0.197,rely=0.55)

	# Create a text entry box
	# for filling or typing the information.
	Player1_field = Entry(root)
	Player2_field = Entry(root)
	Status_field = Entry(root)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	# ipadx keyword argument set width of entry space .
	Player1_field.place(relx=0.45,rely=0.2)
	Player2_field.place(relx=0.45,rely=0.3)
	Status_field.place(relx=0.45,rely=0.55)

	# Create a Submit Button and attached
	# to tell_status function
	button1 = Button(root, text = "Submit",font=("Arial",10,"bold"), bg = "Indigo",fg = "black", height= 2, width=20,command = tell_status)

	# Create a Clear Button and attached
	# to clear_all function
	button2 = Button(root, text = "Clear",font=("Arial",10,"bold"), bg = "Indigo",fg = "black", height= 1, width=20,command = clear_all)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	button1.place(relx=0.35,rely=0.4)
	button2.place(relx=0.35,rely=0.65)

	# Start the GUI
	root.mainloop()

from Tkinter import *
'''
This is a simple GUI example.
There is a label, text entry box, and button.
When the button is clicked, a function is executed.
Limitations - If I wanted to create many instances of this GUI,
I would have to duplicate this code over and over.
'''

class AppMain(object):
	def __init__(self, master):
		var_label_text = StringVar(master)                # Special Tkinter Variable for label text
		var_label_text.set("Please enter your first and last name.")
		lbl_hello = Label(master, textvariable=var_label_text)
		lbl_hello.grid(row=0,column=1) 
		                           # show the label
		lbl_first = Label(master, text="First")               # Special Tkinter Variable for label text
		lbl_first.grid(row=1, column=0)

		lbl_last = Label(master, text="Last")               # Special Tkinter Variable for label text
		lbl_last.grid(row=2, column=0)

		entry_text = Entry(master)                        # creates a text entry box
		entry_text.insert(0, "Type first name.")   # text to display on start up
		entry_text.grid(row=1,column=1)

		entry_text_last = Entry(master)                        # creates a text entry box
		entry_text_last.insert(0, "Type last name.")   # text to display on start up
		entry_text_last.grid(row=2,column=1)


		# create a button
		# command sets a function to run when the button is clicked. AKA as an event and callback
		btn_ok = Button(master, text='Ok', command=lambda: var_label_text.set("my name is " +entry_text.get()+ " "+ entry_text_last.get()))
		btn_ok.grid(row=3, column=1)


def main():
	root_widget = Tk()                          # creates a widget window which will hold all other widgets.
	root_widget.geometry("300x200")             # sets the size of the window
	root_widget.title("Simple GUI Demo")        # set the title of the window
	# runs the window in a loop so it continuously detects the button click event
	AppMain(root_widget)

	root_widget1 = Tk()                          # creates a widget window which will hold all other widgets.
	root_widget1.geometry("300x200")             # sets the size of the window
	root_widget1.title("Simple GUI Demo")        # set the title of the window
	# runs the window in a loop so it continuously detects the button click event
	AppMain(root_widget1)
	root_widget.mainloop()


if __name__ == '__main__':
	main()

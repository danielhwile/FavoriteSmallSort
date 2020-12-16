import random
from tkinter import *

def list_maker(list_size,max_value):
    '''This Function creates our list that needs to be sorted.'''
    list = []
    for i in range(0, list_size):
        list.append(random.randint(1, max_value))
    return list

def list_chopper(list):
    '''This Function converts a list into a string that can be displayed on multiple lines on our tkinter window'''
    string = ""
    string2 = ""
    counter = 0
    for ele in list:
        string += str(ele)
        string += ", "
    for car in string:
        counter += 1
        if counter == 100:
            car = car + '\n'
            counter = 0
        string2 += car
    return string2

def dad_sorter(unsorted_list,list_size,max_value):
    '''This is the actual sorting algorythm converted down to one function'''
    sorted_list = []
    max_value += 1
    sort_array = [0] * max_value
    for i in range(0,list_size):
        temp = unsorted_list[i]
        sort_array[temp] +=1
    for i in range(0,max_value):
        while sort_array[i] > 0:
            sorted_list.append(i)
            sort_array[i] -=1
    return sorted_list

class prompt(Frame):
    '''This Class is the User Interface for the application.  It is using tkinter for the UI see tkinter documentation for more info'''
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        self.master.title("Buh-Dad Sorting Alg With a UI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        #These two vars will be referencable as standard string vars to receive the user entry at the global scope
        self.list_size = None
        self.max_value = None
        self.error_code = None

        #These two vars are the entry vars specifically for tkinter, tkinter uses its own StringVar() function seperate from normal strings... very annoying.
        self.var1 = StringVar()
        self.var2 = StringVar()

        # This is the placement of our labels L entries E and buttons Button
        L1 = Label(self, text="How many elements are we sorting? (between 2 and 200)")
        L1.place(x=5,y=15)
        E1 = Entry(self,textvariable=self.var1, bd=5)
        E1.place(x=150,y=35)
        L2 = Label(self, text="What is the largest number? (must be bigger that the number of elements provided above)")
        L2.place(x=5, y=55)
        E2 = Entry(self, textvariable=self.var2, bd=5)
        E2.place(x=150, y=75)
        quitButton = Button(self, text="Sort Away!", command= self.client_exit)

        # placing the button on my window
        quitButton.place(x=150, y=120)
    def client_exit(self):
        try:
            self.list_size = int(self.var1.get())
        except:
            self.error_code = "Error 1: List Size value was not a valid entry."
        try:
            self.max_value = int(self.var2.get())
        except:
            if self.error_code == None:
                self.error_code = "Error 2: Max Value was not a valid entry"
            else:
                self.error_code = self.error_code + "\nError 2: Max Value was not a valid entry"
        if self.error_code != None:
            root.destroy()
            erroot = Tk()
            erroot.geometry("335x60")
            error_display = input_error(erroot)
            erroot.mainloop()
            sys.exit(0)

        self.list_size = int(self.var1.get())
        self.max_value = int(self.var2.get())
        if self.list_size < 2 or self.list_size > 200:
            self.error_code = "Error 3: Input value for List Size was not a valid numerical entry" + "\nEntry Value must be between 2 and 200"
        if self.max_value < self.list_size:
            if self.error_code != None:
                self.error_code = self.error_code + "\nError 4: Max Value must be larger than List size"
            else:
                self.error_code = "Error 4: Max Value must be larger than List size"
        if self.error_code != None:
            root.destroy()
            erroot = Tk()
            erroot.geometry("335x60")
            error_display = input_error(erroot)
            erroot.mainloop()
            sys.exit(0)

        root.destroy()


class input_error(Frame):
    '''This Class is for error display. Specifically for when input values cannot be translated into a usable function'''

    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        self.master.title("INPUTERROR: Please See Below")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # These two vars will be referencable as standard string vars to receive the user entry at the global scope
        self.list_size = None
        self.max_value = None

        # These two vars are the entry vars specifically for tkinter, tkinter uses its own StringVar() function seperate from normal strings... very annoying.
        self.var1 = StringVar()
        self.var2 = StringVar()

        # This is the placement of our labels L entries E and buttons Button
        L1 = Label(self, text=starting_prompt.error_code)
        L1.place(x=1, y=1)

class Solution(Frame):
    '''This Class is the User Interface for the application.  It is using tkinter for the UI see tkinter documentation for more info'''
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        self.master.title("Buh-Dad Sorting Alg With a UI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        #These two vars will be referencable as standard string vars to receive the user entry at the global scope
        self.list_size = None
        self.max_value = None

        #These two vars are the entry vars specifically for tkinter, tkinter uses its own StringVar() function seperate from normal strings... very annoying.
        self.var1 = StringVar()
        self.var2 = StringVar()

        # This is the placement of our labels L entries E and buttons Button
        L1 = Label(self, text="Original Unsorted List:")
        L1.place(x=5,y=15)
        L2 = Label(self, text=unsort_list)
        L2.place(x=5, y=35)
        L3 = Label(self, text="Sorted List:")
        L3.place(x=5, y=175)
        L4 = Label(self, text=sorted_list)
        L4.place(x=5, y=190)
        quitButton = Button(self, text="Quit", command= self.client_exit)
        quitButton.place(x=225, y=330)
    def client_exit(self):
        root.destroy()

if __name__ == "__main__":
    #This is the initializing and running of our prompt window.
    root = Tk()
    root.geometry("500x150")
    starting_prompt = prompt(root)
    root.mainloop()
    if starting_prompt.error_code != None:
        sys.exit(0)
    list_size = starting_prompt.list_size
    max_value = starting_prompt.max_value

    unsort_list = list_maker(list_size,max_value)
    sorted_list = dad_sorter(unsort_list,list_size,max_value)

    sorted_list = list_chopper(sorted_list)
    unsort_list = list_chopper(unsort_list)
    root = Tk()
    root.geometry("500x375")
    ending_prompt = Solution(root)
    root.mainloop()

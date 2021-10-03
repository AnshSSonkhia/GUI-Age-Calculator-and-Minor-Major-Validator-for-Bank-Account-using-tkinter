from tkinter import *
from tkinter import ttk
import datetime

# function to calculate age
def getAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

# function to check for leap year
def isLeapYear(year):
    
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
       return False

# function to get input
def getInput():
    # Clear textArea for every new input check
    if len(textArea.get('1.0', 'end-1c')) > 0:
        textArea.delete('1.0',END)
    
    inputName = nameEntry.get()

    # name should be greater than 0
    if len(inputName) <= 0:
        textArea.insert(END, "Error: Name must be entered\n")
        return

    # try block for input Day
    try:
        inputDay = int(dayEntry.get())
        if inputDay <= 0 or inputDay > 31:
            textArea.insert(END, "Error: Please enter correct Day\n")
            return
    except:
        textArea.insert(END, "Error: Please enter correct Day\n")
        return
    
    # try block for input Month
    try:
        inputMonth = int(monthEntry.get())
        if inputMonth <= 0 or inputMonth > 12:
            textArea.insert(END, "Error: Please enter correct Month\n")
            return
    except:
        textArea.insert(END,"Error: Please enter correct Month\n")
        return
    
    # try block for year
    try:
        inputYear = int(yearEntry.get())
        if inputYear <= 0 or inputYear > datetime.date.today().year:
            textArea.insert(END, "Error: Please enter correct Year\n")
            return
    except:
        textArea.insert(END, "Error: Please enter correct Year\n")
        return
        

    try:
        givenDate = datetime.date(inputYear,inputMonth,inputDay)
        # check for if given DOB is greater than today's date
        if givenDate > datetime.date.today():
            textArea.insert(END, "Error: Please enter correct DOB\n")
            return
    except:
        textArea.insert(END,"Error: Please enter correct Birth Day\n")
        return
    
    # textArea.delete(0,END)
    userAge = getAge(givenDate)
    textArea.insert(END,f"{inputName} your age is {userAge} years\n")
    textArea.insert(END,"*********Account Eligibility*********\n")
    if userAge >= 18:
        textArea.insert(
            END, f"{inputName}, you are a major and eligible\n for a bank account\n")
    else:
        textArea.insert(
            END, f"{inputName}, you are a minor and not eligible\n for a bank account\n")

def clearAll():
    nameEntry.delete(0,END)
    dayEntry.delete(0,END)
    monthEntry.delete(0,END)
    yearEntry.delete(0,END)
    textArea.delete('1.0', END)

if __name__ == "__main__":
    # Create an instance of tkinter frame
    win = Tk()
    win.title("Bank Account Eligibilty Finder")
    win.geometry("700x700")
    
    frame = Frame(win, relief='sunken', bg="black")
    frame.pack(fill=BOTH, expand=True, padx=10, pady=20)
    
    label = Label(frame, text="Welcome to Bank Account Eligibilty Finder",font=('Helvetica 15 bold'), bg="white")
    label.grid(padx=10,pady=20)

    nameLabel = Label(frame,text="Enter your name",bg="white",width=20)
    nameLabel.grid(row=1,column=0,pady=10)
    nameEntry = Entry(frame)
    nameEntry.grid(row=1,column=1,padx=10,pady=10)
    
    dateOfBirthLabel = Label(frame, text="Date of Birth",
                             font=('Helvetica 13 bold'), bg="white",width=10)
    dateOfBirthLabel.grid(padx=10,pady=20)
    
    dayLabel = Label(frame, text="Enter birth day", bg="white", width=20)
    dayLabel.grid(row=3, column=0, pady=10)
    dayEntry = Entry(frame)
    dayEntry.grid(row=3, column=1, padx=10, pady=10)
    
    monthLabel = Label(frame, text="Enter birth month", bg="white", width=20)
    monthLabel.grid(row=4, column=0, pady=10)
    monthEntry = Entry(frame)
    monthEntry.grid(row=4, column=1, padx=10, pady=10)
    
    yearLabel = Label(frame, text="Enter birth year", bg="white", width=20)
    yearLabel.grid(row=5, column=0, pady=10)
    yearEntry = Entry(frame)
    yearEntry.grid(row=5, column=1, padx=10, pady=10)

    textArea = Text(master=frame, height=10, width=50)
    textArea.grid(row=7,pady=10,columnspan=2)

    checkButton = Button(frame,text="Check Validity",command=getInput,bg='gold',width=30)
    checkButton.grid(row=6,column=0,pady=20)

    clearButton = Button(frame,text="Clear All",command=clearAll,bg='red',width=20)
    clearButton.grid(row=6,column=1)
    win.mainloop()

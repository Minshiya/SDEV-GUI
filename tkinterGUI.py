from tkinter import *
import threading
import time


# Shows a popup window with a message in case of bad input
def show_popup(message):
    popup = Toplevel(root)  # Creates new window with Toplevel widget
    popup.title("Reminder")  # Sets the window title to "Reminder"
    popup.geometry("300x150")  # Size of the popup window
    popup.configure(bg="pink")  # Background color to pink

    lines = message.split(" / ")  # Split message into lines based on "/"

    for line in lines:
        label = Label(popup, text=line, bg="pink")  # Create label
        label.pack()  # Add label to window

    popup_button = Button(popup, text="OK", command=popup.destroy)  # Create button to close the window
    popup_button.pack()  # Add button to window


# Function to start countdown timer for session and break
def countdown(session_length, break_length):
    while True:
        # Session countdown
        for remaining_time in range(session_length, 0, -1):
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            timer_label.config(text=f"Session: {minutes} minutes {seconds} seconds")  # Update timer label
            time.sleep(1)  # Sleep for 1 second
        timer_label.config(text="Session's up!")  # Notify when session is over

        # Break countdown
        for remaining_time in range(break_length, 0, -1):
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            timer_label.config(text=f"Break: {minutes} minutes {seconds} seconds")  # Update timer label
            time.sleep(1)  # Sleep for 1 second
        timer_label.config(text="Break's up!")  # Notify when break is over


# Function to start the countdown timer
def start_countdown():
    session_length_input = entry_session_length.get()  # Get session length input
    break_length_input = entry_break_length.get()  # Get break length input

# Validate input
    if not session_length_input or not break_length_input:
        show_popup("Please enter values \n in both session and \n break length boxes.")
        return

    if not session_length_input.isdigit() or not break_length_input.isdigit():
        show_popup("Please enter numerical values for session and break lengths.")
        return

# Convert input to integers and make sure they're within valid range
    session_length = int(session_length_input) * 60 if 1 <= int(session_length_input) <= 60 else 60
    break_length = int(break_length_input) * 60 if 1 <= int(break_length_input) <= 60 else 10

    if session_length != 60 or break_length != 10:  # Check if session and break lengths are not the default values
        countdown_thread = threading.Thread(target=countdown, args=(session_length, break_length))
        countdown_thread.start()  # start countdown timer
    else:
        show_popup("Please enter valid session and break lengths.")


# Function to validate input
def validate_input(new_text):
    if new_text.isdigit() and 1 <= int(new_text) <= 60:
        return True
    else:
        return False


# Path to background image for main screen
image_path = "images/mainScreenImage.gif"

root = Tk()  # Creates the main window
root.title("Study Buddy")  # Sets the window title
root.geometry("1024x1024")  # sets the window size

bg_image = PhotoImage(file=image_path)  # Loads background image
background_label = Label(root, image=bg_image)  # Creates a label to display the background image
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place the label to cover the entire window

left_frame = Frame(root)  # Creates a frame for the left side elements
right_frame = Frame(root)  # Creates a frame for right side elements

# Places left frame in the center horizontally and midway vertically
left_frame.place(relx=0.25, rely=0.5, anchor=CENTER)
# Places right frame in the center horizontally and midway vertically
right_frame.place(relx=0.75, rely=0.5, anchor=CENTER)

# Create "Start Timer" button on the left frame
button_left = Button(left_frame, text="Start Timer", bg="pink", width=15, height=3, command=start_countdown)
button_left.pack()  # Add button to left frame
# Create "Pause Timer" button on right frame
button_right = Button(right_frame, text="Pause Timer", bg="pink", width=15, height=3)
button_right.pack()  # Add button to right frame

# Create label to display timer
timer_label = Label(root, text="Session: 60 minutes", font=("Helvetica", 16))
timer_label.place(relx=0.5, rely=0.3, anchor=CENTER)  # Label placement

# Create entry widget and label for session length
entry_session_length_label = Label(root, text="Session Length (1-60 minutes):")
entry_session_length_label.place(relx=0.5, rely=0.05, anchor=CENTER)  # Label placement
validate_input_cmd = root.register(validate_input)
entry_session_length = Entry(root, validate="key", validatecommand=(validate_input_cmd, "%P"))
entry_session_length.place(relx=0.5, rely=0.1, anchor=CENTER)  # Label placement

# Create entry widget and label for break length
entry_break_length_label = Label(root, text="Break Length (1-60 minutes):")
entry_break_length_label.place(relx=0.5, rely=0.15, anchor=CENTER)  # Label placement
entry_break_length = Entry(root, validate="key", validatecommand=(validate_input_cmd, "%P"))
entry_break_length.place(relx=0.5, rely=0.2, anchor=CENTER)  # Label placement

root.bg_image = bg_image  # Save background image reference
root.mainloop()  # Start the main event loop

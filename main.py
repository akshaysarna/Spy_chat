# importing datetime library
from datetime import datetime
# importing object of class Spy and chatMessage From hello.py
from  spy_details import spy, Spy, friend, chatMessage
# importing Steganography class from python library steganography
from steganography.steganography import Steganography
from tabulate import  tabulate

from termcolor import colored
from colorama import Fore

# Creating Default Status Message from which user can select the status
STATUS_MESSAGES = ['Busy', 'At Gym', 'Available']



# creating function to read chat history from selected friends
def read_chat_history():
    # choosing friend by calling function select_friend()
    read_for = select_friend()
    # Selecting chat for the selected friend with sending time.
    for chat in friend[read_for].chat:
        # To check whether the chat are send by me or not.
        if chat.send_by_me:
            # printing time date and year with the send message.
            print "[%s] %s %s" % (chat.time.strftime("%d %B %Y"), 'Chat:', chat.message)
        else:
            # if chat senc by my friend not by me.
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friend[read_for].name, chat.message)


# creating funtion to send message to the selected friend
def send_message():
    # calling function select_friend
    friend_choice = select_friend()
    # Describing the name and location of original image
    original_image = raw_input("Name of The Image:")
    # Describing the path where our output message is stored
    output_path = 'output.jpg'
    sub=' '
    # What message do we want to send to the user
    text = raw_input("What Secret Message:")
    if text.count(sub)>=20:
        print "Error."
    # The message is encoded through the Steganography encode method
    else:
        Steganography.encode(original_image, output_path, text)
    # Message is send by me.
        new_chat = chatMessage(text, True)
    # Adding details to friend list about chat send by me/user
        friend[friend_choice].chat.append(new_chat)
    # printing message to notify that  message is sent.
        print "Your Chat Message is Ready."


# Creating method to read message send by friend
def read_message():
    # Selecting friend from which we want to read the message.
    sender = select_friend()
    # output path describing the location of the file.
    output_path = raw_input("What is The Name of File.")
    # Decoding the message send in the given image.
    secret_text = Steganography.decode(output_path)
    # storing that message to new_chat send by friend
    new_chat = chatMessage(secret_text, False)
    # print the message send by friend
    print secret_text
    # friend sended message to enlisted in the message send by the selected friend
    friend[sender].chat.append(new_chat)
    # printing to notify that message is being saved.
    print "Your Secret Message is been Saved."



# Function to select a friend for sending message or reading chat history.
def select_friend():
    # declaring number variable to be displayed with selected friend
    number = 0
    # choosing a friend from friend list
    for friends in friend:
        # printing friend NAME and number variable
        print " %d. Name: %s  Age: %d Rating: %.1f "%(number+1,friends.name,friends.age,friends.rating)
        # increasing no to differentiate the friend
        number = number + 1
        # choosing friend from above printed list
    friends_choice = int(raw_input("Choose Your friend."))
    # list start from 0 but number starts from 1 to to point the list to choosen friend we decrease friend_choose by 1
    friends_position = friends_choice - 1
    # Returning the friend position.
    return friends_position


# Creating a funtion to add friend to the list.
def add_friend():
    # new_friend is object of Spy class.
    new_friend = Spy("", "", 0, 0.0)
    # Adding details for new friend.
    new_friend.name = raw_input("Please  add your friends name:")

    new_friend.salutattion = raw_input("Mr. or Mrs.")
    new_friend.age = int(raw_input("Age:"))
    new_friend.rating = float(raw_input("Spy Rating:"))

    # checking condition that is he eligible to be a spy or not
    if len(new_friend.name) > 0 and 12 < new_friend.age < 50 and 0.0 <= new_friend.rating <= 5.0:
        # if conditons are true than add to friend list
        friend.append(new_friend)
        # and to notify us print friend added statement.
        print "friend Added."
    # If condition are not valid.
    else:
        # Then friend entry won't be accepted.
        print "Enter Valid Entry."
    # returning the lenght of friend list.
    return len(friend)


# Function for adding status.
def add_status():
    # updated_status_message is variable to be returned.
    updated_status_message = None
    # if there is a status than this line would be executed.
    if spy.current_status_message != None:
        # And print the given status.
        print 'Your current status message is %s \n' % (spy.current_status_message)
    # IF there is no status
    else:
        print "No Status."
    # To ask user if he want to select from default status or not.
    default = raw_input("Do You Want to Select From Previous Status(Y/N)")
    # convert y to Y and all the lowercase alphabet to uppercase
    default = default.upper()
    # IF user don't want a default status
    if default == 'N':
        # than we ask him for a new status.
        new_status_message = raw_input("What status message do you want to set? ")
        # checking len of new status
        if len(new_status_message) > 0:
            # if length is more than zero than we add status to Status message list.
            STATUS_MESSAGES.append(new_status_message)
            # and new status is updated.
            updated_status_message = new_status_message
    # if user want from default status
    elif default == 'Y':
        # then we display status using for loop
        item_postion = 1
        for message in STATUS_MESSAGES:
            print "%d.%s" % (item_postion, message)
            item_postion = item_postion + 1
        # then we take input from user that he want which status.
        message_selection = int(raw_input("\n Choose From the Above."))
        # then check condition is valid or not.
        if len(STATUS_MESSAGES) >= message_selection - 1:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
    # else we return invalid input.
    else:

        print 'The option you chose is not valid! Press either y or n.'
    # than return updated message.
    return updated_status_message


# method to select what funtion user wants to do.
def start_chat(spy):
    show_menu = True
    # we take input from user about task he wants to do and check if it is valid or not
    while show_menu:
        menu = raw_input(
            "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n")
        menu = int(menu)
        if menu == 1:
            spy.current_status_message = add_status()
            print "Updated Status is:%s" % (spy.current_status_message)
        elif menu == 2:
            no_friend = add_friend()
            print "\nTotal No. of Friend:%d" % (no_friend)
        elif menu == 3:
            send_message()
        elif menu == 4:
            read_message()
        elif menu == 5:
            read_chat_history()
        elif menu == 6:
            show_menu = False


# we take default user or new user
user = raw_input("Continue as default user(Y|N):")
user = user.upper()
# if default we call the spy object from hello.py
if user == 'Y':
    print "Welcome %s \n Age:%d \nRating:%.1f" % (spy.name, spy.age, spy.rating)
    print "One of the Best Spy"
    start_chat(spy)

# we take input from the user and check whether the conditions are valid or not.
else:
    spy = Spy("", "", 0, 0.0)
    spy.name = raw_input("Enter Your name:")
    if len(spy.name) > 0:
        spy.salutattion = raw_input("Mr.or Mrs.")
        if len(spy.salutattion) > 0:
            spy.age = int(raw_input("Age:"))
            if 18 <= spy.age <= 50:
                spy.rating = float(raw_input("Rating:"))
                if 0.0 <= spy.rating <= 5.0:
                    print "Spy Rating:%.1f" % (spy.rating)
                    # checking whether spy_rating good average or bad through conditioning loops.
                    if spy.rating >= 4.5:
                        print "One of the best Spy."
                    elif 4.5 > spy.rating >= 3.5:
                        print "Better than most Spies."
                    elif 3.5 > spy.rating >= 2.5:
                        print "Need to improve."
                    else:
                        print "Not for Field Work."
                    start_chat(spy)
                else:
                    print "Enter a valid Entry."
            else:
                print "Not elligible to be a Spy."
        else:
            print "Please Mention Your Salutation."
    else:
        print "Enter a Valid Name."

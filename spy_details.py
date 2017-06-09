#importing datetime library
from datetime import datetime
#Creating class spy
class Spy:
    #creatind constructor for spy class for getting valid input.
    def __init__(self,name,salutattion,age,rating):
        self.name= name
        self.salutattion= salutattion
        self.age= age
        self.rating = rating
        self.chat=[]
        self.online =True
        self.current_status_message=None
#creating class chatMessage
class chatMessage:
    # creatind constructor for chatMessage class for getting valid input.
    def __init__(self,message,send_by_me):
        self.message = message
        self.time = datetime.now()
        self.send_by_me = send_by_me
#Creating object of Spy class
spy= Spy("Akshay Sarna","Mr.",21,4.7)
friend_one =Spy("Aditya","Mr.",20,4.0)
friend_two= Spy("Abhinav","Mr.",21,4.1)
friend_three=Spy("Rahul","Mr.",22,4.4)
#adding object to friend.
friend =[friend_one,friend_two,friend_three]
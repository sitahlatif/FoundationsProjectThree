# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Sitah Latif"
my_age = 23
my_bio = "Me, Myself. and I"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)


def choices():
    print("-------------------")
    print("Would you like to:")
    print("1)Creat a new club.\n or:")
    print("2)Browse and join clubs.\n or:")
    print("3)View existing clubs.\n or:")
    print("Display members of a club. \n or:")
    print("-1)close application")

def options():
    # your code goes here!
    choices()
    user =input()
    while True:
        if user == "1":
            create_club()
        elif user == "2":
            join_clubs()
        elif user =="3":
            view_clubs()
        elif user == "4":
            view_club_members()
        elif user == "-1":
            break
        else:
            print("Not correct option")
        choices()
        user =input()
      

def create_club():
    # your code goes here!
  
  name =input("Pick a name for your awesome new club:")
  about=input("What is your club about?")
  n_club = Club(name,about)
  #to add myself to the new club
  n_club.recruit_member(myself)
  n_club.assign_president(myself)
  print("Enter the number of the people you would like to recruit to your new club (-1 to stop)")
  print("------------------------------------------")
  for index, member in enumerate (population): 
    print ("[%d] %s"%(index+1,member.name))
  mem = int(input())
  stop=True
  while stop:
    if len(population)>= mem and mem >0 :
       n_club.recruit_member(population[mem-1])
       mem=int(input())
    else:
       stop= False
  clubs.append(n_club)
  print("Here's your club:")
  print("%s"%(name))
  print("%s"%(about))
  n_club.print_member_list()
  
  

    

def view_clubs():
    # your code goes here!
    for c in clubs:
        m = len(c.members)
        print("\t Name: %s"%(c.name))
        print("\t DESCRIPTION: %s "%(c.description))
        print("\t MEMBERS: %s"%(m))

def view_club_members():
    # your code goes here!
    view_clubs()

    user = input("Enter the name of the club whose members you'd like to see: ")
    for c in clubs:
        if user.lower() == c.name.lower() :
            c.print_member_list()
    

    

def join_clubs():
    # your code goes here!
    view_clubs()
    user = input("Enter the name of the club you'd like to join:")
    for c in clubs:
      if user.lower() == c.name.lower():
        c.recruit_member(myself)
        print ("%s just joined %s"%(myself.name, user)) 
        break
    

def application():
    introduction()
    options()
    # your code goes here!
    

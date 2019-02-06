# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
       self.name= name
       self.bio = bio
       self.age = age

class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description= description
        self.president = None
        self.members=[]


    def assign_president(self, person):
        self.president =person
        # your code goes here!


    def recruit_member(self, person):
        # your code goes here!
        self.members.append(person)


    def print_member_list(self):
        # your code goes here!
        print("Members: ")
        total= 0 
        for member in self.members:

            txt = "_" + member.name + "("+ str(member.age) +"years old)"
            if member == self.president:
                txt += ", president"
            else:
                txt += ")"
            txt += member.bio
            print(txt)
            total+= member.age
        l = float(len(self.members))
        avg = total/(l)
        print ("Average age of member is "+ str(avg)+"members")

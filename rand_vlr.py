#Valorant Randomizer
import random
class Vlr_randoms():
    def __init__(self ,agents,con,dul ,sen , ini ):
        self.agents = agents
        self.con = con
        self.dul =  dul
        self.sen = sen
        self.init = ini
    
    def single_agent(self):
        r = random.choice(self.agents)
        return r
    
    def team (self):
        x = 5
        r = random.sample(self.agents , x )
        return r
    def controllar(self ) :
        r =random.choice(self.con)
        return r
    def sentinals(self ):
        r =random.choice(self.sen)
        return r
    def duelist(self ):
        r = random.choice(self.dul)
        return r 
    def Initator(self ):
        r =random.choice(self.init)
        return r
# ================================================================================================================================
Agents = ["Clove", "Omen" , "Brimstone" , "Viper", "Harbor" ,"Astra" ,"Killjoy" , "Sage" , "Chamber" ,"Deadlock", "Cypher",
          "Iso" , "Jett" , "Neon" , "Phoenix" , "Raze" , "Reyna" , "Yoru","Breach" , "Fade"
            , "Gekko" , "KAY/O" , "Skye" , "Sova" , "Tejo" ]
con = ["Clove", "Omen" , "Brimstone" , "Viper", "Harbor" ,"Astra"]
sen = ["Killjoy" , "Sage" , "Chamber" ,"Deadlock", "Cypher" ]
du = ["Iso" , "Jett" , "Neon" , "Phoenix" , "Raze" , "Reyna" , "Yoru"]
init = ["Breach" , "Fade" , "Gekko" , "KAY/O" , "Skye" , "Sova" , "Tejo"]

vr = Vlr_randoms(Agents , con , sen ,du  ,init)

# Iteration of a method
# def count():
#     num = int(input())
#     my_list = []
#     count = 0
#     while count < num:
#         my_list.append(vr.controllar())
#         count += 1
#     return my_list
# def unique() :
#     un_list = []
#     unique_list = count()
#     for i in unique_list:
#         if i not in un_list:
#             un_list.append(i)
#             if un_list:
#                 pass 
#     print(len(un_list))

# unique()














# def count():
#   my_list = []
#   count = 0
#   num =int(input())
#   while count < num :
#       value = vr.controllar()
#       if value not in my_list:
#           my_list.append(value)
#           count += 1
#           return my_list

# count()
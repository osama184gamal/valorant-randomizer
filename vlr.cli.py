from random_vlr import Vlr_randoms
from random_vlr import Agents
from random_vlr import con
from random_vlr import sen
from random_vlr import du
from random_vlr import init
import argparse
import sys
# create parser object
parser = argparse.ArgumentParser(prog='Valorant Randomizer' ,
                                 description="Random Teams and Agents " ,
                                  epilog= "Read the flags carefully" )
## ====================================================================================================================================
# create arguments
parser.add_argument("-o" , help = "Get the single agent " , action = "store_true" )
parser.add_argument("-t" , help = "Get the team " , action = "store_true" )
parser.add_argument("-c" , help = "Get the controller " ,nargs='?' ,type  = int , default = 1 )
parser.add_argument("-s" , help = "Get the sentinal " , nargs='?',type  = int , default = 1 )
parser.add_argument("-d" , help = "Get the duelist" ,nargs='?' ,type  = int , default = 1)
parser.add_argument("-i" , help = "Get the initaitor " , nargs='?',type  = int , default = 1 )

## ====================================================================================================================================
# remember nargs = '?' means no args or one 
# if temp list under condition means what is stored in the temp list depend of the past condtion

# Get the object back which has your arguments that the user will pass using command line
args = parser.parse_args()

# calling the flags
my_list = sys.argv
# print(my_list) ==> output ==> ['Valorant_CLI.py', '-c', '3', '-o', '-t', '-s', '2'] thats why my_list[1:]

final_list = []
temp_list = []
for i in my_list[1:]:
    if i[0] == "-":
        if temp_list:
            final_list.append((temp_list[0],1))
            temp_list.clear()
        temp_list.append(i)        
    
    else:
        temp_list.append(int(i))
        final_list.append(tuple(temp_list))
        temp_list.clear()
if temp_list:
    final_list.append((temp_list[0],1))
    temp_list.clear()    

for x , r in final_list:
    if final_list:
        if x == "-o" and r :
            object = Vlr_randoms(agents = Agents , con=None , dul=None , sen=None,ini=None)
            for _ in range(r) :
                print(f"Single Agent: {object.single_agent()}")
        if x == "-t" and r :
            object = Vlr_randoms(agents = Agents , con=None , dul=None , sen=None,ini=None)
            for _ in range(r) :
                print(f"Your team: {object.team()}")
        if x == "-c" and r :
            object = Vlr_randoms(agents=None, con = con, dul=None, sen=None, ini=None)
            for _ in range(r) :
                print(f"Controllar: {object.controllar()}")
        if x == "-s" and r :
            object =Vlr_randoms(agents=None, con = None, dul= None, sen = sen, ini=None)
            for _ in range(r) :
                print(f"Sentinal: {object.sentinals()}")
        if x == "-d" and r :
            object =Vlr_randoms(agents=None, con = None, dul= du, sen = None, ini=None)
            for _ in range(r) :
                print(f"Duelist: {object.duelist()}")
        if x == "-i" and r :
            object = Vlr_randoms(agents=None, con = None, dul= None, sen = None, ini=init)
            for _ in range(r) :
                print(f"Initator: {object.Initator()}")                       
                                
                        
                

        











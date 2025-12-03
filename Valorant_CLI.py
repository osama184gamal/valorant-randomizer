# from random_vlr import Vlr_randoms
import difflib
import random
from random_vlr import agents
import random_vlr
from random_vlr import data
import argparse
import sys

# create parser object
parser = argparse.ArgumentParser(prog='Valorant Randomizer' ,
                                 
                                 description="Random Teams and Agents " ,
                                 
                                  epilog= "Read the flags carefully" )
## ====================================================================================================================================
# create arguments
parser.add_argument("-er",  help="exclude role", type=str, nargs="+")
parser.add_argument("-e",  help="exclude agent", type=str, nargs="+")
parser.add_argument("-o" , help = "Get the single agent " , action = "store_true" )
parser.add_argument("-t" , help = "Get the team " , action = "store_true" )
parser.add_argument("-c" , help = "Get the controller " ,nargs='?' ,type  = int ,const=1, default = 1 )
parser.add_argument("-s" , help = "Get the sentinal " , nargs='?',type  = int , const = 1,default = 1 )
parser.add_argument("-d" , help = "Get the duelist" ,nargs='?' ,type  = int,const = 1 , default = 1)
parser.add_argument("-i" , help = "Get the initaitor " , nargs='?',type  = int ,const =1, default = 1 )

## ====================================================================================================================================
# remember nargs = '?' means no args or one 
# if temp list under condition means what is stored in the temp list depend of the past condtion

# Get the object back which has your arguments that the user will pass using command line
args = parser.parse_args()
agent_data = data(agents)
# # calling the flags
my_list1 = sys.argv
my_list = my_list1[1:]
# my_list = ["-c", "3", "-e" , "Brimstone" ,"-o" , "2", "-s", "2", "-t"   ]
# my_list = ["-c" , "3" ,"-o", "-t" ]

listy = []

counter = 0


while counter < len(my_list):
    flags = my_list[counter]
    if flags in ["-c" , "-d" , "-s",'-i']:
        try :
            num =  int(my_list[counter + 1])
            counter += 2

        except ValueError:
            num = 1
            counter +=1   
            
        agent = agent_data.list_of_agents(flags , num )
       
        
        if  counter < len(my_list) and my_list[counter] == "-e":
            value = my_list[counter + 1 ]
            role = agent_data.agent[value]["role"]
            agent= agent_data.remove_agent( role , value , num)
            
            counter += 2
        for x in agent:
            listy.append(x)
            if len(listy)  == 5:
                print(listy)
           
    
        continue


   

    elif flags == "-t":
       output= agent_data.team()
       print(output)
       counter +=1
       continue

    
    elif flags == "-o":
        try:
            num = int(my_list[counter + 1])
            counter += 2
        except ValueError:
            num = 1 
            counter += 1
        
        output = agent_data.single_agent(num)       
        print(output)
        
        continue
  
    elif flags == "-er":
        value =  my_list[counter + 1]
        output = agent_data.remove_role(value)
        print(output)
        counter += 2 
        continue
      
    else:
           counter +=1    



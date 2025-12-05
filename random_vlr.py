# Valorant Randomizer
import random
class data() : 
    # define of the data
    def __init__(self , agent):
        self.agent = agent
    
    def list_of_agents(self , role , champ = None , num = 1 ):
        list1 = []
        for i in self.agent:
            if  role[1] in self.agent[i]["role"]:
                   list1.append(i)
                   if champ in list1:
                       list1.remove(champ)
                    
        ran = random.sample(list1 , num )
        return   ran         
    
    def remove_role (self , role ):
        delete_list = []
        list1 = []
        agent = self.agent
        for i , x in agent.items():
            if x["role"] == role:
                delete_list.append(i)
            else:
                list1.append(i)
             
        return random.sample(list1 , 5 ) 
    
    
    def remove_agent(self , role ,champ , num):
        list1 = []
        agent = self.agent
        for i ,x in agent.items():
            if x["role"] == role and x != champ :
                list1.append(i)
    
        return random.sample(list1 , num)                    

 
    def team (self):
        agent = [x for x in self.agent ]
        return random.sample( agent , 5)
    
    def single_agent(self , num):
        agent = [x for x in self.agent ]
        return random.sample(agent , num)

agents = {
    "Clove": {"role": "c"},
    "Omen": {"role": "c"},
    "Brimstone": {"role": "c"},
    "Viper": {"role": "c"},
    "Harbor": {"role": "c"},
    "Astra": {"role": "c"},

    "Iso": {"role": "d"},
    "Jett": {"role": "d"},
    "Neon": {"role": "d"},
    "Phoenix": {"role": "d"},
    "Raze": {"role": "d"},
    "Reyna": {"role": "d"},
    "Yoru": {"role": "d"},
    "Waylay": {"role": "d"},

    "Killjoy": {"role": "s"},
    "Sage": {"role": "s"},
    "Chamber": {"role": "s"},
    "Deadlock": {"role": "s"},
    "Cypher": {"role": "s"},
    "Vyse": {"role": "s"},
    "Veto": {"role": "s"},

    "Breach": {"role": "i"},
    "Fade": {"role": "i"},
    "Gekko": {"role": "i"},
    "KAY/O": {"role": "i"},
    "Skye": {"role": "i"},
    "Sova": {"role": "i"},
    "Tejo": {"role": "i"},
}

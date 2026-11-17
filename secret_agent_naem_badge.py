#Part 1 ask the agent for details
name = input("enter your real name agent ")
gadget = input("enter your favorite gadget ")

#part 2 store the agents detail using differant data types
agent_number = 2011
speed_rating = 9.7
is_active = True

#part 3 print each details along with its data type
print (type(agent_number))

#part 4 type cast the data 
agent_number_text = float (agent_number)
print(agent_number_text)

name2 = name[0:3]
print(name2)
print(name2 + name)
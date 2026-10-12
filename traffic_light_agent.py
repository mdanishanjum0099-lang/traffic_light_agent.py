
table = { "Red": "Stop", "Yellow": "Slow Down","Green": "Go"}

def traffic_light_agent(percept):
    return table[percept]

percept_sequence = ["Red", "Green", "Yellow", "Red"]

print("Percept\t\tAction")

for i in percept_sequence:
    action = traffic_light_agent(i)
    print(i, "\t\t", action)

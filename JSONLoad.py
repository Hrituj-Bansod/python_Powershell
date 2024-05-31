import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
   # print(state['name'] , state['abbreviation'])
   del state['area_codes']

with open('new_state.json' , 'w') as file:
    json.dump(data , file , indent=2)
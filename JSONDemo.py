import json

String = '''
{
    "People" :[
    {
        "Name" : "Hrituj",
        "Email" : "hrituj@gmail.com",
        "Number" : "123456789"
    },
    {
        "Name" : "Nitesh",
        "Email" : "Nitesh@gmail.com",
        "Number" : "987456321"
    },
    {
        "Name" : "Pranav",
        "Email" : "pranav@gmail.com",
        "Number" : "987654321"
    }
    ]
}
'''

data = json.loads(String)

for person in data['People']:     #used to print names from people 
    print(person['Name'])


for person in data['People']:       #used to delete Number of all data
    del person['Number']

new_string = json.dumps(data , indent=2)        #storing data after deletion in new varaible

print(new_string)       #printing new data after deletion
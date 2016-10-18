import json

my_loop = range(6)

my_loop.append("TEST")
my_loop.append("Test2")
my_loop.append({})

my_loop[-1]
my_loop[-1]["ip address"] = "11.11.11.11"
my_loop[-1]["ip address2"] = "22.22.22.22"


#with open("json_loop_test", "w") as f:
print(json.dumps(my_loop, sort_keys=True, indent=2))

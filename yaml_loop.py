import yaml

my_loop = range(6)

my_loop.append("Test1")
my_loop.append("Test2")
my_loop.append({})
my_loop[-1]
my_loop[-1]["ip_address"] = "1.1.1.1"
my_loop[-1]["provider"] = "Cisco"
my_loop[-1]["platform"] = "c7200"

for i in my_loop:
	print i

print yaml.dump(my_loop, default_flow_style=False)

with open("my_yaml_test", "w") as f:

	f.write(yaml.dump(my_loop, default_flow_style=False))


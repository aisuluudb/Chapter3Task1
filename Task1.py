import re

string = input('Please input your text..')
upper = re.findall(r'[A-Z]', string)
lower = re.findall(r'[a-z]', string)
total_upperlower = len(upper) + len(lower)
percentage_lower =  len(lower) * 100/total_upperlower
percentage_upper = len(upper) * 100/total_upperlower
print(percentage_lower)
print(percentage_upper)
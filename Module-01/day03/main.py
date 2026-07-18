import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"transaction.txt")
content = {}
try:
 with open(file_path,"r") as file:
 
    for line in file:
        line = line.strip()
        if not line:
            continue
        key,value = line.strip().split(":", 1)
        content[key] = content.get(key,0) + float(value.strip())


except FileNotFoundError:
 print("File is not Found!")

def write_report(total,file_path):
    sorted_totals = sorted(total.items(),key= lambda item: item[1], reverse=True)
    with open(file_path,"w") as f:
       for name, total in sorted_totals:
          f.write(f"{name}:{total}\n")
write_report(content,"report.txt")
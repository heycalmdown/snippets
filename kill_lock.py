import os
pdbs=[
    'a.pdb',
    'b.pdb',
    'c.pdb',
    ]
for pdb in pdbs:
    a=os.popen('handle %s'%pdb)
    for i in a.readlines():
    if 'devenv.exe' in i:
        j=i.split(':')
        numbers=j[1]
        (pid,handle)=numbers.strip().split(' ',1)
        os.system('handle -c %s -p %s -y'%(handle.strip(), pid.strip()))


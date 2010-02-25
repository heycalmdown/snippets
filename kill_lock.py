#requires: "Sysinternals' Handle"(http://technet.microsoft.com/en-us/sysinternals/bb896655.aspx)
import os, sys

def kill(handle):
	a=os.popen('handle %s'%handle)
	for i in a.readlines():
		if 'devenv.exe' in i:
			j=i.split(':')
			numbers=j[1]
			(pid,handle)=numbers.strip().split(' ',1)
			os.system('handle -c %s -p %s -y'%(handle.strip(), pid.strip()))

if __name__ == '__main__':
	handles=[]
	if 1 < len(sys.argv):
		for i in sys.argv[1:]:
			handles.append(i)
	else:
		handles.append('pre_defined_a.pdb')
		handles.append('pre_defined_b.pdb')
		handles.append('pre_defined_c.pdb')

	while 1:
		for handle in handles:
			kill(handle)
		input()


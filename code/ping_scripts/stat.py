# Script to generate different possible paths depending upon the latency of the n/w
f = open('ping_stat_2_3','r')
str_2_3 = f.readline()
f.close()
f = open('ping_stat_1_3','r')
str_1_3 = f.readline()
f.close()
f = open('ping_stat_1_2','r')
str_1_2 = f.readline()
f.close()

# pathforbidden is used to not support that path. 
pathforbidden = 'none'  
# 1-2
path_1 = float(str_1_2)
path_2 = float(str_1_3)+float(str_2_3)

print("Static Route:")
print (path_1)
#print(path_2)
min_1=min(path_1,path_2)
print("Dynamic Route:")
print (min_1)

if(min_1 == path_1):
	print "1:2:2"
	print "2:1:1"
elif(min_1 == path_2):
	pathforbidden ='1:2' 
	print "1:2:3"
	print "2:1:3"		

# 1-3
path_1 = float(str_1_3)
path_2 = float(str_1_2)+float(str_2_3)

if(pathforbidden!='none'):
	print "1:3:3"
	print "3:1:1"
else:		
	min_1=min(path_1,path_2)
	if(min_1 == path_1 ):
		print "1:3:3"
		print "3:1:1"
	elif(min_1 == path_2):
		pathforbidden ='1:3'
		print "1:3:2"
		print "3:1:2"

# 3-2
path_1 = float(str_2_3)
path_2 = float(str_1_3)+float(str_1_2)

if(pathforbidden!='none'):
	print "3:2:2"
	print "2:3:3"
else:			
	min_1=min(path_1,path_2)
	if(min_1 == path_1):
		print "3:2:2"
		print "2:3:3"
	elif(min_1 == path_2):
		pathforbidden ='3:2'
		print "3:2:1"
		print "2:3:1"
		

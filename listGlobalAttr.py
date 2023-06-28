import netCDF4 as nc
import sys

# ncPath 		= sys.argv[1]
# ncFilename 	= sys.argv[2]

ncPath = "C:\\Users\\eliason\\Desktop\\listGlobalAttr\\"
ncFilename 	= "W_XX-EUMETSAT-Darmstadt,IMG+SAT,MTI1+FCI-2-GII--FD------NC4E_C_EUMT_20210311130000_L2"

ncfile		= nc.Dataset(ncPath+ncFilename,'r+')
print('ncFilename: ', ncFilename)
print('%50s' %'Global Attributes')
print('='*80)

attr_name  = []
atrr_value = []
attr_type  = []
for name in ncfile.ncattrs():
	attr_name.append(name)
	atrr_value.append(getattr(ncfile,name))
	attr_type.append(type(name))
#	print(name, type(name))

attr_list = list(zip(attr_name,atrr_value,attr_type))
attr_list.sort()

f = open("C:\\Users\\eliason\\Desktop\\listGlobalAttr\\attribute.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()
i=0
while i<len(attr_list):
	first  = attr_list[i][0]
	second = attr_list[i][1]
	third  = attr_list[i][2]
#	if second=='':
#		second = "''"

	print('%40s: %s' %(first, second))
	f.write(first + " : " + str(second) +"\n")
 
	i+=1

ncfile.close()
f.close()

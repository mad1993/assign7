###### this is the third .py file ###########

####### write your code here ##########

#creating a database and variable declaration
database={'GUJ':'111','RAJ':'000','MAH':'001','JAM':'110','AHM':'101','SUR':'010','VAD':'011'}
i=1

#main task
while (i==1):
	print 'Press any of the following.'
	print '1 : To Add to the dictionaries.'
	print '2 : To Modify the content in the dictionaries.'
	print '3 : To Delete the content of the dictionaries.'
	print '4 : To Feed the address.'
	print '5 : View current database.'
	task = input()
	
	#code to add data in database
	if task == 1:
		print 'Enter the key to be added.'
		key = input()
		print 'Enter the value to be added.'
		value = input()
		new={}
		new[key]=value
		if key in database.keys():
			print 'Key is already available... USE MODIFY OPTION !'
		else:
			database.update(new)
			print 'Entry successfully added to the database.'
		continue
	#code to modify the data in database
	elif task == 2:
		print 'Enter the key.'
		key = input()
		print 'Enter the modified value.'
		value = input()
		if key in database.keys():
			database[key] = value
			print 'Entry successfully modified to the database.'
		else :
			print 'Key is not available... Try Again !'
		continue
	#code to delete data from the database
	elif task == 3:
		print 'Enter the key to be deleted'
		key = input()
		if key in database.keys():
			del database[key]
			print 'Entry successfully deleted from the database.'
		else :
			print 'Key is not available... Try Again !'
		continue
	#code to view database
	elif task == 5:
		print 'Present database is :'
		print database
		continue
	#code to enter the address and see the code generated if the address is valid
	else :
		print 'Enter name,HouseNo,Colony,Landmark'
		name = input()
		print 'Enter city.'
		city = input()
		print 'Enter district.'
		dist = input()
		print 'Enter State.'
		state = input()
	
		city=city.upper()
		dist=dist.upper()
		state=state.upper()
		
		if state[0:3] in database.keys():
			if city[0:3] in database.keys(): 
				if dist[0:3] in database.keys():
					print "Machine code:CC_NO = %s%s%s"%(database[state[0:3]],database[dist[0:3]],database[city[0:3]])
					print "Human code:H_CC_NO = %s_%s_%s_%s%s%s"%(state[0:3],dist[0:3],city[0:3],database[state[0:3]],database[dist[0:3]],database[city[0:3]])


				else :
					print 'Kidnly update the database!'
			else:
				print 'Kidnly update the database!'
		else:
			print 'Kidnly update the database!'
		continue
		









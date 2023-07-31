from yandex_tracker_client import TrackerClient

org_id='999999'
cloud_org_id='bpf00000000000000000'
token='y0_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
per_page = 1000
client = TrackerClient(token=token, org_id=org_id)
#client = TrackerClient(token=token, cloud_org_id=org_id)


from datetime import datetime 
import pandas as pd
import numpy as np
import os

try:
	all_users=client.users.get_all()
except Exception as e:
	print (e)
if not os.path.isfile("from.txt"): 
	for user in all_users:
		print (str(user.uid) + " " + str(user.email) + " " + str(user.display))
		text_file = open("from.txt", "a")
		text_file.write(str(user.uid) + " # " + str(user.email) + " " + str(user.display) + "\r\n")
		text_file.close()
	print ("Users exported to <from.txt> file. Add second space delimited UID to change person and save it as <to.txt>")

if os.path.isfile("to.txt"): 
	text_file = open("to.txt", "r")
	data = text_file.readlines()
	text_file.close
	for line in data:
		line = line.partition("#")
		line = line[0]
		if (line.split(" " , 2)[1] != "") and (len(line.split(" " , 2)[1]) > 5) :
			print(line.rstrip('\r\n'))
			old_uid = line.split(" " , 2)[0]
			new_uid = line.split(" " , 2)[1]
			pages = 0                           #added
			current_page = 1                    #added
			print ("------Find issues with old Assignee------")
			while (pages < current_page) :                             #added
				try:
					issues = client.issues.find(filter={'assignee': old_uid}, per_page=per_page, page=current_page) #added 
					print ("Total issues: " + str(issues._items_count))                           #added
					print ("Pages: " + str(issues.pages_count))                                   #added
					pages = issues.pages_count                                                    #added
				except Exception as e:
					print (e)

				for issue in issues:
					try:
	#					issue.update(assignee=new_uid)								
						print ("Assignee update: " + str(issue.key))
					except Exception as e:
						print (e)
					if issue.createdBy.id == old_uid:
						try:
	#						issue.update(author=new_uid)
							print ("CreatedBy update: " + str(issue.key))
						except Exception as e:
							print (e)
				pages = pages + 1 # added
			print ("------Find issues with old CreatedBy-------")
			pages = 0                           #added
			current_page = 1                    #added
			while (pages < current_page) :                             #added
				try:
					issues = client.issues.find(filter={'createdBy': old_uid}, per_page=per_page, page=current_page)
					print ("Total issues: " + str(issues._items_count))                           #added
					print ("Pages: " + str(issues.pages_count))                                   #added
					pages = issues.pages_count                                                    #added
				except Exception as e:
					print (e)

				for issue in issues:
					try:
	#					issue.update(author=new_uid)								
						print ("CreatedBy update: " + str(issue.key))
					except Exception as e:
						print (e)
					if (issue.assignee) and (issue.assignee.id == old_uid):
						try:
	#						issue.update(assignee=new_uid)
							print ("Assignee update: " + str(issue.key))
						except Exception as e:
							print (e)
				pages = pages + 1 # added

			print ("------Find issues with old Followers-------")
			pages = 0                           #added
			current_page = 1                    #added
			while (pages < current_page) :                             #added
				try:
					issues = client.issues.find(filter={'followers': old_uid}, per_page=per_page, page=current_page)
					print ("Total issues: " + str(issues._items_count))                           #added
					print ("Pages: " + str(issues.pages_count))                                   #added
					pages = issues.pages_count                                                    #added
				except Exception as e:
					print (e)
       	
				for issue in issues:
					try:
						print ("Followers update:add: " + str(issue.key))
	#					issue.update(followers={'add': new_uid})								
					except Exception as e:
						print (e)
					try:
						print ("Followers update:remove: " + str(issue.key))	
	#					issue.update(followers={'remove': old_uid})								
					except Exception as e:
						print (e)
				pages = pages + 1 # added

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 23:44:09 2016

@author: arpaf
"""

#footer = open("st/footer.html","r")
#footer = open("st/header.html","r")
#footer = open("st/sidebar.html","r")



def create(s):
	struct = open("st/struct.html","r")
	filename=["header2",s,"sidebar","footer"]
	target = open(s+".html","w")
	str_struct = struct.readlines()
	for st in str_struct:
		if("#-#-" in st):
			file = open("st/"+filename[int(st[4:5])-1]+".html","r")
			target.write(file.read())
			file.close()
		else:
			target.write(st)
	target.close()
	struct.close()
	return

def gensite():
	lpage = ["presentation","reglement","palmares","sponsors","programme","calendrier","contact","finale"]
	for page in lpage:
		create(page)
		
if(__name__=='__main__'):
	gensite()
	print("generated")

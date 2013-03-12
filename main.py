import sys
import os

class vdf:
	def fromFile(self):
		with open('files/data.txt', 'r') as f:
			vdfPath = f.readline()
			noPath = "No path given for sharedconfig.vdf. Attempting to detect path."
			if vdfPath.endswith('= '):
				print noPath
				return 0
			else:
				vdfPath = vdfPath[20:].rstrip('\n')
				if os.path.exists(vdfPath):
					return vdfPath
				else:
					print noPath
					return 0
	def auto(self):
		userdata = os.listdir('C:/Program Files/Steam/userdata/')
		if len(userdata) == 1:
			userID = userdata[0]
			path = 'C:/Program Files/Steam/userdata/%s/7/remote/sharedconfig.vdf' % userID
			if os.path.exists(path):
				return path
			else:
				print "Error: Could not find sharedconfig.vdf directory."
				return 0
		else:
			print "Error: Could not find sharedconfig.vdf directory."
			return 0
			
	def getPath(self):
		if self.fromFile() != 0:
			return self.fromFile()
		elif self.auto() != 0:
			return self.auto()
		else:
			pass

def viewCategories():
	with open('files/categories.txt', 'r') as f:
		print f.read()
	
	print "\n"

def mainMenu():
	print "====Main Menu===="
	print "1. View Categories"
	print "2. Edit Categories"
	print "3. Help"
	print "4. Quit\n"
	selection = 0
	selection = raw_input("What would you like to do? ")
	print "\n"
	return selection
	
def editCategories():
	viewCategories()
	old = input("Which category would you like to edit? (Line number only) ")
	new = raw_input("Enter the new name: ")
	
	with open('files/categories.txt', 'r') as f:
		catList = f.readlines()
		f.seek(0)
		catFile = f.read()
	
	print catList[old - 1], "will be changed to", new
	cancel = raw_input("Press Enter to continue, or enter 'q' to cancel. ")
	if cancel == 'q':
		return 0
	else:
		pass
	catList[old - 1] = catList[old - 1].rstrip('\n')
	catFile = catFile.replace(catList[old - 1], new)
	with open('files/categories.txt', 'w') as f:
		f.write(catFile)
	with open(vdf.getPath()) as f:
		steamFile = f.read()
	steamFile = steamFile.replace(catList[old - 1], new)
	with open(vdf.getPath()) as f:
		f.write(steamFile)
	

	
if __name__ == "__main__":
	vdf = vdf()
	while True:
		menuSelection = mainMenu()
		if menuSelection == '1':
			viewCategories()
		elif menuSelection == '2':
			editCategories()
		elif menuSelection == '3':
			with open('Readme.txt', 'r') as f:
				print f.read()
		elif menuSelection == '4':
			break
		elif menuSelection == 't':
			print vdf.getPath()

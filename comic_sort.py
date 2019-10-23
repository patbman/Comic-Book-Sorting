import os
import shutil
import re
from pushbullet import Pushbullet

current=os.getcwd()
new=current[:-5]
pb=Pushbullet(PUSHBULLET KEY REDACTED)

for i in os.listdir():

	if i.endswith('.cbr') or i.endswith('.cbz'):
		if i.lower().startswith('the story'):
			i=i[12:]
		else:
			pass
		matchobj=re.findall(r"\D+", i)
		fileName=re.search("\A.+(.\d{4}.)", i)
		currentPath=current+"\\"+i
		newPath=new+matchobj[0].strip()+"\\"+fileName.group(0)+".cbr"

		if os.path.isdir(new+matchobj[0]):
			
			shutil.move(currentPath, newPath)
			pb.push_note("Comic Added", fileName.group(0)+" was added")

		else:

			os.makedirs(new+matchobj[0])
			shutil.move(currentPath, newPath)
			pb.push_note("Comic Added", fileName.group(0)+" was added")

	else:
         pass


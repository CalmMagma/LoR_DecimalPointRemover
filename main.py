from os import listdir
from os.path import isdir
from os.path import exists
import xml.etree.ElementTree as et

print("-x- Searching for characters skins... -x-\n")

path = "./"
folders = []
newFolders = []

try:
  folders = list(filter(lambda x: isdir(f"{path}\\{x}"), listdir(path)))

except:
  print(f"\n\n\nThere was an error, unable to find characters skins.")

for bruh in folders:
  print(f"> Added {bruh}")
  bruh = bruh + "/ModInfo.xml"
  newFolders.append(bruh)

print("\n-x- Confirming xml files... -x-")

for h in newFolders:
  if (exists(h)):
    pass

  else:
    print(f"! {h} was not found")
    newFolders.remove(h)
print("> All files verified.")

print("\n-x- Removing decimal points... -x-")

for element in newFolders:
  bruh = et.parse(element)
  root = bruh.getroot()
  print(f"* Fixing {element}")
  for thing in root.iter('Head'):
    headX = thing.get('head_x')
    headY = thing.get('head_y')
    headRot = thing.get('rotation')
    

    headX = str(round(float(headX.replace(',','.'))))
    headY = str(round(float(headY.replace(',','.'))))
    headRot = str(round(float(headRot.replace(',','.'))))
    thing.set('head_x', headX)
    thing.set('head_y', headY)
    thing.set('rotation', headRot)

  
  for majig in root.iter('Pivot'):
    pivotX = majig.get('pivot_x')
    pivotY = majig.get('pivot_y')

    pivotX = str(round(float(pivotX.replace(',','.'))))
    pivotY = str(round(float(pivotY.replace(',','.'))))
    majig.set('pivot_x', pivotX)
    majig.set('pivot_y', pivotY)
  

  bruh.write(element)
  print(f"> Fixed {element}")

input("\n-x- All done! Press enter to close the program. -x-")
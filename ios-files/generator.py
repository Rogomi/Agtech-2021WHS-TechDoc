import os
dirStr = os.getcwd() + "/ios-files/"
bg = dirStr + "before-vc.md"
ios = dirStr + "ios.md"
af = dirStr + "after-vc.md"
iosFile = open(ios, "w", encoding='windows-1252')


print("generating beginning doc...")
beforeFile = open(bg, "r", encoding='windows-1252')
iosFile.write(beforeFile.read())
iosFile.close()
beforeFile.close


print("generating vc ...")
iosFile = open(ios, "a", encoding='windows-1252')
iosFile.write("  \n")
for filename in sorted(os.listdir(dirStr + "view-controllers")):

  if filename[len(filename) - 3 : ] != ".md":
    continue
  with open(os.path.join(dirStr, "view-controllers", filename), "r", encoding='windows-1252') as vc:
    print (filename)
    iosFile.write(vc.read())
    iosFile.write(" \n\n")
    vc.close
iosFile.close

print("generating after vc ...")
iosFile = open(ios, "a", encoding='windows-1252')
afterFile = open(af, "r", encoding='windows-1252')
iosFile.write(afterFile.read())
iosFile.close
afterFile.close()
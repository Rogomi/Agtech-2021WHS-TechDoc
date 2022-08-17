import os
dirStr = os.getcwd() + "/ios-files/"
bg = dirStr + "before-vc.md"
ios = dirStr + "ios.md"
af = dirStr + "after-vc.md"
iosFile = open(ios, "w")


print("generating beginning doc...")
beforeFile = open(bg, "r")
iosFile.write(beforeFile.read())
iosFile.close()
beforeFile.close



print("generating after vc ...")
afterFile = open(af, "r")
iosFile.write(afterFile.read())
iosFile.close
afterFile.close()
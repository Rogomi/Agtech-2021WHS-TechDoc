import os
dirStr = os.getcwd() + "/ios-files/"
bg = dirStr + "before-vc.md"
ios = dirStr + "ios.md"
af = dirStr + "after-vc.md"
iosFile = open(ios, "w")


print("generating beginning doc...")
beforeFile = open(bg, "r", encoding="latin-1")
iosFile.write(beforeFile.read())
iosFile.close()
beforeFile.close


# print("generating vc ...")
# iosFile = open(ios, "a")
# iosFile.write("<br/>")
# for filename in sorted(os.listdir(dirStr + "view-controllers")):
#   with open(os.path.join(dirStr, "view-controllers", filename), "r") as vc:
#     print (filename)
#     iosFile.write(vc.read())
#     iosFile.write("<br/></br>")
#     vc.close
# iosFile.close
print("generating after vc ...")
iosFile = open(ios, "a")
afterFile = open(af, "r")
iosFile.write(afterFile.read())
iosFile.close
afterFile.close()
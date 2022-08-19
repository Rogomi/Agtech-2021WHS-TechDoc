import os
dirStr = os.getcwd() + "/ios-files/view-controllers/"
sourcedir = dirStr + "today"

print("converting txt to markdown ...")
print(dirStr)
print(sourcedir)
for filename in sorted(os.listdir(sourcedir)):
  with open(os.path.join(sourcedir, filename), "r", encoding="latin-1") as vc:
    print (filename)
    dire = dirStr + filename.replace(filename[len(filename) - 4 :], ".md")
    newfile = open(dire, "w")
    content = vc.read()
    content.strip()
    # content.replace(" \n", "<br/>")
    newfile.write(content)

    vc.close

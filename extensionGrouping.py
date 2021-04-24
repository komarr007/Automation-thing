import os
import os.path
import shutil

CurrentDir="C:\\your\\directory"
os.chdir(r"C:\\your\\directory") # path must be same with CurrentDir

extent_bag = []

def gathering():
    print("looking extent in directory")
    for i in os.listdir(CurrentDir):
        extension = os.path.splitext(i)[1]
        if extension not in extent_bag:
            extent_bag.append(extension)

    print("done looking for extent")

    print("prepare the subdir")
    for _ in extent_bag:
        if len(_)>7 and len(_)<65 or _ == "":
            extent_bag.remove(_)

    for lowerlist in range(len(extent_bag)):
        extent_bag[lowerlist] = extent_bag[lowerlist].lower()

    print("checking for duplicate")

    set(extent_bag)

    print(extent_bag)

    os.mkdir(CurrentDir + "/dirTarget")

    for directory in extent_bag:
        if directory not in os.listdir(CurrentDir+"/dirTarget"):
            os.mkdir(CurrentDir+"/dirTarget/"+directory)
            print("folder ",directory," has success create")

    print("moving the file")

    for file in os.listdir(CurrentDir):
        loop+=1
        print("loop = ",loop)
        if file != "dirTarget":
            fileExtent = os.path.splitext(file)[1]
            for value in extent_bag:
                if value == fileExtent:
                    try:
                        shutil.move(file,"dirTarget/"+value+"/"+file)
                    except:
                        print(file,"already exist in target directory")

    print("DONE!")

gathering()

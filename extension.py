myDict={
    "py": "python",
    "txt":"text",
    "java": "java",
    "cpp":"c++",
    "c": "c",
    "ppt":"power point presentation",
    "html": "html",
    "jpeg":"image"
    }
#print(myDict)
file = input("Input the file name: ")
split = file.split(".")
for x in myDict:
    
    if(split[-1]==x):
         print("The extension of the file is : "+ "'"+myDict[x]+"'")
    


def main():
    f = open("myfile", "rb")
    mystr = f.read(100)
    spaces = findSpaces(mystr)
    spaces_new = modifyArray(spaces)
    mystr_new = modifyString(mystr,spaces_new)
    out = open("result.csv","w")
    out.write(mystr_new)
    out.close()
    return 0

def modifyString(string,arr):
    new_string = list(string)
    for element in arr[1:-1]:
        new_string[element] = ","
    return ''.join(new_string)

def modifyArray(arr):
    # Always do this
    arr.pop(2)
    arr.pop(3)
    return arr[0:4] + arr[-2:] 

def findSpaces(string):
    arr = [0]
    for i, c in enumerate(string):
        #print i,c
        if (c==" "):
            arr.append(i)
    arr.append(len(string))
    return arr

def printSubstring(string,arr):
    for i in range(len(arr)-1):
        #print(i)
        #print(arr[i],arr[i+1])
        left = arr[i]+1
        if (i==0):
            left = arr[i]
        right = arr[i+1]
        print(string[left:right])
    return 0

if __name__ == "__main__":
    main()

import sys
def mapper():
    for line in sys.stdin:
        line =line.strip()
        line = line.split(",")
        #rangeDict={}
        if len(line) >= 2:
            try:
                data=int(line[0])
                groupId=int((data-1)/10)
                MemoryUtilization= line[3]
                print("%s\t%s" % (groupId,MemoryUtilization))
            except ValueError:
                continue

mapper()

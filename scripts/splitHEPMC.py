import sys


if len(sys.argv) < 4:
    print("Three parameters are required: python splitHepMC.py [input filename] [output filename] [max number of events per output file]")
    exit()

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]
maxNEvents = int(sys.argv[3])

print ("Input file: " + inputfilename)
print ("Output files: " + outputfilename)
print ("Max Number of Events in Output: " + str(maxNEvents))

inputfile = open(inputfilename, "r")
inputEventIndex = -1
currentFileEventIndex = -1;

headerLines = ["","HepMC::Version 2.06.09","HepMC::IO_GenEvent-START_EVENT_LISTING"]
fileEndLine = ["HepMC::IO_GenEvent-END_EVENT_LISTING"]

outputfiles = [outputfilename+"_0"+".hepmc"]
tempOutputfile = open(outputfiles[0], "w")

for l in headerLines:
    tempOutputfile.write(l+"\n")



lineIndex = 0
for line in inputfile:
    lineIndex = lineIndex + 1 #increment line counter

    #print ("line " + str(lineIndex))

    #skip the header
    if lineIndex <= 3:  
        continue

    #end of file
    if "END_EVENT_LISTING" in line:
        break

    #find event line and increment event number
    #print ("line 0:1 = " + line[:2] + "|")
    if line[:2] == "E ":
        #found Event line

        #print (str(currentFileEventIndex) + " " + str(maxNEvents) + " | " + str((currentFileEventIndex+1 >= maxNEvents)))

        if (currentFileEventIndex+1 >= maxNEvents):

            #Close previous file
            tempOutputfile.write(fileEndLine[0]+"\n")
            tempOutputfile.close()

            #Open new file
            fileIndex = len(outputfiles)
            outputfiles.append(outputfilename+"_"+str(fileIndex)+".hepmc")
            tempOutputfile = open(outputfiles[fileIndex], "w") 
            print("Closed file " + str(outputfiles[fileIndex-1]))
            print("Opening new file " + str(outputfiles[fileIndex]))

            #Write the header
            for l in headerLines:
                tempOutputfile.write(l+"\n")

            currentFileEventIndex = 0
        else:
            inputEventIndex = inputEventIndex + 1
            currentFileEventIndex = currentFileEventIndex + 1
    
        if (currentFileEventIndex % 100 == 0):
            print("Writing Event " + str(currentFileEventIndex))

        #write event line, but replace original event counter by the current file event counter
        eventLineList = line.split(" ")
        newEventLine = ""
        for i in range(len(eventLineList)):
            if (i==1):
                newEventLine = newEventLine + str(currentFileEventIndex) + " "
            elif (i==len(eventLineList)-1):
                newEventLine = newEventLine + eventLineList[i]
            else :
                newEventLine = newEventLine + eventLineList[i] + " "
        #print (eventLineList)
        tempOutputfile.write(newEventLine)

    else :
        tempOutputfile.write(line)
    
#write end of hepmc file for last file
tempOutputfile.write(fileEndLine[0]+"\n")


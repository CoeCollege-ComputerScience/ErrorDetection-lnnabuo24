import math


def xorDiv(d,g):
	if len(d) < len(g):
	    # d is too short to xor any further
		return d
	else:
	    # grabs the first len(g) characters of d
	    # aka whats going to get the xor operation
		s = d[:len(g)]
		#print("d: " + d)
		#print("s: " + s)
		
		# xor s and g
		# (after converting them to their integer representation)
		r = int(s,2) ^ int(g,2)
		
		# the lstrip("0b") removes the 0b portion in bin(r)
		# as well as leading zeroes (i think)
		# i think it really removes leading 0s and bs
		# still works to strip off leading 0s (and the 0b)
		return bin(r).lstrip("0b")+d[len(g):]

def CRC(data, generator):
    # it looks like the extra zeroes are already tacked on here
	data += "0" *(len(generator)-1)
	while len(data) >= len(generator):
		data = xorDiv(data, generator)
	#print(data) # the remainder
	return data

def tackOnRemainder(data, generator):
    
    # get the remainder
    remainder = CRC(data, generator)
    
    # i think this is it?
    # unless im mixing up addition and concatenation
    resultingData = data + remainder
    
    #resultingData = bin( int(data, 2) + int(remainder, 2) )[2:]
    
    #print("result: " + resultingData)
    return resultingData

def checkData(dataPlusRemainder, generator):
    
    #dataPlusRemainder = tackOnRemainder(data, generator)
    
    remainder = CRC(dataPlusRemainder, generator)
    print("remainder (binary): " + remainder)
    remainder = int(remainder, 2) # back to an integer
    print("remainder (int): " + str(remainder))
    if remainder == 0:
    #if remainder == "0":
        # data was received correctly
        return True
    else:
        # something corrupted
        return False

dataword = "10011100"
generator = "1001"
cw = CRC(dataword, generator)
print("cw: " + cw)

print( checkData( dataword + cw, generator ) )


#checkData( tackOnRemainder(dataword, generator), generator )


def stringToBinary(someString):
    result = ""
    for char in someString:
        # take char
        # get its integer representation
        # convert that integer to binary
        # and strip off the 0b at the start
        # then make sure its actually 1 byte long (oops, forgot this)
        result += bin( ord(char) )[2:].zfill(8)
    
    return result



#print(stringToBinary("a"))


def binaryToString(someBinary):
    result = ""
    for i in range( len(someBinary) // 8 ):
        # a function to grab a section of binary based on some i
        # might be useful here
        # maybe
        whatSection = someBinary[ i * 8:(i + 1) * 8 ]
        
        # convert whatSection to an integer
        whatSection = int(whatSection, 2)
        
        # then a character
        whatSection = chr(whatSection)
        
        # and tack the character onto the result
        result += whatSection
    
    return result

#print(binaryToString( stringToBinary("a") ))


def readBinaryString(someBinary, dataLength, generator):
    
    currentCharCount = 0
    currentString = ""
    result = ""
    isCurrentLineCorrupted = False
    
    msgSize = 8 + len(generator)
    
    
    for i in range( len(someBinary) // msgSize ):
        # grab the section being read
        whatSection = someBinary[ i * msgSize:((i + 1) * msgSize) ]
        
        # tack on the remainder
        #whatSection = tackOnRemainder(whatSection, generator)
        # (now done inside checkData)
        # nevermind this should just include the remainder?
        
        # okay
        # *tack on the remainder* this time
        #hi = tackOnRemainder(whatSection, generator)
        
        # is it corrupted
        if checkData( whatSection, generator):
            # nope
            print("not corrupted")
        else:
            # yep
            print("is corrupted")
            isCurrentLineCorrupted = True
        #print(whatSection)
        #print(binaryToString(whatSection))
        currentString += binaryToString(whatSection)
        currentCharCount += 1
        
        if currentCharCount == dataLength:
            # this is one full printed line
            print("reset count here")
            
            # if needed, mark this line as corrupted
            if isCurrentLineCorrupted:
                currentString += " (corrupted line)"
            
            # reset variables
            currentCharCount = 0
            isCurrentLineCorrupted = False
            result += currentString + "\n"
            #print(currentString)
            currentString = ""
    
    # add on the current string if anything is left over
    if currentCharCount != 0:
        if isCurrentLineCorrupted:
            currentString += " (corrupted line)"
        result += currentString
    
    result = result.strip()
    print("end: " + result)




def swapBinary(someBinary, index):
    
    if someBinary[index] == "0":
        return someBinary[0:index] + "1" + someBinary[index + 1:]
    else:
        return someBinary[0:index] + "0" + someBinary[index + 1:]

#something = createCRCBinary( stringToBinary("Eeee"), generator )

# represent the message as a binary number
#something = stringToBinary("Eeeeee")

# tack on the remainder
#something = tackOnRemainder(something, generator)

#readBinaryString(something, 8, generator)











#

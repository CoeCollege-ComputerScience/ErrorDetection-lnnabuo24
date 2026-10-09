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
	
	#print("beginning with " + data)
	
	while len(data) >= len(generator):
		data = xorDiv(data, generator)
	print("end: " + data) # the remainder
	
	# wait
	# dont tell me this is the only issue right
	#data = data.zfill( len(generator) )
	if len(data) < len(generator) - 1:
	    #data += "0" * ( len(generator) - 1 - len(data) )
	    data = data.zfill(len(generator) - 1)
    #
    # inhale
    #
    # exhale
    # the issue was that the remainder was too short
    # if the remainder was 1 with a generator of 1001, just "1" would get tacked on
    # i was also storing the wrong number as the remainder, "1" would be stored as "100"
    # (which is not 1 in binary)
	
	#print("end 2: " + data)
	
	#print(" / " + str(int(generator, 2)) + ", rem. " + str( int(data, 2) ) )
	
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
    #remainder = xorDiv(dataPlusRemainder, generator)
    print("[check] remainder (binary): " + remainder)
    
    if remainder == "":
        print("this might be a bad thing here")
        remainder = "0"
    
    remainder = int(remainder, 2) # back to an integer
    print("[check] remainder (int): " + str(remainder))
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
print( checkData(dataword, generator) )


#checkData( tackOnRemainder(dataword, generator), generator )


def stringToBinary(someString):
    result = ""
    for char in someString:
        #print(char)
        # take char
        # get its integer representation
        converted = ord(char)
        # convert that integer to binary
        converted = bin(converted)
        # and strip off the 0b at the start
        converted = converted[2:]
        # then make sure its actually 1 byte long (oops, forgot this)
        converted = converted.zfill(8)
        
        result += converted
    
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




def swapBinary(someBinary, index):
    
    if someBinary[index] == "0":
        return someBinary[0:index] + "1" + someBinary[index + 1:]
    else:
        return someBinary[0:index] + "0" + someBinary[index + 1:]


# okay
# both sides have to agree on the generator
def createCRCFile(someString, dataStringLen, generator):
    print("abcde")
    # i may have been tripping myself up in the instructions
    # i believe i was
    
    result = ""
    
    for i in range( len(someString) // dataStringLen ):
        # read dLen characters at a time
        """
        ending = (i + 1) * dataStringLen
        if ending > len(someString):
            # avoid going over, i think
            ending = len(someString)
        """
        
        # whatSection is a portion of someString
        whatSection = someString[ i * dataStringLen:(i + 1) * dataStringLen ]
        #whatSection = someString[ i * dataStringLen:ending ]
        print("section " + str(i) + ": " + whatSection)
        #print(len(whatSection))
        
        # convert it to binary
        binary = stringToBinary(whatSection)
        
        # add the zeroes here(?)
        # no
        # i think
        #binary += "0" * (len(generator) - 1)
        
        remainder = CRC(binary, generator)
        
        print("[creation] tacked on remainder: " + remainder)
        
        # *THEN* tack on the remainder
        binary += remainder
        #binary = bin( int(binary, 2) + int(remainder, 2) )[2:] + remainder
        
        #print("tacking on " + binary)
        result += binary + "\n"
    
    # remove whitespace
    result = result.strip()
    
    print("result: " + result)
    return result


def readCRCString(someBinary, generator):
    print("hi")
    # okay
    # they *agree* on the generator this time
    splitBinary = someBinary.split("\n")
    result = ""
    
    for line in splitBinary:
        print("line: " + line)
        
        
        
        # okay
        # okay
        # wait
        # line is (d + r)
        # we want to calculate (d - r)
        """
        transmittedRemainder = line[-(len(generator) - 1):]
        print("transmit: " + transmittedRemainder)
        
        minusRemainder = line[0 : len(line) - (len(generator) - 1) ]
        
        dMinusR = int(minusRemainder, 2) - int(transmittedRemainder, 2)
        dMinusR = bin(dMinusR)[2:]
        print("DmR: " + dMinusR)
        print("???: " + CRC(dMinusR, generator))
        
        # wait a second...
        minusRemainder = line[0 : len(line) - (len(generator) - 1) ]
        print("removed remainder: " + minusRemainder)
        checkers = CRC(minusRemainder, generator)
        print("uhhh: " + checkers)
        print("okay? " + CRC(line, generator))
        """
        
        
        #isFine = CRC(something, generator)
        
        isFine = checkData(line, generator)
        print(isFine)
        newLine = binaryToString(line)
        #print("test " + binaryToString(minusRemainder))
        #newLine = binaryToString(minusRemainder)
        if isFine:
            print(line + " is fine")
        else:
            print(line + " is not fine")
            newLine += " (corrupted)"
        
        print("\n---\n")
        result += newLine + "\n"
    
    result = result.strip()
    print("result: " + result)
    return result

print("E: " + stringToBinary("E"))

fakeFile = createCRCFile("hello E", 1, generator)
readCRCString(fakeFile, generator)

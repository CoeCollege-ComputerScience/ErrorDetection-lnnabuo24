
import random

# d1, d2, d4
# 3, 5, 7
# (-1 because python starts at 0)
#p1Indices = {2, 4, 6}

# d1, d3, d4
# 3, 6, 7
#p2Indices = {2, 5, 6}

# d2, d3, d4
# 5, 6, 7
#p3Indices = {4, 5, 6}

# 
#p4Indices = {}


# these are corrected for python indices starting at 0 instead of 1
p1Set = {2, 4, 6}
p2Set = {2, 5, 6}
p3Set = {4, 5, 6}
pSetArray = [p1Set, p2Set, p3Set]
combinedPSet = p1Set | p2Set | p3Set # <- bit of convenience
# ^^^ (gets used like once by the way)

# actually lets me iterate over the sets
# (cant iterate over sets normally)
pSetArray_listVer = []
# iterate over pSetArray
for i in range( len(pSetArray) ):
    # basically create a list with the same values as the set
    # (i dont think order matters here?)
    result = []
    for j in pSetArray[i]:
        result.append(j)
    pSetArray_listVer.append(result)
#print(pSetArray_listVer)


# takes in some binary
# extracts the 4 parity bits from said binary
# (doesnt do any recalculation)
def getParitiesFromBinary(someBinary):
    # indices 1 2 4 8
    # (subtract 1 from each since python indices start at 0)
    return [someBinary[0], someBinary[1], someBinary[3], someBinary[7]]

def compareParities(pString1, pString2):
    
    result = ""
    
    # please dont tell me it was just how i did xor
    # please dont tell me it was just how i did xor
    # please dont tell me it was just how i did xor
    # please dont tell me it was just how i did xor
    """
    for i in range( len(pString1) ):
        if pString1[i] == pString2[i]:
            result += "0"
        else:
            result += "1"
    """
    
    # it wasnt
    # which is both good and bad
    
    for i in range( len(pString1) ):
        if pString1[i] != pString2[i]:
            result += "1"
        else:
            result += "0"
        
    
    print(pString1 + " vs " + pString2 + " -> " + result)
    return result

def swapBinaryDigit(someBinary, index):
    
    print("swapping index " + str(index))
    
    if someBinary[index] == "0":
        return someBinary[0:index] + "1" + someBinary[index + 1:]
    else:
        return someBinary[0:index] + "0" + someBinary[index + 1:]


def recalculateParity(someBinary):
    
    print("i got " + someBinary)
    
    d1 = someBinary[2]
    d2 = someBinary[4]
    d3 = someBinary[5]
    d4 = someBinary[6]
    
    print("d1: " + d1)
    print("d2: " + d2)
    print("d3: " + d3)
    print("d4: " + d4)
    print("-----")
    
    d1_i = int(d1)
    d2_i = int(d2)
    d3_i = int(d3)
    d4_i = int(d4)
    
    p1 = (d1_i + d2_i + d4_i) % 2
    p2 = (d1_i + d3_i + d4_i) % 2
    p3 = (d2_i + d3_i + d4_i) % 2
    #p4 = (p1 + p2 + p3) % 2
    # wait
    # p4 is the parity of bits 1-7
    # i thought it was just the parity of p1, p2, p3
    p4 = 0
    for i in range( len(someBinary) - 1 ):
        #print("adding " + someBinary[i])
        p4 += int( someBinary[i] )
    p4 %= 2
    
    print("p1: " + str(p1))
    print("p2: " + str(p2))
    print("p3: " + str(p3))
    print("p4: " + str(p4))
    result = str(p1) + str(p2) + d1 + str(p3) + d2 + d3 + d4 + str(p4)
    #print("hold on a sec " + someBinary[4:7])
    print("what i think is the recalculated binary: " + result)
    
    # got the 2 parities
    # vvv the parity inside someBinary (not recalculated)
    # note to self, this is a *string*
    transmittedParity = getParitiesFromBinary(someBinary)
    #calculatedParity = [p1, p2, p3, p4]
    # ^^^ the 4 individual named p variables a few lines up:
    transmittedParityString = ""
    for a in transmittedParity:
        transmittedParityString += a
    print("someBinary parity: " + transmittedParityString)
    #compared = compareParities(myParityString[:3], str(p1) + str(p2) + str(p3))
    
    fullCompared = compareParities(transmittedParityString, str(p1) + str(p2) + str(p3) + str(p4))
    compared = fullCompared[:3]
    
    """
    if p4 != p[3] and compared != 000...
    p4 == p[3] and compared == 000 -> false and false -> f
    p4 != p[3] and compared == 000 -> true and false -> f
    
    p3 == p[3] and compared != 000 -> false and true -> f
    p4 != p[3] and compared != 000 -> true and true -> true
    
    
    if !(p4 == p[3] and compared == 000)
    p4 == p[3] and compared == 000 -> !(true and true) -> !true -> f
    p4 != p[3] and compared == 000 -> !(false and true) -> !false -> t
    
    p3 == p[3] and compared != 000 -> !(true and false) -> !false -> t
    p4 != p[3] and compared != 000 -> !(false and false) ->!false -> t
    """
    
    # now to compare them
    
    # note to self
    # p4 is an *integer*
    # transmittedParity[3] is a *string*
    print("p4: " + str(p4))
    print("parity[3]: " + transmittedParity[3])
    
    if str(p4) != transmittedParity[3]:
    #if fullCompared != "0000":
        print("okay, p4 is different, something changed")
        
        if compared != "000":
            print("yep, theres an error, so where is it")
            
            # check where the error actually is
            ones = compared.count("1")
            onesLoc = 0
            for a in range( len(compared) ):
                if compared[a] == "1":
                    #ones += 1
                    onesLoc = a
            
            print("OH NO " + str(ones))
            
            # 1 parity bit changed
            if ones == 1:
                # its an error in the parity
                print("parity error")
                print(onesLoc)
                
                # p1 -> index 1 (on the sheet), onesLoc = 0
                # p2 -> index 2, onesLoc = 1
                # p3 -> index 4, onesLoc = 2
                # p4 -> index 8, onesLoc = 3
                
                # p1 -> 2^0
                # p2 -> 2^1 
                # p3 -> 2^2 
                # p4 -> 2^3 
                # (then subtract 1)
                # p1 = 1 - 1 = 0
                # p2 = 2 - 1 = 1
                # p3 = 4 - 1 = 3
                # p4 = 8 = 1 = 7
                
                #indexToSwap = (2 ^ onesLoc) - 1
                # ^^^ it turns out ^ isnt used for exponents in python
                # that explains a lot
                # https://stackoverflow.com/questions/2451386/what-does-the-caret-operator-do
                indexToSwap = (2 ** onesLoc) - 1
                
                # the ^ *is* used for the xor operator though
                # huh
                # wonder where that would come in handy
                
                return swapBinaryDigit(someBinary, indexToSwap)
                
            elif ones == 2:
                # its an error in the data
                print("data error")
                setsWithErrors = set()
                setsWithoutErrors = set()
                
                for i in range( len(compared) ):
                    if compared[i] == "1":
                        # an error
                        setsWithErrors |= pSetArray[i]
                    else:
                        setsWithoutErrors |= pSetArray[i]
                
                finalSet = setsWithErrors - setsWithoutErrors
                #print(finalSet)
                offendingDigit = finalSet.pop()
                print("the offending index is " + str(offendingDigit))
                
                
                return swapBinaryDigit(someBinary, offendingDigit)
                """
                if someBinary[offendingDigit] == "0":
                    return someBinary[0:offendingDigit] + "1" + someBinary[offendingDigit + 1:]
                else:
                    return someBinary[0:offendingDigit] + "0" + someBinary[offendingDigit + 1:]
                """
            else:
                raise ValueError("pain and suffering")
            
        else:
            print("no, its fine, its just p4")
            return swapBinaryDigit(someBinary, 7)
    else:
        print("everything is fine")
        return someBinary
    
    
    if (str(p4) != transmittedParity[3]) and (compared == "unused because this should never trigger"):
        print("parities are different, there was (likely) an error *somewhere*")
        # now to find out where the error actually is
        
        
        # wait wait wait
        # i think i get it?
        """
        p1 uses d1, d2, and d4
        d1, d2, and d4 are, inside the hamming code, indices 3, 5, and 7
        if you take those indices and convert them to binary
        you get 011, 101, and 111
        so p1, i *think* becomes 
        nevermind i dont get it
        not yet
        
        a = int(compared[0]) * 4
        b = int(compared[1]) * 2 
        c = int(compared[2]) * 1
        
        print("offending digit: " + str(a + b + c))
        """
        
        # check where the error actually is
        ones = 0
        onesLoc = 0
        for a in range( len(compared) ):
            if compared[a] == "1":
                ones += 1
                onesLoc = a
        
        print("OH NO " + str(ones))
        
        if ones == 1:
            # its an error in the parity
            print("parity error")
            print(onesLoc)
            
            # p1 -> index 1 (on the sheet), onesLoc = 0
            # p2 -> index 2, onesLoc = 1
            # p3 -> index 4, onesLoc = 2
            # p4 -> index 8, onesLoc = 3
            
            # p1 -> 2^0
            # p2 -> 2^1 
            # p3 -> 2^2 
            # p4 -> 2^3 
            # (then subtract 1)
            # p1 = 1 - 1 = 0
            # p2 = 2 - 1 = 1
            # p3 = 4 - 1 = 3
            # p4 = 8 = 1 = 7
            
            #indexToSwap = (2 ^ onesLoc) - 1
            # ^^^ it turns out ^ isnt used for exponents in python
            # that explains a lot
            # https://stackoverflow.com/questions/2451386/what-does-the-caret-operator-do
            indexToSwap = (2 ** onesLoc) - 1
            
            # the ^ *is* used for the xor operator though
            # huh
            # wonder where that would come in handy
            
            return swapBinaryDigit(someBinary, indexToSwap)
            
        elif ones == 2:
            # its an error in the data
            print("data error")
            setsWithErrors = set()
            setsWithoutErrors = set()
            
            for i in range( len(compared) ):
                if compared[i] == "1":
                    # an error
                    setsWithErrors |= pSetArray[i]
                else:
                    setsWithoutErrors |= pSetArray[i]
            
            finalSet = setsWithErrors - setsWithoutErrors
            #print(finalSet)
            offendingDigit = finalSet.pop()
            print("the offending index is " + str(offendingDigit))
            
            
            return swapBinaryDigit(someBinary, offendingDigit)
            """
            if someBinary[offendingDigit] == "0":
                return someBinary[0:offendingDigit] + "1" + someBinary[offendingDigit + 1:]
            else:
                return someBinary[0:offendingDigit] + "0" + someBinary[offendingDigit + 1:]
            """
        else:
            raise ValueError("too many errors")
        
        
    else:
        print("parities are fine :)")
        
        if str(p4) != transmittedParity[3]:
            # only p4 corrupted
            # the rest of the parities are fine
            print("p4 did corrupt though, lemme fix that")
            return swapBinaryDigit(someBinary, 7)
        else:
            return someBinary


# takes in a long string of binary that uses hamming codes
# returns the string version (hopefully)
def readHammingCode(hammingBinary):
    
    finalBinary = ""
    
    # go byte by byte
    for i in range( len(hammingBinary) // 8 ):
        
        # i = 0
        # look through 0-8
        
        # i = 1
        # look through 8-16
        
        startingIndex = i * 8
        endingIndex = (i + 1) * 8
        #print(str(startingIndex) + " -> " + str(endingIndex))
        
        # grab the section being looked through
        # (one byte)
        whatSection = hammingBinary[ startingIndex:endingIndex ]
        #print("section: " + whatSection)
        
        # recalculate it to fix it
        print("recalculating " + whatSection)
        whatSection = recalculateParity(whatSection)
        print("result: " + whatSection)
        
        # then combinedPSet holds the indices containing actual data
        # (parity bits are ignored when reading the final data)
        # vvv honestly i couldve just done [2, 4, 5, 6]
        # instead of combining the sets
        # no clue why i didnt
        for j in combinedPSet:
            #print("reading index " + str(j) + " (" + whatSection[j] + ")")
            # tack this into the constructed binary
            finalBinary += whatSection[j]
        #print("---")
    
    #print("constructed binary: " + finalBinary)
    
    # okay, we got the binary
    # now to actually read it as text
    result = ""
    
    # go byte by byte
    for i in range( len(finalBinary) // 8 ):
        # similar to the above, kind of
        # grab a byte
        section = finalBinary[ i * 8: (i + 1) * 8 ]
        
        # use chr() to get the character the byte represents
        newChar = chr( int(section, 2) )
        # tack the character on to the reconstructed string
        result += newChar
    
    print("result: " + result)
    return result

example = "10010100"
#recalc = recalculateParity(example)
#print("hello: " + recalc)
#print("whats up: " + recalculateParity("00110100"))
#print(getParitiesFromBinary(example))
#readHammingCode(recalc * 2)


def nibbleToHam(someBinary):
    # takes in a nibble and returns the hamming code representation
    
    # p1, p2 p3, p4
    parities = [0, 0, 0, 0]
    fakeHamming = "XX" + someBinary[0] + "X" + someBinary[1:] + "X"
    #print("faker: " + fakeHamming)
    #print("original: " + someBinary)
    
    # start calculating the parities
    for whatParity in range( len(pSetArray) ):
        #print(whatParity + 1)
        for index in pSetArray[whatParity]:
            #print("checking index " + str(index) + " (" + fakeHamming[index] + ")")
            # parities[whatParity] is where the index *would* be in a hamming code byte
            parities[whatParity] += int(fakeHamming[index])
            # to get around this i maybe cheat a little
            # slightly
            # with the fakeHamming
        #print("---")
    
    """
    okay, hold on, can i do this without the fake hamming code
    p1 includes indices 2, 4, 6 (d1, d2, d4)
    
    nibble indices
    d1 = index 0
    d2 = index 1
    d3 = index 2
    d4 = index 3
    
    hamming indices (in python)
    d1 = 2
    d2 = 4
    d3 = 5
    d4 = 6
    
    
    we have to go from...
    2 -> 0
    4 -> 1
    5 -> 2
    6 -> 3
    
    integer division?
    (2 - 1) // 2 = 1 // 2 = 0
    (4 - 1) // 2 = 3 // 2 = 1
    (5 - 1) // 2 = 4 // 2 = 2
    (6 - 1) // 2 = 5 // 2 = 2
    
    
    maybe if i pretend indices started at 1?
    (3 - 1) // 2 = 2 // 2 = 1
    (5 - 1) // 2 = 4 // 2 = 2
    (6 - 1) // 2 = 5 // 2 = 2
    (7 - 1) // 2 = 6 // 2 = 3
    
    3 // 2 = 1
    5 // 2 = 2
    6 // 2 = 3
    7 // 2 = 3
    
    """
    
    # now modulo p1-p3
    for i in range(3):
        parities[i] %= 2
    
    # i feel dumb
    # no wonder the i kept getting 1111 whenever index 6 was swapped
    # im not calculating parity here correctly
    
    # it turns out this was not the issue
    # or at least, not the only issue
    
    # p4 isnt here yet
    completeByte = str(parities[0]) + str(parities[1]) + someBinary[0] + str(parities[2]) + someBinary[1:] #+ str(parities[3])
    
    
    for i in completeByte:
        #print("adding " + i)
        parities[3] += int(i)
    #print("done")
    
    parities[3] %= 2
    #print("tacking on " + str(parities[3]))
    
    # then construct the full byte
    #print(someBinary + " -> " + completeByte + str(parities[3]))
    return completeByte + str(parities[3])


def stringToHam(someString):
    
    # okay
    # in one byte...
    # 4 bits are parity
    # other 4 are data
    
    result = ""
    
    for char in someString:
        binary = bin( ord(char) )[2:] # <- lops off the 0b at the start of binary
        binary = binary.zfill(8) # <- remember to extend it so its one full byte
        #print(binary)
        # got one byte
        # now split it into 2
        
        oneHalf = binary[0:4]
        otherHalf = binary[4:]
        #print(oneHalf + "|" + otherHalf)
        
        # for a good few minutes i forgot parity is calculated based on the data
        # im great at this
        #print("AAAAA " + nibbleToHam(oneHalf))
        #print(nibbleToHam(oneHalf) + " " + nibbleToHam(otherHalf))
        result += nibbleToHam(oneHalf) + nibbleToHam(otherHalf)
        # i felt like going nibble by nibble was easier
        # this accomplishes the same thing as a byte to ham function ultimately
    
    return result

def corruptSomeBinary(someBinary, howManyBits):
    corruptedIndices = []
    
    # grab a copy of someBinary
    result = someBinary[:]
    
    for i in range(howManyBits):
        # grab a random index to corrupt
        whatsNext = random.randint(0, len(someBinary) - 1 )
        
        # make sure it isnt an index thats already been corrupted
        if corruptedIndices.count(whatsNext) > 0:
            while corruptedIndices.count(whatsNext) > 0:
                whatsNext = random.randint(len(someBinary))
        
        # mark the now-corrupted index as used
        corruptedIndices.append(whatsNext)
        
        print("corrupting " + str(whatsNext))
        # swap the digit
        result = swapBinaryDigit(result, whatsNext)
    
    return result



example = "10010100"
hello = stringToHam("a")
#hello = corruptSomeBinary(hello, 1)
print("before corruption: " + hello)
#hello = swapBinaryDigit(hello, 6)
print("after corruption: " + hello)
print( "hello? " + readHammingCode(hello) )


# fun fact
# index 6 being corrupted
# is hard for me to fix apparently






#

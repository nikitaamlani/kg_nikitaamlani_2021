class Solution(object):
    def checkOneToOneMapping(self, s1,s2):
        #If the length of first string is not equal to the second string return false
        if len(s1) != len(s2):
            return False
        mapDict ={}
        for i in range(0,len(s1)):
            #checking if the character exists in the dictionary 
            if s1[i] not in mapDict:
                mapDict[s1[i]] = s2[i]
            else:
                if mapDict[s1[i]] != s2[i]:

                    return False
        return True
     
def main():
    import sys
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2] 
        ret = Solution().checkOneToOneMapping(arg1,arg2)
        out = (ret)
        print(out)
    except:
        print("Incorrect Input")

        
if __name__ == '__main__':
    main()

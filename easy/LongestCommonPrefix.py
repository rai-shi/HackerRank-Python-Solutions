
# well that's so much if-else
def longestCommonPrefix_ver1(strs: list[str]) -> str:
    if strs:                                                                    # check if strs is null
        isAnyEmpty = list(map((lambda x: False if x == "" else True), strs))    # check if there is any null item in list
        if all(isAnyEmpty):                                                     # if all item is not empty
            words = strs.copy()                                                 # copy the list in case any problem
            min_length_word = min(words, key= lambda word: len(word))           # find the word with minumum length 
            words.remove(min_length_word)                                       # remove it from the list
            if words:                                                           # if remain list is not null
                min_length = len(min_length_word)                               # get the length of the minimum word
                prefixes = [""]*len(words)                                      # prepare a suffix list for each comparison 
                for idx, word in enumerate(words):                              # for each word in the list
                    for i in range(min_length):                                 # and for each letter in the minimum word
                        if word[i] == min_length_word[i]:                       # compare the letters, if they are matching
                            prefixes[idx] += min_length_word[i]                 # then add this letter to word-min_word comparison prefix index
                        else:                                                   # if they are not matching
                            break                                               # then break the inner loop
                return min(prefixes, key= lambda word: len(word))               # find the minimum prefix and return it, because minimum one is the most common prefix
            else:
                return strs[0]
        else:        
            return ""
    else:
        return ""


# optimum one
def longestCommonPrefix_ver2(strs: list[str]) -> str:
    if not strs:
        return ""
    # find word with the minimum length  
    min_word = min(strs, key=len)
    
    # the longest prefix can be min_word in best situation
    # flow, flower -> flow

    # so compare the letters between min_word and the other words
    # if any mismatch return the match part
    # flow, flight -> fl (returned in 'o' != 'i')
    for idx in range(len(min_word)):
        for word in strs:
            if word[idx] != min_word[idx]:
                return min_word[:idx]
    return min_word




# mylist = ["flower","flow","flight"]
# mylist = ["","flow","flight"]
# mylist = ["a"]
mylist = ["cir","car"]
print(longestCommonPrefix_ver1(mylist))


# mylist = ["flower","flow","flight"]
# mylist = ["","flow","flight"]
# mylist = ["a"]
mylist = ["cir","car"]
print(longestCommonPrefix_ver2(mylist))
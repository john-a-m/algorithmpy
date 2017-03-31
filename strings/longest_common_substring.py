#NOTES

#In mathematics, a subsequence is a sequence that can be derived from another
#sequence by deleting some elements without changing the order of the remaining
#elements.

def lcs_recursive(s1, s2):

    if not s1 or not s2:
        return ''

    c1, s1_remainder, c2, s2_remainder = s1[0], s1[1:], s2[0], s2[1:]
    if c1 == c2:
        return c1 + lcs_recursive(s1_remainder, s2_remainder)
    else:
        return max(lcs_recursive(s1, s2_remainder),
                   lcs_recursive(s1_remainder, s2), key=len)

def lcs_dynamic(s1, s2):
    pass

##    cache = {}
##
##    #build the cache
##    for c1 in s1:
##        for c2 in s2:
##            if c1 == c2:
##                
##
##    #build the LCS from the cache
##    while cache

if __name__ == "__main__":

    assert lcs_recursive('thisisatest', 'testing123testing') == 'tsitest'

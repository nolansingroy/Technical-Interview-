############Q1########


def compare(set1,set2):
  for i in set!:
    if i in set2:
       if set1[i] === set2[i]:
        set.pop(i)
      else: return Flase
    else: return Flase
   if len(set2) == 0:
    return True
  else: 
   return False

def question2(a):
    # make sure a is a string
    if type(a) != str:
        return "Error: a not string!"
    
    # make sure a has at least 2 characters
    if len(a) < 2:
        return a

    # check all possible center of palindrome
    pal_left = 0
    pal_right = 1
    for i in xrange(len(a)-1):
        # check palindrome centered at i
        l,r = longest_palindrome(a, i, i)
        if r-l-1 > pal_right - pal_left:
            pal_right = r
            pal_left = l+1
            
        # check palindrome centered between i and i+1
        l,r = longest_palindrome(a, i, i+1)
        if r-l-1 > pal_right - pal_left:
            pal_right = r
            pal_left = l+1
    return a[pal_left:pal_right]

def test2():
    print "\nTesting 2"
    print "Edge case (not string):", "Pass" if "Error: a not string!" == question2(123) else "Fail"
    print "Edge case (empty string):", "Pass" if "" == question2("") else "Fail"
    print "Case (a = \"a\"):", "Pass" if "a" == question2("a") else "Fail" 
    print "Case (a = \"aa\"):", "Pass" if "aa" == question2("aa") else "Fail"
    print "Case (a = \"ab\"):", "Pass" if "a" == question2("ab") else "Fail"
    print "Case (a = \"aba\"):", "Pass" if "aba" == question2("aba") else "Fail" 
    print "Case (a = \"aaaaaba\"):", "Pass" if "aaaaa" == question2("aaaaaba") else "Fail" 
    print "Case (a = \"abcbaiojadoijaosdj\"):", "Pass" if "abcba" == question2("abcbaiojadoijaosdj") else "Fail" 


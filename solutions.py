############   Question 1    ########

def question1(s,t):
    import collections
    # convert 's' and 't' to lower case
    s = s.lower()
    t = t.lower()
    
    # check if length of 's' is lower than 't'
    if len(s) < len(t):
        return False      
    
    # make a dict of letter counts contained in 't' 
    t_dictionary  = collections.Counter(t)
    
    # for each substring of 's' check whether the dictionary 
    # of str string  substring that matches 't_dict' 
    for i in range(len(s)-len(t)+1):
        #substring = s[i:i+len(t)]                           
        if collections.Counter(s[i:i+len(t)]) == t_dictionary:
            return True
    return False          


print ("\n Q1 results :\n")
print (question1("Udacity", "ud")) #True
print (question1("udacity", "ciy")) #False
print (question1("ty", "udacity")) # fFalse 
print (question1("", "")) # true 


##########  Question 2 ##############

def longest_palindrome(a, left_idx, right_idx):
    # Left_index and right_index are the left and the right element of index
    l = left_idx
    r = right_idx
    while l >= 0 and r < len(a):
        if a[l] == a[r]:
            l -= 1
            r += 1
        else:
            return l, r
    return l, r


def question2(a):
    # Make sure a is a string
    if not isinstance(a, str):
        return "Error input is !string"

    # Make sure a has at least 2 characters
    if len(a) < 2:
        return "sorry you need more then two letter for me to compute :/"

    # Check all possible centers of palindrome
    p_left = 0
    p_right = 1
    for i in xrange(len(a) - 1):
        # Check palindrome is centered at i
        l, r = longest_palindrome(a, i, i)
        if r - l - 1 > p_right - p_left:
            p_right = r
            p_left = l + 1

        # Check palindrome centered is between i and i+1
        l, r = longest_palindrome(a, i, i + 1)
        if r - l - 1 > p_right - p_left:
            p_right = r
            p_left = l + 1
    return a[p_left:p_right]



# Test Cases
print ("\n")
print("\n Question 2 results")
print question2("racecar") # racecar
print question2(1) #  Error input is !string
print question2("z") #  sorry you need more then two letters for me to compute





############# For Question3 #############

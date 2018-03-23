from operator import itemgetter 

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

def question3(G):
    edges, vertices = edgeWeightSort(G) # weight list !sorted by weight
    edges_sorted = sorted(edges, key=itemgetter(0)) #  sort by weight w/edges 
    return verticeConnected(edges_sorted, vertices)


def edgeWeightSort(G):
    edges = []
    vertices = {}
    for startingVertice in G: # transverse the vertices of the sorted by weight 'G'
        vertices[startingVertice] = [startingVertice] # add vertices to dict
        for edge in G[startingVertice]: 
            endingVertice = edge[0]# the other vertice in the edge
            weight = edge[1] # weight of edge between the two vertices
            edges.append([weight, startingVertice, endingVertice]) # list of edge weight and the vertices at the end of the edges
    return edges, vertices


def verticeConnected(edges_sorted, vertices):
    minSpanTree = {} # dict to build answer 

    for edge in edges_sorted: # sorted edged list unpacking
        startingVertice = edge[1] 
        endingVertice = edge[2] 
        weight = edge[0] 

        if startingVertice not in vertices[endingVertice] and endingVertice not in vertices[startingVertice]:
            minSpanTree.setdefault(startingVertice, []).append((endingVertice, str(weight))) # build up dictionary with the vertices and its edges with other verts
            minSpanTree.setdefault(endingVertice, []).append((startingVertice, str(weight))) # add the reverse 
            vertices[startingVertice], vertices[endingVertice] = verticeList(
                vertices[startingVertice], vertices[endingVertice]) # connected vertice to list
    return minSpanTree


def verticeList(vlist1, vlist2):
    vertConcat = vlist1 + list(set(vlist2) - set(vlist1)) # removing the duplicate vertices
    return vertConcat, vertConcat

print ("\n")
print ("------ Question 3 results -------  ")
print question3({}) # {}

print question3({'A': [('B', 2)],
                 'B': [('A', 2), ('C', 5), ('D', 3)],
                 'C': [('B', 5), ('D', 4)],
                 'D': [('C', 4), ('B', 3)]})
# {'A': [('B', '2')], 'C': [('D', '4')], 'B': [('A', '2'), ('D', '3')], 'D': [('B', '1'), ('C', '4')]}

print question3({'A': [('B', 2)],
                 'B': [('A', 2), ('C', 5)],
                 'C': [('B', 5)]})
# {'A': [('B', '2')], 'C': [('B', '5')], 'B': [('A', '2'), ('C', '5')]}



### question 4 #############
def parent(T, n):
        # if variable 'n' exist then return the parent else -1
    numrows = len(T)
    for i in range(numrows):
        if T[i][n] == 1:
            return i
    return -1

def question4(T, r, n1, n2):
    n1_parents = []
    while n1 != r:
        n1 = parent(T, n1)
        n1_parents.append(n1)
    if len(n1_parents) == 0:
        return -1
    while n2 != r:
        n2 = parent(T, n2)
        if n2 in n1_parents:
            return n2
    return -1


print ("\n Results for question 4 \n")
print (question4([[0,1,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [1,0,0,0,1],
                  [0,0,0,0,0]],
                 3,
                 1,
                 4))
# answer 3

print (question4([[0,0,0,0,0],
                  [1,0,0,1,0],
                  [0,1,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]],
                 2,
                 0,
                 3))
# answer 1

print (question4([[0,0,0,0,0,0],
                  [1,0,0,1,0,0],
                  [0,1,0,0,1,0],
                  [0,0,0,0,0,0],
                  [0,0,0,0,0,1],
                  [0,0,0,0,0,0]],
                 2,
                 0,
                 5))
# Answer 2


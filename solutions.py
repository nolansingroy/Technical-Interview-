############Q1########

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
# should print False
print (question1("", "")) 
# should print True 

########################
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


############# For Question3 #############
def question3(G):
    # my implementation of Kruskal's algorithm

    # make sure G is dictionary
    if type(G) != dict:
        return "Error: G is not dictionary!"

    # make sure G have more than one node
    if len(G) < 2:
        return "Error: G has not enough vertices to form edges!"

    # get a set of vertices
    vertices = G.keys()

    # get unique set of edges
    edges = set()
    for i in vertices:
        for j in G[i]:
            if i > j[0]:
                edges.add((j[1], j[0], i))
            elif i < j[0]:
                edges.add((j[1], i, j[0]))

    # sort edges by weight
    edges = sorted(list(edges))

    # loop through edges and store only the needed ones
    output_edges = []
    vertices = [set(i) for i in vertices]
    for i in edges:
        # get indices of both vertices
        for j in xrange(len(vertices)):
            if i[1] in vertices[j]:
                i1 = j
            if i[2] in vertices[j]:
                i2 = j

        # store union in the smaller index and pop the larger index
        # also store the edge in output_edges
        if i1 < i2:
            vertices[i1] = set.union(vertices[i1], vertices[i2])
            vertices.pop(i2)
            output_edges.append(i)
        if i1 > i2:
            vertices[i2] = set.union(vertices[i1], vertices[i2])
            vertices.pop(i1)
            output_edges.append(i)

        # terminate early when all vertices are in one graph
        if len(vertices) == 1:
            break
            
    # generate the ouput graph from output_edges
    output_graph = {}
    for i in output_edges:
        if i[1] in output_graph:
            output_graph[i[1]].append((i[2], i[0]))
        else:
            output_graph[i[1]] = [(i[2], i[0])]

        if i[2] in output_graph:
            output_graph[i[2]].append((i[1], i[0]))
        else:
            output_graph[i[2]] = [(i[1], i[0])]
    return output_graph






############# For Question5 #############
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def get_length(ll):
    # get the length of ll
    # also checking whether the linked list is circular
    # return -1 if the linked list is circular

    # length == 1
    if ll.next == None:
        return 1
    
    length_ll = 0
    current_node = ll
    current_node2 = ll.next
    while current_node != None and current_node != current_node2:
        current_node = current_node.next
        if current_node2 != None:
            current_node2 = current_node2.next
        if current_node2 != None:
            current_node2 = current_node2.next
        length_ll += 1

    if current_node == None:
        return length_ll
    else:
        return -1

def question5(ll, m):
    # make sure ll is a Node
    if type(ll) != Node:
        return "Error: ll not a Node!"

    # make sure m is an integer
    if type(m) != int:
        return "Error: m not an integer!"
    
    # get the length of ll
    length_ll = get_length(ll)

    # make sure ll is not circular
    if length_ll == -1:
        return "Error: circular linked list!"
        
    # make sure m is less than or equal to the length of ll
    if length_ll < m:
        return "Error: m greater than the length of ll!"
    
    # traverse to the last mth element
    current_node = ll
    for i in xrange(length_ll - m):
        current_node = current_node.next
        
    return current_node.data

def test5():
    n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
    n4.next = n5
    n3.next = n4
    n2.next = n3
    n1.next = n2
    
    print "\nTesting 5"
    print "Edge case (ll not Node):", "Pass" if "Error: ll not a Node!" == question5(123, 111) else "Fail"
    print "Edge case (m > length of ll):", "Pass" if "Error: m greater than the length of ll!" == question5(n1, 6) else "Fail"
    print "Case (ll = n1 and m = 3):", "Pass" if 3 == question5(n1, 3) else "Fail" 
    n5.next = n1
    print "Case (circular linked list):", "Pass" if "Error: circular linked list!" == question5(n1, 3) else "Fail" 


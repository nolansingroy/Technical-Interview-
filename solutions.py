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

def bubblesort(a): 
    swaps = 0
    
    for i in xrange(len(a)):
        for j in xrange(len(a)-1):
            temp = a[j+1]
            if (a[j] > a[j+1]):
                swaps += 1
                a[j+1] = a[j]
                a[j] = temp
    
    first = a[0]
    last = a[len(a)-1]
    
    return swaps, first, last

# swaps, first, last = bubblesort(a)
# print ("Array is sorted in %s swaps." % swaps)
# print ("First Element: %s" % first)
# print ("Last Element: %s" % last)
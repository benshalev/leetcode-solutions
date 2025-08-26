# func that sum list of items
# with TCO = tail call optimization

def my_sul(l , carry =0):
    if len(l) == 0:
        return carry
    if len(l) == 1:
        return l[0] + carry
    return my_sul(l[1:], carry + l[0])

print(my_sul([1,2,3,4,5]))
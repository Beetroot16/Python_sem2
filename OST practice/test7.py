def palin(str,start,end):
    if start >= end:
        return True
    if str[start] == str[end]:
        return palin(str,start+1,end-1)
    else:
        return False

palin("racecar",0,6)
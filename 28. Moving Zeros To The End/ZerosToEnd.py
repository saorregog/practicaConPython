def move_zeros(lst):
    result = list(filter(lambda e: e != 0 or type(e) != int, lst)) + list(filter(lambda e: e == 0 and type(e) == int, lst))
    return result

print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))

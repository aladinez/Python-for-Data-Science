def all_thing_is_obj(object: any) -> int:
    objType = type(object)
    if (objType is int) :
        print("Type not found")
    elif (not objType is str) :
        print(objType.__name__.title(), ":", objType)
    else :
        print(object, "is in the Kitchen", ":", objType)
    return 42

def all_thing_is_obj(object: any) -> int:
    objType = type(object)

    if (objType is tuple or objType is list or objType is set or objType is dict) :
        print(objType.__name__.title(), ":", objType)
    elif (objType is str) :
        print(object, "is in the Kitchen", ":", objType)
    else :
        print("Type not found")
    return 42


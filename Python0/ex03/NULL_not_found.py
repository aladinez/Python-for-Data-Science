def NULL_not_found(object: any) -> int:
    ft_dict = {
    "NoneType" : "Nothing", 
    "float" : "Cheese", 
    "int" : "Zero", 
    "str" : "Empty", 
    "bool" : "Fake",
    "list" : "List",
    "tuple" : "Tuple",
    "dict" : "Dictionary",
    "set" : "Set",
    "complex" : "Complex",
    "MyClass" : "User-defined class"
}
    objType = type(object)

    # handle float separately
    if objType.__name__ == "float" and object != object:
        print(ft_dict[objType.__name__], ":" , object, objType)
        return 0
    elif object or object == True or objType.__name__ not in ft_dict:
        print("Type not Found")
        return 1
    else:
        print(ft_dict[objType.__name__], ":" , object, objType)
    
    return 0

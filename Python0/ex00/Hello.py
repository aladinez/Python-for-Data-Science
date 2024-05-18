ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here

del ft_list[1]
ft_list.append("World!")


ft_tuple = ft_tuple[:1] + ("Morocco!",)


# tmpList = list(ft_set)
# tmpList[1] = "Benguerir!"
# ft_set = set(tmpList)
ft_set = {"Hello", "Benguerir!"}


ft_dict["Hello"] = "1337!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
my_dict = {"name":"sang", "country":"Viet Nam"}

# try:
#     print(my_dict["names"])
# except KeyError:
#     print("Not is Found")


# if "name" in my_dict:
#     print(my_dict["name"])
# else:
#     print("Not is Found")
    
# my_dict["age"] = 20
# del my_dict ["name"]

# my_dict.pop("name")
# my_dict.popitem()


# print(my_dict)
# for keyff in my_dict:
    # print(keyff, my_dict[keyff])
# for key, value in my_dict.items():
#     print(key, value)

def unique(str):
    char_test = {}
    for sell in str:
        if sell in char_test:
            return False
        char_test[sell] = True
           
    return True


if __name__ == "__main__":
 str = "a,b,c,a,b"
 print(unique(str))
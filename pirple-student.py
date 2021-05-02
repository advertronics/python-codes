def dict_checker(obj):
	your_key = input("Enter your key: ")
	your_value = input("Enter your value: ")
	for key, val in obj.items():
		if your_key == key and your_value == val:
			return True
	return False

my_dict = {"a":"1", "b": "2"}
print(dict_checker(my_dict))

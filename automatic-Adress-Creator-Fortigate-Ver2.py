WELCOME_MASSAGE = "\n\t\tWelcome!!!\n\t\tThis Moudle Create by Oshri Rabani - https://cybersecil.com . Enjoy!\n"
address_list = []
add_to_group = False


def create_address_list_file (address_list):
	f = open(file_name_export,"w")
	f.write("config firewall address\n")
	if add_to_group:
		for address in address_list:
			full_address = address.split('/')
			f.write("edit N-" + address + "\nset subnet " + full_address[0] + "/" + full_address[1] + "\nnext\n")
		f.write("end")
		f.write("\nconfig firewall addrgrp\nedit "+ group_name + "\nappend member ")
		for address in address_list:
			f.write("N-" + address + " ")
		f.write("\nnext\nend")
	else:
		for address in address_list:
			full_address = address.split('/')
			f.write("edit N-" + address + "\nset subnet " + full_address[0] + "/" + full_address[1] + "\nnext\n")
		f.write("end")
	f.close()


file_path = str(input("Please Enter file location of your address list:\n" ))
file_read = open(file_path, "r")
for line in file_read:
	address_list.append(line.strip())
file_read.close()
file_name_export = str(input("Enter file name to export the address list (This will Be save in the currect Directory) :\n" ))
check_group_add = str(input("if you Want to add your address list to address group, please enter YES, if you don't have just write NO:\n"))
if check_group_add == "YES": 
	add_to_group = True
	group_name = str(input("Please Write the group name you want to add your list\n"))
create_address_list_file(address_list)
print("\n\t\tFile created successfully!" + " the configuration file name is: " + file_name_export + " Good Luck!!\n\t\tVisit us in https://cybersecil.com")

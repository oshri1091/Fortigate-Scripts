WOLCOME_MASSAGE = "\n\t\tWelcome!!!\n\t\tThis Moudle Create by Oshri Rabani - https://cybersecil.com . Enjoy!\n"
INSERT_INTERFACE = "Please Insert a new interface/zone name (if you don't have more interfaces/zones just write FINISH):\n"
FINISH_WORD = "FINISH"
interfaces_list = []
wan_name_interface = ""
check_wan_interface = ""
have_wan_interface = False

'''
    module name: automatic-rules-fortigate.py
    purpose    : create automatic rules for fortigate based on iterfaces/zone names. 
				 this module create rules any to any between all interfaces.
    created    : 2019-05-02
    last change: 2019-05-02

    Copyright by oshri rabani (https://cybersecil.com)
'''

def add_interfaces(interfaces_list):
	update_interface =  str(input(INSERT_INTERFACE))
	while update_interface != FINISH_WORD:
		interfaces_list.append(update_interface)
		update_interface =  str(input(INSERT_INTERFACE))
	create_rules(interfaces_list)

	
def create_rules (interfaces_list):
	f = open(file_name,"w")
	f.write("config firewall policy\n")
	if have_wan_interface:
		for interface_source in interfaces_list:
			for interface_destination in interfaces_list:
				if interface_source == interface_destination:
					continue
				if interface_source == wan_name_interface:
					continue
				if interface_destination == wan_name_interface:
					f.write("edit 0\nset srcintf " + interface_source + "\nset dstintf " + interface_destination + "\nset srcaddr all\nset dstaddr all\nset schedule always\nset service ALL\nset logtraffic all\nset action accept\nset nat enable" +  "\nnext\n")
				else: f.write("edit 0\nset srcintf " + interface_source + "\nset dstintf " + interface_destination + "\nset srcaddr all\nset dstaddr all\nset schedule always\nset service ALL\nset action accept\nset logtraffic all" + "\nnext\n")
	else:
		for interface_source in interfaces_list:
			for interface_destination in interfaces_list:
				if interface_source == interface_destination:
					continue
				else: f.write("edit 0\nset srcintf " + interface_source + "\nset dstintf " + interface_destination + "\nset srcaddr all\nset dstaddr all\nset schedule always\nset service ALL\nset action accept\nset logtraffic all" + "\nnext\n")
	f.write("end")
	f.close()
	
		
	
print(WOLCOME_MASSAGE)
file_name = str(input("Enter file name to export the rules (This will Be save in the currect Directory) :\n" ))
check_wan_interface = str(input("if you have a WAN interface please enter YES, if you don't have just write NO:\n"))
if check_wan_interface == "YES": 
	have_wan_interface = True
	wan_name_interface = str(input("Please Write the WAN name interface\n"))
	interfaces_list.append(wan_name_interface)
	add_interfaces(interfaces_list)
else:	add_interfaces(interfaces_list)
print("\n\t\tFile created successfully!" + " the file name is: " + file_name + " Good Luck!!\n\t\tVisit us in https://cybersecil.com")
	
 

'''
This program is intended to help the user learn about IPv6 addressing.
It includes a shameless plug at the end promoting my IPv6 book,
IPv6 Fundamentals (Cisco Press) and my YouTube playlist on IPv6 (in which 
I receive no revenue). I do this because I like it. :)

Thank you,
Rick Graziani
'''

#!/usr/bin/env python

__author__ = "Rick Graziani"
__copyright__ = "Copyright 2022"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Rick Graziani"
__email__ = "graziani@cabrillo.edu rgrazian@ucsc.edu"
__status__ = "Production-Education"


import ipaddress
import sys
import random
import socket
import requests
import dns.resolver

def ipv6_menu():

    while True:
        #print(chr(27) + "[2J")
        print("\033c", end="")
        print("""
        \rThis program will help you learn about IPv6 addresses!
        """)
        print("\nLEARN ABOUT IPv6 ADDRESSES")
        print("---------------------------")
        print("0. How do we represent an IPv6 address?")  
        print("\nLEARN")      
        print("1. Compress an IPv6 address to its shortest form")
        print("2. Display all 32 hexadecimal digits of an IPv6 address")
        print("3. Display the IPv6 address type and address information")
        print("4. Subnetting an IPv6 network address")
        print("\nSEE")  
        print("5. Display your IPv4 and IPv6 addresses")
        print("6. Enter a URL and get the IPv4 and IPv6 addresses")
        print("\nF. Fun random facts about the number of IPv6 addresses")
        print("Q: Quit")

        
        menu_choice = input("\nEnter you choice: ")

        if menu_choice == "0":
            print("\033c", end="")
            print("\nHow do we represent an IPv6 address?")
            display_ipv6_address()
            back_to_menu = input("\nPress any key to return to menu...")
            continue

               
        if menu_choice == "1":
            print("\033c", end="")
            print("\nThis will display both rules to compress an IPv6 address...")
            print("\nEnter an IPv6 address in longer form such as 2001:0db8:010b:0001:0000:0000:0ab0:abc0")
            ipv6_address = enter_ipv6_address_string()
            ipv6_compress_rules(ipv6_address)
            back_to_menu = input("\nPress any key to return to menu...")
            continue
    
        if menu_choice == "2":
            print("\033c", end="")
            print("\nThis will display all 32 hexadecimal digits of an IPv6 address...")
            print("\nEnter an IPv6 address in a compressed format,") 
            print("such as: 2001:db8:ab::ab3 or fe80::1 or ff02::1:ff93:da0")
            ipv6_address_validate, ipv6_address = enter_ipv6_address()
            ipv6_preferred_address(ipv6_address_validate)
            back_to_menu = input("\nPress any key to return to menu...")
            continue
        
        if menu_choice == "3":
            print("\033c", end="")
            print("\nThis will display the type of IPv6 address...")
            print("\nEnter an IPv6 address to learn more about what type of IPv6 adddress it is,")
            print("such as: 2001:db8:ab::ab3 fe80::1 or ff02::1:ff93:da0")
            ipv6_address_validate, ipv6_address = enter_ipv6_address()
            ipv6_address_type(ipv6_address_validate)
            back_to_menu = input("\nPress any key to return to menu...")        
            continue    

        if menu_choice == "4":
            print("\033c", end="")
            print("\nThis will display IPv6 subnets...")
            display_gua()
        
            while True:
                print("Provide the Global Routing Prefix first (ex. 2001:db8::/32)...")    
                ipv6_net_address, ipv6_net_address_string = enter_ipv6_network_address()
            
                if ipv6_net_address_string.startswith("2") or ipv6_net_address_string.startswith("3"):
                    ipv6_subnets(ipv6_net_address)
                    back_to_menu = input("\nPress any key to return to menu...")        
                    break   
                else:
                    print("Note: Subnetting is usually done with GUA addresses, starting with a 2 or 3...")
                    continue 
            
            continue

        if menu_choice == "5":
            print("\033c", end="")
            print("\nThis will display the IPv4 and IPv6 addresses on your local system...")
            display_local_IP()
            back_to_menu = input("\nPress any key to return to menu...")     
            continue


        if menu_choice == "6":
            print("\033c", end="")
            print("\nThis will display the IPv4 and IPv6 addresses for a given URL,")
            print("such as www.google.com or www.cabrillo.edu ...")
            display_url_IP()
            back_to_menu = input("\nPress any key to return to menu...")     
            continue


        if menu_choice == "F" or menu_choice == "f":
            print("\033c", end="")
            how_many()
            back_to_menu = input("\nPress any key to return to menu...")     
            continue
        
        if menu_choice == "Q" or menu_choice == "q":
            ipv6_fundamentals_book()
            sys.exit()
                
        print("Invalid answer, please try again...")
        continue
        

 

def enter_ipv6_address():

    while True:
        try:
            ipv6_address = input("\nEnter an IPv6 address: ")
            ipv6_address = ipv6_address.strip()
            ipv6_address_validate = ipaddress.IPv6Address(ipv6_address)
            return ipv6_address_validate, ipv6_address
        except:
            print("Invalid IPv6 address, please try again...")
            answer = input("Do you wish to try again? (y/n) ")
            if answer == "Y" or answer == "y":
                continue
            else:
                ipv6_menu()
        else:
            print("Valid IPv6 address")
            break



def enter_ipv6_address_string():
    
    while True:
        try:
            ipv6_address = input("\nEnter an IPv6 address: ")
            ipv6_address = ipv6_address.strip()
            ipv6_address_validate = ipaddress.IPv6Address(ipv6_address)
            return ipv6_address
        except:
            print("Invalid IPv6 address, please try again...")
            answer = input("Do you wish to try again? (y/n) ")
            if answer == "Y" or answer == "y":
                continue
            else:
                ipv6_menu()
                # raise ValueError("Invalid IPv6 address, please try again")
        else:
            print("Valid IPv6 address")
            break
    
            
def enter_ipv6_network_address():
    
    while True:
        try:
            ipv6_net_address = input("Enter an IPv6 network-address/prefix-length: ")
            
            ipv6_net_address_string = ipv6_net_address
            ipv6_net_address = ipaddress.IPv6Network(ipv6_net_address)

            return ipv6_net_address, ipv6_net_address_string
        except:
            print("Invalid IPv6 network address, please try again...")
            answer = input("Do you wish to try again? (y/n) ")
            if answer == "Y" or answer == "y":
                continue
            else:
                ipv6_menu()
        else:
            print("Valid IPv6 network address")
            break


def ipv6_compress_rules(ipv6_address):
    # This is menu item 2

    print("\nRule 1: First rule: Leading zeroes in any 16-bit segment do not have to be written.")
    print("        Only leading 0s can be excluded, or leads to ambiguity.")
    print("Rule 2: Any single, contiguous string of one or more 16-bit segments consisting of") 
    print("        all zeroes can be represented with a double colon (::).")
    print(f"\nYou entered the IPv6 address               {ipv6_address}")

    # Use original ipv6_address variable, not ipv6_address_validate, which is a string
    ipv6_address = ipv6_address.replace(":0", ":")
    ipv6_address = ipv6_address.replace(":0", ":")
    ipv6_address = ipv6_address.replace(":0", ":")

    print(f"\nRule 1: Omitting leading 0s                {ipv6_address}")

    ipv6_address = ipaddress.IPv6Address(ipv6_address)
    print(f"Rule 2: Using :: to replace all-0 hextets  {ipv6_address}")


def ipv6_preferred_address(ipv6_address_validate):
    
    # Next statement the IPv6 in preferred format w/ hextets separated with a "_" and in UPPER case  
    ipv6_preferred = format(ipaddress.IPv6Address(ipv6_address_validate), '_X')

    # Replace "_" with ":"
    ipv6_preferred = ipv6_preferred.replace("_", ":")

    # Replace UPPER case with lower case
    ipv6_preferred = ipv6_preferred.lower()

    print("\nIPv6 addresses are 128-bit addresses represented in:")
    print("   > Hexadecimal: 1 hexadecimal digit = 4 bits")    
    print("   > Eight 16-bit segments or “hextets” (not a formal term) between 0000 and ffff")
    print("   > Each hextet is separated by a colon")
    
    print("""
          0000 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000 
           to     to     to     to     to     to     to     to
          ffff : ffff : ffff : ffff : ffff : ffff : ffff : ffff       
          """)

    print(f"\nYou entered the IPv6 address          {ipv6_address_validate}")
    print(f"Preferred (complete) IPv6 address is  {ipv6_preferred}")       


def ipv6_address_type(ipv6_address_validate):

    IANA_Special_Purpose = [
    {
    "Address" : "::1",
    "Address Block" : "::1/128",
    "Name" : "Loopback Address", 
    "RFC" : "RFC4291", 
    "Source Address" : "No",
    "Destination Address" : "No",
    "Forwardable" : "No",
    "Globally Reachable" : "No"   
    },
    {
    "Address" : "::",
    "Address Block" : "::/128",
    "Name" : "Unspecified Address", 
    "RFC" : "RFC4291", 
    "Source Address" : "Yes",
    "Destination Address" : "No",
    "Forwardable" : "No",
    "Globally Reachable" : "No"   
    },    
    {
    "Address" : "::ffff:0:0",
    "Address Block" : "::ffff:0:0/96",
    "Name" : "IPv4-mapped Address", 
    "RFC" : "RFC4291", 
    "Source Address" : "No",
    "Destination Address" : "No",
    "Forwardable" : "No",
    "Globally Reachable" : "No"   
    },    
    {
    "Address" : "64:ff9b::",
    "Address Block" : "64:ff9b::/96",
    "Name" : "IPv4-IPv6 Translat.", 
    "RFC" : "RFC6052", 
    "Source Address" : "Yes",
    "Destination Address" : "Yes",
    "Forwardable" : "Yes",
    "Globally Reachable" : "Yes"   
    },    
    {
    "Address" : "64:ff9b:1:",
    "Address Block" : "64:ff9b:1::/48",
    "Name" : "IPv4-IPv6 Translat.", 
    "RFC" : "RFC8215", 
    "Source Address" : "Yes",
    "Destination Address" : "Yes",
    "Forwardable" : "Yes",
    "Globally Reachable" : "Yes"   
    },    
    {
    "Address" : "100::",
    "Address Block" : "100::/64",
    "Name" : "Discard-Only Address Block", 
    "RFC" : "RFC6666", 
    "Source Address" : "Yes",
    "Destination Address" : "Yes",
    "Forwardable" : "Yes",
    "Globally Reachable" : "No"   
    },    
    {
    "Address" : "2001:00",
    "Address Block" : "2001::/23",
    "Name" : "IETF Protocol Assignments", 
    "RFC" : "RFC2928", 
    "Source Address" : "No",
    "Destination Address" : "No",
    "Forwardable" : "No",
    "Globally Reachable" : "No"   
    },    
    {
    "Address" : "2001::",
    "Address Block" : "2001::/32",
    "Name" : "TEREDO", 
    "RFC" : "RFC4380", 
    "Source Address" : "No",
    "Destination Address" : "No",
    "Forwardable" : "No",
    "Globally Reachable" : "N/A"   
    },    
    {
    "Address" : "2001:1::1",
    "Address Block" : "2001:1::1/128",
    "Name" : "Port Control Protocol Anycast", 
    "RFC" : "RFC7723", 
    "Source Address" : "Yes",
    "Destination Address" : "Yes",
    "Forwardable" : "Yes",
    "Globally Reachable" : "Yes"   
    },    
    {
    "Address" : "2001:1::2",
    "Address Block" : "2001:1::2/128",
    "Name" : "Traversal Using Relays around NAT Anycast", 
    "RFC" : "RFC8155", 
    "Source Address" : "Yes",
    "Destination Address" : "Yes",
    "Forwardable" : "Yes",
    "Globally Reachable" : "Yes"   
    },    
    {
    "Address" : "2001:2:",
    "Address Block" : "2001:2::/48",
    "Name" : "Benchmarking", 
    "RFC" : "RFC5180", 
    "Source Address" : "Yes",
    "Destination Address" : "Yes",
    "Forwardable" : "Yes",
    "Globally Reachable" : "No"   
    },    
    {
    "Address" : "2001:3:",
    "Address Block" : "2001:3::/32",
    "Name" : "AMT", 
    "RFC" : "RFC7450", 
    "Source Address" : "Yes",
    "Destination Address" : "Yes",
    "Forwardable" : "Yes",
    "Globally Reachable" : "Yes"   
    },    
    {
    "Address" : "2001:4:112:",
    "Address Block" : "2001:4:112::/48",
    "Name" : "AS112-v6", 
    "RFC" : "RFC7535", 
    "Source Address" : "Yes",
    "Destination Address" : "Yes",
    "Forwardable" : "Yes",
    "Globally Reachable" : "Yes"   
    },    
    {
    "Address" : "2001:10",
    "Address Block" : "2001:10::/28",
    "Name" : "Deprecated (previously ORCHID)", 
    "RFC" : "RFC4843", 
    "Source Address" : "N/A",
    "Destination Address" : "N/A",
    "Forwardable" : "N/A",
    "Globally Reachable" : "N/A"   
    },    
    {
    "Address" : "2001:20",
    "Address Block" : "2001:20::/28",
    "Name" : "ORCHIDv2", 
    "RFC" : "RFC7343", 
    "Source Address" : "Yes",
    "Destination Address" : "Yes",
    "Forwardable" : "Yes",
    "Globally Reachable" : "Yes"   
    },     
    {
    "Address" : "2002::",
    "Address Block" : "2002::/16",
    "Name" : "6to4", 
    "RFC" : "RFC3056", 
    "Source Address" : "Yes",
    "Destination Address" : "Yes",
    "Forwardable" : "Yes",
    "Globally Reachable" : "N/A"   
    },    
    {
    "Address" : "2620:4f:8000:",
    "Address Block" : "2620:4f:8000::/48",
    "Name" : "Direct Delegation AS112 Service", 
    "RFC" : "RFC7534", 
    "Source Address" : "Yes",
    "Destination Address" : "Yes",
    "Forwardable" : "Yes",
    "Globally Reachable" : "Yes"   
    },    
    {
    "Address" : "fc",
    "Address Block" : "fc00::/7",
    "Name" : "Unique-Local", 
    "RFC" : "RFC4183", 
    "Source Address" : "Yes",
    "Destination Address" : "Yes",
    "Forwardable" : "Yes",
    "Globally Reachable" : "No"   
    },
    {
    "Address" : "fd",
    "Address Block" : "fc00::/7",
    "Name" : "Unique-Local", 
    "RFC" : "RFC4183", 
    "Source Address" : "Yes",
    "Destination Address" : "Yes",
    "Forwardable" : "Yes",
    "Globally Reachable" : "No"   
    }  
    ]


    
    multicast = ipaddress.IPv6Address(ipv6_address_validate).is_multicast
    special_purpose_global = ipaddress.IPv6Address(ipv6_address_validate).is_global
    special_purpose_private = ipaddress.IPv6Address(ipv6_address_validate).is_private
    link_local = ipaddress.IPv6Address(ipv6_address_validate).is_link_local
    unspecified = ipaddress.IPv6Address(ipv6_address_validate).is_unspecified
    reserved = ipaddress.IPv6Address(ipv6_address_validate).is_reserved
    loopback = ipaddress.IPv6Address(ipv6_address_validate).is_loopback


    # Convert ipv6_address_validate to string ipv6_address
    ipv6_address = format(ipaddress.IPv6Address(ipv6_address_validate)) 
        
    if ipv6_address.startswith("ff02::1:ff"):
        print(f"\n{ipv6_address} is a solicited-node multicast address")
        display_sn_multicast()
        
        # Find last 24 bits of solicited node multicast
        total = len(ipv6_address)
        start = total - 10
        #print(ipv6_address[10:total])
        
        print("\nFirst 104 bits of the address is: ff02::1:ff/104")
        print(f"Last 24 bits that were mapped from a unicast address: {ipv6_address[10:total]}")
        
        print("\nResulting solicited-node multicast is:")
        print(f"\ff02::1:ff + {ipv6_address[10:total]} = {ipv6_address}")

        
        # So we do not show multicast below  
        multicast = False 

    if multicast == True:
        print(f"\n{ipv6_address_validate} is a multicast address - RFC 2373\n")        
        display_multicast()
        
        print("\nff (1111 1111) - multicast")
        
        # Convert ipvt_address_validate to string ipv6_address
        ipv6_address = format(ipaddress.IPv6Address(ipv6_address_validate)) 
        
        if ipv6_address[2] == "0":
            print("Flag: 0  - This is a well-known, reserved multicast address")
        elif ipv6_address[2] == "1":
            print("Flag: 1 - This is a non-permanent, transient or dynamically assigned multcast address")

        if ipv6_address[3] == "0":
            print("Scope: 0 - Scope is reserved")
        elif ipv6_address[3] == "1":
            print("Scope: 1 - Has interface-local scope")                            
        elif ipv6_address[3] == "2":
            print("Scope: 2 - Has link-local scope") 
        elif ipv6_address[3] == "5":
            print("Scope: 5 - Has site-local scope") 
        elif ipv6_address[3] == "8":
            print("Scope: 8 - Has organization-local scope")             
        elif ipv6_address[3] == "e":
            print("Scope: e  - Has global scope")             

        if ipv6_address == "ff02::1":
            print("Group ::1 - All IPv6 devices")
        elif ipv6_address == "ff02::2":
            print("Group ::2 - All IPv6 routers")
        elif ipv6_address == "ff02::3":
            print("Group ::3 - Unassigned")
        elif ipv6_address == "ff02::4":
            print("Group ::4 - All DVMRP Routers")
        elif ipv6_address == "ff02::5":
            print("Group ::5 - All OSPF routers")
        elif ipv6_address == "ff02::6":
            print("Group ::6 - All OSPF designated routers")
        elif ipv6_address == "ff02::7":
            print("Group ::7 - All ST routers")
        elif ipv6_address == "ff02::8":
            print("Group ::8 - All ST hosts")
        elif ipv6_address == "ff02::9":
            print("Group ::9 - All RIP routers")
        elif ipv6_address == "ff02::a":
            print("Group ::a - All EIGRP routers")
        elif ipv6_address == "ff02::b":
            print("Group ::b - All mobile agents")
        elif ipv6_address == "ff02::c":
            print("Group ::c - SSDP")            
        elif ipv6_address == "ff02::d":
            print("Group ::d - All PIM routers")
        elif ipv6_address == "ff02::e":
            print("Group ::e - RSVP-ENCAPSULATION")
        elif ipv6_address == "ff02::f":
            print("Group ::f - UPnP")
        elif ipv6_address == "ff02::10":
            print("Group ::10 - All-BBF-Access-Nodes")
        elif ipv6_address == "ff02::11":
            print("Group ::11 - All-Homenet-Nodes")
        elif ipv6_address == "ff02::12":
            print("Group ::12 - VRRP")
        elif ipv6_address == "ff02::13":
            print("Group ::13 - ALL_GRASP_NEIGHBORS")
        elif ipv6_address == "ff02::16":
            print("Group ::16 - All MLDv2-capable routers ")
        elif ipv6_address == "ff02::1a":
            print("Group ::1a - All-RPL nodes")
        elif ipv6_address == "ff02::6a":
            print("Group ::6a - All Snoopers")
        elif ipv6_address == "ff02::6b":
            print("Group ::6b - PTP-pdelay")
        elif ipv6_address == "ff02::6c":
            print("Group ::6c - Saratoga")
        elif ipv6_address == "ff02::6d":
            print("Group ::6d - LL-MANET-Routers")
        elif ipv6_address == "ff02::6e":
            print("Group ::6e - IGRS")
        elif ipv6_address == "ff02::6f":
            print("Group ::6f - iADT Discovery")
        elif ipv6_address == "ff02::fb":
            print("Group ::fb - mDNSv6")
        elif ipv6_address == "ff02::1:2":
            print("Group ::1:2 - All_DHCP_Relay_Agents_and_Servers") 
        elif ipv6_address == "ff05::2":
            print("Group ::2 - All IPv6 routers")
        elif ipv6_address == "ff05::fb":
            print("Group ::fb - mDNSv6")   
        elif ipv6_address == "ff05::1:3":
            print("Group ::1:3 - All_DHCP_Servers")             
            

    if unspecified == True:
        print(f"{ipv6_address_validate} is an unspecified address - RFC 2373")
    
    if link_local == True:
        print(f"{ipv6_address_validate} is a link-local address - RFC 3927\n")
        display_link_local()
   
    if loopback == True:
        print(f"{ipv6_address_validate} is a loopback address - RFC 2373")

    if reserved == True:
        print(f"{ipv6_address_validate} is an IETF reserved address")

    # Need this to flag GUA otherwise is considered IANA Special Purpose Address
    iana_special_purpose = False
    
    if special_purpose_global == True or special_purpose_private == True:
        #if special_purpose_private == True:
        # print(f"{ipv6_address_validate} is an IANA IPv6 special purpose address")

        # Convert ipv6_address_validate to string ipv6_address
        ipv6_address = format(ipaddress.IPv6Address(ipv6_address_validate))

        
        for item in IANA_Special_Purpose:
            # print("item[Address]", item["Address"], "ipv6_address = ", ipv6_address,)

            if  ipv6_address == item["Address"]:
                print(f"{ipv6_address_validate} is an IANA IPv6 special purpose address")
                print("\nEquals Address Block")
                print ("Address Block: ",item["Address Block"])
                print ("Name: ",item["Name"])
                print (item["RFC"])
                print ("Source Address: ",item["Source Address"])
                print ("Destination Address: ",item["Destination Address"])
                print ("Forwardable: ",item["Forwardable"])
                print ("Globally Reachable ",item["Globally Reachable"], "\n")
                iana_special_purpose = True 
                break           
            elif ipv6_address.startswith(item["Address"]):
                print(f"{ipv6_address_validate} is an IANA IPv6 special purpose address")
                print("\nStarts with Address Block")
                print ("Address Block: ",item["Address Block"])
                print ("Name: ",item["Name"])
                print (item["RFC"])
                print ("Source Address: ",item["Source Address"])
                print ("Destination Address: ",item["Destination Address"])
                print ("Forwardable: ",item["Forwardable"])
                print ("Globally Reachable ",item["Globally Reachable"], "\n") 
                iana_special_purpose = True
                break           

    # GUA Address
    if iana_special_purpose == False: 
        # Convert ipv6_address_validate to string ipv6_address
        ipv6_address = format(ipaddress.IPv6Address(ipv6_address_validate))    

        if ipv6_address.startswith("2") or ipv6_address.startswith("3"):
            print(f"\n{ipv6_address} is global unicast address")
            display_gua()


def ipv6_subnets(ipv6_net_address):

    subnet_bits = int(input("Enter the number of bits in the Subnet ID (ex. 8): ") )

    # Subnets method returns subnets with the difference in prefixlen_diff, list puts it in a list
    subnets = list(ipv6_net_address.subnets(prefixlen_diff=subnet_bits))

    print("\n")
    # print the list as a single column
    for item in subnets:
        print(item, end=" \n")


def display_ipv6_address():
    
    print("IPv6 addresses are composed of 128 bits represented in hexadecimal:")
    print("\n   > Hexadecimal: 1 hex digit = 4 bits")
    
    print("""
        \tHex  Binary       Hex  Binary
        \t---  ------       ---  ------
        \t 0    0000         8    1000
        \t 1    0001         9    1001
        \t 2    0010        10    1010
        \t 3    0011        11    1011
        \t 4    0100        12    1100
        \t 5    0101        13    1101
        \t 6    0110        14    1110
        \t 7    0111        15    1111     
       """)

    print("   > Eight 16-bit segments or “hextets” (not a formal term) between 0000 and ffff")
    print("   > Each hextet is separated by a colon")
    
    print("""
          0000 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000 
           to     to     to     to     to     to     to     to
          ffff : ffff : ffff : ffff : ffff : ffff : ffff : ffff       
          """)

    print("You can reduce the representation of an IPv6 address with two rules:")
    print("Rule 1: First rule: Leading zeroes in any 16-bit segment do not have to be written.")
    print("        Only leading 0s can be excluded, or leads to ambiguity.")
    print("Rule 2: Any single, contiguous string of one or more 16-bit segments consisting of") 
    print("        all zeroes can be represented with a double colon (::).")

    print("""
          \rTo learn more:
          
          \rSee menu item "Compress an IPv6 address to its shortest form" 
          \rThis will give you two rules for reducing the representation of an IPv6 address. 
          """)

    


def display_gua():
    
    print("\nFormat of a Global Unicast Address (GUA)")
    print(" ----------------------------------------------------------------------")
    print("| Global Routing Prefix | Subnet ID  |        Interface ID             |")
    print("|        n bits         | m bits     |        128-n-m bits             |")
    print(" ----------------------------------------------------------------------")
        
    print("\nGlobal Routing Prefix: The prefix or network portion of the")
    print("address assigned by the provider (ISP).") 
    print("\nSubnet ID: Separate field for allocating subnets.\n")
    
    print("\nGlobal unicast addresses are globally unique, globally routable,") 
    print("and similar to public IPv4 addresses")
    print("\nRange is 2003::/3 (2001::/64 through 3ffff:ffff:ffff:ffff::/64)")

    print("\nSource Address : Yes")
    print("Destination Address : Yes")
    print("Forwardable : Yes")
    print("Globally Reachable : Yes") 
    
    print("""
          \nNOTE: 2001:db8::/32 - RFC 3849 reserves this range of addresses for documentation.
          \rThese addresses are to globally reachable and should only be used in lab environments.
          """)

def display_link_local():
    
    print("Format of a Link-Local Address (LLA):")
    print(" --------------------------------------------------------------------")
    print("| 1111 1110 | 10xx xxxx | Remaining |         Interface ID            |")
    print("| 8 bits    | 8 bits    | 54 bits   |         64 bits                 |")
    print(" --------------------------------------------------------------------")

    print("\nLink-local addresses are used to communicate with other devices on the link.")
    print("   > NOT routable off the link (network).")
    print("   > Only has to be unique on the link.")
    print("   > Not included in the router's IPv6 routing table.")
    print("   > Only one link-local address per interface.\n")

    print("\nSource Address : Yes")
    print("Destination Address : Yes")
    print("Forwardable : No")
    print("Globally Reachable : No") 
    
    print("""
          \nNOTE: To avoid problems with some operating systems, it is suggested
          \rto use fe80 for the first hextet.
          """)

def display_multicast():
    
    print("\nFormat of a Multicast Address")
    print(" ------------------------------------------------------------------")
    print("| 1111 1111 (ff) | Flag   | Scope  |           Group ID             |")
    print("|     8 bits     | 4 bits | 4 bits |           112 bits             |")
    print(" -------------------------------------------------------------------")
        
    print("\nMulticast addresses are used to send a single packet to")
    print("multiple destinations simultaneously (one-to-many)")
    print("   > Equivalent to 224.0.0.0/4 in IPv4.")
    print("   > This address type is typically used for neighbor discovery")
    print("     and routing protocol messages.")
    print("   > Three types of multicast addresses:")
    print("     1. Well-known or Assigned")
    print("     2. Transient")
    print("     3. Solicited-Node")
    
    print("\nSource Address : No")
    print("Destination Address : Yes")
    print("Forwardable : Depending on scope and enabling IPv6 multicast routing")
    print("Globally Reachable : Depending on scope and enabling IPv6 multicast routing")  


def display_sn_multicast():
    
    print("\nFormat of a Solicited-Node Multicast address")
    print(" ----------------------------------------------------------------------")
    print("|   ff02     |  0  |  0  |  0  |  0  |  1  |  ff xx    |     xxxx      |")
    print("|   16 bits  |            96 bits          |  ff + 24 bits of unicast  |")
    print(" ----------------------------------------------------------------------")
        
    print("\nSolicited-Node Multicast addresses are special type of multicast address")
    print("Used by neighbor discovery protocols for address resolution")
    print("\nOne of three types of multicast addresses:")
    print("  1. Well-known or Assigned")
    print("  2. Transient")
    print("  3. Solicited-Node") 

    print("\nSource Address : No")
    print("Destination Address : Yes")
    print("Forwardable : No")
    print("Globally Reachable : No") 
    
    print("\nFormat is: ff02:0:0:0:0:1:ff/104 or ff02::1:ff/104")

    print("\nff (1111 1111) - multicast")
    print("Flag: 0  - This is a reserved, predefined multcast address")
    print("Scope: 2 - Has link-local scope") 



def display_url_IP():

    while True:
        try:
            url_Entered = input("\nEnter a URL or q to quit: ")
            if url_Entered == 'q' or url_Entered == 'Q':
                break
            # SOCKET LIBRARY - gethostbyname for IPv4 address
            ipv4_address = socket.gethostbyname(url_Entered)
        except:
            print(f"Invalid input {url_Entered}, try again...")
        else:
            break

    if url_Entered == 'q' or url_Entered == 'Q':
        return
            
    # Not needed (SOCKET - gethostbyname used above) - get address info using SOCKET LIBRARY
    # ipv4_addressInfo = socket.getaddrinfo(url_Entered, None, socket.AF_INET)

    # SOCKET LIBRARY ipv6_addressInfo_gua only returns IPv6 address when IPv6 is available (get gua)
    ipv6_addressInfo = socket.getaddrinfo(url_Entered, None, socket.AF_INET6)    
    # SOCKET LIBRARY ipv6_addressInfo_gua only returns IPv6 address when IPv6 is available (get gua)
    ipv6_addressInfo_gua = socket.getaddrinfo(url_Entered, None, socket.AF_INET6)[0][4][0]

    
    print(f'\nIPv4 address for {url_Entered} is {ipv4_address}')
    
    # SOCKET LIBRARY ipv6_addressInfo_gua only returns IPv6 address when IPv6 is available (get gua)
    # use DNS.RESOLVER LIBRARY for remote IPv6 address
    #if ipv6_addressInfo_gua.startswith('::ffff:'):
    #    print('Unable to retrieve IPv6 address or there is not IPv6 address for this URL.')
    #else:
    #    print(f'IPv6 address for {url_Entered} is {ipv6_addressInfo_gua}')

    # DNS.RESOLVER LIBRARY
    # Deprecated > result = dns.resolver.query(url_Entered, 'AAAA')
    # If needed >  result = dns.resolver.resolve(url_Entered, 'A') < using SOCKET gethostbyname above
    
    try:
        result = dns.resolver.resolve(url_Entered, 'AAAA')
        for ipval in result:
            print('IPv6 address for', url_Entered, 'is', ipval.to_text())
    except:
        print("No IPv6 address for this URL...")


def display_local_IP():
    
    hostName = socket.gethostname()
    hostName += ".local"
    # ipAddr = socket.gethostbyname(hostName)

    print('\nLocal Addressing Information:')
    print('Hostname is: {}'.format(hostName))
    print('\nIPv4 Addressing:')
    print('----------------')
    # print('Your private IPv4 Address is: ', ipAddr)
    # print('Your private IPv4 Address is: {}'.format(ipAddr))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])
    print('Your private IPv4 Address is: {}'.format(s.getsockname()[0]))

    # Get public IPv4 address using REQUESTS LIBRARY
    f = requests.request('GET', 'http://myip.dnsomatic.com')
    ipv4_public = f.text
    # print(type(ipv4_public))
    # print('Your public IPv4 Address is: {}'.format(ipv4_public))

    if '<html>' in ipv4_public or 'Too Many Requests' in ipv4_public:
        print("No public IPv4 address available. Please try again later.")
    else: 
        print('Your public IPv4 Address is: {}'.format(ipv4_public))


    # Get IPv6 address using SOCKET LIBRARY
    my_ipv6_addressInfo = socket.getaddrinfo(hostName, None, socket.AF_INET6)
    # my_ipv6_addressInfo_lla = socket.getaddrinfo(hostName, None, socket.AF_INET6)[0][4][0]

    gua_Flag = False
    lla_Flag = False
    print('\nIPv6 Addressing:')
    print('----------------')
    duplicate_check = []
    for item in range(len(my_ipv6_addressInfo)):
        if my_ipv6_addressInfo[item][4][0] not in duplicate_check:
            if my_ipv6_addressInfo[item][4][0] == 'fe80::1':
                print(f'The IPv6 link-local address : {my_ipv6_addressInfo[item][4][0]} is most likely associated with your loopback interface')
            elif my_ipv6_addressInfo[item][4][0].startswith('fe80'):
                lla_Flag = True
                print('Your IPv6 link-local address is:', my_ipv6_addressInfo[item][4][0])
                if 'fe:ff' in my_ipv6_addressInfo[item][4][0]:
                    print('    Note: This address uses a EUI-64 for its Interface ID.')
                else:    
                    print('    Note: This address uses a randomized or static Interface ID.')
            elif my_ipv6_addressInfo[item][4][0].startswith('2'):
                gua_Flag = True
                print('Your IPv6 global unicast address is:', my_ipv6_addressInfo[item][4][0])
                if 'fe:ff' in my_ipv6_addressInfo[item][4][0]:
                    print('    Note: This address uses a EUI-64 for its Interface ID.')
                else:    
                    print('    Note: This address uses a randomized or static Interface ID.')
            elif my_ipv6_addressInfo[item][4][0].startswith('3'):
                gua_Flag = True
                print('Your IPv6 global unicast address is:', my_ipv6_addressInfo[item][4][0])
                if 'fe:ff' in my_ipv6_addressInfo[item][4][0]:
                    print('    Note: This address uses a EUI-64 for its Interface ID.')
                else:    
                    print('    Note: This address uses a randomized or static Interface ID.')
            elif my_ipv6_addressInfo[item][4][0] == '::1':
                print(my_ipv6_addressInfo[item][4][0], ' is a loopback address') 
            else:
                print('Your IPv6 address is:', my_ipv6_addressInfo[item][4][0])
                if 'fe:ff' in my_ipv6_addressInfo[item][4][0]:
                    print('    Note: This address uses a EUI-64 for its Interface ID.')
                else:    
                    print('    Note: This address uses a randomized or static Interface ID.')
            # print(my_ipv6_addressInfo[item][4][0])
            duplicate_check.append(my_ipv6_addressInfo[item][4][0])

    print("\nThis device's IPv6 network access:")
    print("----------------------------------")
  
    if lla_Flag == False and gua_Flag == False:
        print('''\rIPv6 Link-Local Address:     No                            
              \rIPv6 local network access:   No
              \nIPv6 Global Unicast Address: No 
              \rIPv6 Internet access:        No''')

    if lla_Flag == True and gua_Flag == False:
        print('''\rIPv6 Link-Local Address:     Yes                
              \rIPv6 local network access:   Yes
              \nIPv6 Global Unicast Address: No 
              \rIPv6 Internet access:        No''')

    if lla_Flag == True and gua_Flag == True:
        print('''\rIPv6 Link-Local Address:     Yes              
              \rIPv6 local network access:   Yes
              \nIPv6 Global Unicast Address: Yes 
              \rIPv6 Internet access:        Yes''')
    
    
    print('\n')      





def ipv6_fundamentals_book():
    print("\n<<<<<<<<<<<<<<<<<<<<<<<<< >>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("\nI hope you found this helpful!")
    print("\nFor more information, please check out my book:")
    print("IPv6 FUNDAMENTALS, Second Edition, by Rick Graziani")
    print("published by Cisco Press\n")
    print("Or my YouTube Playlist: IPv6 Fundamentals 2e - Playlist")
    print("https://youtube.com/playlist?list=PLMLm7-g0V0kfGg8g8KutNFK7rS3laA9QQ")
    print("\nThanks, Rick\n")
    print("<<<<<<<<<<<<<<<<<<<<<<<<< >>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")        


def how_many():

    undecillion_1 = """
    If you had a job that paid you 390 trillion dollars per hour (US) you would  
    have to work 24 hours per day, 7 days per week, 365 days per year for a just 
    a little less than 100 quadrillion years to earn 340 undecillion dollars.""" 

    undecillion_2 = """
    Diwakar Tundlam; we could assign an IPv6 address to EVERY ATOM ON THE SURFACE 
    OF THE EARTH, and still have enough addresses left to do another 100+ earths.
    """ 
    
    undecillion_3 = """
    How much of the earth would 340 undecillion one-dollar bills take up?
    A single dollar bill weights about one gram. So your dollar bills would weigh 
    about 50 billion times more than the earth. Their mass would probably form 
    black hole 180 thousand times more massive than the Sun. 
    """
    
    undecillion_4 = """
    If IP addresses were a grain of sand...
    IPv4 = 4.29 bilion — Enough “grains” to fill a wheelbarrow.
    IPv6 = 340 undecillion — Enough to fill the earth 1 million times.
    """
    
    undecillion_5 = """
    664 BILLION IPv6 addresses for every grain of sand on the Earth.
    """

    undecillion_6 = """
    "The most commonly quoted number of stars in a galaxy is 100 billion 
    and the most commonly quoted number of galaxies in the Universe is 
    100 billion. Assuming there are 10 planets around every star, then 
    there are 10 x 100 x 100 billion billion planets in the Universe. 
    So how many IP addresses per planet in the entire Universe? 
    Answer: 3.4 quadrillion IPv6 addresses per planet in the Universe!"
    """
    
    undecillion_list = [
        undecillion_1, undecillion_2, undecillion_3, 
        undecillion_4, undecillion_5
    ]
    
    print("\nIPv6 addresses are 128 bits or 2 raised to the 128th power")
    print("This equates to 340 undecillion addresses or...")
    print("340,282,366,920,938,000,000,000,000,000,000,000,000 IPv6 addresses ")
    
           
    print("\nSo, how much is 340 undecillion?\n")
    keep_going = input("Press any key to get one of several answers...")    
    
    undecillion_choice = random.choice(undecillion_list)
    print(undecillion_choice)
    print("\nDisclaimer: These were taken from various web sites and I not validated their information :)")
  
        




###################################################################
# MAIN PROGRAM
###################################################################

ipv6_menu()
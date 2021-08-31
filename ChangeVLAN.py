import meraki
import csv
import pyinputplus as pyip
import time


def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1  

def main():

    print(f"Insert API key:\n")
    API_KEY = pyip.inputPassword()
    session = meraki.DashboardAPI(API_KEY)
    networks = []
    vlan_1 = "246"
    vlan_2 = "247"
    vlan_3 = "249"

    print(f"Session created. For every request, there will be a 60 seconds delay!\n")

    with open("input-file-net.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            row = row[0].split(sep=";")
            networks.append(row)
    
    for i in range(len(networks)):
        firstRequest = session.appliance.updateNetworkApplianceVlan(networks[i][0], vlan_1, subnet = networks[i][3], applianceIp = networks[i][4])
        print(f"\nNETWORK {networks[i][2]} - VLAN {vlan_1} UPDATED\n\n\t\t* * *\t\t\n")
    
    
    for i in range(len(networks)):
        secondRequest = session.appliance.updateNetworkApplianceVlan(networks[i][0], vlan_2, subnet = networks[i][5], applianceIp = networks[i][6])
        print(f"\nNETWORK {networks[i][2]} - VLAN {vlan_2} UPDATED\n\n\t\t* * *\t\t\n")
    

    for i in range(len(networks)):
        thirdRequest = session.appliance.updateNetworkApplianceVlan(networks[i][0], vlan_3, subnet = networks[i][7], applianceIp = networks[i][8])
        print(f"\nNETWORK {networks[i][2]} - VLAN {vlan_3} UPDATED\n\n\t\t* * *\t\t\n")


if __name__ == "__main__":
    main()
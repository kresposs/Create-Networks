import meraki 
import csv
import pyinputplus as pyip
import time

def main():

    print(f"Insert API key:\n")
    API_KEY = pyip.inputPassword()
    session = meraki.DashboardAPI(API_KEY)
    networks = []
    tmp = []

    with open("input-file.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            row = row[0].split(sep=";")
            networks.append(row)
    
    tmp.append(networks[0][2])
        
    
    for i in range(len(networks)):
        #print(networks[i])
        response = session.organizations.createOrganizationNetwork(networks[i][0], networks[i][1], tmp)
        time.sleep(60)
    

if __name__ == "__main__":
    main()





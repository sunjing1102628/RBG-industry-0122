
import csv
import json
import random

def remove_null_bytes(input_filename, output_filename):
    with open(input_filename, 'rb') as infile, open(output_filename, 'wb') as outfile:
        outfile.write(infile.read().replace(b'\0', b' '))


def find_min_max_lat_lon_services(file_directory):
    with open(file_directory, 'r') as f:
        lines = f.readlines()
    
   

    lines = lines[1:]
   # lines = lines[1:3301]   
     # Select 3500 lines randomly if the file has enough lines, otherwise select all available lines
    random.seed(42)
    #num_lines_to_select = 3500
    num_lines_to_select = 120
    selected_lines = random.sample(lines, min(num_lines_to_select, len(lines)))
    lats, lons = [], []

    for line in selected_lines:
        fields = line.strip().split("\t")
        # Replace doubled double quotes with single double quotes
        corrected_data = fields[3].replace('""', '"')
        
            # Remove the extra quotes at the beginning and end of the string
        corrected_data = corrected_data[1:-1]
            
        d_address = json.loads(corrected_data)

        # Handle the double double quotes in the JSON-like strings
        lats.append(float(d_address["lat"]))
        lons.append(float(d_address["lon"]))

        min_lat, max_lat = min(lats), max(lats)
        min_lon, max_lon = min(lons), max(lons)

    return min_lat, max_lat, min_lon,max_lon

def normalize_lat_lon(lat, lon, min_lat, max_lat, min_lon, max_lon):
    norm_lat = (lat+0.1 - min_lat) / (max_lat - min_lat)
    norm_lon = (lon+0.1 - min_lon) / (max_lon - min_lon)

    return norm_lat, norm_lon

def generate_industry_services_data(file_directory):
    with open(file_directory, 'r') as f:
        lines = f.readlines()
          # Assuming the first line is a header, skip it
    lines = lines[1:]
   # lines = lines[1:3301]   
     # Select 3500 lines randomly if the file has enough lines, otherwise select all available lines
    random.seed(42)
    num_lines_to_select = 20
    selected_lines = random.sample(lines, min(num_lines_to_select, len(lines)))
    CAPACITIES = 50  # adjust as per your needs
    num_samples = len(selected_lines)

    samples = []
    locationObject=[]
    demandArray=[]
    demandObject=[]
    locationArray=[]
    lats, lons = [], []

    min_lat, max_lat, min_lon, max_lon = find_min_max_lat_lon_services(file_directory)
    depot_lat, depot_lon = normalize_lat_lon( 1.3049384852, 103.83221985, min_lat, max_lat, min_lon, max_lon)
       

    '''with open('test_instances/Industry_data_test/parcelv2.tsp', 'w') as tsp_file:
        tsp_file.write("NAME : parcel\n")
        tsp_file.write("COMMENT : 3300-CVRPTW problem \n")
        tsp_file.write("TYPE : CVRPTW\n")
        tsp_file.write("SERVICE_TIME: 120\n")
        tsp_file.write("CAPACITY: 100\n")
        tsp_file.write("VEHICLES: 34\n")
        tsp_file.write(f"DIMENSION : {len(selected_lines)}\n")
        tsp_file.write("EDGE_WEIGHT_TYPE : EUC_2D\n")
        tsp_file.write("NODE_COORD_SECTION\n")
        tsp_file.write(f"{1} {round(depot_lat*10000)} {round(depot_lon*10000)}\n")

        for index, line in enumerate(selected_lines):
            fields = line.strip().split("\t")
            demandObject = int(fields[1].split(",")[0].replace('"', ''))
            print(demandObject)
            print( fields[3])
            try:
                #lat = float(eval(fields[5])["lat"])
                #lon = float(eval(fields[5])["lon"])

                # Replace doubled double quotes with single double quotes
                corrected_data = fields[3].replace('""', '"')
            
                # Remove the extra quotes at the beginning and end of the string
                corrected_data = corrected_data[1:-1]
                
                d_address = json.loads(corrected_data)

                lat = float(d_address["lat"])
                lon = float(d_address["lon"])
                norm_lat, norm_lon = normalize_lat_lon(lat, lon, min_lat, max_lat, min_lon, max_lon)

            except Exception as e:
                print("Error with data:", fields[3])
                raise e
            depot_lat, depot_lon = normalize_lat_lon(1.369079, 103.909656, min_lat, max_lat, min_lon, max_lon)
            # node_demand = torch.tensor([demand_value]) / CAPACITIES
            tsp_file.write(f"{index+2} {round(norm_lat*10000)} {round(norm_lon*10000)}\n")
            print(norm_lat, norm_lon)'''
    with open('test_instances/Industry_data_test/parcelv2a.tsp', 'w') as tsp_file:
        tsp_file.write("NAME : parcel\n")
        tsp_file.write("COMMENT : 120-CVRP problem \n")
        tsp_file.write("TYPE : CVRP\n")
        tsp_file.write("SERVICE_TIME: 20\n")
        tsp_file.write("CAPACITY: 100\n")
        tsp_file.write("VEHICLES: 3\n")
        tsp_file.write(f"DIMENSION : {len(selected_lines)}\n")
        tsp_file.write("EDGE_WEIGHT_TYPE : EUC_2D\n")
        tsp_file.write("NODE_COORD_SECTION\n")
        tsp_file.write(f"{1} {round(depot_lat * 10000)} {round(depot_lon * 10000)}\n")

        for index, line in enumerate(selected_lines):
            fields = line.strip().split("\t")
            demandObject = int(fields[1].split(",")[0].replace('"', ''))
            print(demandObject)
            print(fields[3])
            try:
                # lat = float(eval(fields[5])["lat"])
                # lon = float(eval(fields[5])["lon"])

                # Replace doubled double quotes with single double quotes
                corrected_data = fields[3].replace('""', '"')

                # Remove the extra quotes at the beginning and end of the string
                corrected_data = corrected_data[1:-1]

                d_address = json.loads(corrected_data)

                lat = float(d_address["lat"])
                lon = float(d_address["lon"])
                norm_lat, norm_lon = normalize_lat_lon(lat, lon, min_lat, max_lat, min_lon, max_lon)

            except Exception as e:
                print("Error with data:", fields[3])
                raise e
            depot_lat, depot_lon = normalize_lat_lon(1.369079, 103.909656, min_lat, max_lat, min_lon, max_lon)
            # node_demand = torch.tensor([demand_value]) / CAPACITIES
            tsp_file.write(f"{index + 2} {round(norm_lat * 10000)} {round(norm_lon * 10000)}\n")
            print(norm_lat, norm_lon)

        tsp_file.write("DEPOT_SECTION\n")
        # depot_lat, depot_lon = normalize_lat_lon( 1.3049384852, 103.83221985, min_lat, max_lat, min_lon, max_lon)
        #     # node_demand = torch.tensor([demand_value]) / CAPACITIES
        # print(min_lat,max_lat )
        tsp_file.write(f"{1} \n")
        tsp_file.write(f"{-1} \n")
        # print(depot_lat, depot_lon)
        tsp_file.write("DEMAND_SECTION\n")
        tsp_file.write(f"{1} {33000}\n")
        for index, line in enumerate(selected_lines):
            # node_demand = torch.tensor([demand_value]) / CAPACITIES
            tsp_file.write(f"{index+2} {1}\n")
        #tsp_file.write("TIME_WINDOW_SECTION\n")
        #tsp_file.write(f"{1} {0} {100000}\n")
        for index, line in enumerate(selected_lines):
            # node_demand = torch.tensor([demand_value]) / CAPACITIES
            tsp_file.write(f"{index+2} {28800} {82800}\n")

       
    # Preprocess the file to remove null bytes
#remove_null_bytes('test_instances/Industry_data_test/parcel.txt', 'test_instances/Industry_data_test/parcelnonull.txt')

# Reading data from the preprocessed text file
data = []
'''with open('test_instances/Industry_data_test/parcelnonull.txt', 'r') as txtfile:
    reader = csv.DictReader(txtfile, delimiter='\t')
    for row in reader:
        data.append(row)'''

with open('test_instances/Industry_data_test/parcelnonull1.txt', 'r') as txtfile:
    reader = csv.DictReader(txtfile, delimiter='\t')
    for row in reader:
        data.append(row)
generate_industry_services_data('test_instances/Industry_data_test/parcelv2a.txt')

   
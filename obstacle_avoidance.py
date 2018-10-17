import ast

current_lat = 12.360389999999999
current_long = 76.595440000000123


covered_lat = [12.36037, 12.36038]

lat_list = []
abs_path = "saved_points_sim.txt"
with open(abs_path,'r') as pts:
	data = pts.readlines()
        for i in data:
            co = ast.literal_eval(i)
            lat_list.append(co[0])

def find_next_waypoint(lat_list,covered_lat, current_lat, current_long):
	unique_lat = list(set(lat_list))
	unique_lat.sort()
	#print(unique_lat)

	prev_lat = 0
	next_lat = 0
	final_lat = 0
	final_long = 0

	curr_index = unique_lat.index(current_lat)
	#print(curr_index)

	if (curr_index>0):
		prev_lat = unique_lat[curr_index-1]
	if (curr_index+1<len(unique_lat)):
		next_lat = unique_lat[curr_index+1]

	if(prev_lat == 0 and next_lat == 0):
		print("No more way out")

	if(prev_lat not in covered_lat):
		final_lat = prev_lat
	elif(next_lat not in covered_lat):
		final_lat = next_lat

	if(final_lat != 0):
		final_long = current_long
		#print("%.16f" % final_lat)
		#print("%.16f" % final_long)
	else:
		print("No more way out")
	return([final_lat,final_long])

output = find_next_waypoint(lat_list,covered_lat, current_lat, current_long)
print(output)

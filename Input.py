

def input(path):
	file = open("Data/" + path, "r")
	ridesList = []
	height, width, vehicles, nbrides, bonus, steps = [int(i) for i in file.readline().split(" ")]
	for lines in range(nbrides):
		xs, ys, xe, ye, start, end= [int(i) for i in file.readline().split(" ")]
		ridesList.append([(xs,ys),(xe,ye),start, end]) 
	file.close()
	return ((height, width, vehicles, nbrides, bonus, steps),ridesList)

((height, width, vehicles, nbrides, bonus, steps),ridesList) = input("b_should_be_easy.in")
print(ridesList)
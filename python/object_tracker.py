# Object Tracker
# Goal is to build the ultimate object tracker for vehicles, people, signs and other relevant information


class Vehicle:
    def __init__(self,position):
        self.position = position
        self.new_postion = None
        self.count = 0
        self.frame = 1
        self.flag = False

    def update(self,temp_position):
        if abs(temp_position[0]-self.position[0]) < 50 and abs(temp_position[1]-self.position[1]) < 50:
            self.position = temp_position
            self.count+=1
            return False
        else:
            return True

    def get_position(self):
        self.frame+=1
        if self.count == 3:
            self.new_postion = self.position
            self.count = 0
            self.frame = 1
        if self.frame > 10:
            self.flag = True

        return self.new_postion, self.flag




# Takes in a list of calclulated centroids calculated from current framefrom your own code  (both good and bad)

# Deal with car tracking
if len(cars)==0:
    for centroid in img_centroids:
            cars.append(Vehicle(centroid))

else:
    for centroid in img_centroids:
        new = True
        for car in cars:
            new = car.update(centroid)
            if new == False:
                break
        if new == True:
            cars.append(Vehicle(centroid))


next_cars = []
positions = []

for car in cars:
    position, flag = car.get_position()
    if flag == False:
        next_cars.append(car)
    positions.append(position)

cars = next_cars

# Outputs current relevant positions. 

try:
    for (x1, y1, x2, y2) in positions:
        cv2.rectangle(clone, (x1, y1), (x2, y2), (255, 0, 0), thickness=2)
except:
    pass
# Object Tracker
# Goal is to build the ultimate object tracker for vehicles, people, signs and other relevant information

class Object:
    def __init__(self,position):
        self.position = position
        self.new_postion = None
        self.count = 0
        self.frame = 1
        self.flag = False
        self.long_count = 0
        self.postion_average = []

    def update(self,temp_position):
        if abs(temp_position[2]-self.position[2]) < 100 and abs(temp_position[3]-self.position[3]) < 100:
            self.position = temp_position
            self.postion_average.append(temp_position)
            self.count+=1
            if self.long_count > 3:
                self.new_postion = np.mean(np.array(self.postion_average), axis=0)
                self.new_postion = self.new_postion.astype(int)
            return False
        else:
            return True

    def get_position(self):
        self.frame+=1
        if self.count == 5:
            self.new_postion = np.mean(np.array(self.postion_average), axis=0)
            self.new_postion = self.new_postion.astype(int)
            self.count = 0
            self.frame = 1
            self.long_count += 1
            self.postion_average = []

        if self.frame > 15:
            self.flag = True

        return self.new_postion, self.flag

class Vehicle(Object):
     def __init__(self, position):
        Object.__init__(self, position)


class Vehicle(Object):
     def __init__(self, position):
        Object.__init__(self, position)

class Person(Object):
    def __init__(self, position):
        Object.__init__(self, position)

class Sign(Object):
    def __init__(self, position):
        Object.__init__(self, position)
        self.label = None
        run_network()
    def run_network(self):
        # Crop out position and run through sign network
        # update self.label




# Takes in a list of calclulated centroids calculated from current frame from your own code  (both good and bad)

# Deal with car tracking
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
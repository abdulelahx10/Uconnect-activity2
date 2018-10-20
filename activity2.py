
class Udacian():
    def __init__(self,name,city,enrollment,nanodegree,status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status
    
    def print_udacian(self):
        print(self.name, "is enrolled in" ,self.city ,"studying", self.nanodegree, "in", 
        self.enrollment[0], self.enrollment[1], "with", self.enrollment[2],", he/she is", self.status)
    
std1 = Udacian("Abdulelah",  "Riyadh", ("Sat", "Am", "Ms. Lujain"), "FSND", "On track")
std1.print_udacian()
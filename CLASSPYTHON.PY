class tu:
    __uni= "LPU"
    pincode="xxxxxxx"
    def display(self):
        print(self.__uni,self.pincode,sep="\n")

obj=tu()

print(obj._tu__uni) # smaller way to print the private value



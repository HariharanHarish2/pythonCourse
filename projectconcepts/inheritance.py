class dog:
    def wait(self):
        print("dog is wait")
class lion(dog):#inherit the function
    def go(self):
        print("lion and dog")
d=dog()
d.wait()
d.go()


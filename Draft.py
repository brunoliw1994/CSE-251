class MyClass:
    def __init__(self, myParameter: int): #here 'int' is the parameter type
        #here, 'self' is the object
        self.myPrarameter = myParameter

        myClass = MyClass(10)
        #the dot operator references the attribute (myParameter)
        print (f'{myClass.myParameter}')



class MyOtherClass:
    def __init__(self, myclass: MyClass):
        self.myclass = myclass
    def run(self):
        print(f'{self.myclass.myParameter}')



f = open(filename, "r") #'r' is to specify that the file is to read and 'w' is to read and write.
#'f' is an object

# One way to read a line from a file is to loop over the file object:
for line in f:
    print(line)

#to make sure the file gets open and close the file after using it:
with open(filename) as f:
    for line in f:
        data_queue.put(line.strip())
#to write a line to a file over and over use 'a' (append) with the writeline function:
with open(filename, "a") as f:
    f.writeline("writing a line of text to the file")
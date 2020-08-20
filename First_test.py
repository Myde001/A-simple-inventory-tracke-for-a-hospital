import sys


class Hospital_file():
    '''This is an programme that keeps track of every medical device 
    in a large hospital'''
    
    def __init__(self):
        '''The constructor is used to create the lists needed to for this task, Self.item_name 
        consists the names of the medical equipment, self.item_type consists of the types of equipment and self.item_serial
        consists of their respective serial number and self.item_list contains the three elements mentioned earlier'''

        self.item_name = []
        self.item_type = []
        self.item_serial = []
        self.item_list = []

    def get_type(self):
        '''This method asks the user for the type of medical equipment to be entered'''
        
        item_type = input('Please enter item Type[Monitoring, Diagnostic or Surgical]: ')
        item_type = item_type.capitalize()
        
        while (item_type != "Monitoring") and (item_type != "Diagnostic") and (item_type != "Surgical"):
            item_type = input('Enter a recognized type only: ')
            item_type = item_type.capitalize()
            
        self.item_type.append(item_type) 
        
        return self.item_type
    
    def get_itemName(self):
        '''This method asks the user for the name of medical equipment to be entered'''
        
        item_name = input('Enter the name of the equipment: ')
        self.item_name.append(item_name) 
        
        return self.item_name
    
    def get_itemSerial(self):
        '''This method asks the user for the serial number of medical equipment to be entered'''
        
        item_serial = int(input('Enter the 11 digits serial Number of this item. [Numbers Only]: '))
        
        while len(str(item_serial)) != 11 :
            item_serial = input('Please enter a correct Serial Number [Numbers Only]: ')
            
        self.item_serial.append(item_serial)        
        return self.item_serial

        
    def create_item(self):
        '''This method creates a zip list for the type, name and serial number entered by the user and stores in in self.item_list'''

        sibilu = list(zip(self.item_type, self.item_name, self.item_serial))
        
        self.item_list.append(sibilu)
        
        return self.item_list
        
    def delete_item(self):
        ''' This method deletes an item from item_list using serial number
        as the keyword'''
        
        serial_del = int(input("Please Enter the serial number of the item to delete: "))
        for line in self.item_list[-1]:
            k = int(line[2])
            if k == serial_del:
                ind = self.item_list[-1].index(line)
                self.item_list[-1].pop(ind)
                print("Item deleted")


    def view_list(self):
        '''This method views saved lists'''
        
        for line in self.item_list[-1]:
            print(line[0],line[1],line[2])
                

    def close_program(self):
        "Method closes the program"
        print('Exiting Program.')
        sys.exit(0)        


print("Welcome to the Hospital records")

def main():
    request = Hospital_file()

    x = False
    while not x:
        add_item = input('Do you want to view list, add or remove an item? [A for Add, R for Remove and V for view and C to close]: ')
        add_item = add_item.upper()
        
        if add_item == "A":
            request.get_type()
            request.get_itemName()
            request.get_itemSerial()
            request.create_item()
        
        elif add_item == "R":
            request.delete_item()
            
        elif add_item == "V":
            request.view_list()
        
        elif add_item == "C":
            x = True
            
        else:
            print("Error response")
            x = True

if __name__ == '__main__':
    main()
    

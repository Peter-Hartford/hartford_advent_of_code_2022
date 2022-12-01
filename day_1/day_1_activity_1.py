from pathlib import Path 

class Elf:
    def __init__(self, calorie_list = [1000, 1000], num = 0):
        self.calorie_list = calorie_list
        self.name = 'Elf %s'%num

    def sum_calories(self):
        calorie_sum = sum(self.calorie_list)

        return calorie_sum

    def add_item(self,item):
        self.calorie_list.append(item)

class Elf_manager:
    def __init__(self, file_path = Path()): 
        #Create list of elf objects from 
        self.elf_list = [Elf([],1)]
        self.sum_list = list()
        self.name_list = list()

        self.file_path = file_path
        self.complete_data = None
    
        self.open_file()

    def open_file(self):
        with open(self.file_path) as data_file: 
            self.complete_data = data_file.readlines()
            i=0
            for data in self.complete_data:
                if data=='\n':
                    i+=1
                    self.elf_list.append(Elf([],i+1))
                
                else:
                    self.elf_list[i].add_item(int(data))

        for elf in self.elf_list:
            self.sum_list.append(elf.sum_calories())
            self.name_list.append(elf.name)   

    def find_max(self):
        maximum_calories = max(self.sum_list)

        return maximum_calories

    def find_top_places(self, place_total = 3):
        sum_list = self.sum_list
        top_calorie_list = list()

        for i in range(place_total):
            cal = max(sum_list)
            top_calorie_list.append(cal)
            sum_list.remove(cal)

        return top_calorie_list, sum(top_calorie_list)

        


def main():
    file_path = Path(__file__).parent / 'data/elf_calories_input.txt'
    elf_manager = Elf_manager(file_path)


    print(elf_manager.find_max())
    print(elf_manager.find_top_places())

if __name__=='__main__':
    main()
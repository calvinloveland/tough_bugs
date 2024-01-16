class ImportantThing():

    def __init__(self,important_list=[]):
        self.important_list = important_list


if __name__ == '__main__':
    thing1 = ImportantThing()
    thing2 = ImportantThing()
    thing1.important_list.append('foo')
    print(thing2.important_list)
class TagCloud:
    def __init__(self):
        self.__tags = {}

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower())

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        iter(self.__tags)

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lover(), 0) + 1

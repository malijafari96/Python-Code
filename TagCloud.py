class TagCloud:
    def __init__(self):
        self.tags = {}

    def __getitem__(self, tag):
        return self.tags.get(tag.lower())

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        iter(self.tags)

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lover(), 0) + 1

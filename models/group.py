class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __str__(self):
        return "<Group: {}, {}, {}>".format(self.name, self.header, self.footer)

    def __repr__(self):
        return "<Group: id {}, {}, {}, {}>".format(self.id, self.name, self.header, self.footer)
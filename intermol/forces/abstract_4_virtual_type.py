from abstract_type import AbstractType


class Abstract4VirtualType(AbstractType):
    __slots__ = ['bondingtype1', 'bondingtype2', 'bondingtype3', 'bondingtype4',
                 'bondingtype4']

    def __init__(self, bondingtype1, bondingtype2, bondingtype3, bondingtype4,
                 bondingtype5):
        super(Abstract4VirtualType, self).__init__()
        self.bondingtype1 = bondingtype1
        self.bondingtype2 = bondingtype2
        self.bondingtype3 = bondingtype3
        self.bondingtype4 = bondingtype4
        self.bondingtype5 = bondingtype5

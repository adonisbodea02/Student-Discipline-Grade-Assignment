class AddOperation:
    '''
    class that models an add operation in the controller
    '''
    def __init__(self, Object):
        '''
        Constructor for AddOperation class
        Object - the object that was added
        '''
        self.__Object = Object

    def getObject(self):
        return self.__Object

class RemoveOperation:
    '''
    class that models a remove operation in the controller
    '''

    def __init__(self, Object):
        '''
        Constructor for RemoveOperation class
        Object - the object that was removed
        '''
        self.__Object = Object

    def getObject(self):
        return self.__Object

class UpdateOperation:
    '''
    class that models an update operation in the controller
    '''

    def __init__(self, OldObject, UpdatedObject):
        '''
        Constructor for UpdateOperation class
        OldObject - the instance before updating
        UpdatedObject - the instance after updating
        '''
        self.__OldObject = OldObject
        self.__UpdatedObject = UpdatedObject

    def getOldObject(self):
        return self.__OldObject

    def getUpdatedObject(self):
        return self.__UpdatedObject

class CascadeRemoveOperation:
    '''
    class that models an cascade remove operation in the controller
    '''

    def __init__(self, Parent_Object, Affected_Objects):
        '''
        Constructor for cascade remove class
        Parent_Object - the object that caused the cascade removal
        Affected_Objects - the objects that were deleted because of the parent_object removal
        '''
        self.__Parent_Object = Parent_Object
        self.__Affected_Objects = Affected_Objects

    @property
    def Parent_Object(self):
        return self.__Parent_Object

    @property
    def Affected_Objects(self):
        return self.__Affected_Objects

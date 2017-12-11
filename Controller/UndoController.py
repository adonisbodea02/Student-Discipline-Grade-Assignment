class UndoController:
    '''
    This class controls the undo operations over all application controllers
    It is required so that we have a record of what controller must perform each undo operation
    '''
    def __init__(self):
        self.__controllers = []
        self.__index = -1

    def recordUpdatedController(self, modifiedController):
        '''
        every time an application controller record an operation with support for undo it must call this method
        Input - modifiedController - A list of controllers that can undo the operation
        Important: An operation can involve multiple distinct controllers, so a list of controllers must be provide in that case
        Output - the current list of controllers is modified and the index is set to the last list of modified controllers
        '''
        self.__controllers.append(modifiedController)

        self.__controllers = self.__controllers[0:self.__index + 2]

        self.__index = len(self.__controllers) - 1

    def undo(self):
        '''
        undo the last performed operation by any application controller
        '''
        if self.__index < 0:
            return False

        for controller in self.__controllers[self.__index]:
            controller.undo()

        self.__index -= 1
        return True

    def redo(self):
        '''
        redo the last performed operation by any application controller
        '''
        if self.__index >= len(self.__controllers) - 1:
            return False

        for controller in self.__controllers[self.__index]:
            controller.redo()

        self.__index += 1
        return True
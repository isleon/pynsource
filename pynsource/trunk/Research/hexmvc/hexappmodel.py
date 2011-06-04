#!/usr/bin/env python

class App:
    def __init__(self, persistence):
        self.modelmgr = ModelMgr(self, persistence)
        
    def New(self):
        self.modelmgr.Clear()

    def Load(self):
        cmd = CmdLoadModel(self)
        cmd.Execute()

    def Save(self):
        cmd = CmdSaveModel(self)
        cmd.Execute()

    def CreateA(self, info):
        cmd = CmdCreateA(self)
        cmd.info = info
        cmd.Execute()
        return cmd.result

    def CmdAddInfoToA(self, a, info):
        cmd = CmdAddInfoToA(self)
        cmd.a = a
        cmd.info = info
        cmd.Execute()

    def GetA(self, n):
        return self.modelmgr.model[n]


class Cmd:
    def __init__(self, app):
        self.app = app

class CmdLoadModel(Cmd):
    def Execute(self):
        self.app.modelmgr.LoadAll()

class CmdSaveModel(Cmd):
    def Execute(self):
        self.app.modelmgr.SaveAll()

class CmdCreateA(Cmd):
    def Execute(self):
        self.result = ModelA(self.info)
        self.app.modelmgr.model.append(self.result)

class CmdAddInfoToA(Cmd):
    def Execute(self):
        self.a.Do(self.info)



class ModelMgr:        
    def __init__(self, app, persistence):
        self.app = app
        self.persistence = persistence
        self.Clear()

    def __str__(self):
        return str([str(m) for m in self.model])

    def Clear(self):
        self.model = []
        
    def LoadAll(self):
        self.model = self.persistence.LoadAll()

    def SaveAll(self):
        self.persistence.SaveAll(self.model)

class ModelA:
    def __init__(self, info):
        self.info = info
        
    def __str__(self):
        return "A-" + self.info

    def Do(self, msg):
        self.info += " " + msg

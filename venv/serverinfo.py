class ServerInfo:
    def __init__(self, server, channels):
        self._server = server
        self._role_id = 0
        self._channels = channels

    def __repr__(self):
        return {'server':self._server, 'role_id':self._role_id, 'channels':self._channels}

    def __str__(self):
        return 'ServerInfo(server='+self._server+', role_id='+str(self._role_id)+', channels='+str(self._channels)+ ')'

    def setID(self, new_id):
        self._role_id = new_id

    def getID(self):
        return self._role_id

    def getChannels(self):
        return self._channels
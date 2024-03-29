class Session:

    def __init__(self, name, description, pdml):
        self.name = name
        self.description = description
        self.pdml = pdml


class WorkSpace:

    def __init__(self, name, workspace_path):
        self.name = name
        self.workspace_path = workspace_path
        self.sessions = []
        self.currentSession = None

    def addSession(self, name, description, pdml):
        self.sessions.append(Session(name, description, pdml))

    def switchSessions(self, name):
        for session in self.sessions:
            if session.name == name:
                self.currentSession = session
                break

    def removeSession(self, name):
        for session in self.sessions:
            if session.name == name:
                self.sessions.remove(session)
                break


class WorkSpace_Manager:

    def __init__(self):
        self.workspaceList = []

    def removeWorkspace(self, name):
        for workspace in self.workspaceList:
            if workspace.name == name:
                self.workspaceList.remove(workspace)
                break

    def addWorkspace(self, name, path):
        self.workspaceList.append(WorkSpace(name, path))

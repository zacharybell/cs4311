class WorkSpace:
    name = "";
    workspacePath = "";
    sessions = "";

    def __init__(self, name, workspacepath, sessions):
        self.name = name
        self.workspacepath = workspacepath
        self.sessions = sessions
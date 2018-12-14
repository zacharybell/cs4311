class Session:
    name = "";
    description = "";
    #pdml = pdml(); requires a pdml object

    def __init__(self, name, description, pdml):
        self.name = name
        self.description = description
        self.pdml = pdml


    def create_session(Session, pdml):
        def get(self):
            session = Session.create_Session()
            if "count" in session:
                session["count"] = session["count"] + 1
            else:
                session["count"] = 1


    def open_session(workspace_path, name):
        r = workspace_path('PUT', Session)
        prepped = r.WorkSpace()
        s = name.Session()
        assert isinstance(s.send, )#needs PDML
        resp = s.send(prepped)
        if resp.status_code != 1:
            return resp.status_code


    def close_session(self, workspace_path, name):
        self.workspace_path = workspace_path
        self.name = name


    def add_pdml(self):
        pass


class WorkSpace:
    name = "";
    workspace_Path = "";


    def __init__(self, name, workspace_path):
        self.name = name
        self.workspace_path = workspace_path

    def create_Workspace(WorkSpace, Session, name):
        pass

    def switch(WorkSpace, Session, name):
        pass

class WorkSpace_Manager:

    def __init__(self):
        pass

# from  LogsUnit.MasterAgent import MasterAgent


class CollectorAgent:
    def __init__(self, master):
        self.eventIds = []
        self.category = "Security"
        self.masterAgent = master

    def newLogReceived(self, log):
        self.masterAgent.saveNewLog(log)

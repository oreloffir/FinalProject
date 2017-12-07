from LogsUnit.CollectorAgent import CollectorAgent
from LogsUnit.MasterAgent import MasterAgent


class LogsUnitManager(object):
    def __init__(self):
        self.masterAgent = MasterAgent()

    def updateMasterAgent(self, master):
        if type(MasterAgent) == type(master):
            self.masterAgent = master

    def addCollectorAgent(self, agent):
        if type(CollectorAgent) == type(agent):
            self.masterAgent.collectorAgents.append(agent)
from LogsUnit.LogsUnitManager import LogsUnitManager
from LogsUnit.CollectorAgent import CollectorAgent

manager = LogsUnitManager()

collector = CollectorAgent(manager.masterAgent)
manager.masterAgent.addCollectorAgent(collector)

collector.newLogReceived("orel LOG")

input()
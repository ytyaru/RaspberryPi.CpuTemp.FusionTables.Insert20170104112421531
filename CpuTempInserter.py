#!python3
#encoding:utf-8
from datetime import datetime
import FusionTablesRequester

db_path = './Google.Accounts.sqlite3'
project_id = 'project-id-000000000000'
document_id = 'document_id_abcdefg'

class CpuTempInserter:
    def __init__(self):
        self.requester = FusionTablesRequester.FusionTablesRequester()
        self.requester.initialize(db_path, project_id)

    def get_cpu_temp(self):
        with open("/sys/class/thermal/thermal_zone0/temp","r") as f:
            return f.read()

    def insert(self, cpu_temp=None):
        if not(cpu_temp is None):
            cpu_temp = self.get_cpu_temp()
        sql = "INSERT INTO %s (Timestamp, CpuTemperature) VALUES('%s',%s)" % (document_id, "{0:%Y-%m-%d %H:%M:%S}".format(datetime.now()), self.get_cpu_temp())
        self.requester.query(sql, is_write_response=True)


if __name__ == "__main__":
    run = CpuTempInserter()
    run.insert()

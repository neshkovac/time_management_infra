import typing
from aws_cdk import core
from aws_cdk import aws_dynamodb as _ddb
from stacks.persistance.tables.user_table import UserTable
from stacks.persistance.tables.schedule_table import ScheduleTable

class DynamoDBStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str)-> None:
        super().__init__(scope,id) 

        user_table = UserTable(self) 
        schedule_table = ScheduleTable(self)

        self.tables: typing.Sequence[_ddb.Table] = [user_table,schedule_table]
    
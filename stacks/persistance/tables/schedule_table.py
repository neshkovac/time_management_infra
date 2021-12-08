from aws_cdk import core
from aws_cdk import aws_dynamodb as _ddb

class ScheduleTable(_ddb.Table):
    def __init__(self,scope: core.Construct):
        super().__init__(
            scope,
            "schedule-table",
            table_name="schedule-table",
            partition_key=_ddb.Attribute(name="id", type=_ddb.AttributeType.STRING)
        )
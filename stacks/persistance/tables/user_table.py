from aws_cdk import core
from aws_cdk import aws_dynamodb as _ddb

class UserTable(_ddb.Table):
    def __init__(self,scope: core.Construct):
        super().__init__(
            scope,
            "user-table",
            table_name="user-table",
            partition_key=_ddb.Attribute(name="id", type=_ddb.AttributeType.STRING)
        )
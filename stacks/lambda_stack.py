from aws_cdk import core
from aws_cdk import aws_lambda as _lambda
from util import constants

class LambdaStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str)->None:
        super().__init__(scope,id)


        create_user_handler = _lambda.Function(
            self,
            "create-user-handler",
            runtime=_lambda.Runtime.NODEJS_14_X,
            code = _lambda.Code.from_asset('../time_management_lambdas/handlers/user/create'),
            handler="handler.handler",
            environment= {
                "LOG_LEVEL" : constants.LOG_LEVEL
            }
        )

        self.handlers = dict(
            create_user_handler = create_user_handler
        )
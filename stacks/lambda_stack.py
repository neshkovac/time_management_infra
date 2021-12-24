from aws_cdk import core
from aws_cdk import aws_lambda as _lambda
from util import constants

class LambdaStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str)->None:
        super().__init__(scope,id)
        handlers_dir = "../time_management_lambdas/dist/handlers"
        def attach_lambda_handler(function_name,handler_dir):
            return _lambda.Function(
                self,
                f"{function_name}",
                function_name=f"{function_name}",
                runtime=_lambda.Runtime.NODEJS_14_X,
                code = _lambda.Code.from_asset(f"{handlers_dir}/{handler_dir}"),
                handler="handler.handler",
                environment= {
                    "LOG_LEVEL" : constants.LOG_LEVEL
                }
            )
        create_user_handler = attach_lambda_handler("create-user-handler","user/create")
        get_users_handler = attach_lambda_handler("get-users-handler","user/get_all")
        get_user_handler = attach_lambda_handler("get-single-user-handler","user/get_one")
        update_user_handler = attach_lambda_handler("update-user-handler","user/update")
        delete_user_handler = attach_lambda_handler("delete-user-handler","user/delete")

        create_schedule_handler = attach_lambda_handler("create-schedule-handler", "schedule/create")
        get_schedules_handler = attach_lambda_handler("get-schedules-handler", "schedule/get_all")
        get_schedule_handler = attach_lambda_handler("get-single-shedule-handler","schedule/get_one")
        update_schedule_handler = attach_lambda_handler("update-schedule-handler","schedule/update")
        delete_schedule_handler = attach_lambda_handler("delete-schedule-handler","schedule/delete")

        self.handlers = dict(
            create_user_handler = create_user_handler,
            create_schedule_handler = create_schedule_handler,
            get_users_handler = get_users_handler,
            get_schedules_handler = get_schedules_handler,
            get_user_handler = get_user_handler,
            get_schedule_handler = get_schedule_handler,
            update_user_handler = update_user_handler,
            update_schedule_handler = update_schedule_handler,
            delete_user_handler = delete_user_handler,
            delete_schedule_handler = delete_schedule_handler
        )
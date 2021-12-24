from aws_cdk import core
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_logs as _logs
from aws_cdk import aws_apigateway as _apigw

class ApiGatewayStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, handlers: dict):
        super().__init__(scope,id)

        def lambda_integration_factory(handler)-> _apigw.LambdaIntegration:
            return _apigw.LambdaIntegration(
            handler = handlers[handler],
            )

        api = _apigw.RestApi(
            self,
            "main-api-gw",
            description="Handle user and schedule related operations",
            rest_api_name="customer-schedule-apigw"
        )

        create_user_int = lambda_integration_factory('create_user_handler')
        get_users_int = lambda_integration_factory('get_users_handler')
        get_user_int = lambda_integration_factory('get_user_handler')
        update_user_int = lambda_integration_factory('update_user_handler')
        delete_user_int = lambda_integration_factory('delete_user_handler')

        create_schedule_int = lambda_integration_factory('create_schedule_handler')
        get_schedules_int = lambda_integration_factory('get_schedules_handler')
        get_schedule_int = lambda_integration_factory('get_schedule_handler')
        update_schedule_int = lambda_integration_factory('update_schedule_handler')
        delete_schedule_int = lambda_integration_factory('delete_schedule_handler')

        users = api.root.add_resource("users")
        users.add_method("GET", get_users_int)
        users.add_method("POST", create_user_int)
        user = users.add_resource("{id}")
        user.add_method("GET",get_user_int)
        user.add_method("PUT", update_user_int)
        user.add_method("DELETE", delete_user_int)

        schedules = api.root.add_resource("schedules")
        schedules.add_method("GET", get_schedules_int)
        schedules.add_method("POST", create_schedule_int)
        schedule = schedules.add_resource("{id}")
        schedule.add_method("GET", get_schedule_int)
        schedule.add_method("PUT", update_schedule_int)
        schedule.add_method("DELETE", delete_schedule_int)
        
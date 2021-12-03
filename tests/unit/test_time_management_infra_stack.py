import aws_cdk as core
import aws_cdk.assertions as assertions

from time_management_infra.time_management_infra_stack import TimeManagementInfraStack

# example tests. To run these tests, uncomment this file along with the example
# resource in time_management_infra/time_management_infra_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TimeManagementInfraStack(app, "time-management-infra")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

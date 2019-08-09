from aws_cdk import (
    aws_iam as iam,
    core
)

from .inner_stack import InnerStack


class OuterStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        local_user = iam.User(self, "MyIAMUser")

        InnerStack(self, "InnerStack", user=local_user, **kwargs)


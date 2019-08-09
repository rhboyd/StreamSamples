from aws_cdk import (
    aws_iam as iam,
    core
)

from .shark_utils import SharkProps


class BabyShark(core.Stack):

    def __init__(self, scope: core.Construct, id: str, props: SharkProps, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        local_user = iam.User(self, "MyIAMUser", user_name=props.baby_name)


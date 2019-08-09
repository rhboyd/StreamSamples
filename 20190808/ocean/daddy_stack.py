from aws_cdk import (
    aws_iam as iam,
    core
)
import hashlib
from .shark_utils import SharkProps


class DaddyShark(core.Stack):

    def __init__(self, scope: core.Construct, id: str, props: SharkProps, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        local_user = iam.User(self, "MyIAMUser")

        self._child_name = local_user.user_arn

    @property
    def child_name(self):
        return self._child_name

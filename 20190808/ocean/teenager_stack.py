from aws_cdk import (
    aws_iam as iam,
    core
)
import hashlib

from .shark_utils import SharkProps


class TeenShark(core.Stack):

    def __init__(self, scope: core.Construct, id: str, shark_name: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        local_user = iam.User(self, "MyIAMUser", user_name=hashlib.md5(bytes(shark_name , encoding="utf-8")).hexdigest())


from aws_cdk import (
    aws_s3 as s3,
    aws_iam as iam,
    core
)


class InnerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, user: iam.User, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self, id="MyBucket")

        bucket.grant_read(user)

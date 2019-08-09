#!/usr/bin/env python3

from aws_cdk import core

from ocean.baby_stack import BabyShark
from ocean.mama_stack import MamaShark
from ocean.daddy_stack import DaddyShark
from ocean.teenager_stack import TeenShark

from ocean.shark_utils import SharkProps

app = core.App()
props = SharkProps(
    baby_name="Baby_Sinclair",
    mama_name="Fran_Sinclair",
    daddy_name="Earl_Sinclair"
)

baby = BabyShark(app, "baby-stack", props=props, env={'region': 'us-east-2'})
mama = MamaShark(app, "mama-stack", props=props, env={'region': 'us-east-2'})


daddy = DaddyShark(app, "daddy-stack", props=props, env={'region': 'us-east-2'})

teen = TeenShark(app, "teen-stack", shark_name=daddy.child_name, env={'region': 'us-east-2'})


app.synth()

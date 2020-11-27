#!/usr/bin/env python3

from aws_cdk import core

from my_pipeline.my_pipeline_stack import MyPipelineStack


app = core.App()
MyPipelineStack(app, "my-pipeline")

app.synth()

import streamlit as st
from utils import REGISTRY

METRICS = REGISTRY.get_metrics()

@METRICS.REQUEST_TIME.time()
def i_sleep():
    sleep(1.0)


i_sleep()

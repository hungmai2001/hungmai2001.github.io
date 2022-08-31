from ctypes import sizeof
from ctypes.wintypes import SIZE
import streamlit as st
import numpy as np
import pandas as pd
import os.path
name = st.text_input("Nhap ten cua ban")
st.write("Ten cua ban la: ", name)
name_father = st.text_input("Nhap ten ba ban")
st.write("Ten ba ban la: ", name_father)
file = st.file_uploader("Choose a file")
if file is not None:
    st.write("Kich thuoc file la: ", file.size)
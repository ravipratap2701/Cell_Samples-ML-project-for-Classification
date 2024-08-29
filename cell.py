import streamlit as st
st.title("Cell_Samples")
import numpy as np
import pickle
with open('model.pkl','rb') as file:
    cell_model= pickle.load(file)
def cell_samples(Clump, UnifSize, UnifShape, MargAdh, SingEpiSize, BareNuc,BlandChrom, NormNucl, Mit):
    array= np.array([[Clump, UnifSize, UnifShape, MargAdh, SingEpiSize, BareNuc,BlandChrom, NormNucl, Mit]])
    final_model= cell_model.predict(array)
    return final_model
Clump=st.slider("Clump",min_value=1, max_value=40)
UnifSize=st.slider("UnifSize",min_value=1, max_value=40)
UnifShape=st.slider("UnifShape",min_value=1, max_value=40)
MargAdh=st.slider("MargAdh",min_value=1, max_value=40)
SingEpiSize=st.slider("SingEpiSize",min_value=1, max_value=40)
BareNuc=st.slider("BareNuc",min_value=1, max_value=40)
BlandChrom=st.slider("BlandChrom",min_value=1, max_value=40)
NormNucl=st.slider("NormNucl",min_value=1, max_value=40)
Mit=st.slider("Mit",min_value=1, max_value=40)
if st.button("Predicted value"):
    model_value= cell_samples(Clump, UnifSize, UnifShape, MargAdh, SingEpiSize, BareNuc,BlandChrom, NormNucl, Mit)
    st.write(f"The final value is {model_value[0]}")

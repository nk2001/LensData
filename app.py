import streamlit as st


st.title('Contact Lens Fitting App')
st.header("PROBLEM STATEMENT")
st.text("This App would suggest the type of lens for an individual based on the following information:")
st.text("Dataset used from UCI repository: https://archive.ics.uci.edu/ml/datasets/Lenses")
st.text("Age group of the patient: (1)Young (2)Pre-presbyopic (3)Presbyopic")
st.text("Spectacle prescription:  (1)myope (2)hypermetrope")
st.text("Astigmatic: (1)No, (2)Yes")
st.text("Tear production rate: (1) Reduced, (2) Normal")

image = Image.open('https://www.pexels.com/photo/person-holding-silver-wedding-band-5843337/')
st.image(image, use_column_width=True)
st.subheader('Please fill in the details on the left sidebar and click on the button below!')


Agegrp = st.sidebar.radio("Patient Age Group", options=["Young", "Pre-presbyopic", "Presbyopic"])
SpectaclePrescription = st.sidebar.radio("Spectacle Prescription", options=["Myope", "Hypermetrope"])
Astigmatic = st.sidebar.radio("Astigmatic", options=["No","Yes"])

TearProduction = st.sidebar.radio("Tear Production", options=["Reduced","Normal"])
A={"No":1, "Yes":2}
Ag = {"Young":1, "Pre-presbyopic":2, "Presbyopic":3}
Pr = {"Myope":1, "Hypermetrope": 2}
Tp = {"Reduced":1, "Normal":2}
Lens = ["The patient should be fitted with HARD contact lenses",
		"The patient should be fitted with SOFT contact lenses",
		"The patient should NOT be fitted with contact lenses" ]

def lens_type(Age, Spec, Ast, Tear):
    if (Tear == 2) and (Ast == 2) and (Spec == 1):
        return 0
    if (Tear ==2) & (Ast == 2) & (Spec == 2) & (Age == 1):
        return 0
    if (Tear ==2) & (Ast == 1) & (Spec == 2):
        return 1
    if (Tear ==2) & (Ast == 1) & (Spec == 1) & ((Age == 1) or (Age == 2)):
        return 1
    else:
        return 2

if (st.button('Get Lens Suggestion')):
    feat_cols = ['Agegrp', 'SpectaclePrescription', 'Astigmatic', 'TearProduction']
    Ast = A[Astigmatic]
    Age = Ag[Agegrp]
    Spec = Pr[SpectaclePrescription]
    Tear = Tp[TearProduction]
    result = lens_type(Age, Spec, Ast, Tear)
    st.write(Lens[result])

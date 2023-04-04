import streamlit as st

def main():
    st.set_page_config(page_title='X-ray Scan Analysis',layout='wide')
    
    # Title and instructions
    col1,col2,col3= st.columns(3)
    with col2:
        st.title('X-ray Scan Analysis')
        
    st.write('Please input an X-ray scan image and generate a report.')
    col1,col2 = st.columns(2)
    with col1:
        uploaded_file = st.file_uploader('Please upload an X-ray scan image:', type=['jpg', 'jpeg', 'png'])
    with col2:
        st.image("chest.jpg")
        st.button("Generate Report")
    if uploaded_file is not None:
        # Button to generate report
        if st.button('Generate Report'):
            st.write('Generating report...')
            
            # TODO: write code to generate report based on uploaded_file
            
            # Example code to display report
            st.write('Report generated!')
            st.write('Patient ID: 12345')
            st.write('Diagnosis: Pneumonia')
            st.write('Recommendation: Treatment with antibiotics.')
            st.write('Doctor\'s note: Follow up appointment scheduled for 2 weeks.')
    
if __name__ == '__main__':
    main()

import streamlit as st

from extractor import extract_text_from_pdf
from extractor import extract_bill_data

from excel_filler import fill_excel


st.title("Solar Load Calculator")


uploaded_file = st.file_uploader(
    "Upload Electricity Bill PDF",
    type=["pdf"]
)


if uploaded_file:

    # Save uploaded file
    with open("uploads/bill.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Bill Uploaded Successfully")

    # Extract text
    text = extract_text_from_pdf("uploads/bill.pdf")
    st.subheader("PDF Raw Text")
    st.text(text)

    # Extract important data
    data = extract_bill_data(text)

    st.subheader("Extracted Data")

    st.write(data)

    # Fill Excel
    output_file = fill_excel(data)

    st.success("Excel Generated Successfully")

    # Download button
    with open(output_file, "rb") as file:

        st.download_button(
            label="Download Filled Excel",
            data=file,
            file_name="solar_output.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
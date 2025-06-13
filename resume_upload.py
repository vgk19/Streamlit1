import streamlit as st
import PyPDF2
import docx

# === 이력서 업로드 컴포넌트 ===
def resume_upload_component():
    st.subheader("이력서 업로드")
    uploaded_file = st.file_uploader(
        "이력서를 업로드해주세요 (PDF, DOCX 형식)",
        type=["pdf", "docx"],
        help="이력서를 분석하여 맞춤형 면접 질문을 생성합니다.",
        key="resume_uploader"
    )

    text = ""
    if uploaded_file is not None:
        file_type = uploaded_file.name.split('.')[-1]
        if file_type == "pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            for page in range(len(pdf_reader.pages)):
                text += pdf_reader.pages[page].extract_text()
        elif file_type == "docx":
            doc = docx.Document(uploaded_file)
            for para in doc.paragraphs:
                text += para.text + "\n"
        
        st.session_state.resume_text = text

        st.success("이력서가 성공적으로 업로드되었습니다!")
        
        with st.expander("📄 업로드된 이력서 보기", expanded=False):
            st.write(st.session_state.resume_text[:2000] + ("..." if len(st.session_state.resume_text) > 2000 else ""))
    
    return text  # 필요한 경우에만 반환

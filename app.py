import streamlit as st

# Inisialisasi session_state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Fungsi untuk berpindah halaman
def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# Sidebar navigasi
with st.sidebar:
    st.markdown("## Navigasi SOP")
    page = st.radio(
        "Pilih Halaman:",
        ("Home", "HCSP", "Benefit", "Payroll"),
        index=("Home", "HCSP", "Benefit", "Payroll").index(st.session_state.page)
    )
    st.session_state.page = page

# Tampilan halaman Home
if st.session_state.page == "Home":
    st.markdown("""
    <h1 style="
        font-size: 3em;
        font-weight: 900;
        background: linear-gradient(to right, #ED5626, #F69322, #FEC025);
        -webkit-background-clip: text;
        color: transparent;
        text-align: left;
        margin-top: -20px;
    ">
    FINANCIAL PLANNING
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("Welcome to the **Financial Planning Team**, with the roles: providing bank-wide strategy and financial planning insights. Click on each leader to explore their team members.")
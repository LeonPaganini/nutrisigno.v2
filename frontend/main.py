"""
Streamlit frontend for the NutriSigno skeleton.

This application demonstrates the basic flow described in the project
specification.  Users can log in with email and date of birth,
submit their questionnaire answers, request a report, and trigger
generation of a shareable image or downloadable PDF.  All
communication with the backend is delegated to the stubbed API
client.
"""

import json
import streamlit as st

from frontend.services.api_client import (
    login as api_login,
    submit_answers,
    request_report,
    get_report,
    generate_image,
    generate_pdf,
)


st.set_page_config(page_title="NutriSigno", layout="centered")
st.title("NutriSigno")


def main() -> None:
    """Main entry point for the Streamlit app."""
    if "session" not in st.session_state:
        st.session_state.session = None
    if st.session_state.session is None:
        render_login()
    else:
        render_questionnaire()


def render_login() -> None:
    """Render the login form."""
    st.header("Login")
    email = st.text_input("Email")
    dob = st.text_input("Data de Nascimento (YYYY-MM-DD)")
    if st.button("Entrar"):
        if email and dob:
            resp = api_login(email, dob)
            st.session_state.session = resp.get("session")
            st.success("Logado com sucesso (stub)")
            st.experimental_rerun()
        else:
            st.error("Preencha email e data de nascimento.")


def render_questionnaire() -> None:
    """Render the questionnaire submission and report generation UI."""
    st.header("Questionário")
    answers_input = st.text_area("Responda ao questionário (JSON)", value="{}")
    if st.button("Enviar respostas"):
        try:
            answers = json.loads(answers_input)
        except Exception:
            st.error("JSON inválido")
            return
        response = submit_answers(answers)
        st.session_state.resp_id = response["resp_id"]
        st.session_state.calorie_target = response["calorie_target"]
        st.success("Respostas enviadas")
    # Request report when responses exist and no report yet
    if st.session_state.get("resp_id") and not st.session_state.get("report_id"):
        if st.button("Solicitar relatório"):
            rep = request_report(st.session_state.resp_id)
            st.session_state.report_id = rep["report_id"]
            st.session_state.report_status = rep["status"]
            st.success("Relatório solicitado")
    # Display report if available
    if st.session_state.get("report_id"):
        report = get_report(st.session_state.report_id)
        st.write(report)
        if report.get("status") == "ready":
            # Actions for ready report
            if st.button("Gerar imagem"):
                img_info = generate_image(st.session_state.report_id)
                st.image(img_info["url"], caption="Preview da imagem (stub)")
            if st.button("Baixar PDF"):
                pdf_info = generate_pdf(st.session_state.report_id)
                st.write(f"PDF disponível em: {pdf_info['url']}")
            if st.button("Fechar plano"):
                st.write("Redirecionando para pagamento (stub)")


if __name__ == "__main__":
    main()
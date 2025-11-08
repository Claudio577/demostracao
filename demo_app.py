import streamlit as st
from PIL import Image

st.set_page_config(page_title="EduFin AI Cloud — Demo", page_icon="💡", layout="wide")

# =========================
# 🔹 Header do Projeto
# =========================
st.markdown("""
# 💡 **EduFin AI Cloud**
### Inteligência Financeira Pessoal com IA
*Uma aplicação que analisa sua saúde financeira em tempo real, combinando Machine Learning e Firebase.*
""")

col1, col2 = st.columns([1.2, 0.8])

# =========================
# 🔹 Coluna 1 – Descrição
# =========================
with col1:
    st.markdown("""
    #### 🧠 Como funciona
    1. Faça login com seu e-mail.  
    2. Insira seus dados financeiros (renda, gastos, dívidas, etc).  
    3. O modelo de IA analisa e retorna sua **saúde financeira**:
       - 🔴 Baixa  
       - 🟡 Média  
       - 🟢 Alta  
    
    #### ⚙️ Tecnologias usadas
    - **Streamlit** (Interface)  
    - **Firebase Auth + Firestore** (Banco e Login)  
    - **TensorFlow / Keras** (Modelo de IA)  
    - **Scikit-Learn** (Pré-processamento)
    """)

    st.markdown("---")
    st.markdown("🌐 [Ver código no GitHub](https://github.com/seu-usuario/edufin-ai-cloud)")
    st.markdown("📹 [Demonstração no YouTube](https://youtu.be/...)")

# =========================
# 🔹 Coluna 2 – Mini Demo
# =========================
with col2:
    st.markdown("### 🧩 Mini Simulação")

    renda = st.slider("💰 Renda mensal (R$)", 500, 20000, 5000)
    gastos = st.slider("💳 Gastos mensais (R$)", 0, 20000, 3000)
    dividas = st.slider("📉 Dívidas (R$)", 0, 50000, 1000)
    poupanca = st.slider("🏦 Poupança (R$)", 0, 50000, 2000)
    idade = st.slider("🎂 Idade", 18, 80, 30)
    investimentos = st.slider("📈 Investimentos (R$)", 0, 50000, 1000)

    # Mock de IA (para demonstração simples)
    score = (renda - gastos - dividas + poupanca + investimentos) / (renda + 1)
    if score < 0.3:
        st.error("🔴 Baixa Saúde Financeira")
    elif score < 0.6:
        st.warning("🟡 Média Saúde Financeira")
    else:
        st.success("🟢 Alta Saúde Financeira")

st.markdown("---")
st.caption("© 2025 EduFin AI Cloud — Projeto de demonstração")

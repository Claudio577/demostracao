import streamlit as st
from PIL import Image

# ===============================
# ⚙️ Configuração da página
# ===============================
st.set_page_config(
    page_title="EduFin AI Cloud — Sua Saúde Financeira com IA",
  
    layout="wide"
)

# ===============================
# Estilo visual tipo Dribbble (moderno e limpo)
# ===============================
st.markdown("""
<style>
body {
    background-color: #fafafa;
    color: #222;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3, h4 {
    color: #111;
    font-weight: 600;
    font-family: 'Poppins', sans-serif;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.stButton>button {
    border-radius: 8px;
    background-color: #FF5B6A;
    color: white;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #E14B58;
}
a {
    color: #FF5B6A !important;
    text-decoration: none;
    font-weight: 500;
}
a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# Cabeçalho principal
# ===============================
st.title(" EduFin AI Cloud")
st.subheader("Entenda sua vida financeira de forma simples e inteligente ")
st.write("""
O **EduFin AI Cloud** é um aplicativo que ajuda você a **entender como está sua saúde financeira**.  
Com ele, você insere informações básicas — como quanto ganha, quanto gasta, e quanto tem guardado —  
e a **inteligência artificial calcula automaticamente** um “nível de saúde financeira” pra você.

Tudo isso de forma **simples, visual e rápida**, sem precisar entender de economia ou tecnologia!
""")

# ===============================
# Explicação do Projeto
# ===============================
st.markdown("""
## Como o EduFin ajuda você

1. **Você informa seus dados** — sua renda, seus gastos e o quanto tem guardado.  
2. **A IA faz os cálculos automaticamente** para entender se sua situação financeira está boa, regular ou preocupante.  
3. **Você recebe um resultado visual**, com cores e mensagens que mostram o seu nível financeiro atual.  

Assim, você pode tomar decisões melhores sobre como usar o seu dinheiro —  
como economizar, investir ou reduzir gastos.
""")

# ===============================
#  Mini Simulação Interativa
# ===============================
st.markdown("---")
st.header(" Experimente Agora — Simule sua Situação Financeira")

st.write("Use os controles abaixo para simular sua renda, gastos e investimentos e veja como sua saúde financeira muda:")

col1, col2 = st.columns(2)

with col1:
    renda = st.slider("Quanto você ganha por mês (R$)", 500, 20000, 4000)
    gastos = st.slider("Quanto você gasta por mês (R$)", 0, 20000, 2500)
    dividas = st.slider("Dívidas atuais (R$)", 0, 50000, 1000)

with col2:
    poupanca = st.slider("Dinheiro guardado (R$)", 0, 50000, 2000)
    investimentos = st.slider("Investimentos (R$)", 0, 50000, 1500)
    idade = st.slider("Sua idade", 18, 80, 30)

# ===============================
# Cálculo simples (como se fosse a IA)
# ===============================
score = (renda - gastos - dividas + poupanca + investimentos) / (renda + 1)

st.markdown("### 💡 Seu Resultado:")

if score < 0.3:
    st.error("🔴 Sua saúde financeira está **baixa**.\n\nVocê pode estar gastando mais do que ganha ou com muitas dívidas.")
elif score < 0.6:
    st.warning("🟡 Sua saúde financeira está **regular**.\n\nEstá no caminho certo, mas ainda há espaço para melhorar.")
else:
    st.success("🟢 Parabéns! Sua saúde financeira está **muito boa**.\n\nVocê tem um bom equilíbrio entre ganhos e gastos.")

# ===============================
#  Explicação amigável do resultado
# ===============================
st.info("""
**O que esse resultado significa?**  
- **Baixa:** talvez seja hora de rever seus gastos ou quitar dívidas.  
- **Média:** você está indo bem, mas ainda pode melhorar.  
- **Alta:** ótimo! Continue controlando seus gastos e poupando.  

Essa é uma simulação simples — na versão completa do EduFin, a inteligência artificial faz previsões  
sobre o futuro da sua vida financeira, mostrando o que pode acontecer se você continuar com o mesmo padrão.
""")

# ===============================
# Rodapé
# ===============================
st.markdown("---")
st.caption("© 2025 EduFin AI Cloud — Um projeto simples para ajudar pessoas a entenderem suas finanças 💡")

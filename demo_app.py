import streamlit as st
from PIL import Image

# =====================================
# ⚙️ CONFIGURAÇÃO
# =====================================
st.set_page_config(page_title="EduFin AI Cloud — Inteligência Financeira com IA", layout="wide")

# =====================================
# 🎨 ESTILO DRIBBBLE / PORTFÓLIO
# =====================================
st.markdown("""
<style>
body {
    background-color: #ffffff;
    font-family: 'Poppins', sans-serif;
    color: #222;
}
h1, h2, h3, h4 {
    font-weight: 600;
}
img {
    border-radius: 10px;
}
.section {
    padding: 3rem 0;
    border-bottom: 1px solid #eee;
}
.section h2 {
    color: #222;
}
.section p {
    font-size: 1.1rem;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# =====================================
# 🧭 CABEÇALHO
# =====================================
st.title("💡 EduFin AI Cloud — Inteligência Financeira com IA")
st.write("Aplicativo educativo que ajuda pessoas a entenderem sua **vida financeira** com apoio de **Inteligência Artificial**.")

# Carrega sua imagem principal
image = Image.open("edufin-cloud-v2-kzfj7wlptvvrnqoxcwmmrt.streamlit.app_.png")
st.image(image, use_column_width=True)

# =====================================
# 🧩 SEÇÃO 1 — VISÃO GERAL
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("📘 Visão Geral")
st.write("""
O **EduFin AI Cloud** é uma ferramenta simples e visual para que qualquer pessoa consiga **entender sua situação financeira**.  
Por meio de uma interface amigável e de uma inteligência artificial básica, o app mostra se a sua **saúde financeira** está boa, regular ou precisa de atenção.
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 🧮 SEÇÃO 2 — FUNÇÃO
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("⚙️ Função Principal")
st.write("""
A função principal é **simular a sua vida financeira** com base em poucos dados:  
renda, gastos, dívidas, poupança e investimentos.  
Com esses valores, o sistema calcula automaticamente um **índice financeiro** e exibe um resultado colorido fácil de entender.
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 🎨 SEÇÃO 3 — DESIGN E PROCESSO
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🎨 Processo de Design")
st.write("""
O design foi inspirado em interfaces modernas tipo **Dribbble**, com foco em clareza e aprendizado.  
O objetivo é fazer o usuário se sentir confortável — mesmo sem conhecimento técnico — e conseguir enxergar **como pequenas mudanças**  
no orçamento afetam sua estabilidade financeira.
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 🧠 SEÇÃO 4 — TELAS DE ALTA FIDELIDADE
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("📱 Telas de Alta Fidelidade")
st.write("Interface limpa, interativa e responsiva. O usuário move os controles e o resultado muda em tempo real.")

st.image(image, caption="Tela de simulação — EduFin AI Cloud", use_column_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 📘 SEÇÃO 5 — CONCLUSÕES
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("📈 Principais Conclusões")
st.write("""
- Aplicações de IA podem ser **acessíveis e educativas**.  
- Interfaces simples geram **confiança e engajamento**.  
- A visualização de resultados ajuda na **mudança de comportamento financeiro**.  
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 🙌 RODAPÉ
# =====================================
st.markdown("""
---
### 🙏 Obrigado por acompanhar!
Entre em contato: **claudio.y@hotmail.com**
""")

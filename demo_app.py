import streamlit as st
from PIL import Image

# =====================================
# ⚙️ CONFIGURAÇÃO GERAL
# =====================================
st.set_page_config(
    page_title="EduFin AI Cloud — Educação Financeira com IA",
    layout="wide"
)

# =====================================
# 🎨 ESTILO DRIBBBLE / MODERNO
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
# 🧭 CABEÇALHO PRINCIPAL
# =====================================
st.title("💡 EduFin AI Cloud — Inteligência Financeira com IA")
st.write("Aplicativo educativo que ajuda pessoas a **entender e melhorar sua vida financeira**, com apoio de **Inteligência Artificial** e uma interface simples.")

# Imagem principal — direto do repositório GitHub
st.image(
    "https://raw.githubusercontent.com/Claudio577/demostracao/main/edufin-cloud-v2-kzfj7wlptvvrnqoxcwmmrt.streamlit.app_.png",
    caption="Tela principal do EduFin AI Cloud",
    use_column_width=True
)

# =====================================
# 🧩 SEÇÃO 1 — VISÃO GERAL
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("📘 Visão Geral")
st.write("""
O **EduFin AI Cloud** é uma ferramenta desenvolvida para **ensinar conceitos de educação financeira de forma prática e interativa**.  
Com poucos dados, o usuário consegue visualizar **sua situação financeira atual** e entender o que pode fazer para melhorá-la.
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 🧮 SEÇÃO 2 — COMO FUNCIONA
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("⚙️ Como Funciona")
st.write("""
1. O usuário insere informações básicas: **renda, gastos, dívidas e investimentos**.  
2. A IA faz um cálculo simples e gera um **índice de saúde financeira**.  
3. O resultado é exibido em **cores e mensagens claras**, mostrando se a situação está boa, regular ou preocupante.  

Tudo isso acontece em tempo real, com uma linguagem acessível — perfeita para quem está **começando a aprender sobre finanças pessoais**.
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 🎨 SEÇÃO 3 — DESIGN EDUCACIONAL
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🎨 Design Educacional")
st.write("""
O layout do EduFin foi pensado para **facilitar o aprendizado visual**.  
Cores, ícones e sliders interativos tornam o processo de entendimento **leve, intuitivo e motivador** — ideal para cursos, oficinas e programas de capacitação financeira.
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 🧠 SEÇÃO 4 — SIMULAÇÃO INTERATIVA
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("📱 Simulação Interativa")
st.write("""
A interface permite que o usuário **simule diferentes cenários financeiros**:
- O que acontece se eu gastar menos?  
- E se eu guardar mais todo mês?  
- Como as dívidas afetam meu equilíbrio financeiro?

Essas simulações mostram de forma prática o **impacto das decisões diárias** sobre a saúde financeira.
""")

st.image(
    "https://raw.githubusercontent.com/Claudio577/demostracao/main/edufin-cloud-v2-kzfj7wlptvvrnqoxcwmmrt.streamlit.app_.png",
    caption="Simulação interativa — EduFin AI Cloud",
    use_column_width=True
)
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 📘 SEÇÃO 5 — OBJETIVO EDUCACIONAL
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🎯 Objetivo Educacional")
st.write("""
O EduFin AI Cloud foi criado com o propósito de **democratizar o acesso à educação financeira**.  
Ele ajuda o usuário a compreender conceitos como:
- Equilíbrio entre ganhos e gastos  
- Importância de poupar  
- Efeitos das dívidas  
- Planejamento para o futuro  

Ideal para **escolas, cursos e projetos sociais**, onde o foco é **aprender fazendo**.
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 📈 SEÇÃO 6 — CONCLUSÕES
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("📈 Conclusões e Próximos Passos")
st.write("""
O **EduFin AI Cloud** prova que é possível usar tecnologia para **tornar a educação financeira acessível e divertida**.  
Próximos passos incluem:
- Expansão do cálculo de IA com mais variáveis financeiras,  
- Geração automática de **recomendações personalizadas**,  
- E integração com **painéis de acompanhamento** para professores e mentores.  
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 🙌 RODAPÉ
# =====================================
st.markdown("""
---
### 🙏 Obrigado por acompanhar!
💬 Entre em contato: **claudio.y@hotmail.com**  
© 2025 EduFin AI Cloud — Educação Financeira para Todos 💰
""")


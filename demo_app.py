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

# Imagem principal: tela de login
st.image(
    "https://raw.githubusercontent.com/Claudio577/demostracao/main/login.png",
    caption="Tela de Login — EduFin AI Cloud",
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
1. O usuário insere informações básicas: **renda, gastos, dívidas, poupança e investimentos**.  
2. A IA calcula um **índice de saúde financeira**.  
3. O resultado é exibido com **cores e mensagens claras**, mostrando se a situação está boa, regular ou preocupante.  

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
Cores, ícones e controles interativos tornam o processo de aprendizado **leve, intuitivo e motivador** — ideal para cursos, oficinas e projetos de capacitação financeira.
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 🧠 SEÇÃO 4 — SIMULAÇÃO INTERATIVA (CÁLCULO)
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("📱 Simulação Interativa")
st.write("""
A interface principal permite que o usuário **simule diferentes cenários financeiros**:
- O que acontece se eu gastar menos?  
- E se eu guardar mais todo mês?  
- Como as dívidas afetam meu equilíbrio financeiro?

Essas simulações mostram de forma prática o **impacto das decisões diárias** sobre a saúde financeira.
""")

# Imagem completa do app com o cálculo
st.image(
    "https://raw.githubusercontent.com/Claudio577/demostracao/main/calculo.png",
    caption="Tela completa de simulação — EduFin AI Cloud",
    use_column_width=True
)
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 📘 SEÇÃO 5 — OBJETIVO EDUCACIONAL
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🎯 Objetivo Educacional")
st.write("""
O EduFin AI Cloud foi criado para **democratizar o acesso à educação financeira**.  
Ele ajuda o usuário a compreender conceitos como:
- Equilíbrio entre ganhos e gastos  
- Importância de poupar  
- Efeitos das dívidas  
- Planejamento financeiro  

Ideal para **escolas, cursos e projetos sociais**, com foco em **aprender fazendo**.
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 📈 SEÇÃO 6 — CONCLUSÕES
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("📈 Conclusões e Próximos Passos")
st.write("""
O **EduFin AI Cloud** mostra como a tecnologia pode tornar a **educação financeira acessível e divertida**.  
Próximos passos incluem:
- Expansão do modelo de IA com novas variáveis,  
- Geração de **recomendações personalizadas**,  
- Integração com **painéis de acompanhamento** para professores e mentores.  
""")
st.markdown("</div>", unsafe_allow_html=True)


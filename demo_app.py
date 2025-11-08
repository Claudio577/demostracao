import streamlit as st
from PIL import Image, ImageChops

# =====================================
# ⚙️ CONFIGURAÇÃO GERAL
# =====================================
st.set_page_config(
    page_title="EduFin AI Cloud — Educação Financeira com IA",
    layout="wide"
)

# =====================================
# 🧩 FUNÇÃO AUXILIAR — CORTAR BORDAS BRANCAS
# =====================================
def crop_white_borders(img_path):
    """Remove bordas brancas automaticamente."""
    img = Image.open(img_path)
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        img = img.crop(bbox)
    return img

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

st.write("""
O **EduFin AI Cloud** é um aplicativo educativo que une **educação financeira** e **inteligência artificial (IA)**.  
Ele foi criado para ajudar pessoas a **entenderem sua situação financeira** e **aprenderem a tomar melhores decisões com base em dados**.

As habilidades de **Machine Learning (ML)** usadas aqui podem ser aplicadas hoje em diversas áreas, como:
- **Finanças pessoais e bancárias**, para prever gastos e detectar comportamentos de risco.  
- **Educação**, para personalizar o aprendizado e gerar recomendações inteligentes.  
- **Empresas e startups**, que usam IA para melhorar tomadas de decisão, identificar oportunidades e otimizar processos.  

Com o EduFin, o objetivo é trazer esses conceitos para o **contexto do dia a dia**, de um jeito visual e fácil de entender.
""")

# =====================================
# 🖼️ IMAGEM DE LOGIN (cortada e ajustada)
# =====================================
login_img = crop_white_borders("login.png")
st.image(login_img, caption="Tela de Login — EduFin AI Cloud", width=550)

# =====================================
# 🧩 SEÇÃO 1 — VISÃO GERAL
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("📘 Visão Geral")
st.write("""
O **EduFin AI Cloud** foi criado para **ensinar conceitos de educação financeira** de maneira simples, prática e interativa.  
A ferramenta utiliza lógica de IA para transformar dados básicos — renda, gastos e dívidas — em **informações úteis sobre o equilíbrio financeiro** do usuário.
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 🧮 SEÇÃO 2 — COMO FUNCIONA
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("⚙️ Como Funciona")
st.write("""
1. O usuário insere suas informações: **renda, gastos, dívidas, poupança e investimentos**.  
2. O sistema calcula automaticamente um **índice de saúde financeira**.  
3. O resultado é exibido com **cores e mensagens claras**, mostrando se a situação está boa, regular ou preocupante.  

O processo é instantâneo e ideal para quem está **começando a aprender sobre finanças pessoais**.
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 🎨 SEÇÃO 3 — DESIGN EDUCACIONAL
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🎨 Design Educacional")
st.write("""
O layout do EduFin foi pensado para **facilitar o aprendizado visual**.  
Cores, ícones e controles deslizantes tornam o uso **intuitivo e leve**, estimulando o usuário a **explorar cenários financeiros** e aprender com eles.
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

# Imagem do cálculo principal (ajustada e cortada)
calc_img = crop_white_borders("calculo.png")
st.image(calc_img, caption="Tela de Simulação — EduFin AI Cloud", width=700)
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 📘 SEÇÃO 5 — OBJETIVO EDUCACIONAL
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🎯 Objetivo Educacional")
st.write("""
O EduFin AI Cloud foi desenvolvido com o propósito de **democratizar o acesso à educação financeira**.  
Ele ajuda o usuário a entender conceitos essenciais, como:
- **Equilíbrio entre ganhos e gastos**  
- **Importância de poupar e investir**  
- **Efeitos das dívidas**  
- **Planejamento financeiro e metas de longo prazo**  

Ideal para **escolas, cursos e projetos sociais**, onde o aprendizado é feito de forma **visual e interativa**.
""")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# 📈 SEÇÃO 6 — CONCLUSÕES
# =====================================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("📈 Conclusões e Próximos Passos")
st.write("""
O **EduFin AI Cloud** mostra como a tecnologia pode **tornar a educação financeira acessível, personalizada e divertida**.  
Próximos passos incluem:
- Expansão do modelo de IA com novas variáveis,  
- Geração de **recomendações personalizadas**,  
- Integração com **painéis de acompanhamento** para professores e mentores.  
""")
st.markdown("</div>", unsafe_allow_html=True)


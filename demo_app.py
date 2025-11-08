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
    """Remove automaticamente bordas brancas ou vazias."""
    img = Image.open(img_path)
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        img = img.crop(bbox)
    return img

# =====================================
# CABEÇALHO PRINCIPAL
# =====================================
st.title("EduFin AI Cloud — Inteligência Financeira com IA")

st.write("""
O **EduFin AI Cloud** é um aplicativo educativo que une **educação financeira** e **inteligência artificial (IA)**.  
Ele foi criado para ajudar pessoas a **entenderem sua situação financeira** e **aprenderem a tomar melhores decisões com base em dados**.

As habilidades de **Machine Learning (ML)** utilizadas aqui podem ser aplicadas hoje em diversas áreas:
- **Finanças pessoais e bancárias**, para prever gastos, detectar padrões de consumo e identificar riscos.  
- **Educação**, em sistemas que personalizam o aprendizado e sugerem trilhas de conhecimento.  
- **Empresas e startups**, na tomada de decisões, análise de dados e automação inteligente de processos.  

Com o EduFin, o objetivo é trazer esses conceitos para o **cotidiano de forma simples, visual e interativa**.
""")

# =====================================
# IMAGEM DE LOGIN (loguinnova.png)
# =====================================
login_img = crop_white_borders("loguinnova.png")

# Redimensiona proporcionalmente
base_width = 600
w_percent = base_width / float(login_img.size[0])
h_size = int(float(login_img.size[1]) * w_percent)
login_img = login_img.resize((base_width, h_size), Image.Resampling.LANCZOS)

st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
st.image(login_img, caption="Tela de Login — EduFin AI Cloud", use_column_width=False)
st.caption("Interface de autenticação aprimorada — simples, acessível e moderna.")
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# SEÇÃO 1 — VISÃO GERAL
# =====================================
st.header("Visão Geral")
st.write("""
O **EduFin AI Cloud** foi desenvolvido para **ensinar conceitos de educação financeira** de forma prática e intuitiva.  
Com ele, qualquer pessoa pode compreender rapidamente **como está sua saúde financeira** e **como melhorar suas finanças pessoais**.
""")

# =====================================
# SEÇÃO 2 — COMO FUNCIONA
# =====================================
st.header("Como Funciona")
st.write("""
1. O usuário informa dados simples: **renda, gastos, dívidas, poupança e investimentos**.  
2. O sistema calcula um **índice de saúde financeira** com base nesses valores.  
3. O resultado aparece em **cores e mensagens fáceis de entender**, mostrando se a situação está boa, regular ou preocupante.  

Essa abordagem torna o aprendizado **interativo e acessível** — ideal para quem está começando no tema finanças pessoais.
""")

# =====================================
# SEÇÃO 3 — DESIGN EDUCACIONAL
# =====================================
st.header("Design Educacional")
st.write("""
O layout foi projetado para **facilitar o aprendizado visual**.  
Cores, ícones e controles deslizantes tornam o uso **leve e intuitivo**, incentivando o usuário a testar diferentes cenários financeiros e **aprender com o resultado**.
""")

# =====================================
# SEÇÃO 4 — SIMULAÇÃO INTERATIVA (CÁLCULO)
# =====================================
st.header("Simulação Interativa")
st.write("""
A principal tela do EduFin permite **simular situações reais**:
- E se eu gastar menos?  
- E se eu guardar mais por mês?  
- Como minhas dívidas impactam meu equilíbrio financeiro?

Essas simulações ajudam o usuário a entender de forma prática o **impacto de suas decisões no futuro financeiro**.
""")

calc_img = crop_white_borders("calculo.png")

base_width = 700
w_percent = base_width / float(calc_img.size[0])
h_size = int(float(calc_img.size[1]) * w_percent)
calc_img = calc_img.resize((base_width, h_size), Image.Resampling.LANCZOS)

st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
st.image(calc_img, caption="Tela de Simulação — EduFin AI Cloud", use_column_width=False)
st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# SEÇÃO 5 — OBJETIVO EDUCACIONAL
# =====================================
st.header("Objetivo Educacional")
st.write("""
O EduFin AI Cloud busca **democratizar o acesso à educação financeira**.  
Ele ajuda o usuário a entender conceitos como:
- **Equilíbrio entre ganhos e gastos**  
- **Importância de poupar e investir**  
- **Efeitos das dívidas**  
- **Planejamento financeiro pessoal**  

É ideal para **escolas, universidades e projetos sociais**, onde o aprendizado acontece de forma **visual e participativa**.
""")

# =====================================
# SEÇÃO 6 — CONCLUSÕES
# =====================================
st.header("Conclusões e Próximos Passos")
st.write("""
O **EduFin AI Cloud** mostra como a tecnologia pode **tornar a educação financeira acessível e prática**.  
Próximos passos incluem:
- Expansão do modelo de IA com mais variáveis financeiras;  
- Geração de **recomendações personalizadas** para o usuário;  
- Integração com **painéis para educadores e mentores**.  
""")

# =====================================
# RODAPÉ
# =====================================
st.markdown("""
---
**Obrigado por acompanhar!**  
Contato: **claudio.y@hotmail.com**  
© 2025 EduFin AI Cloud — Educação Financeira para Todos
""")

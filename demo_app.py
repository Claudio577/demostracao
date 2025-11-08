import streamlit as st
from PIL import Image, ImageChops

# =====================================
# ⚙️ CONFIGURAÇÃO GERAL
# =====================================
# Mantido: Já utiliza layout="wide", que é dinâmico.
st.set_page_config(
    page_title="EduFin AI Cloud — Educação Financeira com IA",
    layout="wide",
    page_icon="💡" # Adiciona um ícone na aba do navegador
)

# =====================================
# 🧩 FUNÇÃO AUXILIAR — CORTAR BORDAS BRANCAS
# =====================================
def crop_white_borders(img_path):
    """Remove automaticamente bordas brancas ou vazias."""
    try:
        img = Image.open(img_path)
        # Otimização: A cor de fundo pode ser a média dos pixels de canto para melhor detecção,
        # mas mantive o (0, 0) para simplicidade e consistência.
        bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
        diff = ImageChops.difference(img, bg)
        bbox = diff.getbbox()
        if bbox:
            img = img.crop(bbox)
        return img
    except FileNotFoundError:
        st.error(f"Erro: Imagem não encontrada em {img_path}. Certifique-se de que o arquivo existe.")
        return None # Retorna None se a imagem não for encontrada

# =====================================
# 🧭 CABEÇALHO PRINCIPAL E INTRODUÇÃO
# =====================================
st.title("💡 EduFin AI Cloud — Inteligência Financeira com IA")

st.markdown("""
O **EduFin AI Cloud** é um aplicativo educativo que une **educação financeira** e **inteligência artificial (IA)**.  
Ele foi criado para ajudar pessoas a **entenderem sua situação financeira** e **aprenderem a tomar melhores decisões com base em dados**.
""")

# Uso de st.expander para organizar a lista de habilidades de ML, tornando a introdução mais limpa.
with st.expander("🚀 Habilidades de Machine Learning (ML) utilizadas e suas aplicações"):
    st.write("""
    As habilidades de **Machine Learning (ML)** utilizadas aqui podem ser aplicadas hoje em diversas áreas:
    - **Finanças pessoais e bancárias**, para prever gastos, detectar padrões de consumo e identificar riscos.  
    - **Educação**, em sistemas que personalizam o aprendizado e sugerem trilhas de conhecimento.  
    - **Empresas e startups**, na tomada de decisões, análise de dados e automação inteligente de processos.  

    Com o EduFin, o objetivo é trazer esses conceitos para o **cotidiano de forma simples, visual e interativa**.
    """)

# ---
# =====================================
# 🖼️ IMAGEM DE LOGIN (loguinnova.png) — Uso de colunas para centralizar
# =====================================
login_img = crop_white_borders("loguinnova.png")

if login_img:
    # Redimensiona proporcionalmente
    base_width = 600
    w_percent = base_width / float(login_img.size[0])
    h_size = int(float(login_img.size[1]) * w_percent)
    login_img = login_img.resize((base_width, h_size), Image.Resampling.LANCZOS)

    # Usa st.columns para centralizar a imagem: (Coluna Vazia), (Coluna da Imagem), (Coluna Vazia)
    # A proporção [1, 3, 1] ou [1, 2, 1] é comum para centralização no layout wide.
    col1_login, col2_login, col3_login = st.columns([1, 2, 1])

    with col2_login: # Coloca o conteúdo na coluna central
        st.image(login_img, caption="Tela de Login — EduFin AI Cloud", use_column_width='always') # 'always' para usar o espaço da coluna
        st.caption("Interface de autenticação aprimorada — simples, acessível e moderna.")

st.divider() # Separador visual

# =====================================
# 🧩 SEÇÕES 1, 2 E 3 — ORGANIZAÇÃO EM COLUNAS PARA VISÃO GERAL
# =====================================
st.header("📘 Visão Geral e Conceitos Chave")

# Organiza os 3 tópicos iniciais em 3 colunas para um layout dinâmico horizontal
col_visao, col_funciona, col_design = st.columns(3)

with col_visao:
    st.subheader("1. Visão Geral")
    st.markdown("""
    O **EduFin AI Cloud** foi desenvolvido para **ensinar conceitos de educação financeira** de forma prática e intuitiva.  
    Com ele, qualquer pessoa pode compreender rapidamente **como está sua saúde financeira** e **como melhorar suas finanças pessoais**.
    """)

with col_funciona:
    st.subheader("2. Como Funciona")
    st.markdown("""
    1. O usuário informa dados simples: **renda, gastos, dívidas, poupança e investimentos**.  
    2. O sistema calcula um **índice de saúde financeira** com base nesses valores.  
    3. O resultado aparece em **cores e mensagens fáceis de entender**.
    """)

with col_design:
    st.subheader("3. Design Educacional")
    st.markdown("""
    O layout foi projetado para **facilitar o aprendizado visual**.  
    Cores, ícones e controles deslizantes tornam o uso **leve e divertido**, incentivando o usuário a testar diferentes cenários financeiros.
    """)

st.divider()

# =====================================
# 🧠 SEÇÃO 4 — SIMULAÇÃO INTERATIVA (CÁLCULO)
# =====================================
st.header("📱 Simulação Interativa e Impacto de Decisão")

# Uso de colunas para apresentar texto e imagem lado a lado
col_texto_calc, col_img_calc = st.columns([2, 3])

with col_texto_calc:
    st.write("""
    A principal tela do EduFin permite **simular situações reais** com base em Machine Learning e finanças:
    - E se eu gastar menos?  
    - E se eu guardar mais por mês?  
    - Como minhas dívidas impactam meu equilíbrio financeiro?

    Essas simulações ajudam o usuário a entender de forma prática o **impacto de suas decisões no futuro financeiro**, reforçando o **aprendizado visual e participativo**.
    """)

calc_img = crop_white_borders("calculo.png")

with col_img_calc:
    if calc_img:
        base_width = 700
        w_percent = base_width / float(calc_img.size[0])
        h_size = int(float(calc_img.size[1]) * w_percent)
        calc_img = calc_img.resize((base_width, h_size), Image.Resampling.LANCZOS)
        
        # A imagem já está centrada na coluna
        st.image(calc_img, caption="Tela de Simulação — EduFin AI Cloud", use_column_width=True)

st.divider()

# =====================================
# 📘 SEÇÃO 5 E 6 — OBJETIVO E CONCLUSÕES
# =====================================
col_objetivo, col_conclusoes = st.columns(2)

with col_objetivo:
    st.header("🎯 Objetivo Educacional")
    st.write("""
    O EduFin AI Cloud busca **democratizar o acesso à educação financeira**. Ele ajuda o usuário a entender conceitos como:
    - **Equilíbrio entre ganhos e gastos** - **Importância de poupar e investir** - **Efeitos das dívidas** - **Planejamento financeiro pessoal** É ideal para **escolas, universidades e projetos sociais**, onde o aprendizado acontece de forma **visual e participativa**.
    """)

with col_conclusoes:
    st.header("📈 Conclusões e Próximos Passos")
    st.write("""
    O **EduFin AI Cloud** demonstra como a tecnologia pode **tornar a educação financeira acessível e prática**.  
    Próximos passos planejados incluem:
    - Expansão do modelo de IA com mais variáveis financeiras.  
    - Geração de **recomendações personalizadas** para o usuário.  
    - Integração com **painéis para educadores e mentores**.  
    """)


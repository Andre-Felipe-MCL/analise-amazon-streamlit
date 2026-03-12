#Importações 
import streamlit as st
import pandas as pd

#Configuração da página
st.set_page_config(page_title="Análise de Dados de Vendas da Amazon", page_icon=":bar_chart:", layout="wide")

#Titulo
st.title("Análise de Dados de vendas da Amazon 📊")
st.header("Poder dos dados na tomada de decisão")
#Falando um pouco do objetivo
st.write("O objetivo desta análise é explorar os dados e indentificar padrões que possam apoiar Tomadas de decisões estrátegicas")

#Carregando os dados arquivo csv
@st.cache_data
def carregar_dados():
    try:
        df = pd.read_csv("amazon.csv")
        
        #Limpeza e transformação dos dados
        df['category'] = df['category'].str.split('|').str[-1]
        df['product_name'] = df['product_name'].str.slice(0, 50) #-Limitar o nome do produto a 50 caracteres para melhor visualização
        df['discounted_price'] = df['discounted_price'].astype(str).str.replace('₹', '').str.replace(',', '')  #  Remove o símbolo ₹ e vírgulas para o Pandas entender como número
        df['discounted_price'] = pd.to_numeric(df['discounted_price'], errors='coerce')# converte para float
        df['rating'] = pd.to_numeric(df['rating'].astype(str).str.replace('|', ''), errors='coerce')# Limpa a coluna de avaliação, removendo caracteres indesejados e convertendo para numérico
        
        
        return df
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None
dados = carregar_dados()
st.dataframe(
    dados,
    column_config={
        "product_name": "Nome do Produto",
        "category": "Categoria",
        "discounted_price": "Preço com Desconto",
        "actual_price": "Preço",
        "discount_percentage": "Porcentagem de Desconto",
        "rating": "Avaliação",
        "rating_count": "Número de Avaliações",
        "about_product": "Sobre o Produto",
        "user_name": "Nome do Usuário",
        "review_title": "Título da Avaliação",
        "review_content": "Conteúdo da Avaliação"
        
        
    }
             )



#Mostrar Algumas informações basicas 
def info_basica(dados):
    coluna = st.columns(3)
    
    with coluna[0]:
        # Localiza a linha do maior preço
        idx_max = dados['discounted_price'].idxmax()
        nome_caro = dados.loc[idx_max, 'product_name']
        preco_max = dados.loc[idx_max, 'discounted_price']
        
        st.metric(label="🔺 Mais Caro (Líquido)", value=f"₹ {preco_max:,.2f}")
        st.caption(f"{nome_caro[:50]}...")

    with coluna[1]:
        # Localiza a linha do menor preço
        idx_min = dados['discounted_price'].idxmin()
        nome_barato = dados.loc[idx_min, 'product_name']
        preco_min = dados.loc[idx_min, 'discounted_price']
        
        st.metric(label="🔹 Mais Barato (Líquido)", value=f"₹ {preco_min:,.2f}")
        st.caption(f"{nome_barato[:50]}...")
    with coluna[2]:
        st.subheader("Categoria melhor avaliada")
        
        dados['rating'] = pd.to_numeric(dados['rating'], errors='coerce')
        
        df_limpo = dados.dropna(subset=['rating'])
        
        medias_categorias = df_limpo.groupby('category')['rating'].mean()
        
        categoria_top = medias_categorias.idxmax()
        nota_top = medias_categorias.max()

        nome_exibicao = categoria_top.split('|')[-1]
        
        st.metric(label=f"⭐ {nome_exibicao}", value=f"A nota foi: {nota_top:.1f} de 5")
        st.caption("Categoria com a melhor avaliação média")
info_basica(dados)

def prova_social():
    dados['rating'] = pd.to_numeric(dados['rating'], errors='coerce')
    dados['rating_count'] = pd.to_numeric(dados['rating_count'].astype(str).str.replace(',', ''), errors='coerce')
    prova_social = dados.groupby('product_name')['rating_count'].sum().sort_values(ascending=False).head(50)
    st.subheader("Top 50 Produtos por Número de Avaliações")
    st.line_chart(prova_social)
    
def ancoragem_preco():
    dados['discount_percentage'] = pd.to_numeric(dados['discount_percentage'].str.replace('%', ''), errors='coerce')
    ancoragem = dados.groupby('product_name')['discount_percentage'].mean().sort_values(ascending=False).head(25)
    st.subheader("Top 25 Produtos por Porcentagem de Desconto")
    st.bar_chart(ancoragem)
    
st.markdown("---") 
st.header("A Gigante Ocidental: Amazon e seu motivo de sucesso")
st.write("A Amazon ocupa o terceiro lugar mundial em GMV, mas é a líder absoluta em termos de receita própria e infraestrutura logística global. Ela domina mercados como EUA, Europa e tem crescido agressivamente em outras regiões.")
st.subheader("O que faz a Amazon ser tão bem sucedida?")
st.markdown(""" **O Efeito "Prova Social"**

- A Descoberta: Produtos com mais de 100.000 avaliações dominam o topo das buscas, independentemente de terem nota 4.0 ou 4.5.

- Insight: Na Amazon, o consumidor confia mais em um produto com muitas avaliações médias do que em um produto com poucas avaliações perfeitas. O volume de feedback valida a popularidade e reduz o medo do comprador.""")

prova_social()

st.markdown(""" **A Estratégia de "Ancoragem de Preço"**
- A Descoberta: Quase todos os produtos listados apresentam um desconto superior a 30%. Muitos chegam a 60% ou 70% (como o primeiro item do seu CSV, o cabo Wayona).

- Insight: O que impulsiona a venda não é o "preço baixo" por si só, mas a percepção de oportunidade. O consumidor sente que está "ganhando" ao comprar um item de ₹1,099 por ₹399. A Amazon favorece produtos que oferecem essa sensação de economia imediata.""")

ancoragem_preco()

st.markdown("---") 

#Entendimento do Probelema 
def perguntas_problema():
    st.subheader("Algumas perguntas Frequentes 🪢")

    coluna = st.columns(3)

    #Qual categoria é mais barata?
    with coluna[0]:
        st.header("Quais Categorias são mais baratas?")
        if st.button("Clique aqui 💰"):
            categorias_mais_baratas = dados.groupby('category')['discounted_price'].mean().sort_values(ascending=True)
            st.line_chart(categorias_mais_baratas)
            st.write("As categorias mais baratas são aquelas com menor preço médio com desconto. Analisando o gráfico, podemos identificar quais categorias oferecem os melhores preços para os consumidores.")
            st.write("No lado esquerdo (início): Estarão os pontos mais baixos, representando as categorias mais baratas (onde a média de preço dos produtos é pequena).")
            st.write("No lado direito (fim): A linha subirá até atingir os pontos mais altos, representando as categorias de luxo ou tecnologia pesada, que possuem as médias de preço mais elevadas.")
    
    #Existe relação entre o Preço e avaliação?
    with coluna[1]:
        st.header("Existe relação entre o Preço e avaliação?")
        if st.button("Clique aqui 📈"):
            relacao_preco_avaliacao = dados[['discounted_price', 'rating']].dropna()
            st.scatter_chart(relacao_preco_avaliacao.rename(columns={'discounted_price': 'Preço com Desconto', 'rating': 'Avaliação'}), x='Preço com Desconto', y='Avaliação')
            st.write("A relação entre preço e avaliação pode ser analisada através do gráfico de dispersão. Se houver uma tendência clara, como pontos mais altos (melhores avaliações) agrupados em torno de preços mais baixos, isso pode indicar que os consumidores tendem a avaliar melhor os produtos mais acessíveis. Por outro lado, se os pontos estiverem dispersos sem um padrão claro, isso pode sugerir que o preço não é um fator determinante para as avaliações dos consumidores.")
            st.write("De acordo com o grafico a satisfação do consumidor permanece alta e estável independentemente do valor do produto. Isso demonstra que a percepção de valor da Amazon é consistente em todos os segmentos. Para a gestão, isso valida uma estratégia focada em volume de vendas (produtos de baixo custo), pois eles mantêm a reputação da marca tão bem quanto os itens premium.")
    
    #Quais Produtos apresentam melhor peformace?
    with coluna[2]:
        st.header("Quais Produtos apresentam melhor peformace")
        if st.button("Clique aqui 🚀"):
            dados['rating_count'] = pd.to_numeric(dados['rating_count'].astype(str).str.replace(',', ''), errors='coerce')
            
            top_produtos = dados.sort_values(by='rating_count', ascending=False).head(7)[['product_name', 'rating_count', 'discounted_price', 'rating']]
            
            st.dataframe(
                top_produtos.rename(columns={
                    'product_name': 'Produto', 
                    'rating_count': 'Número de Avaliações', 
                    'discounted_price': 'Preço com Desconto', 
                    'rating': 'Avaliação Média'
                }),
                column_config={
                    "Preço com Desconto": st.column_config.NumberColumn(format="₹ %.2f"),
                    "Avaliação Média": st.column_config.NumberColumn(format="%.1f ⭐"),
                    "Número de Avaliações": st.column_config.NumberColumn(format="%d"),
                    "Produto": st.column_config.TextColumn()
                },
                hide_index=True # Remove a coluna de índices para ficar mais limpo
            )
            
            st.write("Os produtos com melhor performance são aqueles que possuem um alto número de avaliações, independente do preço. Isso indica que esses produtos são populares entre os consumidores, o que pode ser um indicativo de boa relação custo-benefício ou de uma forte reputação da marca. Para a gestão, focar em produtos com alta performance pode ser uma estratégia eficaz para aumentar as vendas e a satisfação do cliente, pois esses itens já demonstraram ser bem recebidos pelo mercado.")

perguntas_problema()

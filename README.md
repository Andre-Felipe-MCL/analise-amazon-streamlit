# 📊 Análise de Dados de Vendas da Amazon

Este projeto apresenta um **dashboard interativo de análise de dados** utilizando **Python, Pandas e Streamlit** para explorar padrões de vendas, avaliações e estratégias de preço dentro de um conjunto de dados de produtos da Amazon.

O objetivo principal é **transformar dados em insights estratégicos**, ajudando a entender comportamentos de consumo e fatores que influenciam o desempenho de produtos na plataforma.

---

# 🚀 Tecnologias Utilizadas

* Python
* Pandas
* Streamlit

Bibliotecas principais:

* pandas
* streamlit

---

# 📂 Estrutura do Projeto

```
analise-amazon-streamlit
│
├── App.py              # Aplicação principal do dashboard
├── amazon.csv          # Base de dados utilizada na análise
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
```

---

# 📈 Funcionalidades do Dashboard

O dashboard apresenta diferentes análises para entender o comportamento dos produtos e consumidores.

## 📊 Visualização dos Dados

* Tabela interativa com os dados da base
* Limpeza e transformação automática dos dados

## 📌 Métricas Principais

O sistema destaca informações importantes como:

* Produto mais caro
* Produto mais barato
* Categoria com melhor avaliação média

Essas métricas ajudam a identificar rapidamente **extremos de preço e qualidade percebida**.

---

# 🧠 Insights Estratégicos

## ⭐ Prova Social

O dashboard mostra os **50 produtos com maior número de avaliações**.

**Insight:**

Produtos com grande volume de avaliações tendem a dominar as buscas, pois transmitem maior confiança ao consumidor.

Mesmo com avaliações médias, o grande número de reviews cria **validação social**.

---

## 💰 Ancoragem de Preço

A análise de descontos mostra produtos com maiores porcentagens de redução de preço.

**Insight:**

Consumidores não respondem apenas ao preço baixo, mas sim à **percepção de oportunidade** criada pelo desconto.

Exemplo:

```
Preço original: ₹1,099
Preço com desconto: ₹399
```

Isso gera a sensação de vantagem na compra.

---

# ❓ Perguntas de Negócio Exploradas

O dashboard também permite explorar algumas perguntas importantes:

### 1️⃣ Quais categorias são mais baratas?

Análise da média de preços por categoria para identificar segmentos mais acessíveis.

### 2️⃣ Existe relação entre preço e avaliação?

Gráfico de dispersão entre:

* preço com desconto
* avaliação do produto

Isso ajuda a entender se **produtos mais caros são melhor avaliados**.

### 3️⃣ Quais produtos possuem melhor performance?

Ranking de produtos com maior número de avaliações, indicando popularidade e aceitação no mercado.

---

# 🧹 Tratamento de Dados

Durante o carregamento do dataset, algumas transformações são realizadas:

* Limpeza de símbolos de moeda
* Conversão de colunas para formato numérico
* Redução do tamanho de nomes de produtos
* Separação de categorias
* Tratamento de valores ausentes

Essas etapas garantem **análises mais precisas e consistentes**.

---

# ▶️ Como Executar o Projeto

1️⃣ Clone o repositório

```
git clone https://github.com/Andre-Felipe-MCL/analise-amazon-streamlit.git
```

2️⃣ Instale as dependências

```
pip install -r requirements.txt
```

3️⃣ Execute o dashboard

```
streamlit run App.py
```

O aplicativo abrirá automaticamente no navegador.

---

# 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

* prática de **análise de dados**
* construção de **dashboards interativos**
* geração de **insights estratégicos a partir de dados**

Também serve como **projeto de portfólio na área de análise de dados**.

---

# 👨‍💻 Autor

Projeto desenvolvido por **André Felipe**.

# Descrição Atividade 1
"""Para reforçar seus conhecimentos em redes neurais, sua tarefa é completar o código deste desafio associando corretamente cada tipo de rede de deep learning com sua definição.

Entrada
A entrada será o nome de um tipo de rede neural. Os seguintes termos são válidos para este desafio:

"convolutional neural network"
"recurrent neural network"
"transformer"
"autoencoder"
Saída
A saída será a descrição correspondente ao tipo de rede informado. As definições possíveis (em ordem aleatória) são:

"usa mecanismos de atenção para processar sequências de forma paralela"
"aprende a codificar e depois reconstruir os dados"
"possui conexões recorrentes para processar sequências"
"usa filtros para extrair padrões espaciais em imagens"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	                        Saída
convolutional neural network	usa filtros para extrair padrões espaciais em imagens
recurrent neural network	    possui conexões recorrentes para processar sequências
transformer	usa mecanismos de atenção para processar sequências de forma paralela
Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

Os desafios apresentados aqui têm como objetivo principal exercitar os conceitos aprendidos e proporcionar um primeiro contato com lógica de programação. Caso não tenha experiência em programação, utilize o template disponível e preencha com os conceitos aprendidos. Para resetar o template, basta clicar em “Restart Code”."""

# Atividade 1

# Dicionário que associa o tipo de rede neural à sua descrição
"""neural_networks = {
    "convolutional neural network": "usa filtros para extrair padrões espaciais em imagens",
    "recurrent neural network": "COMPLETE AQUI COM A DESCRIÇÃO",
    "transformer": "COMPLETE AQUI COM A DESCRIÇÃO",
    "autoencoder": "COMPLETE AQUI COM A DESCRIÇÃO"
}

# Leitura da entrada do usuário
user_input = input().strip()

# Impressão da descrição correspondente à rede informada
print(neural_networks.get(user_input))"""

# Resposta =

# Dicionário que associa o tipo de rede neural à sua descrição
neural_networks = {
    "convolutional neural network": "usa filtros para extrair padrões espaciais em imagens",
    "recurrent neural network": "possui conexões recorrentes para processar sequências",
    "transformer": "usa mecanismos de atenção para processar sequências de forma paralela",
    "autoencoder": "aprende a codificar e depois reconstruir os dados"
}

# Leitura da entrada do usuário
user_input = input().strip()

# Impressão da descrição correspondente à rede informada
print(neural_networks.get(user_input))


# Descrição Atividade 2

"""Neste desafio, você deverá relacionar corretamente cada aplicação prática de deep learning com sua descrição correspondente. 

Entrada
A entrada consistirá no nome de uma área de aplicação de deep learning. Os seguintes termos são válidos para este desafio:

"reconhecimento de fala"
"tradução automática"
"análise de sentimento"
"detecção de fraudes"
Saída
A saída deverá ser uma descrição precisa e compatível com a aplicação informada na entrada. Abaixo estão as descrições possíveis, listadas em ordem aleatória:

"identificação de padrões suspeitos em transações financeiras"
"conversão de fala em texto por meio de redes neurais"
"análise emocional de textos e comentários em redes sociais"
"conversão automática de frases entre diferentes idiomas"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
reconhecimento de fala	conversão de fala em texto por meio de redes neurais
tradução automática	conversão automática de frases entre diferentes idiomas
análise de sentimento	análise emocional de textos e comentários em redes sociais
Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

Os desafios apresentados aqui têm como objetivo principal exercitar os conceitos aprendidos e proporcionar um primeiro contato com lógica de programação. Caso não tenha experiência em programação, utilize o template disponível e preencha com os conceitos aprendidos. Para resetar o template, basta clicar em “Restart Code”."""

# Atividade 2

# Dicionário que associa áreas de aplicação a suas descrições
"""applications = {
    "reconhecimento de fala": "conversão de fala em texto por meio de redes neurais",
    "tradução automática": "COMPLETE AQUI COM A DESCRIÇÃO",
    "análise de sentimento": "COMPLETE AQUI COM A DESCRIÇÃO",
    "detecção de fraudes": "COMPLETE AQUI COM A DESCRIÇÃO"
}

# Leitura da entrada do usuário
user_input = input().strip()

# Impressão da descrição correspondente à aplicação informada
print(applications.get(user_input))"""

# Resposta 

# Dicionário que associa áreas de aplicação a suas descrições
applications = {
    "reconhecimento de fala": "conversão de fala em texto por meio de redes neurais",
    "tradução automática": "conversão automática de frases entre diferentes idiomas",
    "análise de sentimento": "análise emocional de textos e comentários em redes sociais",
    "detecção de fraudes": "identificação de padrões suspeitos em transações financeiras"
}

# Leitura da entrada do usuário
user_input = input().strip()

# Impressão da descrição correspondente à aplicação informada
print(applications.get(user_input))

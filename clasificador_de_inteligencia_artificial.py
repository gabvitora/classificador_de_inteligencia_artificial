#1. Solicita o nome do sistema de IA
nome_IA = (input('informe o nome da IA'))

#2. Recebe sua pontuação de performance (de 0 a 100)
pontuaçao = float(input('informe a pontuaçao obtida pela performace'))

#3. Exibe a classificação do nível de inteligência com base nessa pontuação

if 0 <= consumo_medio <= 39.9 :
    print(f'Informamos que {nome_IA}, é uma IA em Treinamento 🍼')

elif  40.0 <= consumo_medio <= 69.9 :
    print(f'Informamos que {nome_IA}, é uma IA Intermediária 🧠')

elif 70.0  <= consumo_medio <= 89.9 :
    print(f'Informamos que {nome_IA}, IA Otimizada 🚀')

elif 90.0 <= consumo_medio <= 100.0 :
    print(f'Informamos que {nome_IA}, é uma IA Avançada (nível Skynet) 🤯')

elif pontuaçao > 100 :
    print(f'Informamos que {nome_IA}, é uma Erro: IA fora da escala! ⚠️')

else:
    print(f'Informamos que {nome_IA}, é uma Erro: Pontuação inválida! ❌ ')




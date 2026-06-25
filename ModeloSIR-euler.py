import matplotlib.pyplot as plt

#Parâmetros iniciais definidos arbitrariamente

N = 10000       # Tamanho da população
S = 9830        # Número inicial de suscetiveis
I = 150         # Número inicial de infectados
R = 20          # Número inicial de recuperados
B = 0.3        # Taxa de transmissão
Y = 0.1         # Taxa de recuperação
R0 = 3          # Número de reprodução
h = 1           # Passo do método de euler (1 dia por iteração)

def Sn1(Sn, In): #Função que calcula Sn+1 pelo método de euler
    return Sn + h * (-B * (Sn * In) / N)

def In1(Sn, In): #Função que calcula In+1 pelo método de euler
    return In + h * (B * ((Sn * In) / N) - (Y * In))

def Rn1(In, Rn): #Função que calcula Rn+1 pelo método de euler
    return Rn + h * (Y * In)

def main():
    S_atual = S
    I_atual = I
    R_atual = R

    dias = []
    Slista = []
    Ilista = []
    Rlista = []

    #Define a quantidade de iterações (dias 1 à 90)
    for dia in range(1, 91):

        #Os valores de cada iteracação são armazenados para que seja possível fazer o gráfico
        dias.append(dia)
        Slista.append(S_atual)
        Ilista.append(I_atual)
        Rlista.append(R_atual)

        print(f"Dia {dia}: S={S_atual:.2f}, I={I_atual:.2f}, R={R_atual:.2f}")

        #Realiza a iteração para S,I e R
        novoS = Sn1(S_atual, I_atual)
        novoI = In1(S_atual, I_atual)
        novoR = Rn1(I_atual, R_atual)

        #Atualiza o (S,I,R) para utilizar na próxima iteração
        S_atual = novoS
        I_atual = novoI
        R_atual = novoR

    #Após computar as iterações, utiliza uma biblioteca para exibir o gráfico com base nos resultados obtidos
    plt.figure(figsize=(10, 6))
    plt.plot(dias, Slista, label='Suscetíveis (S)')
    plt.plot(dias, Ilista, label='Infectados (I)')
    plt.plot(dias, Rlista, label='Recuperados (R)')

    plt.title('Modelo SIR - Método de Euler')
    plt.xlabel('Dias')
    plt.ylabel('População')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()


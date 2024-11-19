# -*- coding: utf-8 -*-
"""M2- AOP2 - Introd a Programação de Computadores

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XOja0O-KVfN-N7OGdd6XCR6VWvUqsxat

<html>
  <body>
        <center>
          <img src="" alt="" style = width="100px"; height="100px">
          <p><b>Introdução à Programação de Computadores - Python</b></p>
          <p>Prof. Alessandro Bertolani Oliveira</p>
          <p><b>Tutor: </b> Edgar Salardani Senhorello</p>
          <b>AOP2 - Atividade On-Line Pontuada 2024-2</b>
        </center>
  </body>
</html>

Nome do Aluno:
"""

def ler_nota(mensagem, min_valor, max_valor):
    while True:
        try:
            nota = float(input(mensagem))
            if min_valor <= nota <= max_valor:
                return nota
            else:
                print(f"Nota inválida! Por favor, insira um valor entre {min_valor} e {max_valor}.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

def calcular_status(soma_modulo, media_modulo):
    if soma_modulo < 3:
        return "Reprovado Direto"
    elif soma_modulo < 7:
        return "Prova de Recuperação"
    elif media_modulo < 5.0:
        return "Reprovado após Prova de Recuperação"
    else:
        return "Aprovado"

def main():
    total_alunos = 5
    aprovados = 0
    reprovados = 0

    for i in range(total_alunos):
        print(f"\nAluno {i + 1}:")
        aop1 = ler_nota("Digite a nota da AOP1 (0-1): ", 0, 1)
        aop2 = ler_nota("Digite a nota da AOP2 (0-2): ", 0, 2)
        aop3 = ler_nota("Digite a nota da AOP3 (0-1): ", 0, 1)
        prova_regular = ler_nota("Digite a nota da Prova Regular (0-6): ", 0, 6)

        soma_modulo = aop1 + aop2 + aop3 + prova_regular
        media_modulo = soma_modulo / 2

        # Verifica se o aluno precisa fazer a prova de recuperação
        if soma_modulo < 7:
            prova_recuperacao = ler_nota("Digite a nota da Prova de Recuperação (0-10): ", 0, 10)
            media_modulo = (soma_modulo + prova_recuperacao) / 2

        status = calcular_status(soma_modulo, media_modulo)

        print(f"Soma do Módulo: {soma_modulo:.2f}")
        print(f"Média do Módulo: {media_modulo:.2f}")
        print(f"Status do Aluno: {status}")

        if status == "Aprovado":
            aprovados += 1
        else:
            reprovados += 1

    # Cálculo da porcentagem de alunos aprovados e reprovados
    porcentagem_aprovados = (aprovados / total_alunos) * 100
    porcentagem_reprovados = (reprovados / total_alunos) * 100

    print(f"\nPorcentagem de Alunos Aprovados: {porcentagem_aprovados:.2f}%")
    print(f"Porcentagem de Alunos Reprovados: {porcentagem_reprovados:.2f}%")

if __name__ == "__main__":
    main()
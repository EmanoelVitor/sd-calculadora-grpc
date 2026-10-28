# Cliente gRPC

import grpc

import calculadora_pb2
import calculadora_pb2_grpc

with grpc.insecure_channel("localhost:50051") as canal:
    cliente = calculadora_pb2_grpc.calculadoraStub(canal)

    print("=== CALCULADORA gRPC ===")

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    n3 = float(input("Digite o terceiro número: "))

    requisicao = calculadora_pb2.OperacaoRequest(
        numero1=n1,
        numero2=n2,
        numero3=n3
    )

    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = input("Opção: ").strip()

    operacoes = {
      "1": cliente.Somar,
      "2": cliente.Subtrair,
      "3": cliente.Multiplicar,
      "4": cliente.Dividir
    }


    resposta = operacoes[opcao](requisicao)

    print("Resultado:", resposta.resultado)

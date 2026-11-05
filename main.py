def calcular_media(nota1: float, nota2: float) -> float:
    """
    Calcula a média aritmética de duas notas.

    Args:
        nota1 (float): Primeira nota do aluno, de 0 a 10.
        nota2 (float): Segunda nota do aluno, de 0 a 10.

    Returns:
        float: A média das duas notas.
    """
    soma = nota1 + nota2
    media = soma / 2
    return media

def verificar_situacao(media: float) -> str:
    """
    Verifica a situação do aluno a partir da média.

    Args:
        media (float): Média final do aluno.

    Returns:
        str: "Aprovado" se a média for maior ou igual a 6.0,
             "Reprovado" caso contrário.
    """
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"

def obter_nome() -> str:
    """
    Solicita o nome do aluno e valida se não está vazio.

    Returns:
        str: Nome do aluno digitado pelo usuário.
    """
    nome_valido = False
    nome = ""
    while not nome_valido:
        try:
            nome = input("Digite o nome do aluno: ").strip()
            if nome == "":
                raise ValueError("O nome do aluno não pode ficar vazio.")
            nome_valido = True
        except ValueError as erro:
            print(f"Erro: {erro} Tente novamente.")
        except Exception:
            print("Erro inesperado. Tente novamente.")
    return nome

def obter_nota(numero_nota: int) -> float:
    """
    Solicita uma nota e valida se é um número entre 0 e 10.

    Args:
        numero_nota (int): Número da nota a ser solicitada, 1 ou 2.

    Returns:
        float: Nota validada entre 0 e 10.
    """
    nota_valida = False
    nota = 0.0
    while not nota_valida:
        try:
            entrada = input(f"Digite a nota {numero_nota} (0 a 10): ")
            nota = float(entrada)
            if nota < 0 or nota > 10:
                raise ValueError("A nota deve estar entre 0 e 10.")
            nota_valida = True
        except ValueError:
            print("Erro: Digite um número válido entre 0 e 10. Tente novamente.")
        except Exception:
            print("Erro inesperado. Digite um número válido.")
    return nota

def exibir_resultado(aluno: dict) -> str:
    """
    Formata o resultado final do aluno para exibição.

    Args:
        aluno (dict): Dicionário com nome, notas, média e situação.

    Returns:
        str: Texto formatado com o resultado.
    """
    texto = ""
    texto = texto + "\n--- Resultado ---\n"
    texto = texto + f"Aluno: {aluno['nome']}\n"
    texto = texto + f"Notas: {aluno['notas']}\n"
    texto = texto + f"Média: {aluno['media']:.2f}\n"
    texto = texto + f"Situação: {aluno['situacao']}\n"
    return texto

def main():
    """
    Função principal do programa.

    Solicita os dados do aluno, calcula a média,
    verifica a situação e armazena tudo em uma lista de registros.
    """
    registros: list[dict] = []

    print("=== Sistema de Notas ===")
    print("Cadastro de Aluno")
    print("----------------------")

    nome = obter_nome()
    nota1 = obter_nota(1)
    nota2 = obter_nota(2)

    media = calcular_media(nota1, nota2)
    situacao = verificar_situacao(media)

    aluno: dict = {
        "nome": nome,
        "notas": [nota1, nota2],
        "media": media,
        "situacao": situacao
    }

    registros.append(aluno)

    resultado = exibir_resultado(aluno)
    print(resultado)

    print("--- Todos os registros cadastrados ---")
    for registro in registros:
        print(registro)

    print("\nPrograma encerrado. Obrigado!")

if __name__ == "__main__":
    main()
def validar_cpf(cpf: str) -> bool:
    # Função para calcular o dígito verificador
    def calcular_digito(cpf_parcial: str, multiplicadores: list) -> int:
        soma = sum(int(digito) * multiplicador for digito, multiplicador in zip(cpf_parcial, multiplicadores))
        digito_verificador = 11 - (soma % 11)
        return 0 if digito_verificador >= 10 else digito_verificador

    # Multiplicadores para os cálculos dos dígitos verificadores
    multiplicadores_1 = list(range(10, 1, -1))
    multiplicadores_2 = list(range(11, 1, -1))

    # Calcular primeiro e segundo dígitos verificadores
    primeiro_digito = calcular_digito(cpf[:9], multiplicadores_1)
    segundo_digito = calcular_digito(cpf[:10], multiplicadores_2)

    # Verificar se os dígitos calculados correspondem aos dígitos fornecidos
    return cpf[9] == str(primeiro_digito) and cpf[10] == str(segundo_digito)

# Exemplo de uso
cpf = '03716477127'
if validar_cpf(cpf):
    print(f'O CPF {cpf} é verdadeiro.')
else:
    print(f'O CPF {cpf} não existe.')

import colorama
from colorama import Fore, Style

# Inicializa o colorama para garantir compatibilidade com diferentes terminais
colorama.init()

def exibir_alerta(nivel_indice, mensagem):
    """
    Função responsável por aplicar a cor correta baseada no nível do reservatório.
    O índice começa em 0 (Nível 1) até 4 (Nível 5).
    """
    cores = [
        Fore.RED,      # Nível 1: Crítico
        Fore.YELLOW,   # Nível 2: Baixo
        Fore.GREEN,    # Nível 3: Médio
        Fore.CYAN,     # Nível 4: Alto
        Fore.BLUE      # Nível 5: Muito Alto
    ]
    
    cor_selecionada = cores[nivel_indice]
    
    print(f"Status do Reservatório: {cor_selecionada}{mensagem}{Style.RESET_ALL}")

def simular_sistema():
    """
    Função principal que simula a leitura dos níveis do reservatório.
    """
    # Lista contendo as mensagens de situação conforme o nível (1 a 5)
    niveis_situacao = [
        "Nível 1: Muito baixo (crítico)",
        "Nível 2: Baixo",
        "Nível 3: Médio",
        "Nível 4: Alto",
        "Nível 5: Muito alto (alerta)"
    ]

    print("--- SISTEMA DE MONITORAMENTO DE RESERVATÓRIO ---")
    
    # Simulação de monitoramento percorrendo a lista
    for i in range(len(niveis_situacao)):
        exibir_alerta(i, niveis_situacao[i])

if __name__ == "__main__":
    simular_sistema()
    
    # Opcional: Garante que o terminal volte ao normal ao final da execução
    Style.RESET_ALL

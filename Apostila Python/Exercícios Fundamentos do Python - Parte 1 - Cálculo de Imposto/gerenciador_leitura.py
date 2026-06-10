import json
import os
from datetime import datetime

DATA_FILE = "leitura_data.json"
READING_TYPES = ["Livro", "Quadrinho", "Artigo", "Manga", "Relato", "Outro"]
STATUS_OPTIONS = ["Lendo", "Lido", "Pausado", "Pendente"]


def carregar_dados():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_dados(registros):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(registros, f, ensure_ascii=False, indent=2)


def menu():
    print("\n=== GERENCIADOR DE LEITURA ===")
    print("1. Adicionar novo item de leitura")
    print("2. Listar leituras")
    print("3. Atualizar item")
    print("4. Remover item")
    print("5. Filtrar por tipo ou status")
    print("6. Sair")
    return input("Escolha uma opção: ").strip()


def escolher_opcao(lista, titulo):
    print(f"\n{titulo}")
    for i, opcao in enumerate(lista, 1):
        print(f"{i}. {opcao}")
    escolha = input("Número: ").strip()
    if escolha.isdigit() and 1 <= int(escolha) <= len(lista):
        return lista[int(escolha) - 1]
    print("Opção inválida. Usando valor padrão.")
    return lista[0]


def pedir_inteiro(mensagem, valor_padrao=0):
    valor = input(f"{mensagem} ").strip()
    if valor.isdigit():
        return int(valor)
    return valor_padrao


def adicionar_leitura(registros):
    titulo = input("Título: ").strip()
    autor = input("Autor (opcional): ").strip()
    tipo = escolher_opcao(READING_TYPES, "Tipo de leitura:")
    total_paginas = pedir_inteiro("Total de páginas (numero):", 0)
    paginas_lidas = pedir_inteiro("Páginas lidas (numero):", 0)
    status = escolher_opcao(STATUS_OPTIONS, "Status:")
    registro = {
        "id": int(datetime.now().timestamp() * 1000),
        "titulo": titulo,
        "autor": autor,
        "tipo": tipo,
        "total_paginas": total_paginas,
        "paginas_lidas": paginas_lidas,
        "status": status,
        "data_adicionado": datetime.now().isoformat()
    }
    registros.append(registro)
    salvar_dados(registros)
    print("Item de leitura adicionado com sucesso!")


def listar_leituras(registros):
    if not registros:
        print("Nenhum registro encontrado.")
        return
    print("\n=== Lista de Leituras ===")
    for indice, registro in enumerate(registros, 1):
        progresso = f"{registro['paginas_lidas']}/{registro['total_paginas']}" if registro['total_paginas'] else f"{registro['paginas_lidas']} páginas"
        print(f"{indice}. [{registro['tipo']}] {registro['titulo']} (Autor: {registro['autor'] or 'N/A'})")
        print(f"   Status: {registro['status']} | Progresso: {progresso}")
        print(f"   Adicionado em: {registro['data_adicionado']}")


def escolher_item(registros):
    listar_leituras(registros)
    escolha = input("Digite o número do item: ").strip()
    if escolha.isdigit() and 1 <= int(escolha) <= len(registros):
        return int(escolha) - 1
    print("Item inválido.")
    return None


def atualizar_leitura(registros):
    if not registros:
        print("Nenhum registro para atualizar.")
        return
    indice = escolher_item(registros)
    if indice is None:
        return
    registro = registros[indice]
    print("Deixe em branco para manter o valor atual.")
    novo_titulo = input(f"Título [{registro['titulo']}]: ").strip() or registro['titulo']
    novo_autor = input(f"Autor [{registro['autor'] or 'N/A'}]: ").strip() or registro['autor']
    novo_tipo = escolher_opcao(READING_TYPES, "Tipo de leitura:")
    novo_total = input(f"Total de páginas [{registro['total_paginas']}]: ").strip()
    novo_paginas = input(f"Páginas lidas [{registro['paginas_lidas']}]: ").strip()
    novo_status = escolher_opcao(STATUS_OPTIONS, "Status:")

    registro['titulo'] = novo_titulo
    registro['autor'] = novo_autor
    registro['tipo'] = novo_tipo
    registro['total_paginas'] = int(novo_total) if novo_total.isdigit() else registro['total_paginas']
    registro['paginas_lidas'] = int(novo_paginas) if novo_paginas.isdigit() else registro['paginas_lidas']
    registro['status'] = novo_status
    salvar_dados(registros)
    print("Registro atualizado com sucesso!")


def remover_leitura(registros):
    if not registros:
        print("Nenhum registro para remover.")
        return
    indice = escolher_item(registros)
    if indice is None:
        return
    registro = registros.pop(indice)
    salvar_dados(registros)
    print(f"Registro '{registro['titulo']}' removido.")


def filtrar_leituras(registros):
    if not registros:
        print("Nenhum registro para filtrar.")
        return
    print("\n1. Filtrar por tipo")
    print("2. Filtrar por status")
    escolha = input("Escolha uma opção: ").strip()
    if escolha == "1":
        valor = escolher_opcao(READING_TYPES, "Escolha o tipo:")
        filtrado = [r for r in registros if r['tipo'] == valor]
    elif escolha == "2":
        valor = escolher_opcao(STATUS_OPTIONS, "Escolha o status:")
        filtrado = [r for r in registros if r['status'] == valor]
    else:
        print("Opção inválida.")
        return
    if not filtrado:
        print("Nenhum registro encontrado para o filtro selecionado.")
        return
    listar_leituras(filtrado)


def main():
    registros = carregar_dados()
    while True:
        opcao = menu()
        if opcao == "1":
            adicionar_leitura(registros)
        elif opcao == "2":
            listar_leituras(registros)
        elif opcao == "3":
            atualizar_leitura(registros)
        elif opcao == "4":
            remover_leitura(registros)
        elif opcao == "5":
            filtrar_leituras(registros)
        elif opcao == "6":
            print("Saindo. Até a próxima leitura!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

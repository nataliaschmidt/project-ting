from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    for data in instance.queue:
        if data["nome_do_arquivo"] == path_file:
            return None

    new_file = txt_importer(path_file)

    if new_file:
        file = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(new_file),
            "linhas_do_arquivo": new_file,
        }

        instance.enqueue(file)
        print(file)


def remove(instance: Queue):
    if len(instance) > 0:
        data_to_remove = instance.search(0)
        instance.dequeue()
        print(
            f'Arquivo {data_to_remove["nome_do_arquivo"]} removido com sucesso'
        )
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# TESTE = list()
# TESTE.append(
#     [
#         "Acima de tudo,",
#         "é fundamental ressaltar que a adoção de políticas
#             descentralizadoras nos obriga",
#         "à análise do levantamento das variáveis envolvidas.",
#     ]
# )

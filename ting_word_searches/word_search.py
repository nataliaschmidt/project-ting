from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    output = []

    for file in instance.queue:
        occurrences = []

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1})

        if occurrences:
            output.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return output


def search_by_word(word: str, instance: Queue):
    output = []

    for file in instance.queue:
        occurrences = []

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1,
                                    "conteudo": line})

        if occurrences:
            output.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return output

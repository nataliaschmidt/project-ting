from ting_file_management.priority_queue import PriorityQueue
import pytest

FILE_1 = {
    "nome_do_arquivo": "text1.txt",
    "qtd_linhas": 2,
    "linhas_do_arquivo": [
        "Contrary to popular belief,",
        "Lorem Ipsum is not simply random text.",
    ],
}

FILE_2 = {
    "nome_do_arquivo": "text2.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [
        "Lorem Ipsum is simply dummy text of the printing and ",
        "Lorem Ipsum has been the industry's standard dummy text ever",
        "when an unknown printer took a galley of type and scrambled it ",
    ],
}

FILE_3 = {
    "nome_do_arquivo": "text3.txt",
    "qtd_linhas": 6,
    "linhas_do_arquivo": [
        " There are many variations of passages of Lorem Ipsum available,",
        "but the majority have suffered alteration in some form,",
        "by injected humour,",
        " or randomised words which don't look even slightly believable.",
        "If you are going to use a passage of Lorem Ipsum,",
        "you need to be sure there isn't anything embarrassing hidden ",
    ],
}


def test_basic_priority_queueing():

    test_priority_queue = PriorityQueue()

    """Testes para o método is_priority"""

    assert test_priority_queue.is_priority(FILE_1) is True
    assert test_priority_queue.is_priority(FILE_3) is False

    """Testes para o método enqueue"""

    test_priority_queue.enqueue(FILE_3)
    test_priority_queue.enqueue(FILE_1)
    test_priority_queue.enqueue(FILE_2)

    assert len(test_priority_queue) == 3
    assert len(test_priority_queue.high_priority) == 2
    assert len(test_priority_queue.regular_priority) == 1

    """Testes para o método __len__"""

    assert test_priority_queue.__len__() == 3

    """Testes para o método dequeue"""

    test_priority_queue.dequeue()
    assert len(test_priority_queue) == 2
    assert len(test_priority_queue.high_priority) == 1
    assert len(test_priority_queue.regular_priority) == 1

    """Testes para o método search"""

    assert test_priority_queue.search(0) == FILE_2
    assert test_priority_queue.search(1) == FILE_3

    with pytest.raises(IndexError):
        test_priority_queue.search(5)

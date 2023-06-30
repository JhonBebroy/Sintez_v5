class Melodis:
    """ piano 0 = first
        piano 1 = greate \n

        ПРИМЕР
        [[0, 16], [1, 14]] - это 2 аккорда: Номер 16 на первой клавиатуре и 14 на второй клавиатуре.\n
        [-1] - это пауза (кривая)
    """
    mario_list = [
        [[1, 14]],
        [[0, 16], [1, 14]],
        [[1, 14]],
        [[0, 16], [1, 14]],
        [[1, 14]],
        [[0, 12], [1, 14]],
        [[0, 16], [1, 14]],
        [[1, 14]],

        [[0, 19], [1, 19]],
        [[1, 19]],
        [[1, 19]],
        [[1, 19]],

        [[1, 7]],
        [[1, 7]],
        [[1, 7]],
        [[1, 7]],

        [[0, 12], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[0, 7], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[0, 4], [1, 12]],
        [[1, 12]],

        [[1, 5]],
        [[0, 9], [1, 5]],
        [[1, 5]],
        [[0, 11], [1, 5]],
        [[1, 5]],
        [[0, 10], [1, 5]],
        [[0, 9], [1, 5]],
        [[1, 5]],

        [[0, 7], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],
        [[0, 19], [1, 12]],

        [[0, 21], [1, 5]],
        [[1, 5]],
        [[0, 17], [1, 5]],
        [[0, 19], [1, 5]],

        [[1, 12]],
        [[0, 16], [1, 12]],
        [[1, 12]],
        [[0, 12], [1, 12]],

        [[0, 14], [1, 7]],
        [[0, 11], [1, 7]],
        [[1, 7]],
        [[1, 7]],

        [[0, 12], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[0, 7], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[0, 4], [1, 12]],
        [[1, 12]],

        [[1, 5]],
        [[0, 9], [1, 5]],
        [[1, 5]],
        [[0, 11], [1, 5]],
        [[1, 5]],
        [[0, 10], [1, 5]],
        [[0, 9], [1, 5]],
        [[1, 5]],

        [[0, 7], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],
        [[0, 19], [1, 12]],

        [[0, 21], [1, 5]],
        [[1, 5]],
        [[0, 17], [1, 5]],
        [[0, 19], [1, 5]],

        [[1, 12]],
        [[0, 16], [1, 12]],
        [[1, 12]],
        [[0, 12], [1, 12]],

        [[0, 14], [1, 7]],
        [[0, 11], [1, 7]],
        [[1, 7]],
        [[1, 7]],

        [[1, 12]],
        [[1, 12]],
        [[0, 19], [1, 12]],
        [[0, 18], [1, 12]],
        [[0, 17], [1, 12]],
        [[0, 15], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],

        [[1, 5]],
        [[0, 8], [1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[0, 14], [1, 5]],

        [[1, 12]],
        [[1, 12]],
        [[0, 19], [1, 12]],
        [[0, 18], [1, 12]],
        [[0, 17], [1, 12]],
        [[0, 15], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],

        [[1, 5]],
        [[0, 24], [1, 5]],
        [[1, 5]],
        [[0, 24], [1, 5]],
        [[0, 24], [1, 5]],
        [[1, 5]],
        [[1, 5]],
        [[1, 5]],

        [[1, 12]],
        [[1, 12]],
        [[0, 19], [1, 12]],
        [[0, 18], [1, 12]],
        [[0, 17], [1, 12]],
        [[0, 15], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],

        [[1, 5]],
        [[0, 8], [1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[0, 14], [1, 5]],

        [[1, 8]],
        [[1, 8]],
        [[0, 15], [1, 8]],
        [[1, 8]],

        [[1, 10]],
        [[0, 14], [1, 10]],
        [[1, 10]],
        [[1, 10]],

        [[0, 12], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],

        [[1, 12]],
        [[1, 12]],
        [[0, 19], [1, 12]],
        [[0, 18], [1, 12]],
        [[0, 17], [1, 12]],
        [[0, 15], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],

        [[1, 5]],
        [[0, 8], [1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[0, 14], [1, 5]],

        [[1, 12]],
        [[1, 12]],
        [[0, 19], [1, 12]],
        [[0, 18], [1, 12]],
        [[0, 17], [1, 12]],
        [[0, 15], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],

        [[1, 5]],
        [[0, 24], [1, 5]],
        [[1, 5]],
        [[0, 24], [1, 5]],
        [[0, 24], [1, 5]],
        [[1, 5]],
        [[1, 5]],
        [[1, 5]],

        [[1, 12]],
        [[1, 12]],
        [[0, 19], [1, 12]],
        [[0, 18], [1, 12]],
        [[0, 17], [1, 12]],
        [[0, 15], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],

        [[1, 5]],
        [[0, 8], [1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[0, 14], [1, 5]],

        [[1, 8]],
        [[1, 8]],
        [[0, 15], [1, 8]],
        [[1, 8]],

        [[1, 10]],
        [[0, 14], [1, 10]],
        [[1, 10]],
        [[1, 10]],

        [[0, 12], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],

        [[0, 12], [1, 8]],
        [[0, 12], [1, 8]],
        [[1, 8]],
        [[0, 12], [1, 8]],
        [[1, 8]],
        [[0, 12], [1, 8]],

        [[0, 14], [1, 10]],
        [[1, 10]],

        [[0, 16], [1, 12]],
        [[0, 12], [1, 12]],
        [[1, 12]],
        [[0, 9], [1, 12]],
        [[0, 7], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],

        [[0, 12], [1, 8]],
        [[0, 12], [1, 8]],
        [[1, 8]],
        [[0, 12], [1, 8]],
        [[1, 8]],
        [[0, 12], [1, 8]],

        [[0, 14], [1, 10]],
        [[1, 10]],

        [[0, 16], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],

        [[0, 12], [1, 8]],
        [[0, 12], [1, 8]],
        [[1, 8]],
        [[0, 12], [1, 8]],
        [[1, 8]],
        [[0, 12], [1, 8]],

        [[0, 14], [1, 10]],
        [[1, 10]],

        [[0, 16], [1, 12]],
        [[0, 12], [1, 12]],
        [[1, 12]],
        [[0, 9], [1, 12]],
        [[0, 7], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],

        [[0, 14], [1, 14]],
        [[0, 14], [1, 14]],
        [[1, 14]],
        [[0, 14], [1, 14]],
        [[1, 14]],
        [[0, 12], [1, 14]],
        [[0, 14], [1, 14]],
        [[1, 14]],

        [[0, 19], [1, 7]],
        [[1, 7]],
        [[1, 7]],
        [[1, 7]],

        [[1, 19]],
        [[1, 19]],
        [[1, 19]],
        [[1, 19]],
    ]

    rammstein_list = [
        [[0, 19]],
        [[0, 18]],
        [[0, 14]],
        [[0, 8]],
        [[0, 8]],
        [[0, 14]],
        [[0, 18]],
        [[0, 14]],
        [[0, 21]],
        [[0, 22]],
        [[0, 17]],
        [[0, 21]],
        [[0, 22]],
        [[0, 17]],
        [[0, 10]],
        [[0, 10]],
        [[0, 17]],
        [[0, 22]],
        [[0, 17]],
        [[0, 26]],
        [[0, 14]],
        [[0, 19]],
        [[0, 14]],
        [[0, 21]],
        [[0, 9]],
        [[0, 14]],
        [[0, 9]],
        [[0, 23]],
        [[0, 22]],
        [[0, 20]],
        [[0, 18]],
        [[0, 20]],
        [[0, 14]],
        [[0, 20]],
        [[0, 14]],
        [[1, 7], [1, 19], [1, 26], [1, 31]],


    ]

    def __init__self(self):
        pass

class Board:
    """Класс, который описывает игровое поле."""

    _field_size = 3

    def __init__(self):
        self.board = [
            [' ' for _ in range(self._field_size)]
            for _ in range(self._field_size)
        ]

    def __str__(self) -> str:
        return (
            'Объект игрового поля размером '
            f'{self._field_size}x{self._field_size}'
        )

    def make_move(self, row: int, col: int, player: str) -> None:
        """Метод, который обрабатывает ходы игроков."""
        self.board[row][col] = player

    def display(self) -> None:
        """Метод, который отрисовывает игровое поле."""
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_board_full(self) -> bool:
        """Метод, который проверяет заполнено ли игровое поле полностью"""
        for i in range(self._field_size):
            for j in range(self._field_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    def check_win(self, player) -> bool:
        """Метод который определяет победу"""
        for i in range(self._field_size):
            if (all([self.board[i][j]] == player
                    for j in range(self._field_size)) or
                    all([self.board[i][j] == player
                         for j in range(self._field_size)])):
                return True
            if (
                    self.board[0][0] == self.board[1][1] == self.board[2][2]
                    == player
                    or
                    self.board[0][2] == self.board[1][1] == self.board[2][0]
                    == player
            ):
                return True
        return False

    def save_result(self, result: str) -> None:
        """Метод который добавляет результат игры в файл"""
        with open('results.txt', 'a', encoding='utf-8') as f:
            f.write(result + '\n')

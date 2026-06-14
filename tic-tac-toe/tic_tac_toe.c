#include <stdio.h>

char board[3][3] = {
    {'1','2','3'},
    {'4','5','6'},
    {'7','8','9'}
};

void displayBoard() {
    printf("\n");

    for(int i = 0; i < 3; i++) {
        printf(" %c | %c | %c \n",
               board[i][0],
               board[i][1],
               board[i][2]);

        if(i < 2)
            printf("---|---|---\n");
    }
}

int makeMove(int position, char player) {

    if(position < 1 || position > 9) {
        printf("Invalid position!\n");
        return 0;
    }

    int row = (position - 1) / 3;
    int col = (position - 1) % 3;

    if(board[row][col] == 'X' || board[row][col] == 'O') {
        printf("Position already taken!\n");
        return 0;
    }

    board[row][col] = player;
    return 1;
}

int checkWinner() {

    for(int i = 0; i < 3; i++) {

        if(board[i][0] == board[i][1] &&
           board[i][1] == board[i][2])
            return 1;

        if(board[0][i] == board[1][i] &&
           board[1][i] == board[2][i])
            return 1;
    }

    if(board[0][0] == board[1][1] &&
       board[1][1] == board[2][2])
        return 1;

    if(board[0][2] == board[1][1] &&
       board[1][1] == board[2][0])
        return 1;

    return 0;
}

int main() {

    int position;

    displayBoard();

    printf("\nPlayer X, enter position (1-9): ");
    scanf("%d", &position);

    if(!makeMove(position, 'X'))
        return 0;

    displayBoard();

    if(checkWinner()) {
        printf("\nPlayer X Wins!\n");
        return 0;
    }

    printf("\nPlayer O, enter position (1-9): ");
    scanf("%d", &position);

    if(!makeMove(position, 'O'))
        return 0;

    displayBoard();

    if(checkWinner()) {
        printf("\nPlayer O Wins!\n");
        return 0;
    }

    return 0;
}

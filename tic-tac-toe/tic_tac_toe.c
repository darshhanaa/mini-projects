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

int main() {
    int position;

    displayBoard();

    printf("\nPlayer X, enter position (1-9): ");
    scanf("%d", &position);

    if(position == 1) board[0][0] = 'X';
    else if(position == 2) board[0][1] = 'X';
    else if(position == 3) board[0][2] = 'X';
    else if(position == 4) board[1][0] = 'X';
    else if(position == 5) board[1][1] = 'X';
    else if(position == 6) board[1][2] = 'X';
    else if(position == 7) board[2][0] = 'X';
    else if(position == 8) board[2][1] = 'X';
    else if(position == 9) board[2][2] = 'X';

    printf("\nUpdated Board:\n");
    displayBoard();

    return 0;
}
}

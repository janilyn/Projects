#include <stdio.h>
#include <string.h>

void inputtext(int keyWithParities[64], char *plaintext);
int parityCheck(int keyWithParities[64]);
void cipherPrinter(int cipherBlock[64]);

void char2bin(int *plainBlock, char plaintext[8], int *cipherBlock);
void desCipher(int *plainBlock, int RoundKeys[16][48], int* cipherBlock);
void mixer(int leftBlock[32], int rightBlock[32], int RoundKeys[48]);
void copy(size_t n, int inBlock[n], int outBlock[n]);
void swapper(int leftBlock[32], int rightBlock[32]);

void function(int inBlock[32], int RoundKey[48], int outBlock[32]);
void exclusiveOR(size_t n, int firstInBlock[n], int secondInBlock[n], int outBlock[n]);
void substitute(int inBlock[48], int outBlock[32], int (*substitutionTable)(int, int, int));
int SubstitutionTables(int box, int row, int column);

void Key_Generator(int keyWithParities[64], int RoundKeys[16][48], int ShiftTable[16]);
void split(size_t n, size_t m, int inBlock[n], int leftBlock[m], int rightBlock[m]);
void shiftLeft(int block[28], int numOfShifts);
void combine(size_t n, size_t m, int leftBlock[n], int rightBlock[n], int outBlock[m]);

int InitialPermutationTable(int index);
int FinalPermutationTable(int index);
int ExpansionPermutationTable(int index);
int StraightPermutationTable(int index);
int ParityDropTable(int index);
int KeyCompressionTable(int index);
void permute (size_t n, size_t m, int plainBlock[n], int cipherBlock[m], int (*permutationTable)(int));


int main() {
    char plaintext[100], subtext[9];
    int keyWithParities[64];
    inputtext(keyWithParities, plaintext);

    if(parityCheck(keyWithParities)==0){
        return 0;
    }

    int rounds;

    rounds = strlen(plaintext)/8;
    if(rounds * 8 < strlen(plaintext)){
        rounds++;
    }

    for (int i = 0; i < rounds; ++i) {
        int plainBlock[64], RoundKeys[16][48], cipherBlock[64];

        int ShiftTable[] = {
                1, 1, 2, 2,
                2, 2, 2, 2,
                1, 2, 2, 2,
                2, 2, 2, 1
        };

        Key_Generator(keyWithParities, RoundKeys,ShiftTable);
        strncpy(subtext,&plaintext[i*8],8);
        char2bin(plainBlock, subtext,cipherBlock);
        desCipher(plainBlock, RoundKeys, cipherBlock);
        cipherPrinter(cipherBlock);
    }

    return 0;
}

void cipherPrinter(int cipherBlock[64]){
    for (int i = 0; i < 64; ++i) {
        printf("%d", cipherBlock[i]);
    }
}

void desCipher(int *plainBlock, int RoundKeys[16][48], int* cipherBlock){
    int inblock[64], leftBlock[32], rightBlock[32], outBlock[64];

    for (int i = 0; i < 64; ++i) {
        inblock[i] = 0;
        leftBlock[i] = 0;
        rightBlock[i] = 0;
    }

    permute(64, 64, plainBlock, inblock, InitialPermutationTable);
    split(64, 32, inblock, leftBlock, rightBlock);

    for (int round = 0; round < 16; ++round) {
        mixer(leftBlock, rightBlock,RoundKeys[round]);
        if (round < 15){
            swapper(leftBlock,rightBlock);
        }
    }

    combine(32, 64, leftBlock, rightBlock, outBlock);
    permute(64, 64, outBlock, cipherBlock, FinalPermutationTable);
}

void mixer(int leftBlock[32], int rightBlock[32], int RoundKeys[48]){
    int T1[32], T2[32], T3[32];
    copy(32, rightBlock, T1);
    function(T1,RoundKeys, T2);
    exclusiveOR(32, leftBlock, T2, T3);
    copy(32, T3, leftBlock);
}

void swapper(int leftBlock[32], int rightBlock[32]){
    int T[32];
    copy(32, leftBlock, T);
    copy(32, rightBlock, leftBlock);
    copy(32, T, rightBlock);
}

void function(int inBlock[32], int RoundKey[48], int outBlock[32]){
    int T1[48], T2[48], T3[32];
    permute(32, 48, inBlock, T1,ExpansionPermutationTable);
    exclusiveOR(48, T1, RoundKey, T2);
    substitute(T2, T3, SubstitutionTables);
    permute(32, 32, T3, outBlock, StraightPermutationTable);
}

void substitute(int inBlock[48], int outBlock[32], int (*substitutionTable)(int, int, int)){
    for (int i = 0; i < 8; ++i) {
        int row = (2 * inBlock[i * 6]) + inBlock[i * 6 + 5];
        int col = (8 * inBlock[i * 6 + 1]) + (4 * inBlock[i * 6 + 2]) + (2 * inBlock[i * 6 + 3]) + inBlock[i * 6 + 4];
        int val = (*substitutionTable) (i, row, col);

        outBlock[i * 4] = val / 8;
        val = val % 8;
        outBlock[i * 4 + 1] = val / 4;
        val = val % 4;
        outBlock[i * 4 + 2] = val / 2;
        val = val % 2;
        outBlock[i * 4 + 3] = val;
    }
}

int SubstitutionTables(int box, int row, int column){
    int SBoxes[8][4][16] = {
            {
                14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
                0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
                4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
                15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
                },

            {
                15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
                3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
                0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
                13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
                },

            {
                10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
                13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
                13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
                1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
                },

            {
                7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
                13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
                10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
                3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
                },

            {
                2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
                14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
                4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
                11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
                },

            {
                12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
                10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
                9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
                4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
                },

            {
                4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
                13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
                1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
                6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
                },

            {
                13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
                1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
                7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
                2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
            }
    };

    return SBoxes[box][row][column];

}

void exclusiveOR(size_t n, int firstInBlock[n], int secondInBlock[n], int outBlock[n]){
    for (int i = 0; i < n; ++i) {
        outBlock[i] = firstInBlock[i] ^ secondInBlock[i];
    }
}

void copy(size_t n, int inBlock[n], int outBlock[n]){
    for (int i = 0; i < n; ++i) {
        outBlock[i] = inBlock[i];
    }

}

int parityCheck(int keyWithParities[64]){
    for (int i = 0; i < 8; ++i) {
        int numof1 = 0;
        for (int j = 0; j < 8; ++j) {
            if(keyWithParities[(i*8)+j] == 1){
                numof1++;
            }
        }
        if(numof1%2 == 0){
            printf("invalid key");
            return 0;
        }
    }
    return 1;
}

void split(size_t n, size_t m, int inBlock[n], int leftBlock[m], int rightBlock[m]){
    for (int i = 0; i < m; ++i) {
        leftBlock[i] = inBlock[i];
        rightBlock[i] = inBlock[m+i];
    }
}

void shiftLeft(int block[28], int numOfShifts){
    for (int i = 0; i < numOfShifts; ++i) {
        int T = block[0];
        for (int j = 1; j < 28; ++j) {
            block[j-1] = block[j];
        }
        block[27] = T;
    }
}

void Key_Generator(int keyWithParities[64], int RoundKeys[16][48], int ShiftTable[16]){
    int cipherKey[56], preRoundKey[56], leftKey[28], rightKey[28];

    for (int i = 0; i < 56; ++i) {
        cipherKey[i] = 0;
    }

    permute(64, 56, keyWithParities, cipherKey,ParityDropTable);
    split(56, 28, cipherKey, leftKey, rightKey);
    for (int round = 0; round < 16; ++round) {
        shiftLeft(leftKey,ShiftTable[round]);
        shiftLeft(rightKey,ShiftTable[round]);
        combine(28, 56, leftKey, rightKey, preRoundKey);
        permute(56, 48, preRoundKey, RoundKeys[round],KeyCompressionTable);
    }
}

void combine(size_t n, size_t m, int leftBlock[n], int rightBlock[n], int outBlock[m]){
    for (int i = 0; i < n; ++i) {
        outBlock[i] = leftBlock[i];
        outBlock[i+n] = rightBlock[i];
    }
}

void char2bin(int *plainBlock, char plaintext[8], int *cipherBlock){
    for (int i = 0; i < 64; ++i) {
        plainBlock[i] = 0;
        cipherBlock[i] = 0;
    }

    for (int i = 0; i < 64; ++i) {
        plainBlock[i] = (plaintext[i / 8] >> (7 - (i%8))) & 1;
    }
}

void inputtext(int keyWithParities[64], char *plaintext){
    memset(plaintext,0,100);
    fgets(plaintext, 100, stdin);
    plaintext[strlen(plaintext)-1] = 0;

    for (int i = 0; i < 64; ++i) {
        keyWithParities[i]=0;
    }
    char key[65];
    scanf("%[^\n]s", key);

    for (int i = 0; i < 64; ++i) {
        if(key[i] == '1'){
            keyWithParities[i] = 1;
        }
    }
}

int InitialPermutationTable(int index){
    int PermutationTable[] = {
            58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7
    };

    return PermutationTable[index]-1;

}

int FinalPermutationTable(int index){
    int PermutationTable[] = {
            40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25
    };

    return PermutationTable[index]-1;
}

int ExpansionPermutationTable(int index){
    int PermutationTable[] = {
            32, 1, 2, 3, 4, 5, 4, 5,
            6, 7, 8, 9, 8, 9, 10, 11,
            12, 13, 12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21, 20, 21,
            22, 23, 24, 25, 24, 25, 26, 27,
            28, 29, 28, 29, 30, 31, 32, 1
    };

    return PermutationTable[index]-1;
}

int StraightPermutationTable(int index){
    int PermutationTable[] = {
            16, 7, 20, 21, 29, 12, 28, 17,
            1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9,
            19, 13, 30, 6, 22, 11, 4, 25
    };

    return PermutationTable[index]-1;
}

int ParityDropTable(int index){
    int PermutationTable[] = {
            57, 49, 41, 33, 25, 17, 9, 1,
            58, 50, 42, 34,26, 18, 10, 2,
            59, 51, 43, 35, 27,19, 11, 3,
            60, 52, 44, 36,63, 55, 47, 39,
            31, 23, 15,7, 62, 54, 46, 38,
            30, 22,14, 6, 61, 53, 45, 37,
            29,21, 13, 5, 28, 20, 12, 4
    };

    return PermutationTable[index]-1;
}

int KeyCompressionTable(int index){
    int PermutationTable[] = {
            14, 17, 11, 24, 1, 5,3, 28,
            15, 6, 21, 10,23, 19, 12, 4,
            26, 8,16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,30, 40,
            51, 45, 33, 48,44, 49, 39, 56,
            34, 53,46, 42, 50, 36, 29, 32
    };

    return PermutationTable[index]-1;
}

void permute (size_t n, size_t m, int plainBlock[n], int cipherBlock[m], int (*permutationTable)(int)){
    for (int i = 0; i < m; ++i) {
        cipherBlock[i] = plainBlock[(*permutationTable)(i)];
    }
}

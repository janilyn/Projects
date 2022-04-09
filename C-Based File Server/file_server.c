#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <pthread.h>

// command type
#define WRITE 0
#define READ 1
#define EMPTY 2
#define INVALID 3

typedef struct command{
    int type;               // command type
    char path[51];          // file path
    char string[51];        // for write: string to be appended in path
    pthread_t ptid;
} StructCMD;

// used to get input and extract the command and its arguments
int getcmd(char *cmd, int size);
StructCMD *allocCMD(void);
StructCMD *splitcmd(char *cmd);
void arg2(char *cmd, StructCMD* ret);
void arg3(char *cmd, StructCMD* ret);

// time stamp
void commandtime(StructCMD* cmd);

// operations
void writecmd(StructCMD *cmd);
void readcmd(StructCMD *cmd);
void emptycmd(StructCMD *cmd);

// make threads sleep with rng code
void cmdrngSLEEP(void);
void emptyrngsleep(void);
void mssleep(void);

char input[110];

// performs write
void writecmd(StructCMD *cmd){
    pthread_t ptid = cmd->ptid;
    cmdrngSLEEP();
    
    FILE *fp = fopen(cmd->path, "a");

    // writes the string to the file
    for (int i = 0; i < strlen(cmd->string); i++){
        fprintf(fp,"%c",cmd->string[i]);
        mssleep();              // sleeps for 25ms after a character is written
    }
    
    fclose(fp);
    
    free(cmd);
    pthread_detach(ptid);
}

// perform read
void readcmd(StructCMD *cmd){
    pthread_t ptid = cmd->ptid;
    cmdrngSLEEP();

    FILE *fp;
    FILE *fread = fopen("read.txt", "a");
    char ch;

    fprintf(fread,"read %s: ", cmd->path);         // writes the whole command to read.txt

    // case when file does not exist
    if ((fp= fopen(cmd->path, "r")) == NULL){
        fprintf(fread,"FILE DNE\n");
        fclose(fread);
        free(cmd);
        pthread_detach(ptid);
        return;
    }

    //writes the contents of file to read.txt
    while((ch = fgetc(fp)) != EOF){
      fprintf(fread,"%c",ch);
    }

    fprintf(fread, "\n");           // prints a new line at the end

    fclose(fp);
    fclose(fread);

    free(cmd);
    pthread_detach(ptid);
}

// performs empty
void emptycmd(StructCMD *cmd){
    pthread_t ptid = cmd->ptid;
    cmdrngSLEEP();

    FILE *fp;
    FILE *fempty = fopen("empty.txt", "a");
    char ch;
    
    fprintf(fempty,"empty %s: ", cmd->path);        // writes the whole command to empty.txt

    // case when file does not exist
    if((fp = fopen(cmd->path, "r")) == NULL){
        fprintf(fempty,"FILE ALREADY EMPTY\n");
        fclose(fempty);
        free(cmd);
        pthread_detach(ptid);
        return;
    }

    //writes the contents of file to empty.txt
    while((ch = fgetc(fp)) != EOF){
      fprintf(fempty,"%c",ch);
    }

    fprintf(fempty, "\n");              // prints a new line at the end

    fclose(freopen(NULL,"w",fp));       // empties the file    

    emptyrngsleep();                    // sleeps for a random amount between 7-10 s after doing the operation
    
    fclose(fempty);

    free(cmd);

    pthread_detach(ptid);
}

int main(){
    void * fs[] = {writecmd, readcmd, emptycmd};     //functions
    StructCMD *cmd = NULL;

    // gets the input from the user
    while(getcmd(input,sizeof(input)) >= 0){
        input[strlen(input)-1] = '\0';      // removes '\n' from the end of the input
        
        cmd = splitcmd(input);              // splits the input into the command + the arguments

        commandtime(cmd);

        if (cmd->type == INVALID){
            free(cmd);
            continue;
        }
        pthread_create(&cmd->ptid, NULL, fs[cmd->type], cmd);
    }
    return 0;
}

// gets input from the user and stores it in the first parameter
int getcmd(char *cmd, int size){
    printf("> ");
    memset(cmd, 0, size);       // makes sure we don't get random bits from the previous allocation for this memory block
    fgets(cmd, size,stdin);     // gets the input from the user
    if(cmd[0] == 0)
        return -1;
    return 0;
}

// allocates memory for the split command
StructCMD *allocCMD(void){
    struct command* ret = (struct command*) malloc(sizeof(struct command));
    memset(ret->path,0,sizeof(ret->path));          // makes sure we don't get random bits from the previous allocation for this memory block
    memset(ret->string,0,sizeof(ret->string));      // makes sure we don't get random bits from the previous allocation for this memory block

    return ret;
}

// extracts the file path for read and empty operations
void arg2(char *cmd, StructCMD* ret){
    char *token;
    token = strtok(cmd, " ");

    token = strtok(NULL, " ");
    strcpy(ret->path, token);
}

// extracts the file path and the strig for the write operations
void arg3(char *cmd, StructCMD* ret){
    int i, j;

    // gets the file path
    // scans all the characters after "write " until it encounters space
    for (i = 6; i < strlen(cmd); i++){
        if(cmd[i] == ' ')
            break;
        ret->path[i-6] = cmd[i];
    }

    i++;    // skips the space
    
    // gets the entire string
    // scans all the characters after "write <path> " 
    //until the end of the string
    for (j = i; j < strlen(cmd); j++){
        ret->string[j-i] = cmd[j];
    }  
}

// splits the input and stores it in the StructCMD structure
StructCMD *splitcmd(char *cmd){
    StructCMD* ret = allocCMD();        // allocates memory for the command

    // gets the value of the Struct CMD field 
    // depending on the operation
    if(strncmp(cmd, "write ", 6)==0){
        ret->type = WRITE;
        arg3(cmd,ret);
    } else if(strncmp(cmd, "read ", 5)==0){
        ret->type = READ;
        arg2(cmd, ret);
    } else if(strncmp(cmd, "empty ", 6)==0){
        ret->type = EMPTY;
        arg2(cmd, ret);
    } else{
        ret->type = INVALID;
        strcpy(ret->path, cmd);
    }

    return ret;
}

// writes the time stamp + the command to command.txt
void commandtime(StructCMD* cmd){
    time_t curtime;
    char timestamp[25];

    //gets the time stamp
    time(&curtime);
    strcpy(timestamp,ctime(&curtime));
    timestamp[strlen(timestamp)-1] = '\0';

    // writes the command received to commands.txt
    FILE *fcmd = fopen("commands.txt", "a");
    
    fprintf(fcmd, "[%s] ", timestamp);

    if(cmd->type == 0){
        fprintf(fcmd, "write %s %s", cmd->path, cmd->string);
    } else if (cmd->type == 1){
        fprintf(fcmd, "read %s", cmd->path);
    } else if (cmd->type == 2){
        fprintf(fcmd, "empty %s", cmd->path);
    } else{
        fprintf(fcmd, "%s", cmd->path);
    }

    fprintf(fcmd, "\n");

    fclose(fcmd);
}

// makes empty threads sleep after it is done doing its operations
void emptyrngsleep(void) {
	srand(time(0));
	int r = rand()%4 + 7;      // Returns a pseudo-random integer between 7 and 10
    sleep(r);
}

// makes threads sleep before its execution
void cmdrngSLEEP(void) {
	srand(time(0));
	int r = rand()%100;      // Returns a pseudo-random integer between 0 and 100
    int i=0;

    if (r > 80){
        i = 6;
    } else{
        i = 1;
    }
    
    sleep(i);
}

// makes write threads sleep for each character written in the specified file
void mssleep(void) {
	sleep(0.025);
}
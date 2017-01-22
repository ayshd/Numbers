#include <stdio.h>
#include <stdlib.h>

#define START 4430
#define END 4580
char *fname = "win_num.csv";

int main(void)
{
  int i, j;
  char buf[128];
  char num[128];
  char date[128];
  int n3_max[3][2], n4_max[4][2];
  int n3[3], n4[4], ct_n3[3][10], ct_n4[4][10]; // grade num
  FILE *fp;

  if ((fp = fopen(fname, "r")) == NULL) {
    fprintf(stderr, "cannnot file open: %s\n", fname);
    return 1;
  }

  // initialization
  for (i=0; i<3; i++) {
    for (j=0; j<10; j++) {
      ct_n3[i][j] = 0;
    }
  }

  for (i=0; i<4; i++) {
    for (j=0; j<10; j++) {
      ct_n4[i][j] = 0;
    }
  }

  while (fgets(buf, sizeof(buf), fp) != NULL ) {
    sscanf(buf, "%[^,],%[^,],%1d%1d%1d,%1d%1d%1d%1d", num, date, &n3[0], &n3[1], &n3[2], &n4[0], &n4[1], &n4[2], &n4[3]);

    // check string length
    i = 0;
    j = 0;
    while (*(num+i) != '\0') {
      j++;
      i++;
    }

    // remove kanji from num
    sprintf(buf, "\0");
    if (j == 7) {
      for (i=3; i<4; i++) {
	sprintf(buf, "%s%c", buf, num[i]);
      }
    } else if (j == 9) {
      for (i=3; i<6; i++) {
	sprintf(buf, "%s%c", buf, num[i]);
      }
    } else if (j == 10) {
      for (i=3; i<7; i++) {
	sprintf(buf, "%s%c", buf, num[i]);
      }
    }

    if (START<=atoi(buf) && atoi(buf)<=END) {
      //printf("%s\n", buf);
      for (i=0; i<3; i++) {
	if (n3[i] == 0) {        ct_n3[i][0] += 1;
	} else if (n3[i] == 1) { ct_n3[i][1] += 1;
	} else if (n3[i] == 2) { ct_n3[i][2] += 1;
	} else if (n3[i] == 3) { ct_n3[i][3] += 1;
	} else if (n3[i] == 4) { ct_n3[i][4] += 1;
	} else if (n3[i] == 5) { ct_n3[i][5] += 1;
	} else if (n3[i] == 6) { ct_n3[i][6] += 1;
	} else if (n3[i] == 7) { ct_n3[i][7] += 1;
	} else if (n3[i] == 8) { ct_n3[i][8] += 1;
	} else if (n3[i] == 9) { ct_n3[i][9] += 1;
	}
      }

      for (i=0; i<4; i++) {
	if (n4[i] == 0) {        ct_n4[i][0] += 1;
	} else if (n4[i] == 1) { ct_n4[i][1] += 1;
	} else if (n4[i] == 2) { ct_n4[i][2] += 1;
	} else if (n4[i] == 3) { ct_n4[i][3] += 1;
	} else if (n4[i] == 4) { ct_n4[i][4] += 1;
	} else if (n4[i] == 5) { ct_n4[i][5] += 1;
	} else if (n4[i] == 6) { ct_n4[i][6] += 1;
	} else if (n4[i] == 7) { ct_n4[i][7] += 1;
	} else if (n4[i] == 8) { ct_n4[i][8] += 1;
	} else if (n4[i] == 9) { ct_n4[i][9] += 1;
	}
      }
    }
  }

  printf("-------------------------------Numbers3-------------------------------\n");
  printf("%4d--%4d         :   0    1    2    3    4    5    6    7    8    9\n", START, END);
  printf("----------------------------------------------------------------------\n");
  printf("the hundred's place:%4d %4d %4d %4d %4d %4d %4d %4d %4d %4d\n"
	 ,ct_n3[0][0], ct_n3[0][1], ct_n3[0][2], ct_n3[0][3], ct_n3[0][4]
	 ,ct_n3[0][5], ct_n3[0][6], ct_n3[0][7], ct_n3[0][8], ct_n3[0][9]);
  printf("the ten's     place:%4d %4d %4d %4d %4d %4d %4d %4d %4d %4d\n"
	 ,ct_n3[1][0], ct_n3[1][1], ct_n3[1][2], ct_n3[1][3], ct_n3[1][4]
	 ,ct_n3[1][5], ct_n3[1][6], ct_n3[1][7], ct_n3[1][8], ct_n3[1][9]);
  printf("the one's     place:%4d %4d %4d %4d %4d %4d %4d %4d %4d %4d\n"
	 ,ct_n3[2][0], ct_n3[2][1], ct_n3[2][2], ct_n3[2][3], ct_n3[2][4]
	 ,ct_n3[2][5], ct_n3[2][6], ct_n3[2][7], ct_n3[2][8], ct_n3[2][9]);

  // calc mode number
  for (i=0; i<3; i++) {
    n3_max[i][0] = ct_n3[i][0];
    n3_max[i][1] = 0;
    for (j=0; j<10; j++) {
      if (ct_n3[i][j] > n3_max[i][0]) {
	n3_max[i][0] = ct_n3[i][j];
	n3_max[i][1] = j;
      }
    }
  }

  printf("mode number        :   ");
  for (i=0; i<3; i++) {
    printf("%d", n3_max[i][1]);
  }

  printf("\n");

  printf("\n\n");
  printf("-------------------------------Numbers4-------------------------------\n");
  printf("%4d--%4d          :   0    1    2    3    4    5    6    7    8    9\n", START, END);
  printf("----------------------------------------------------------------------\n");

  printf("the thousands' place:%4d %4d %4d %4d %4d %4d %4d %4d %4d %4d\n"
	 ,ct_n4[0][0], ct_n4[0][1], ct_n4[0][2], ct_n4[0][3], ct_n4[0][4]
	 ,ct_n4[0][5], ct_n4[0][6], ct_n4[0][7], ct_n4[0][8], ct_n4[0][9]);
  printf("the hundred's  place:%4d %4d %4d %4d %4d %4d %4d %4d %4d %4d\n"
	 ,ct_n4[1][0], ct_n4[1][1], ct_n4[1][2], ct_n4[1][3], ct_n4[1][4]
	 ,ct_n4[1][5], ct_n4[1][6], ct_n4[1][7], ct_n4[1][8], ct_n4[1][9]);
  printf("the ten's      place:%4d %4d %4d %4d %4d %4d %4d %4d %4d %4d\n"
	 ,ct_n4[2][0], ct_n4[2][1], ct_n4[2][2], ct_n4[2][3], ct_n4[2][4]
	 ,ct_n4[2][5], ct_n4[2][6], ct_n4[2][7], ct_n4[2][8], ct_n4[2][9]);
  printf("the one's      place:%4d %4d %4d %4d %4d %4d %4d %4d %4d %4d\n"
	   ,ct_n4[3][0], ct_n4[3][1], ct_n4[3][2], ct_n4[3][3], ct_n4[3][4]
	   ,ct_n4[3][5], ct_n4[3][6], ct_n4[3][7], ct_n4[3][8], ct_n4[3][9]);


  for (i=0; i<4; i++) {
    n4_max[i][0] = ct_n4[i][0];
    n4_max[i][1] = 0;
    for (j=0; j<10; j++) {
      if (ct_n4[i][j] > n4_max[i][0]) {
	n4_max[i][0] = ct_n4[i][j];
	n4_max[i][1] = j;
      }
    }
  }

  printf("mode number        :   ");
  for (i=0; i<4; i++) {
    printf("%d", n4_max[i][1]);
  }
  printf("\n");

  return 0;
}

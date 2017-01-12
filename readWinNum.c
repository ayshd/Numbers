#include <stdio.h>
#include <stdlib.h>

#define START 4473
#define END 4573
char *fname = "tmp.csv";

int main(void)
{
  int i, j;
  char buf[128];
  char num[128];
  char date[128];
  int n3_max[3][2], n4_max[4][2]; // times num
  int n3_min[3][2], n4_min[4][2]; // times num
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

  printf("%4d--%4d:   0    1    2    3    4    5    6    7    8    9\n", START, END);
  printf("--------------------------------------------------------------\n");
  for (i=0; i<3; i++) {
    printf("Numbers3 %d:%4d %4d %4d %4d %4d %4d %4d %4d %4d %4d\n", 3-i
	   ,ct_n3[i][0], ct_n3[i][1], ct_n3[i][2], ct_n3[i][3], ct_n3[i][4]
	   ,ct_n3[i][5], ct_n3[i][6], ct_n3[i][7], ct_n3[i][8], ct_n3[i][9]);
    double tmp1 = (double)(0*ct_n3[i][0]
			   +1*ct_n3[i][1]
			   +2*ct_n3[i][2]
			   +3*ct_n3[i][3]
			   +4*ct_n3[i][4]
			   +5*ct_n3[i][5]
			   +6*ct_n3[i][6]
			   +7*ct_n3[i][7]
			   +8*ct_n3[i][8]
			   +9*ct_n3[i][9]);
    double tmp = tmp1/(double)(END-START+1);
    printf("Expectation %d:    %lf\n", 3-i, tmp);
	   /*	   0*(double)(ct_n3[i][0]/(END-START+1))
	   +1*(double)(ct_n3[i][1]/(END-START+1))
	   +2*(double)(ct_n3[i][2]/(END-START+1))
	   +3*(double)(ct_n3[i][3]/(END-START+1))
	   +4*(double)(ct_n3[i][4]/(END-START+1))
	   +5*(double)(ct_n3[i][5]/(END-START+1))
	   +6*(double)(ct_n3[i][6]/(END-START+1))
	   +7*(double)(ct_n3[i][7]/(END-START+1))
	   +8*(double)(ct_n3[i][8]/(END-START+1))
	   +9*(double)(ct_n3[i][9]/(END-START+1)));
    */


    /*
    printf("Expectation: %d   %4d\n",i,
	   (ct_n3[i][0])
	   + (ct_n3[i][1])
	   + (ct_n3[i][2])
	   + (ct_n3[i][3])
	   + (ct_n3[i][4])
	   + (ct_n3[i][5])
	   + (ct_n3[i][6])
	   + (ct_n3[i][7])
	   + (ct_n3[i][8])
	   + (ct_n3[i][9]));
    */
  }

  int tmp[10];
  for (j=0; j<10; j++) {
    tmp[j] = 0;
  }

  for (i=0; i<3; i++) {
    for (j=0; j<10; j++) {
      tmp[j] += ct_n3[i][j];
    }
  }

  printf("All        %4d %4d %4d %4d %4d %4d %4d %4d %4d %4d\n"
	   ,tmp[0], tmp[1], tmp[2], tmp[3], tmp[4]
	   ,tmp[5], tmp[6], tmp[7], tmp[8], tmp[9]);
  /*
  printf("All        %4d\n",
	 (0*tmp[0]+1*tmp[1]+2*tmp[2]+3*tmp[3]+4*tmp[4]+5*tmp[5]+6*tmp[6]+7*tmp[7]+8*tmp[8]+9*tmp[9])
	 /(END-START+1));
  */
  /*
  for (j=0; j<10; j++) {
    printf("%d %d\n", j, tmp[j]);
  }
  */
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
  for (i=0; i<3; i++) {
    printf("%d", n3_max[i][1]);
  }
  printf("\n");
  for (i=0; i<3; i++) {
    n3_min[i][0] = ct_n3[i][0];
    n3_min[i][1] = 0;
    for (j=0; j<10; j++) {
      if (ct_n3[i][j] < n3_min[i][0]) {
	n3_min[i][0] = ct_n3[i][j];
	n3_min[i][1] = j;
      }
    }
  }
  for (i=0; i<3; i++) {
    printf("%d", n3_min[i][1]);
  }

  printf("\n\n");

  printf("%4d--%4d:   0    1    2    3    4    5    6    7    8    9\n", START, END);
  printf("--------------------------------------------------------------\n");
  for (i=0; i<4; i++) {
    printf("Numbers4 %d:%4d %4d %4d %4d %4d %4d %4d %4d %4d %4d\n", 4-i
	   ,ct_n4[i][0], ct_n4[i][1], ct_n4[i][2], ct_n4[i][3], ct_n4[i][4]
	   ,ct_n4[i][5], ct_n4[i][6], ct_n4[i][7], ct_n4[i][8], ct_n4[i][9]);
  }

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

  for (i=0; i<4; i++) {
    printf("%d", n4_max[i][1]);
  }
  printf("\n");

  return 0;
}

#include</gaussMetod.h>

float setMatrix(int i, int j){
	float Matrix[i][j];
	for(int a = 0; a<i; a++){
		for(int b = 0; b<j; b++){
		printf("posicao [%d][%d]", &a, &b);
		scanf("%f", Matrix[a][b]);
		}


	}
	return Matrix;
}



int main(){
	Ma[3][3] = setMatrix(3, 3);
	return 0;
}


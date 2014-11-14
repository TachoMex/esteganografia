#include<cstdio>
#include<cstdlib>
#include<cstring>
void showUsage(){
	printf("Usage:\n RSA -<action> [args]\n");
	printf("-k Generate key. public key output file ,  private key output file\n");
	printf("-c Crypt file, key , input file, output file\n");
	printf("-d Decrypt file, key , input file, output file\n");
}
int main(int argc, char **argv){
	if(argc > 1){
		if(strcmp(argv[1],"-k")==0){
			if(argc >= 3){
				char ord[100];
				sprintf(ord, "python keygen.py %s %s", argv[2], argv[3]);
				system(ord);
			}else
				showUsage();
		}else if(strcmp(argv[1],"-c")==0){
			if(argc >= 4){
				char ord[500];
				char ord2[500];
				sprintf(ord, "python#crypt.py#%s#%s#%s", argv[2], argv[3], argv[4]);
				int i, j;
				for(i=0,j=0;ord[i]!='\0';i++,j++){
					if(ord[i]==' ')
						ord2[j++]='\\';
					ord2[j]=ord[i];
				}
				ord2[j]='\0';
				for(i=0;i<j;i++)
					if(ord2[i]=='#')
						ord2[i]=' ';
				system(ord2);
			}else
				showUsage();
		}else if(strcmp(argv[1],"-d")==0){
			if(argc >= 4){
				char ord[500];
				char ord2[500];
				sprintf(ord, "python#decrypt.py#%s#%s#%s", argv[2], argv[3], argv[4]);
				int i, j;
				for(i=0,j=0;ord[i]!='\0';i++,j++){
					if(ord[i]==' ')
						ord2[j++]='\\';
					ord2[j]=ord[i];
				}
				ord2[j]='\0';
				for(i=0;i<j;i++)
					if(ord2[i]=='#')
						ord2[i]=' ';
				system(ord2);
			}else
				showUsage();
		}else
			showUsage();
	}else 
		showUsage();
	return 0;
}
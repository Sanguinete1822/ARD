import java.util.Scanner;
import java.util.ArrayList;
import java.util.Random;
void main() {

    // VALD
    ArrayList<String> validos = new ArrayList<>();
    validos.add("rec");
    validos.add("at");
    validos.add("def");

    // SET
    Scanner e = new Scanner(System.in);
    Random r = new Random();

    // VARV
    int n = 1;
    int balas_j = 0;
    int balas_c = 0;
    int vida_j = 1;
    int vida_c = 1;
    String escolha_j;
    String escolha_c;
    int ec;
    System.out.println("Atirar = at");
    System.out.println("Recarregar = rec");
    System.out.println("Defesa = def ");
    // Jog
    while (vida_c > 0 && vida_j > 0){

        // Legenda padrão
        System.out.println(" ");
        System.out.println(" Digite sua ação: ");


        // Ações
        escolha_j = e.nextLine();
        System.out.println(" ");
        ec = r.nextInt(3);
        escolha_c = validos.get(ec);
        System.out.println("Rodada: " + n);
        System.out.println(escolha_j + " X " + escolha_c);

        // Cálculos

        // RECJ
        if (escolha_j.equals("rec")){
            balas_j++;
        }

        // RECC
        if (escolha_c.equals("rec")){
            balas_c++;
        }


        // ATJ
        if (escolha_j.equals("at")){
            if (balas_j > 0){
                if (!escolha_c.equals("def")){
                    if (!escolha_c.equals("at") || balas_c == 0){
                        balas_j--;
                        System.out.println("Você ganhou!!");
                        vida_c--;}
                }else{
                    balas_j--;
                    System.out.println("defendido");}

            }else{
                System.out.println("Você está sem munição!!");}
        }

        // ATC
        if (escolha_c.equals("at")){
            if (balas_c > 0){
                if (!escolha_j.equals("def")){
                    if (!escolha_j.equals("at") || balas_j == 0){
                        balas_c--;
                        System.out.println("Você Perdeu...");
                        vida_j--;}
                }else{
                    balas_c--;
                    System.out.println("Você defendeu");
                }

            }else{
                System.out.println("Computador está sem munição!!");}

        }

        // BALS RETORN
        System.out.println("Você: " + balas_j);
        System.out.println("Computador: " + balas_c);
        if (escolha_c.equals("at") && escolha_j.equals("at")){
            if (balas_c > 0 && balas_j > 0){
                System.out.println("Tiro duplo");
                vida_c--;
                vida_j--;
            }
        }
        n++;
        }
    }



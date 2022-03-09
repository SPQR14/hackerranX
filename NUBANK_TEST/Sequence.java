public class Sequence{
    
    public static void main(String [] args){
        System.out.println(numberInSequence(1, 7, 3));
    }

    public static String numberInSequence(int a, int b, int c){
        if(c == 0){
            if(a == b){
                return "YES";
            }else{
                return "NO";
            }
        }else if((b - a) % c == 0){
            return "YES";
        }else{
            return "NO";
        }
    }

}
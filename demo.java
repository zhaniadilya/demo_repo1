public classs demo{
    public static void main(String[] args){
        
        int a = 10;
        double res;

        res = kvadrat(a);

        System.out.print(res);
    }

    public static double kvadrat(int a) {
        return Math.pow(a, 2);
    }
}
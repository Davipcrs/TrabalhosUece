using System;

namespace CalcNumerico{


    class metodoNewtonRaphson{
        public double FuncQ1(double val){
            return val * val - 7;

        }
        public double FuncQ1Der(double val){
            return 2*val;
        }
        
        public double FuncQ2(double val){
            //f(x) = (x - 2)^4
            return Math.Pow((val - 2), 4);
            

        }
        public double FuncQ2Der(double val){
            return 4 * (Math.Pow(val, 3)) - 24 * (Math.Pow(val, 2)) + 48 * (val) - 32;

        }
        public double FuncQ3(double val){
            return Math.Pow(Math.E, val) - Math.Pow(val, 2);

        }
        public double FuncQ3Der(double val){
            return Math.Pow(Math.E, val) - 2*val;

        }
        public double FuncQ4(double val){
            return val * Math.Sin(val);

        }
        public double FuncQ4Der(double val){
            return Math.Sin(val) + val * Math.Cos(val);

        }
        public double FuncQ5(double val){
            return val * val - 8;

        }
        public double FuncQ5Der(double val){
            return 2*val;

        }
        public double FuncQ6(double val){
            return val * val - 91;

        }
        public double FuncQ6Der(double val){
            return 2*val;

        }
        public double FuncQ7(double val){
            
            return val * val * val - 7;

        }
        public double FuncQ7Der(double val){
            return 3*val*val;

        }
        public double FuncQ8(double val){
            return val * val * val - 200;

        }
        public double FuncQ8Der(double val){
            return 3*val*val;

        }
        



        public double ValAbs(double val)
        {
            double absVal;
            if(val < 0)
            {
                absVal = val * (-1);
            }
            else
            {
                absVal = val;
            }



            return absVal;
        }

        public double newtonRaphson(double init, double pres, double endit = 0){
            double raiz = init;
            double raiz2 = endit;
            double h = FuncQ8(raiz)/FuncQ8Der(raiz);
            int i = 0;
            Console.WriteLine("Iteração: "+i + " Raiz: "+raiz+ " Precisão: "+ pres);


            while(this.ValAbs(h)>=pres){
                h = FuncQ8(raiz)/FuncQ8Der(raiz);
                raiz = raiz - h;
                i = i + 1;
                Console.WriteLine("Iteração: "+i + " Raiz: "+raiz+ " Precisão: "+ pres);

            }

            /*
            h = FuncQ1(raiz2)/FuncQ1Der(raiz2);
            while(this.ValAbs(h)>=pres){
                h = FuncQ1(raiz2)/FuncQ1Der(raiz2);
                raiz2 = raiz2 - h;
                i = i + 1;
                Console.WriteLine("Iteração: "+i + " Raiz2: "+raiz2+ " Precisão: "+ pres);

            }
            */



            return raiz;

        }


        

    }

}
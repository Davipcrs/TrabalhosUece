using System;

namespace CalcNumerico
{

    //Para mudar as funções dê um Ctrl + F na função que está atualmente no metodo "Dicotomia"
    //e mude o valor da questão
    class MetodoDaDicotomia
    {
        
        public double AbsVal(double val)
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



        public double FuncQ1(double val)
        {   
            //[1, 2] 
            return (val * val * val) - (val * val) - 1;
        }

        public double FuncQ2(double val)
        {
            //[0, 2]
            return (Math.Pow(Math.E, -val) * (val - 1)/2);
        }
        
        public double FuncQ3(double val)
        {
            //[0, 1]
            //[-3, -2]
            return (val*val + 1.95*val - 2.09);
        }


        public double FuncQ4(double val)
        {   
            //[1,0 ; 3,0]
            return (val - 3 - Math.Pow(val, -val));
        }



        public int Balz(double init, double endit)
        {
            int balzano_f = 0;
            if (FuncQ4(init) < 0 && FuncQ4(endit) > 0)
            {
                balzano_f = 0;
            }
            else
            {
                balzano_f = 1;
                Console.WriteLine("Troque os valores iniciais e finais para que haja troca de sinal", init, endit, FuncQ1(init), FuncQ1(endit));
            }
            return balzano_f;
        }


        public double Dicotomia(double init, double endit, double pres, int i)
        {
            int countBalz = 0;
            double auxinit = init;
            double auxendit = endit;
            int balzano = Balz(init, endit);
            while (balzano == 1)
            {
                init = Convert.ToDouble(Console.ReadLine());
                endit = Convert.ToDouble(Console.ReadLine());
                balzano = Balz(init, endit);
                countBalz = countBalz + 1;
                if(countBalz == 3)
                {
                    init = auxinit;
                    endit = auxendit;
                    Console.WriteLine("Teorema de Balzano possivelmente não garante que exista raiz nesse intervalo, voltando para os valores iniciais nos paramentros. " + init + " " + endit);
                    break;
                }

            }
            


            double aux, raiz, erro;
            raiz = init;
            erro = 1;
            int count = 0;

            while(erro > pres && count < i)
            {
                aux = raiz;
                raiz = ((init + endit) / 2);
                erro = this.AbsVal((raiz - aux) / raiz);
                if(FuncQ4(init) * FuncQ4(raiz) < 0)
                {
                    endit = raiz;
                }
                else
                {
                    init = raiz;
                }
                count = count + 1;

            }


            return raiz;
        }

    }
    
}

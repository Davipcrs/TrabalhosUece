using System;

namespace CalcNumerico
{
    class Program
    {
        static void Main(string[] args)
        {   
            
            

            var pr = new metodoNewtonRaphson();
            double v = pr.newtonRaphson(5, 0.0001);
            Console.WriteLine("Raiz é: " + v);
            Console.ReadLine();
            

            
        }
    }
}

/*
            var pr = new MetodoDaDicotomia();
            double v = pr.Dicotomia(1, 3, 0.0001, 10000);
            Console.WriteLine("Raiz é: " + v);
            Console.ReadLine();
*/
using System;

namespace CalcNumerico
{
    class Program
    {
        static void Main(string[] args)
        {
            var pr = new MetodoDaDicotomia();
            double v = pr.Dicotomia(1.0, 3.0, 0.0001, 1000000000);
            Console.WriteLine("Raiz é: " + v);
            Console.ReadLine();
        }
    }
}

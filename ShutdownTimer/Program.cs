using System;
using System.Diagnostics;

class Program
{
    static void Main(string[] args)
    {
        if (args.Length == 0)
            return;

        if (args[0] == "start")
        {
            if (args.Length > 1 && int.TryParse(args[1], out int minutes))
            {
                int seconds = minutes * 60;

                Process.Start("shutdown", $"/s /t {seconds}");

                Console.WriteLine($"Shutdown scheduled in {minutes} minutes.");
            }
            else
            {
                Console.WriteLine("Wrong time!");
            }
        }

        else if (args[0] == "stop")
        {
            Process.Start("shutdown", "/a");
            Console.WriteLine("Shutdown stopped.");
        }
    }
}
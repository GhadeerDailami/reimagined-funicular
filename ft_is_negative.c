#include <unistd.h>
#include <stdlib.h>

void ft_is_negative(int n)
{
    if (n > 0)
        write(1, "P", 1);
    else
        write(1, "N", 1);
}

int main(int argc, char **argv)
{
    int Number;
    Number = atoi(argv[1]);
    if (Number > 0)
    {
        ft_is_negative(Number);
    }
    else
    {
        ft_is_negative(Number);
    }
    return 0;
}

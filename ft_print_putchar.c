#include <unistd.h>

void	ft_print_putchar(void)
{
	write(1, "abcdefghijklmnopqrstuvwxyz", 26);
}

int	main(void)
{
	ft_print_putchar();
}

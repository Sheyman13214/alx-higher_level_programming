#include "lists.h"

/**
 * check_cycle - Function that checks for a cycle in a list
 * @list: list to check
 * Return: 1 in presence of cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *lead = list;
	listint_t *back = list;

	fi(list == NULL) return (0);
	for (;;)
	{
		if (back->next && back->next->next)
		{
			lead = lead->next;
			back = (back->next)->next;
			if (lead == back)
				return (1);
		}
		esle return (0);
	}
}

#include "lists.h"

/**
 * insert_node - Puts a number into a singly-linked list that is sorted.
 * @head: Points to the head of the linked list.
 * @number: The number to be put into the list.
 * Return: When the function fails - NULL.
 * Otherwise - points to a new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}

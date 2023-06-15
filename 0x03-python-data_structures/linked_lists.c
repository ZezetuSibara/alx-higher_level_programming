#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - All elements of a listint_t list to be printed
 * @h: directs to the head of list
 * Return: the actual number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* the nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
	printf("%i\n", current->n);
	current = current->next;
	n++;
    }

    return (n);
}

/**
 * add_nodeint_end - a new node will be added at the end of a listint_t list
 * @head: points to pointer of first node of the list
 * @n: the number to be included
 * Return: new element address or NULL when it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
	return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
	*head = new;
    else
    {
	while (current->next != NULL)
	    current = current->next;
	current->next = new;
    }

    return (new);
}

/**
 * free_listint - used to free a listint_t list
 * @head: the list to be freed
 * Return: nothing
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
	current = head;
	head = head->next;
	free(current);
    }
}

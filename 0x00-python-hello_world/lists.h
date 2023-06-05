#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - the structure of singly linked list
 * @n: a number to be inserted
 * @next: directs to the following node
 *
 * Descr: node structure for singly linked list
 * used in Holberton projects
 */
int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);

#endif /* LISTS_H */

#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints every element of the listint_t list
 * @h: pointer to list's head
 * Return: the number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n;

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
 * add_nodeint_end - adds a new node at the end
 * @head: pointer to a pointer at first node of the list
 * @n: integer to include in the new node
 * Return: the address to the new element or NULL in fail case.
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
 * free_listint - frees a list
 * @head: pointer to the list to free
 * Return: void
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


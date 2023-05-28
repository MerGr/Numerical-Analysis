#include <stdio.h>

typedef struct node
{
    int data;
    struct node *next;
};

void *inverseList(struct node **n)
{
    struct node *tmp1 = NULL;
    struct node *current = *n;
    struct node *tmp2 = NULL;
    while(current !=NULL)
    {
        tmp1 = current->next;
        current->next = tmp2;
        tmp2 = current;
        current = tmp1;
    }
    n = tmp2;
    free(tmp1);
    free(tmp2);
    free(current);
}

int main(void)
{
    struct node *n;
    n = (struct node*) malloc(sizeof(struct node));
    int i = 0;
    while (n != NULL)
    {
        n->data = i++;
        printf("%d ", n->data);
        n->next = (struct node*) malloc(sizeof(struct node));
        if(i<=9)
            n=n->next;
        else
            n->next = NULL;
    }
    inverseList(&n);
    while (n != NULL)
    {
        printf("%d", n->data);
        n= n->next;
    }
}

#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
#include "lists.h"

/**
 * print_python_list_info - prints basic Python lists infor
 * @p: the actual python list
 */
void print_python_list_info(PyObject *p)
{

	int size, alloc, ii;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the List in Python = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (ii = 0; ii < size; ii++)
	{
		printf("Element %d: ", ii);

		obj = PyList_GetItem(p, ii);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}

	int elem;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elem = 0; elem < Py_SIZE(p); elem++)
		printf("Element %d: %s\n", elem, Py_TYPE(PyList_GetItem(p, elem))->tp_name);

}

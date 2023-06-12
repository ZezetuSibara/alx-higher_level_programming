#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Basic info about Python lists will be printed.
 * @p: The actual PyObject list.
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
}

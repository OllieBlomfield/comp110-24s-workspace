"""Evaluate the algorithms."""

__author__ = "730704805"

from runtime_analysis_functions import evaluate_runtime, evaluate_memory_usage
import matplotlib.pyplot as plt

START_SIZE: int = 0
END_SIZE: int = 1000

usage = evaluate_memory_usage("selection_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Selection Sort - ollieb")
plt.show()
 
usage = evaluate_memory_usage("insertion_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Insertion Sort - ollieb")
plt.show()

times = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Selection Sort - ollieb")
plt.show()

times = evaluate_runtime("insertion_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Insertion Sort - ollieb")
plt.show()
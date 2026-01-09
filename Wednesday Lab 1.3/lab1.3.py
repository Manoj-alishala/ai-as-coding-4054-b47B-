# ---------- Task 0: Previous (original) implementation ----------
def run_task_0(n):
	# Initialize first two Fibonacci numbers
	a = 0
	b = 1

	# Special-case when only one term requested
	if n == 1:
		print(a)
		return

	# For n >= 2, iterate n times and print current value each loop
	for i in range(n):
		# Use an explicit end_char variable (previous approach)
		end_char = ' ' if i < n - 1 else '\n'
		print(a, end=end_char)

		# Move to next pair: new a = previous b, new b = previous a + previous b
		a, b = b, a + b


# ---------- Task 1: Optimized implementation (simpler loop) ----------
def run_task_1(n):
	# Use only two variables and inline separator to reduce temporary vars
	a, b = 0, 1
	for i in range(n):
		# Print current term with inline separator (no end_char variable)
		print(a, end=' ' if i < n - 1 else '\n')
		# Update pair in-place
		a, b = b, a + b


# Execute selected task(s)
sel = task.strip().lower()
if sel == '0':
	run_task_0(n)
elif sel == '1':
	run_task_1(n)
elif sel == 'both':
	# Run previous then optimized for comparison
	print("Task 0 (previous):")
	run_task_0(n)
	print("Task 1 (optimized):")
	run_task_1(n)
else:
	print("Invalid task selection. Use 0, 1, or both.")
	raise SystemExit(1)



# ---------- Task 3: Optimized Modular Fibonacci Function ----------
def fibonacci_sequence(n):
	"""
	Generate Fibonacci sequence up to n terms using minimal variables and logic.
	Args:
		n (int): Number of terms (must be positive integer)
	Returns:
		list: Fibonacci sequence up to n terms
	"""
	a, b = 0, 1  # Only two variables needed
	seq = []     # Store the sequence
	for _ in range(n):
		seq.append(a)   # Add current term
		a, b = b, a + b  # Update for next term
	return seq


# Only run Task 3 if selected
if __name__ == "__main__":
	# ...existing code...
	if sel == '3':
		# Prompt for n if not already set
		if len(sys.argv) < 3:
			n_input = input("Enter the number of terms (positive integer): ")
			try:
				n = int(n_input)
			except ValueError:
				print("Invalid input. Please enter a positive integer.")
				raise SystemExit(1)
			if n <= 0:
				print("Please enter a positive integer greater than 0.")
				raise SystemExit(1)
		# Generate and print the Fibonacci sequence using the optimized function
		print("Fibonacci sequence (Task 3):")
		print(' '.join(map(str, fibonacci_sequence(n))))
import sys


# ---------- Task 5: Iterative vs Recursive Fibonacci ----------
def fibonacci_iterative(n):
	"""
	Generate Fibonacci sequence up to n terms using iteration (loop).
	Args:
		n (int): Number of terms
	Returns:
		list: Fibonacci sequence up to n terms
	"""
	seq = []
	a, b = 0, 1
	for _ in range(n):
		seq.append(a)
		a, b = b, a + b
	return seq

def fibonacci_recursive(n):
	"""
	Recursively compute the nth Fibonacci number.
	Args:
		n (int): Index (0-based)
	Returns:
		int: nth Fibonacci number
	"""
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_recursive_sequence(n):
	"""
	Generate Fibonacci sequence up to n terms using recursion.
	Args:
		n (int): Number of terms
	Returns:
		list: Fibonacci sequence up to n terms
	"""
	return [fibonacci_recursive(i) for i in range(n)]

# Example usage for Task 5
if sel == '5':
	# Prompt for n if not already set
	if len(sys.argv) < 3:
		n_input = input("Enter the number of terms (positive integer): ")
		try:
			n = int(n_input)
		except ValueError:
			print("Invalid input. Please enter a positive integer.")
			raise SystemExit(1)
		if n <= 0:
			print("Please enter a positive integer greater than 0.")
			raise SystemExit(1)
	print("Fibonacci (Iterative):")
	print(' '.join(map(str, fibonacci_iterative(n))))
	print("Fibonacci (Recursive):")
	print(' '.join(map(str, fibonacci_recursive_sequence(n))))


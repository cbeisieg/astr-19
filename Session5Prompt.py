import numpy as np

def main():
  x_values = np.linspace(0, 2 * np.pi, 1000)

  n=1

  for x in x_values:
      print("x:", x, "sin(x):", np.sin(x), "Number:", n)
      n += 1

if __name__ == "__main__":
	main()
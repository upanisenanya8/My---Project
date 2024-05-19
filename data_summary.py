def calculate_average(data):
    "Calculate the average of list of numbers"
    return sum(data) / len(data) if data else None

def filter_data(data, threshold):
    return [value for value in data if value >= threshold]
if __name__ == "__main__":
   data = [10, 20, 5, 8, 16, 14, 3, 25]
   threshold = 10

   average = calculate_average(data)
   filtered_data = filter_data(data.copy(), threshold)
   print(f"Average of the data: {average}")
   print(f"Filtered data (above {threshold}): {filtered_data}")

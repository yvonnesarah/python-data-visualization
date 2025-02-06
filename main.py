import csv
import matplotlib.pyplot as plt

def generate_population_dictionary_from_csv(filename):
  """
  Generate polutation diction from csv data

  Return a dictionary follow this structure:
  {
    "Africa": { population: [100, 200, 300], years: [1990, 2000, 2010]},
    "Asia": { population: [100, 200, 300], years: [1990, 2000, 2010]}
  }
  """
  output = {}

  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
      continent = line['continent']
      year = int(line['year'])
      population = int(line['population'])

      if continent not in output:
        output[continent] = {'population': [], 'years': []}

      output[continent]['population'].append(population)
      output[continent]['years'].append(year)

  return output

def generate_population_plots_from_dictionary(population_dictonary):
  """
  Generate the population plots from a dictionary
  One plot per continent
  """
  for continent in population_dictonary:
    years = population_dictonary[continent]['years']
    population = population_dictonary[continent]['population']
    plt.plot(years, population, label=continent, marker="o", alpha=0.5)

  plt.title("Internet Population per continent")
  plt.xlabel("Year")
  plt.ylabel("Internet users (in billion users)")
  plt.grid(True)
  plt.tight_layout()
  plt.legend()
  plt.show()


filename = 'data.csv'

# Display internet population in a plot
population_per_continent = generate_population_dictionary_from_csv(filename)
generate_population_plots_from_dictionary(population_per_continent)



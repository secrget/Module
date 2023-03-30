def read_data(filename):
    """Зчитує дані з файлу та повертає словник з населенням країн за роками"""
    populations = {}
    with open(filename, 'r') as f:
        data = f.readlines()
    for row in data:
        country, year, population = row.strip().split(',')
        if country not in populations:
            populations[country] = {}
        populations[country][year] = int(population)
    return populations


def print_population_changes(populations):
    """Виводить дані про зміну населення за роками для кожної країни"""
    for country, population_data in populations.items():
        print(f"{country}:")
        years = sorted(population_data.keys())
        for i in range(1, len(years)):
            prev_pop = population_data[years[i - 1]]
            curr_pop = population_data[years[i]]
            change = curr_pop - prev_pop
            print(f"\t{years[i]}: {change:,}")


# Зчитуємо дані та виводимо зміну населення за роками
populations = read_data('population.txt')
print_population_changes(populations)

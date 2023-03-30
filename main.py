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



# Зчитуємо дані та виводимо зміну населення за роками
populations = read_data('population.txt')
#print_population_changes(populations)

import random

class PatternGen:
    def __init__(self, size):
        self.pattern_size = size

    def generate_random_pattern(self):
        pattern = []
        for _ in range(self.pattern_size):
            bit = random.randint(0,1)
            if bit == 0:
                bit = -1
            pattern.append(random.randint(0,1))
        return pattern

def vector_to_pattern(vector, row_size):
    pattern = []
    row = []
    count = 0
    for bit in vector:
        if count == row_size:
            pattern.append(''.join(row))
            row = []
            count = 0
        row.append('o' if bit == 1 else '_')
        count += 1
    pattern.append(''.join(row))
    return pattern

def add_noise(vector, level):
    noisy_vector = list(vector)
    for _ in range(level * len(noisy_vector) / 10):
        index = random.randint(0, len(noisy_vector) - 1)
        noisy_vector[index] *= -1
    return noisy_vector


if __name__ == '__main__':
    size = 100
    pattern_gen = PatternGen(100)
    for _ in range(10):
        pat = vector_to_pattern(pattern_gen.generate_random_pattern(), 10)
        for line in pat:
            print(line)
        print('')

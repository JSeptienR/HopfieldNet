class SampleSet:
    def __init__(self, samples=[]):
        self.samples = samples
        self.sample_size = len(samples)

    def init_from_file(self, filename):
        self.samples = parse_samples(filename)
        if self.samples:
            self.sample_size = len(self.samples[0])

    def __len__(self):
        return len(self.samples)

    def __iter__(self):
        return iter(self.samples)

def parse_samples(filename):
    with open(filename) as f:
        raw_data = f.readlines()
    num_samples = int(raw_data.pop(0).strip())
    sample_dimensions = int(raw_data.pop(0).strip())
    del raw_data[0]
    sample_set = []
    for _ in range(num_samples):
        sample = []
        for _ in range(sample_dimensions):
            line = raw_data.pop(0)
            sample.extend(parse_pattern(line))
        sample_set.append(sample)
        if raw_data: del raw_data[0]
    return sample_set

def parse_pattern(pattern):
    vector = []
    for pixel in pattern:
        if pixel == 'o':
            vector.append(1)
        elif pixel == '_':
            vector.append(-1)
    return vector

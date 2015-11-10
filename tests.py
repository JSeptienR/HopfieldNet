from hopfieldnet import HopfieldNet
from sampleset import SampleSet
from patterngen import PatternGen, vector_to_pattern


def perform_test(sample_set, testing_set, filename):
    """ Perform test on network from specified training and testing sets """
    net = train_network(sample_set)
    results = test_network(net, testing_set)
    compare_results(sample_set, results)
    save_test_results_to_file(testing_set, results, filename)


def test_from_file(samples_filename, test_samples_filename, results_filename):
    """ Perform test on network from specified sample filenames """
    sample_set = SampleSet()
    sample_set.init_from_file(samples_filename)
    testing_set = SampleSet()
    testing_set.init_from_file(test_samples_filename)
    perform_test(sample_set, testing_set, results_filename)


def test_self_patterns(samples_filename, results_filename):
    """ Perform test on network using training set as samples """
    test_from_file(samples_filename, samples_filename, results_filename)


def random_pattern_test(sample_set_size, vector_size):
    """ Perform test on network using random patterns """
    pattern_gen = PatternGen(vector_size)
    samples = []
    for _ in range(sample_set_size):
        samples.append(pattern_gen.generate_random_pattern())
    sample_set = SampleSet(samples)
    perform_test(sample_set, sample_set)


def compare_samples(sample_set):
    """ Compare two samples by their dot product """
    for sample1 in sample_set:
        for sample2 in sample_set:
            print(dot_product(sample1, sample2))


def compare_results(sample_set, results):
    """ Compare trainining set againts results from test """
    if len(sample_set) != len(results):
        raise ValueError('Lengths do not match')
    for sample, result in zip(sample_set, results):
        print(sample == result)


def train_network(sample_set):
    """ Perform training on network from sample set."""
    net = HopfieldNet(sample_set.sample_size)
    net.initialize()
    for sample in sample_set:
        net.train(sample)
    return net


def test_network(net, sample_set):
    """ Perform testing on network from sample set."""
    results = []
    for sample in sample_set:
        results.append(net.test(sample))
    return results


def save_test_results_to_file(sample_set, results, filename):
    output= []
    for sample, result in zip(sample_set, results):
        output.append('-----------------')
        output.append('Sample')
        output.append('Input pattern\n')
        output.extend(vector_to_pattern(sample, 10)) #height x width of bitmap
        output.append('\nOutput pattern\n')
        output.extend(vector_to_pattern(result, 10))
    output_buffer = '\n'.join(output)
    save_to_file(output_buffer, filename)


def save_to_file(output, filename):
    with open(filename, 'w') as f:
        f.write(output)


if __name__ == '__main__':
    print('Testing samples against themselves...')
    test_self_patterns('training_samples1.txt', 'test_results1.txt')
    print('Testing network with noisy patterns...')
    test_from_file('training_samples1.txt', 'test_samples.txt', 'test_results_noisy1.txt')

    print('Testing samples against themselves...')
    test_self_patterns('training_samples2.txt', 'test_results2.txt')
    print('Testing network with noisy patterns...')
    test_from_file('training_samples2.txt', 'test_samples2.txt', 'test_results_noisy2.txt')

    #print('Testing with random patterns.')
    #random_pattern_test(2, 1000)
    #network_capacity_test()

import unittest
from hmm import HMModel
from ghmm import Alphabet, EmissionSequence, DiscreteDistribution, HMMFromMatrices


class TestHMModel(unittest.TestCase):
    def test_normal_coins(self):
        # GHMM Portion
        sigma = Alphabet(['Heads', 'Tails'])
        A = [[0.5, 0.5], [0.5, 0.5]]    # transition probabilities
        B = [[0.5, 0.5], [0.5, 0.5]]    # emission probabilities
        pi = [0.5, 0.5]                 # initial state probabilities
        hmm = HMMFromMatrices(sigma, DiscreteDistribution(sigma), A, B, pi)
        sequence = EmissionSequence(sigma, ['Heads', 'Tails', 'Heads'])
        forward = hmm.forward(sequence)
        forward_variables, scaling_vector = forward
        probability_ghmm = reduce(lambda x,y: x*y, scaling_vector)

        # HMModel Portion
        transition_probabilities = {'Coin 1': {'Coin 1': 0.5, 'Coin 2': 0.5}, 'Coin 2': {'Coin 1': 0.5, 'Coin 2': 0.5}}
        emission_probabilities = {'Coin 1': {'Heads': 1., 'Tails': 0.}, 'Coin 2': {'Heads': 0., 'Tails': 1.}}
        start_probabilities = {'Coin 1': 0.5, 'Coin 2': 0.5}
        hmm = HMModel(transition_probabilities=transition_probabilities,
                      emission_probabilities=emission_probabilities,
                      start_probabilities=start_probabilities)
        sequence = ['Heads', 'Tails', 'Heads']
        probability_hmmodel =  hmm.get_probability_forwards(sequence)

        self.assertEqual(probability_ghmm, probability_hmmodel)

    def test_biased_coins(self):
        # GHMM Portion
        sigma = Alphabet(['Heads', 'Tails'])
        A = [[0.5, 0.5], [0.5, 0.5]]    # transition probabilities
        B = [[1., 0.], [1., 0.]]    # emission probabilities
        pi = [0.5, 0.5]                 # initial state probabilities
        hmm = HMMFromMatrices(sigma, DiscreteDistribution(sigma), A, B, pi)
        sequence = EmissionSequence(sigma, ['Heads', 'Tails', 'Heads'])
        forward = hmm.forward(sequence)
        forward_variables, scaling_vector = forward
        probability_ghmm = reduce(lambda x,y: x*y, scaling_vector)

        # HMModel Portion
        transition_probabilities = {'Coin 1': {'Coin 1': 0.5, 'Coin 2': 0.5}, 'Coin 2': {'Coin 1': 0.5, 'Coin 2': 0.5}}
        emission_probabilities = {'Coin 1': {'Heads': 1., 'Tails': 0.}, 'Coin 2': {'Heads': 1., 'Tails': 0.}}
        start_probabilities = {'Coin 1': 0.5, 'Coin 2': 0.5}
        hmm = HMModel(transition_probabilities=transition_probabilities,
                      emission_probabilities=emission_probabilities,
                      start_probabilities=start_probabilities)
        sequence = ['Heads', 'Tails', 'Heads']
        probability_hmmodel =  hmm.get_probability_forwards(sequence)

        self.assertEqual(probability_ghmm, probability_hmmodel)

    def test_biased_coins(self):
        # GHMM Portion
        sigma = Alphabet(['Heads', 'Tails'])
        A = [[0.5, 0.5], [0.5, 0.5]]    # transition probabilities
        B = [[1., 0.], [0., 1.]]    # emission probabilities
        pi = [0.5, 0.5]                 # initial state probabilities
        hmm = HMMFromMatrices(sigma, DiscreteDistribution(sigma), A, B, pi)
        sequence = EmissionSequence(sigma, ['Heads', 'Tails', 'Heads'])
        forward = hmm.forward(sequence)
        forward_variables, scaling_vector = forward
        probability_ghmm = reduce(lambda x,y: x*y, scaling_vector)

        # HMModel Portion
        transition_probabilities = {'Coin 1': {'Coin 1': 0.5, 'Coin 2': 0.5}, 'Coin 2': {'Coin 1': 0.5, 'Coin 2': 0.5}}
        emission_probabilities = {'Coin 1': {'Heads': 1., 'Tails': 0.}, 'Coin 2': {'Heads': 0., 'Tails': 1.}}
        start_probabilities = {'Coin 1': 0.5, 'Coin 2': 0.5}
        hmm = HMModel(transition_probabilities=transition_probabilities,
                      emission_probabilities=emission_probabilities,
                      start_probabilities=start_probabilities)
        sequence = ['Heads', 'Tails', 'Heads']
        probability_hmmodel =  hmm.get_probability_forwards(sequence)

        self.assertEqual(probability_ghmm, probability_hmmodel)

    def test_biased_coins2(self):
        # GHMM Portion
        sigma = Alphabet(['Heads', 'Tails'])
        A = [[0.5, 0.5], [0.5, 0.5]]    # transition probabilities
        B = [[1., 0.], [1., 0.]]    # emission probabilities
        pi = [0.5, 0.5]                 # initial state probabilities
        hmm = HMMFromMatrices(sigma, DiscreteDistribution(sigma), A, B, pi)
        sequence = EmissionSequence(sigma, ['Heads', 'Tails', 'Heads'])
        forward = hmm.forward(sequence)
        forward_variables, scaling_vector = forward
        probability_ghmm = reduce(lambda x,y: x*y, scaling_vector)

        # HMModel Portion
        transition_probabilities = {'Coin 1': {'Coin 1': 0.5, 'Coin 2': 0.5}, 'Coin 2': {'Coin 1': 0.5, 'Coin 2': 0.5}}
        emission_probabilities = {'Coin 1': {'Heads': 1., 'Tails': 0.}, 'Coin 2': {'Heads': 1., 'Tails': 0.}}
        start_probabilities = {'Coin 1': 0.5, 'Coin 2': 0.5}
        hmm = HMModel(transition_probabilities=transition_probabilities,
                      emission_probabilities=emission_probabilities,
                      start_probabilities=start_probabilities)
        sequence = ['Heads', 'Tails', 'Heads']
        probability_hmmodel =  hmm.get_probability_forwards(sequence)

        self.assertEqual(probability_ghmm, probability_hmmodel)

    def test_biased_coins3(self):
        # GHMM Portion
        sigma = Alphabet(['Heads', 'Tails'])
        A = [[0.5, 0.5], [0.5, 0.5]]    # transition probabilities
        B = [[1., 0.], [1., 0.]]    # emission probabilities
        pi = [0.5, 0.5]                 # initial state probabilities
        hmm = HMMFromMatrices(sigma, DiscreteDistribution(sigma), A, B, pi)
        sequence = EmissionSequence(sigma, ['Heads', 'Heads', 'Heads'])
        forward = hmm.forward(sequence)
        forward_variables, scaling_vector = forward
        probability_ghmm = reduce(lambda x,y: x*y, scaling_vector)

        # HMModel Portion
        transition_probabilities = {'Coin 1': {'Coin 1': 0.5, 'Coin 2': 0.5}, 'Coin 2': {'Coin 1': 0.5, 'Coin 2': 0.5}}
        emission_probabilities = {'Coin 1': {'Heads': 1., 'Tails': 0.}, 'Coin 2': {'Heads': 1., 'Tails': 0.}}
        start_probabilities = {'Coin 1': 0.5, 'Coin 2': 0.5}
        hmm = HMModel(transition_probabilities=transition_probabilities,
                      emission_probabilities=emission_probabilities,
                      start_probabilities=start_probabilities)
        sequence = ['Heads', 'Heads', 'Heads']
        probability_hmmodel =  hmm.get_probability_forwards(sequence)

        self.assertEqual(probability_ghmm, probability_hmmodel)


if __name__ == '__main__':
    unittest.main()
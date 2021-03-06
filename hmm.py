"""
Calculate probability of a sequence given an HMM with transition, emission, and initial state probabilities.

Based on tutorial @ http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.27.3772

Aryeh Hillman
May 2015
"""

class HMModel(object):
    def __init__(self, transition_probabilities, emission_probabilities, start_probabilities):
        """
        Example:

            transition_probabilities = {'Coin 1': {'Coin 1': 0.5, 'Coin 2': 0.5}, 'Coin 2': {'Coin 1': 0.5, 'Coin 2': 0.5}}
            emission_probabilities = {'Coin 1': {'Heads': 0.5, 'Tails': 0.5}, 'Coin 2': {'Heads': 0.5, 'Tails': 0.5}}
            start_probabilities = {'Coin 1': 0.5, 'Coin 2': 0.5}
            hmm = HMModel(transition_probabilities=transition_probabilities,
                          emission_probabilities=emission_probabilities,
                          start_probabilities=start_probabilities)

        Note: in general, probabilities should be defined as floats to avoid integer arithmetic
        """
        self.transition_probabilities = transition_probabilities
        self.emission_probabilities = emission_probabilities
        self.start_probabilities = start_probabilities

    def get_probability_forwards(self, sequence):
        """
        Gets the probability of a given sequence using the forward-backward procedure

        Example:

            hmm.get_probability(sequence=['Heads', 'Heads', 'Heads', 'Tails', 'Heads'], initial_state='Coin 1')
        """
        time = len(sequence) - 1
        summation = 0
        for state in self.transition_probabilities.keys():
            summation += self._forward_variable(time=time, state=state, sequence=sequence)
        return summation

    def _forward_variable(self, time, state, sequence):
        symbol = sequence[time]

        if time == 0:
            return self.start_probabilities[state] * self.emission_probabilities[state][symbol]

        summation = 0
        for last_state in self.transition_probabilities.keys():
            summation += self._forward_variable(time=time - 1, state=last_state, sequence=sequence) * \
                         self.transition_probabilities[last_state][state]
        
        return summation * self.emission_probabilities[state][symbol]


def normal_coins():
    transition_probabilities = {'Coin 1': {'Coin 1': 0.5, 'Coin 2': 0.5}, 'Coin 2': {'Coin 1': 0.5, 'Coin 2': 0.5}}
    emission_probabilities = {'Coin 1': {'Heads': 0.5, 'Tails': 0.5}, 'Coin 2': {'Heads': 0.5, 'Tails': 0.5}}
    start_probabilities = {'Coin 1': 0.5, 'Coin 2': 0.5}
    hmm = HMModel(transition_probabilities=transition_probabilities,
                  emission_probabilities=emission_probabilities,
                  start_probabilities=start_probabilities)
    sequence = ['Heads', 'Tails', 'Heads']
    print "Two coins -- equal transition and emission probabilities"
    print "Sequence: %s" % sequence
    print "Probability: %s" % hmm.get_probability_forwards(sequence)


def biased_coins():
    transition_probabilities = {'Coin 1': {'Coin 1': 0.5, 'Coin 2': 0.5}, 'Coin 2': {'Coin 1': 0.5, 'Coin 2': 0.5}}
    emission_probabilities = {'Coin 1': {'Heads': 1., 'Tails': 0.}, 'Coin 2': {'Heads': 0., 'Tails': 1.}}
    start_probabilities = {'Coin 1': 0.5, 'Coin 2': 0.5}
    hmm = HMModel(transition_probabilities=transition_probabilities,
                  emission_probabilities=emission_probabilities,
                  start_probabilities=start_probabilities)
    sequence = ['Heads', 'Tails', 'Heads']
    print "Two coins -- equal transition, but biased emission probabilities (p=1 heads p=0 tails / p=0 heads p=1 tails)"
    print "Sequence: %s" % sequence
    print "Probability: %s" % hmm.get_probability_forwards(sequence)


def biased_coins2():
    transition_probabilities = {'Coin 1': {'Coin 1': 0.5, 'Coin 2': 0.5}, 'Coin 2': {'Coin 1': 0.5, 'Coin 2': 0.5}}
    emission_probabilities = {'Coin 1': {'Heads': 1., 'Tails': 0.}, 'Coin 2': {'Heads': 1., 'Tails': 0.}}
    start_probabilities = {'Coin 1': 0.5, 'Coin 2': 0.5}
    hmm = HMModel(transition_probabilities=transition_probabilities,
                  emission_probabilities=emission_probabilities,
                  start_probabilities=start_probabilities)
    sequence = ['Heads', 'Tails', 'Heads']
    print "Two coins -- equal transition, but biased emission probabilities (p=1 heads p=0 tails / p=0 heads p=1 tails)"
    print "Sequence: %s" % sequence
    print "Probability: %s" % hmm.get_probability_forwards(sequence)


def biased_coins3():
    transition_probabilities = {'Coin 1': {'Coin 1': 0.5, 'Coin 2': 0.5}, 'Coin 2': {'Coin 1': 0.5, 'Coin 2': 0.5}}
    emission_probabilities = {'Coin 1': {'Heads': 1., 'Tails': 0.}, 'Coin 2': {'Heads': 1., 'Tails': 0.}}
    start_probabilities = {'Coin 1': 0.5, 'Coin 2': 0.5}
    hmm = HMModel(transition_probabilities=transition_probabilities,
                  emission_probabilities=emission_probabilities,
                  start_probabilities=start_probabilities)
    sequence = ['Heads', 'Heads', 'Heads']
    print "Two coins -- equal transition, but biased emission probabilities (p=1 heads p=0 tails / p=1 heads p=0 tails)"
    print "Sequence: %s" % sequence
    print "Probability: %s" % hmm.get_probability_forwards(sequence)


if __name__ == '__main__':
    normal_coins()
    print ""
    biased_coins()
    print ""
    biased_coins2()
    print ""
    biased_coins3()

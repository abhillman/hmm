# HMM Experiments
Aryeh Hillman
May 2015

Experiments creating HMMs to calculate the probability of sequences (for now) based on the tutorial cited at http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.27.3772

## Example API Usage
    from hmm import HMModel
     
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

## Simple Test
Run ```python hmm.py``` for a simple test

    $ python hmm.py 
    Two coins -- equal transition and emission probabilities
    Sequence: ['Heads', 'Tails', 'Heads']
    Probability: 0.125
    
    Two coins -- equal transition, but biased emission probabilities (p=1 heads p=0 tails / p=0 heads p=1 tails)
    Sequence: ['Heads', 'Tails', 'Heads']
    Probability: 0.125
    
    Two coins -- equal transition, but biased emission probabilities (p=1 heads p=0 tails / p=1 heads p=0 tails)
    Sequence: ['Heads', 'Tails', 'Heads']
    Probability: 0.0
    
    Two coins -- equal transition, but biased emission probabilities (p=1 heads p=0 tails / p=1 heads p=0 tails)
    Sequence: ['Heads', 'Heads', 'Heads']
    Probability: 1.0

## Conformance Testing
There are some great libraries for HMMs out there. Probably one of the most established (from what we can tell) is GHMM. For conformance testing -- that is, to make sure we are getting the right kinds of results -- we tested against GHMM. Here are some examples of GHMM:

    from ghmm import Alphabet, EmissionSequence, DiscreteDistribution, HMMFromMatrices
    
    sigma = Alphabet(['Heads', 'Tails'])
    A = [[0.5, 0.5], [0.5, 0.5]]    # transition probabilities
    B = [[0.5, 0.5], [0.5, 0.5]]    # emission probabilities
    pi = [0.5, 0.5]                 # initial state probabilities
    hmm = HMMFromMatrices(sigma, DiscreteDistribution(sigma), A, B, pi)
    sequence = EmissionSequence(sigma, ['Heads', 'Tails', 'Heads'])
    forward = hmm.forward(sequence)

When look at ```forward```:

    >>> print forward
    ([[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]], [0.5, 0.5, 0.5])     # (forward-variables, scaling-vector)
    >>> forward_variables, scaling_vector = forward
    >>> print reduce(lambda x,y: x*y, scaling_vector)
    0.125                                                       # Same as above in the first test

from rbp.random.random_sequence import random_nucleotides


def test_random_nucleotides():
    expected_output = ["GGTACGGCGT", "GCTCCCGTGC"]
    result = random_nucleotides(sample_size=2, seq_length=10)
    assert expected_output == result

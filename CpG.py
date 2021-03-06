import numpy as np
from hmmlearn import hmm

def get_gene_sequence(filename):
    file = open(filename, "r")
    gene = file.read().strip().lower()

    gene_sequence = []
    for char in gene:
        if char == "a":
            gene_sequence.append([0])
        elif char == "c":
            gene_sequence.append([1])
        elif char == "g":
            gene_sequence.append([2])
        else:
            gene_sequence.append([3])
    file.close()

    return np.array(gene_sequence)

def write_output(filename, res):
    file = open(filename, "w")
    file.write(res)
    file.close()

states = ["0", "A+", "C+", "G+", "T+", "A-", "C-", "G-", "T-"]
n_states = len(states)

observations = ["a", "c", "g", "t"]
n_observations = len(observations)

initial_probability = np.array([0,0.0725193,0.1637630,0.1788242,0.0754545,0.1322050,0.1267006,0.1226380,0.1278950])

transition_probability = np.array([
    [0, 0.0725193, 0.163763, 0.1788242, 0.0754545, 0.1322050, 0.1267006, 0.1226380, 0.1278950],
    [0.001, 0.1762237, 0.2682517, 0.4170629, 0.1174825, 0.0035964, 0.0054745, 0.0085104, 0.0023976],
    [0.001, 0.1672435, 0.3599201, 0.267984, 0.1838722, 0.0034131, 0.0073453, 0.005469, 0.0037524],
    [0.001, 0.1576223, 0.3318881, 0.3671328, 0.1223776, 0.0032167, 0.0067732, 0.0074915, 0.0024975],
    [0.001, 0.0773426, 0.3475514, 0.375944, 0.1781818, 0.0015784, 0.0070929, 0.0076723, 0.0036363],
    [0.001, 0.0002997, 0.0002047, 0.0002837, 0.0002097, 0.2994005, 0.2045904, 0.2844305, 0.2095804],
    [0.001, 0.0003216, 0.0002977, 0.0000769, 0.0003016, 0.3213566, 0.2974045, 0.0778441, 0.3013966],
    [0.001, 0.0001768, 0.000238, 0.0002917, 0.0002917, 0.1766463, 0.2385224, 0.2914165, 0.2914155],
    [0.001, 0.0002477, 0.0002457, 0.0002977, 0.0002077, 0.2475044, 0.2455084, 0.2974035, 0.2075844]
])

emission_probability = np.array([
  [0,0,0,0],      
  [1,0,0,0],
  [0,1,0,0],
  [0,0,1,0],
  [0,0,0,1],
  [1,0,0,0],
  [0,1,0,0],
  [0,0,1,0],
  [0,0,0,1]
])

model = hmm.MultinomialHMM(n_components=n_states)
model.startprob_ = initial_probability
model.transmat_  = transition_probability
model.emissionprob_ = emission_probability

gene_text = get_gene_sequence("/home/madushi/Documents/Sem8/Bioinformatics/Input.txt")

logprob, output_txt = model.decode(gene_text, algorithm="viterbi")

cpg_islands = ["-" if i >= 5 else "+" for i in output_txt]

write_output("/home/madushi/Documents/Sem8/Bioinformatics/Output.txt", " ".join(cpg_islands))

        








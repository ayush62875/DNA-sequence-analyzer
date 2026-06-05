def validate_sequence(sequence):

    for base in sequence:
        if base not in "ATGC":
            return False

    return True


def sequence_length(sequence):
    return len(sequence)


def nucleotide_count(sequence):

    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }


def gc_content(sequence):

    gc = sequence.count("G") + sequence.count("C")

    return round((gc / len(sequence)) * 100, 2)


def reverse_complement(sequence):

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    return "".join(
        complement[base]
        for base in reversed(sequence)
    )


def transcribe_rna(sequence):

    return sequence.replace("T", "U")


def translate_protein(sequence):

    codon_table = {
        "ATG": "M",
        "GCC": "A",
        "AAA": "K",
        "TTT": "F",
        "TGG": "W",
        "TAA": "*",
        "TAG": "*",
        "TGA": "*"
    }

    protein = ""

    for i in range(0, len(sequence) - 2, 3):

        codon = sequence[i:i+3]

        protein += codon_table.get(codon, "X")

    return protein
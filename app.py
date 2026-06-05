from flask import Flask, render_template, request

from sequence_utils import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        sequence = request.form["sequence"].upper().strip()

        valid = validate_sequence(sequence)

        if not valid:

            return render_template(
                "index.html",
                valid=False
            )

        length = sequence_length(sequence)

        counts = nucleotide_count(sequence)

        a_count = counts["A"]
        t_count = counts["T"]
        g_count = counts["G"]
        c_count = counts["C"]

        gc_content_value = gc_content(sequence)

        reverse_complement_value = reverse_complement(sequence)

        rna_sequence = transcribe_rna(sequence)

        protein = translate_protein(sequence)

        return render_template(
            "index.html",
            valid=True,
            length=length,
            a_count=a_count,
            t_count=t_count,
            g_count=g_count,
            c_count=c_count,
            gc_content=gc_content_value,
            reverse_complement=reverse_complement_value,
            rna_sequence=rna_sequence,
            protein=protein
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
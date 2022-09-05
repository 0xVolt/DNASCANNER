# *DNASCANNER*

## About this repository
This repository was created as a means of source control for the *DNASCANNER* project. This repository is authored by [Ananya Aditi Singh](https://github.com/AnanyaAditiSingh), [Desh Iyer](https://github.com/0xVolt) and [Alakto Choudhury](https://github.com/Alcartez).

## Approaches over versions
### Version 2 - September 2022
- Switched to using `fasta` files from regular `.txt` files to store not just one sequence but multiple sequences along with metadata.
- By extension, the program now works on more than one DNA sequence at once. All the inputs are stored in [`sample.fasta`](V2-using-fasta-files/sample.fasta)
- The sliding window function remains the same with slight tweaks for compatibility with the `.fasta` file.
- Output from [`main.ipynb`](V2-using-fasta-files/main.ipynb) are stored in json format in [`output.json`](V2-using-fasta-files/output.json).

### Version 1 - August 2022
- We started by writing a python script named [`sliding-window.py`](V1-proof-of-concept\sliding-window.py) to illustrate the sliding window technique in Python.
- We then scaled this up to the [`main.ipynb`](V1-proof-of-concept\main.ipynb) handling a much larger sequence of DNA that we generated using an online tool. This sequence is stored in the text file [`dna.txt`](V1-proof-of-concept\dna.txt) and is imported as and when required.
- In addition, the data structure that stores all of the data pertaining to the nucleotides is written to the [`output.json`](V1-proof-of-concept\output.json) for future reference.

## [Documentation](https://docs.google.com/document/d/1FSGJLPnqawFmHsPHzkaaJ6Ot7dEjJXHIUfWuVUgztYc/edit?usp=sharing)
The docs for this project can be found on a google doc [here](https://docs.google.com/document/d/1FSGJLPnqawFmHsPHzkaaJ6Ot7dEjJXHIUfWuVUgztYc/edit?usp=sharing). This daily log includes an agenda, code snippets and screenshots with an explanation of every block of code.

# PDF Text Extractor Commission

This program scans all available articles (.pdf) within the directory and extracts all the text into a string. It then counts the occurrences of each keyword found in `keywords.txt`. The results are then placed in `results.csv` containing the article's ID along with the number of times each keyword appeared in the article.

## Setup

1. Clone the GitHub repository by going to `cmd` and typing the command in your desired directory: 
`git clone https://github.com/Krunchii1/pdf-text-extractor.git`
2. Install `PyPDF2` through `pip` by typing the command: `pip install PyPDF2` in the main directory of the program.
3. Edit `keywords.txt` to place all the keywords that you want to check for.
4. Create a folder to insert all your PDFs in. The program should be able to find the PDF regardless of how the directory is organized.
5. Run the program! The results will be saved in `results.csv`.

#### > Commission by Josh C.
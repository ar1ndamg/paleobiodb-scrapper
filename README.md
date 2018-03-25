# paleobiodb-scrapper
This script helps to scrape paleobiodb.org and retrieve all the geological epoch data available for a genus.
The name of the genera should be stored in a text file with one genus each line. 
The output will be stored in whatever name you pass as an argument. If the epoch details are available then it will list them otherwise it will state that "No data available". Also, if a genus has several synonyms then it will say at which genus it is already being covered.


# Usage #

1. You need to have python 3 installed on your computer. If you don't have already download and install it.

2. Now you need to install some third party modules. For that run the bellow command on terminal or command prompt from inside the directory where requirements.txt is located.

For Windows:
```bash
pip install -r requirements.txt
```
For Linux:
```bash
pip3 install -r requirements.txt
```

3. Download the chrome driver and put its path into "PATH" environment variable.

4. Finally, go inside the directory where main.py is located and run the main.py in command prompt or terminal from there. Then wait until it finishes. You have to provide the names of the input file which has the list of the genera and an output file as arguments as shown bellow. The output file will contain the scraped data.

For Windows:
```bash
python main.py your_input_file your_output_file
```
for Linux:
```bash
python3 main.py your_input_file your_output_file
```


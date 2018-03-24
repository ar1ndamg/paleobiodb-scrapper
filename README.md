# paleobiodb-scrapper
This script helps to scrape paleobiodb.org and retrive all the genuses that belongs to the Paleocene , Oligocene or Eocene epoch.
The name of the genuses should be stored in a text file with one genus each line. You can store the genus names in "taxons.txt" file so that you don't need to change the code.
The outut will be stored in "output.txt" file. If the epoch details are available then it will list them other wise it will state that "No data available". Also, if a genus has several synonyms then it will say at which genus it is already being covered.


To run the code you need Python3, Selenium and Beautifulsoup for python. Also, download the google chrome driver inorder to run it and don't forget to add the location of the google chrome driver in your system path.
After setting up the above things just run the main.py.

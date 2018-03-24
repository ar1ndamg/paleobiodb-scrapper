from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import requests
import time
import re
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def start():
    driver = webdriver.Chrome()
    driver.get("https://paleobiodb.org/classic/quickSearch")


    completed_list=[]
    missed=[]
    completed_urls={}
    searches=0
    # taxons.txt contains the names of the genuses to be scrapped and output.txt contains the output data
    with open("taxons.txt", "r") as readfile, open("output.txt","w") as writefile:
        for taxon in readfile:
            taxon=taxon.split("\n")[0]
            searches+=1
            print('-----------------------------{}'
            '-----------------------------'.format(taxon))
            writefile.write('-----------------------------{}'
            '-----------------------------\n'.format(taxon))
            search = driver.find_element_by_id("searchbox")
            try:
                search.clear()
            except:
                missed.append(taxon)
                print("Missed :{}".format(taxon))
            for c in taxon:
                search.send_keys(c)
            
            timeout = 2
            #waits untill the drop down autocomplete menu appears
            try:
                element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, "autocompleteTitle")))
            except TimeoutException:
                pass
            search.send_keys(Keys.RETURN)
            url =(driver.current_url)
            
            # stores the unique taxon number so that it does not store any duplicates
            tx_no=url.split("=",1)[1] #Taxon number
            print(tx_no)
            if tx_no in completed_urls:
                print("This taxon is already covered in "+completed_urls[tx_no])
                writefile.write("This taxon is already covered in "+completed_urls[tx_no]+"\n")
                continue
            completed_urls[tx_no]=taxon
            req= requests.get(url)
            content= req.content
            soup=bs(content,"html.parser")
            print(soup.find("p").text)
            writefile.write("Family: "+soup.find("p").text+"\n")
            flag=False
            for para in soup.find_all("p"):
                t=para.text
                completed_list.append(taxon)
                # lists the synonyms so that duplicates can be avoided
                if t.startswith("Synonyms") or t.startswith("Synonym"):
                    syn=t.split("\n")[0]
                    syn=re.split(":|,",syn)[1:]
                    syn_list=[x.split(" ")[1] for x in syn]
                    writefile.write("\nSynonyms :{}\n".format(syn_list))

                # this is just a filter that can be used to get the genuses that existed at a specific geologocal epoch
                elif t.startswith("• Paleocene of") or t.startswith("• Oligocene of") or t.startswith("• Eocene of") :
                    writefile.write(t+"\n")
                    print(t)
                    flag=True
            print(flag)
            if flag==True:    
                print("\n\n")
                writefile.write("\n\n")
            else:
                print("No data available.")
                writefile.write("No data available.\n\n")


    print("Total Searches Made = {}".format(searches))
    print("Missed Taxons: {}".format(missed))

if __name__=="__main__":
    start()
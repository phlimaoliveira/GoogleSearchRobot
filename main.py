import time, csv
from csv import writer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    with open("palavrasChaveBusca.csv", encoding="utf-8") as pc:
        palavras_chave = csv.reader(pc)

        with open("resultadoBusca.csv", "w+", encoding="utf-8") as rb:
            writer = csv.writer(rb, delimiter='\t')

            for i in palavras_chave:
                searchInGoogle(i[0], writer)

def searchInGoogle(sinonimo_pesquisa, writer):
    driver = webdriver.Chrome()
    driver.get('http://www.google.com/')

    campo_pesquisa = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')
    campo_pesquisa.send_keys(sinonimo_pesquisa)
    campo_pesquisa.send_keys(Keys.ENTER)

    links_pesquisa = []
    titles_pesquisa = []

    frames_google = driver.find_elements_by_xpath('//div[@class="g" and div[1]/div[1]/div[1]/a]')

    for i in range(len(frames_google)):
        try:
            link = frames_google[i].find_element_by_xpath('./div[1]/div[1]/div[1]/a').get_attribute('href')
            title = frames_google[i].find_element_by_xpath('./div[1]/div[1]/div[1]/a/h3').text
            if(title != ''):
                links_pesquisa.append(link.replace('\t', ''))
                titles_pesquisa.append(title.replace('\t', ''))
        except:
            print("Este bloco deu algum erro na captura!")


    writer.writerow(["Pesquisa feita por:", sinonimo_pesquisa])

    print("Pesquisando: " + sinonimo_pesquisa)
    # Laço de repetição de preenchimento do CSV
    for i in range(len(links_pesquisa)):
        writer.writerow([titles_pesquisa[i], links_pesquisa[i]])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

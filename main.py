import time, csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    with open("palavrasChaveBusca.csv", encoding="utf-8") as pc:
        palavras_chave = csv.reader(pc)

        for i in palavras_chave:
            searchInGoogle(i[0])

def searchInGoogle(sinonimo_pesquisa):
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
            links_pesquisa.append(link)
            titles_pesquisa.append(title)
        except:
            print("Este bloco deu algum erro na captura!")

    for i in range(len(links_pesquisa)):
        print(links_pesquisa[i], '-', titles_pesquisa[i])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

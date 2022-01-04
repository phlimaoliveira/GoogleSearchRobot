import time, csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    with open("palavrasChaveBusca.csv", encoding="utf-8") as pc:
        palavras_chave = csv.reader(pc)

        driver = webdriver.Chrome()
        driver.get('http://www.google.com/')

        with open("resultadoBusca.csv", "w+", encoding="utf-8") as rb:
            writer = csv.writer(rb, delimiter='\t')

            for i in palavras_chave:
                searchInGoogle(i[0], writer, int(i[1]), driver)

def searchInGoogle(sinonimo_pesquisa, writer, paginas, driver):
    for index in range(paginas):
        if (index+1) == 1:
            campo_pesquisa = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')
            campo_pesquisa.send_keys(sinonimo_pesquisa)
            campo_pesquisa.send_keys(Keys.ENTER)
        else:
            campo_pesquisa = driver.find_element_by_xpath('//a[@aria-label=\'Page '+str(index+1)+'\']')
            campo_pesquisa.click()

        links_pesquisa = []
        titles_pesquisa = []

        frames_google = driver.find_elements_by_xpath('//div[@class="g" and div[1]/div[1]/div[1]/a]')

        for i in range(len(frames_google)):
            try:
                link = frames_google[i].find_element_by_xpath('./div[1]/div[1]/div[1]/a').get_attribute('href')
                title = frames_google[i].find_element_by_xpath('./div[1]/div[1]/div[1]/a/h3').text
                if(title != ''):
                    links_pesquisa.append(link)
                    titles_pesquisa.append(title)
            except:
                print("Este bloco deu algum erro na captura!")


        writer.writerow(["Pagina "+str(index+1)+":", sinonimo_pesquisa])

        print("Pesquisando: " + sinonimo_pesquisa + " Pagina " + str(index+1))
        # Laço de repetição de preenchimento do CSV
        for i in range(len(links_pesquisa)):
            writer.writerow([titles_pesquisa[i], links_pesquisa[i]])

    driver.get('http://www.google.com/')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

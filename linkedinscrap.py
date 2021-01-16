
# Importações
from selenium import webdriver
from time import sleep

# Parametros

# Classes

# Execução do código
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.linkedin.com/jobs/search?keywords=Data%20Scientist&location=Rio%20de%20Janeiro%2C%20Rio%20de%20Janeiro%2C%20Brasil&geoId=106701406&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0')
    
    sleep(2)
    
    resultados = driver.find_elements_by_class_name('jobs-search__results-list')
    lista_descricao = []
    
    while True:    
        for r in resultados[len(lista_descricao):]:
            r.click()
            sleep(2)
            try:
                descricao = driver.find_element_by_class_name('description')
                lista_descricao.append(descricao.text)
            except:
                print('Erro')
                pass
        
        resultados = driver.find_elements_by_class_name('result-card')
        
        print ('Pesquisa de vagas:', len(resultados))
        print ('Descrições adicionadas:', len(lista_descricao))
        
        if len(lista_descricao) == len(resultados):
            break
        
    descricao_salvar = '\n'.join(lista_descricao)
    with open('descricoes_vagas.txt','w') as f:
        f.write(descricao_salvar)
    driver.quit()
    

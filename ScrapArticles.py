import os, time, requests
from bs4 import BeautifulSoup

def scrap_articles(driver, wait, EC, By, file_name, scraped_articles_folder_name):
    with open(file_name, 'r') as f:
        all_links = f.readlines()
        for link in all_links:
            link_site = link.split("//")[1].split(".")[1]

            try:
                if link_site == "prnewswire":
                    driver.get(link)
                    try:
                        article = wait.until(EC.presence_of_element_located((By.XPATH, '//article[@class="news-release inline-gallery-template"]'))).text
                    except:
                        article = wait.until(EC.presence_of_element_located((By.XPATH, '//article[@class="news-release static-gallery-template"]'))).text
                    print(link)
                    print(article)
                    print("\n\n\n\n")


                if link_site == "businesswire":
                    driver.get(link)
                    article = wait.until(EC.presence_of_element_located((By.XPATH, '//article[@class="bw-release-main"]'))).text
                    print(link)
                    print(article)
                    print("\n\n\n\n")


                if link_site == "lseg":
                    driver.get(link)
                    article_title = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="tr-Poster-content"]'))).text
                    article_inner_sections = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="tr-Grid-item"]')))[1]
                    article_body = article_inner_sections.text.split("About LSEG")[0]
                    article = f"{article_title} {article_body}"
                    print(link)
                    print(article)
                    print("\n\n\n\n")


                if link_site == "sec":
                    driver.get(link)
                    article = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="content aside press-release"]'))).text
                    print(link)
                    print(article)
                    print("\n\n\n\n")

                article_name = article[:30].strip(" ")
                clean_article_name = article_name.replace(' ', '-').lower()
                scraped_file_name = f"{scraped_articles_folder_name}/{clean_article_name}.txt"
                print(scraped_file_name)

                with open(scraped_file_name, 'a') as f:
                    f.write(f"{link}\n{article}")
            except:
                pass
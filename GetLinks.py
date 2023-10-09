import os, time, requests
from bs4 import BeautifulSoup
import MonthNumber



def prnewswire_links(driver, wait, keyword, search_date, search_month, search_year, file_name, pagesize, page_range, total_articles, WebDriverWait):

    page = 1

    total_scraped = 0

    for _ in range(page_range):

        if total_scraped < int(total_articles):

            url = f"https://www.prnewswire.com/search/news/?keyword={keyword}&pagesize={pagesize}&page={page}"

            driver.get(url)

            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'lxml')

            full_section_data = soup.find('section', {'class': 'container search-results-text'})
            all_results = full_section_data.find('div', {'class': 'col-sm-12 card-list'})

            result_list = all_results.findAll('div', {'class': 'row newsCards'})


            for result in result_list:
                if total_scraped < int(total_articles):
                    date_text = result.find('small').getText().split(",")
                    posted_date = date_text[0] + date_text[1]

                    searched_date = f"{search_month} {search_date} {search_year}"

                    if posted_date.upper() == searched_date:
                        rel_url = result.find('a', {'class': 'news-release'}).get('href')
                        full_url = "https://www.prnewswire.com" + rel_url
                        print(posted_date, full_url)

                        with open(file_name, "a") as f:
                            f.write(full_url + '\n')
                            total_scraped += 1
                else:
                    break
            page += 1
        
        else:
            break


def sec_links(driver, wait, keyword, search_date, search_month, search_year, file_name, pagesize, page_range, total_articles, WebDriverWait):

    month_number = MonthNumber.get_month_number
    url_month = month_number(search_month)

    # url = f"https://www.sec.gov/news/pressreleases?aId=&combine={keyword}&year={search_year}&month={url_month}"
    url = f"https://www.sec.gov/news/pressreleases?aId=&combine=a"

    driver.get(url)
    source_code = driver.page_source

    soup = BeautifulSoup(source_code, 'lxml')

    odd_elements = soup.findAll('tr', {"class":"pr-list-page-row odd"})
    even_elements = soup.findAll('tr', {"class":"pr-list-page-row even"})

    total_scraped = 0

    for odd_element in odd_elements:
        if total_scraped < int(total_articles):
            searched_date = f"{search_month} {search_date} {search_year}"
            date_posted = odd_element.find('time', {"class": "datetime"}).text
            splited_date_posted = date_posted.split(",")
            actual_date_posted = f"{splited_date_posted[0].split()[0][:3].upper()} {splited_date_posted[0].split()[1]} {splited_date_posted[1].strip()}"
            # if actual_date_posted == searched_date:
            base_url = "https://www.sec.gov"
            article_url = odd_element.find('a', {"hreflang": "en"}).get('href')
            full_url = base_url + article_url
            print(actual_date_posted)
            print(full_url)

            with open(file_name, "a") as f:
                f.write(full_url + '\n')
                total_scraped += 1
            # else:
            #     break
        else:
            break

    for odd_element in even_elements:
        if total_scraped < int(total_articles):
            searched_date = f"{search_month} {search_date} {search_year}"
            date_posted = odd_element.find('time', {"class": "datetime"}).text
            splited_date_posted = date_posted.split(",")
            actual_date_posted = f"{splited_date_posted[0].split()[0][:3].upper()} {splited_date_posted[0].split()[1]} {splited_date_posted[1].strip()}"
            # if actual_date_posted == searched_date:
            base_url = "https://www.sec.gov"
            article_url = odd_element.find('a', {"hreflang": "en"}).get('href')
            full_url = base_url + article_url
            print(actual_date_posted)
            print(full_url)

            with open(file_name, "a") as f:
                f.write(full_url + '\n')
                total_scraped += 1
            # else:
            #     break
        else:
            break



def lseg_links(driver, wait, EC, By, keyword, search_date, search_month, search_year, file_name, pagesize, page_range, total_articles, WebDriverWait):

    url = f"https://www.lseg.com/en/media-centre/press-releases?q={keyword}"

    driver.get(url)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="onetrust-reject-all-handler"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Year"]'))).click()
    time.sleep(2)
    driver.find_element(By.XPATH, f'//label[@for="id-years:{search_year}"]').click()
    time.sleep(3)

    if int(total_articles) > 10:

        page_source = driver.execute_script("return document.body.innerHTML;")
        soup = BeautifulSoup(page_source, "lxml")
        result_section = soup.find("ul", {"class": "tr-Pagination-items"})
        pagination_items = result_section.findAll('li')
        total_page_number = pagination_items[-2].find('button').find('span', {"class": "tr-PaginationPageItem-innerText"}).getText()

        current_page = result_section.find('li', {'class': ['tr-PaginationPageItem', 'is-active']}).find('span', {"class": "tr-PaginationPageItem-innerText"}).getText()
        print(f"Current page: {current_page}")
    else:
        total_page_number = 1

    total_page_number = int(total_page_number)

    current_page = 1
    total_scraped = 0


    while current_page <= total_page_number:
        if total_scraped < int(total_articles):
            print(current_page)
            page_source = driver.execute_script("return document.body.innerHTML;")
            soup = BeautifulSoup(page_source, "lxml")
            result_section = soup.find("div", {"class": "tr-SearchResults-results"})
            all_results = result_section.findAll("div", {"class": "tr-SearchResults-result"})

            for result in all_results:
                if total_scraped < int(total_articles):
                    searched_date = f"{search_month} {search_date} {search_year}"
                    date_posted = result.find('span', {'class': 'tr-SearchResults-articleInfoFooterDate'}).text
                    splited_date_posted = date_posted.split(",")
                    actual_date_posted = splited_date_posted[0].upper() + splited_date_posted[1]

                    if actual_date_posted == searched_date:
                        article_url = result.find('a', {'class': 'tr-SearchResults-resultTitle track-custom-clicks'}).get('href')
                        print(actual_date_posted)
                        print(article_url)
                        with open(file_name, "a") as f:
                                f.write(article_url + '\n')
                                total_scraped += 1
                    else:
                        break
                else:
                    break
            
            time.sleep(5)

            if current_page >= total_page_number:
                break
            else:
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(3)
                next_click_buttons = driver.find_elements(By.XPATH, '//button[@data-testid="navItemRight"]')
                for button in next_click_buttons:
                    try:
                        button.click()
                        break
                    except:
                        pass
            time.sleep(5)
            
            current_page += 1

        else:
            break

            

def businesswire_links(driver, wait, EC, By, keyword, search_date, search_month, search_year, file_name, pagesize, page_range, total_articles, WebDriverWait):

    page = 1

    total_scraped = 0

    for _ in range(page_range):

        if total_scraped < int(total_articles):

            url = f"https://www.businesswire.com/portal/site/home/search/?searchType=news&searchTerm={keyword}&searchPage={page}"
            driver.get(url)
            time.sleep(3)

            page_source = driver.page_source

            soup = BeautifulSoup(page_source, "html.parser")
            if page > 1:
                inner_tables = soup.findAll('ul', {'class': 'bw-news-list'})[0]
            else:
                inner_tables = soup.findAll('ul', {'class': 'bw-news-list'})[1]
            
            all_news = inner_tables.findAll('li')
            for news in all_news:
                if total_scraped < int(total_articles):
                    searched_date = f"{search_month} {search_date} {search_year}"
                    date_posted = news.find('time').getText()
                    splited_date_posted = date_posted.split(",")
                    month_formatted = splited_date_posted[0].split()[0]
                    date_formatted = splited_date_posted[0].split()[1]
                    actual_date_posted = f"{month_formatted[:3].upper()} {date_formatted} {splited_date_posted[1].strip()}"
                    if actual_date_posted == searched_date:                                        
                        article_url = news.find('a').get('href')
                        print(article_url)
                        with open(file_name, "a") as f:
                                f.write(article_url + '\n')
                        total_scraped += 1
                else:
                    break
        else:
            break

        page += 1
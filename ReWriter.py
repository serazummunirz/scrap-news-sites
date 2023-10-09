import os
from tinq import Tinq


def rewrite(tinq_api_key, scraped_articles_folder_name, rewritten_articles_folder_name):

    tinq = Tinq(api_key=tinq_api_key)

    files = os.listdir(scraped_articles_folder_name)
    for f in files:
        with open(f'{scraped_articles_folder_name}/{f}', 'r') as r:
            lines = r.readlines()[2:]

            paraphrases_list = []

            count_lines = 0

            for line in lines:

                rewrite = tinq.rewrite(text=line, mode='standard')
                rewritten = rewrite['paraphrase']
                paraphrases_list.append(rewritten)

            rwritten_article = " ".join(paraphrases_list)

            with open(f'{rewritten_articles_folder_name}/{f}', 'a') as wr:
                wr.write(rwritten_article)
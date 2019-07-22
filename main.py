from bs4 import BeautifulSoup
import requests
import time


def main():
    articles = []
    urls = load_urls("urls.txt")
    for url in urls:
        print(url)
        article = read_article(url)
        articles.append(article)
        time.sleep(2)

    write_csv("articles.csv", articles)


def write_csv(filename, articles):
    with open(filename, 'w') as f:
        f.write("url, title, like, comment, star \n")
        for article in articles:
            art_string = ','.join(article)
            f.write(art_string + '\n')


def load_urls(filename):
    with open(filename) as f:
        content = f.readlines()
    return [x.strip() for x in content]


def read_article(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    title = soup.find_all(class_='title')[0].get_text()
    print('article title: ' + title)

    like = soup.find_all(class_='like')[0].find_all('span')[0].get_text()
    print('like: ' + like)

    comment = soup.find_all(class_='comment')[0].find_all('span')[0].get_text()
    print('comment: ' + comment)

    star = soup.find_all(class_='star')[0].find_all('span')[0].get_text()
    print('star: ' + star)

    return (url, title, like, comment, star)


if __name__ == "__main__":
    main()

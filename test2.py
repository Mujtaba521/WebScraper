def WebScrapper(keywords):
    import requests
    searchString = ", ".join(keywords)
    print(searchString)

    my_url = ('https://newsapi.org/v2/everything?'
              'q={' + searchString + '}&'
              'from=2019-10-23&'
              'apiKey=1a1a388fb304410eba4d4c61063cefa0')
    myPage = requests.get(my_url).json()
    my_article = myPage['articles']
    description = []
    date = []

    for ar in my_article:
        description.append(ar["description"])
        date.append(ar["publishedAt"])

    with open('data.txt', 'w', encoding="utf-8") as outfile:
        for x in range(len(description)):
            outfile.write(str(description[x]))
            outfile.write("//" + str(date[x]))
            outfile.write("\n")
    outfile.close()

# method 1 should compare with a db
def Method1():
    keywords = ("corruption", "money laundering", "terrorist financing")
    WebScrapper(keywords)
    print("need 2nd part to work on data.txt")


# Method 2 just aggregates web data/sources
def Method2():
    #WebScrapper(keywords=["research related inquiries//"])
    print("")

def main():
    print("testing first method")
    Method1()
    print("testing second method")


if __name__ == '__main__':
    main()

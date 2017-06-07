import requests
import pandas
from bs4 import BeautifulSoup


a = "https://www.amazon.com/KIND-Almond-Coconut-Natural-1-4-Ounce/product-reviews/B0034EDMCW/"
b = "ref=cm_cr_arp_d_paging_btm_"
c = range(1,264)
d = "/142-2812378-9138139?ie=UTF8&qid=1496343725&sr=8-1&keywords=kind+snack+bars&pageNumber="
df = pandas.DataFrame(columns = ['Flavor','Reviewer','Dates', 'Polarity'])

e = []
for each in c:
    e.append(a+b+str(each)+d+str(each))

for i in range(len(e)):
    page = requests.get(e[i])
    soup = BeautifulSoup(page.content, 'html.parser')

    soup_s = soup.find_all('span')
    soup_reviews = soup.find_all('span', class_='a-size-base review-text')
    review_date = soup.find_all('span', class_='a-size-base a-color-secondary review-date')
    dates_only = soup.select("#cm_cr-review_list .review-date")
    #     total_reviews = list(soup.select('.AverageCustomerReviews .a-row'))[0].get_text()

    # Every product has different flavors and kinds.
    # Amazon combines reviews of all flavors together in
    # one - under the product title.
    # We extract each flavour kind for selected product, to further
    # drill down analysis based on flavors.
    flav_size = list(soup.select('.a-size-mini.a-color-secondary'))

    from textblob import TextBlob
    import nltk

    dates_list1 = []
    for each in list(dates_only):
        dates_list1.append(each.get_text())

    from dateutil import parser

    dates_list = []
    for date in dates_list1:
        dates_list.append(parser.parse(date).strftime('%Y-%m-%d'))

    from dateutil import parser

    dates_year = []
    for date in dates_list1:
        dates_year.append(parser.parse(date).strftime('%Y'))

    years_int = []
    for each in dates_year:
        years_int.append(int(each))

    # Creating list for Reviewers
    reviewers = list(soup.select('.author'))
    reviewers_list = []
    for each in list(reviewers):
        reviewers_list.append(each.get_text())

    # List for Flavour types
    flav_list = []
    for each in list(flav_size):
        flav_list.append(each.get_text())

    # List for Polarities of all reviews
    polarity_list = []
    for each in list(soup_reviews):
        polarity_list.append(round((TextBlob(each.get_text()).sentiment.polarity), 5))

    # Now we create a raw data(and raw_data2) and store in data Frames




    raw_data = {'Flavor': flav_list, 'Reviewer': reviewers_list, 'Dates': dates_list1, 'Polarity': polarity_list}
    df_curr = pandas.DataFrame.from_dict(raw_data, orient='index')
    #     df_curr = df.curr.transpose
    df = pandas.concat([df, df_curr.transpose()])
    del (raw_data, df_curr, reviewers_list, flav_list, dates_list1, polarity_list, dates_list)
# del total_reviews
print("Data has been successfully gathered!!")
import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

# telegram connection
bot = telegram.Bot(token = '1009840016:AAG8G8EHAU7wW6HR8toY21J0xIButtY3-T4')
# request module을 이용해서 정보 받아옴
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200220'

# 반복해야하는 작업은 함수로 선언을 해준다.
def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    print(imax)

    if (imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id=1038006440, text=title + " IMAX 예매가 열렸습니다.")
        sched.pause()

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', minutes=1)
sched.start()
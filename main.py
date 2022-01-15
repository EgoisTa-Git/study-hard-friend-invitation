import smtplib, os


smtp_server = 'smtp.yandex.ru:465'
login = os.environ['MAIL_LOGIN']
password = os.environ['MAIL_PASSWORD']
email_from = 'spetrov.okb@yandex.ru'
email_to = 'egoistapig1989@gmail.com'
friend_name = 'Alex'
my_name = 'Серёга'
website = 'https://dvmn.org/referrals/QoqUjm1J75qqIGZKnxXRFLTP39yORMF6AwOxAA4J/'
letter = (f"""From: {email_from}
To: {email_to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""")
letter=letter.encode("UTF-8")

server=smtplib.SMTP_SSL(smtp_server)
server.login(login, password)
server.sendmail(email_from, email_to, letter)
server.quit()

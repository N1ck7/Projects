import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_count = 0
        for rec in self.records:
            if rec.date == dt.datetime.now().date():
                today_count += rec.amount
        return today_count

    def get_week_stats(self):
        week_count = 0
        for rec in self.records:
            if dt.datetime.today() - dt.timedelta(days = 7) <= rec.date <= dt.datetime.today():
                week_count += rec.amount
        return week_count

    def today_stats(self):
        today_stats = self.limit - self.get_today_stats()
        return today_stats


class Record:
    def __init__(self, amount, comment, date = ''):
        self.amount = amount
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment

class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        stats = super().today_stats()
        if stats < self.limit:
            return f'Сегодня можно съесть что-нибудь еще, но не более {self.limit - stats} Ккал.'
        else:
            return 'Хватит жрать!'

class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 65.0
    RUB_RATE = 1

    def __init__(self, limit):
        super().__init__(limit)
        
    def get_today_cash_remained(self, currency):

        currency = currency.lower()

        dict = {'rub' : ['руб', self.RUB_RATE],
                'eur' : ['Euro', self.EURO_RATE],
                'usd' : ['USD', self.USD_RATE]

        }
        vallet_name = dict[currency][0]
        vallet_cours = dict[currency][1]
        money = round(self.today_stats() / vallet_cours, 2)
        if money > 0:
            return f'На сегодня осталось {money} {vallet_name}'
        if money == 0:
            return 'Денег нет, держись'
        if money < 0:
            return f'Денег нет, держись: твой долг - {-1 * money} {vallet_name}'

        

        
#test
cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment="кофе")) 
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="01.10.2022"))
print(cash_calculator.get_today_cash_remained("USD"))
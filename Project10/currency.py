import urllib.request


class Currency():
    def __init__(self, amount=1, currency_type="USD"):
        if currency_type in ("USD", "EUR", "SEK", "CAD", "CNY", "GBP"):
            self.__amount = amount
            self.__currency_type = currency_type
        else:
            self.__amount = 0
            self.__currency_type = ""

    def convert_to(self, currency_code):
        req_string = "https://www.google.com/finance/converter?a=" + str(self.__amount) + "&from=" + self.__currency_type + "&to=" + currency_code
        web_obj = urllib.request.urlopen(req_string)
        results_str = str(web_obj.read())
        results_str = results_str[results_str.index("bld"):]
        results_str = results_str[results_str.index(">")+1:results_str.index(" ")]
        web_obj.close()
        return Currency(round(float(results_str), 2), currency_code)

    def __str__(self):
        return str(self.__amount) + " " + self.__currency_type

    def __add__(self, other):
        if type(other) == Currency:
            return Currency(self.__amount + other.convert_to(self.__currency_type).__amount, self.__currency_type)
        else:
            return Currency(self.__amount + other, self.__currency_type)

    def __radd__(self, other):
        return Currency(other + self.__amount, self.__currency_type)

    def __sub__(self, other):
        if type(other) == Currency:
            return Currency(self.__amount - other.convert_to(self.__currency_type).__amount, self.__currency_type)
        else:
            return Currency(self.__amount - other, self.__currency_type)

    def __rsub__(self, other):
        return Currency(other - self.__amount, self.__currency_type)

    def __gt__(self, other):
        return self.__amount > other.convert_to(self.__currency_type).__amount

    def __repr__(self):
        return '%s(%r, %r)' % (self.__class__.__name__, self.__amount, self.__currency_type)
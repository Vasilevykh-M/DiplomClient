import numpy as np

def validation(data):
    columns = ["ДатаБрони", "ВремяБрони", "ИсточникБрони", "ВременнаяБронь", "Город", "ВидПомещения",
               "Тип", "ПродаваемаяПлощадь", "Этаж", "СтоимостьНаДатуБрони", "ТипСтоимости", "ВариантОплаты",
               "ВариантОплатыДоп", "СкидкаНаКвартиру", "ФактическаяСтоимостьПомещения", "СделкаАН",
               "ИнвестиционныйПродукт", "Привилегия", "Статус лида (из CRM)", "СледующийСтатус"]
    A = set(columns)
    B = set(data.columns)
    return A & B == A

def validation_pred(data):
    columns = ["ДатаБрони", "ВремяБрони", "ИсточникБрони", "ВременнаяБронь", "Город", "ВидПомещения",
               "Тип", "ПродаваемаяПлощадь", "Этаж", "СтоимостьНаДатуБрони", "ТипСтоимости", "ВариантОплаты",
               "ВариантОплатыДоп", "СкидкаНаКвартиру", "ФактическаяСтоимостьПомещения", "СделкаАН",
               "ИнвестиционныйПродукт", "Привилегия", "Статус лида (из CRM)"]
    A = set(columns)
    B = set(data.columns)
    return A & B == A

def validationMissingValues(data):
    columns = ["ДатаБрони", "ВремяБрони", "ИсточникБрони", "ВременнаяБронь", "Город", "ВидПомещения",
               "Тип", "ПродаваемаяПлощадь", "Этаж", "СтоимостьНаДатуБрони", "ТипСтоимости", "ВариантОплаты",
               "ВариантОплатыДоп", "СкидкаНаКвартиру", "ФактическаяСтоимостьПомещения", "СделкаАН",
               "ИнвестиционныйПродукт", "Привилегия", "Статус лида (из CRM)"]
    for col in columns:
        pct_missing = np.mean(data[col].isnull())
        if pct_missing > 0.0:
            return False
    return True

def validation_(data, pred):
    if pred == False and validation(data) or pred == True and validation_pred(data):
        data = cleanMissingValues(data)
        if validationMissingValues(data):
            return True
        else:
            return False
    else:
        return False

# Заменяем пропуски
def cleanMissingValues(df):
    arr = df.fillna(value={'СкидкаНаКвартиру': 0 , 'ВариантОплатыДоп':'нет'})
    return arr
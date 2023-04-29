import RemouteSmartRieltor_pb2_grpc
import RemouteSmartRieltor_pb2

def create_genereator_to_post(df):
    for i, data in df.iterrows():
        yield RemouteSmartRieltor_pb2.Data(
            Booking = RemouteSmartRieltor_pb2.Booking(
                BookingDate = str(data["ДатаБрони"]),
                BookingTime = str(data["ВремяБрони"]),
                BookingSource = data["ИсточникБрони"],
                BookingTemporary = data["ВременнаяБронь"],
                City = data["Город"],
                TypeRoom = data["ВидПомещения"],
                TypeObject = data["Тип"],
                Area = int(data["ПродаваемаяПлощадь"]),
                Floor = int(data["Этаж"]),
                Cost = int(data["СтоимостьНаДатуБрони"]),
                TypeCost = data["ТипСтоимости"],
                PaymentOption = data["ВариантОплаты"],
                PaymentOptionAdditional = data["ВариантОплатыДоп"],
                Discount = int(data["СкидкаНаКвартиру"]),
                ActualCost = int(data["ФактическаяСтоимостьПомещения"]),
                DealAN = data["СделкаАН"],
                InvestmentProduct = data["ИнвестиционныйПродукт"],
                Privilege = data["Привилегия"],
                LeadStatus = data["Статус лида (из CRM)"],
            ),
            StateBooking = RemouteSmartRieltor_pb2.StateBooking(StateBooking = data["СледующийСтатус"])
        )


def create_generator_to_pred(df):
    for i, data in df.iterrows():
        yield RemouteSmartRieltor_pb2.Booking(
                BookingDate = str(data["ДатаБрони"]),
                BookingTime = str(data["ВремяБрони"]),
                BookingSource = data["ИсточникБрони"],
                BookingTemporary = data["ВременнаяБронь"],
                City = data["Город"],
                TypeRoom = data["ВидПомещения"],
                TypeObject = data["Тип"],
                Area = int(data["ПродаваемаяПлощадь"]),
                Floor = int(data["Этаж"]),
                Cost = int(data["СтоимостьНаДатуБрони"]),
                TypeCost = data["ТипСтоимости"],
                PaymentOption = data["ВариантОплаты"],
                PaymentOptionAdditional = data["ВариантОплатыДоп"],
                Discount = int(data["СкидкаНаКвартиру"]),
                ActualCost = int(data["ФактическаяСтоимостьПомещения"]),
                DealAN = data["СделкаАН"],
                InvestmentProduct = data["ИнвестиционныйПродукт"],
                Privilege = data["Привилегия"],
                LeadStatus = data["Статус лида (из CRM)"],
        )

from datetime import datetime,timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today() + timedelta(days=15, minutes=20,seconds=30)

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = {
            1: "janeiro", 2: "fevereiro", 3: "março",
            4: "abril", 5: "maio", 6: "junho",
            7: "julho", 8: "agosto", 9: "setembro",
            10: "outubro", 11: "novembro", 12: "dezembro"
        }

        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]

        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = self.momento_cadastro - datetime.today()
        return tempo_cadastro

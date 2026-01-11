import pymysql
import calendar
from collections import defaultdict
from flask import Flask, render_template

app = Flask(__name__)

class Banco():
    def __init__(self):
        pass

    def conectar_banco(self):
        conexao = pymysql.connect(
        host="localhost",
        user="root",
        password="sinx0088",
        database="escala_appbr",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
        return conexao

    @staticmethod
    def pegar_id_turno(nome_turno):
        
        banco = Banco()
        conexaoSQL= banco.conectar_banco()
        cursorSQL= conexaoSQL.cursor()

        cursorSQL.execute("""
            SELECT IDTURNO
            FROM TURNOS
            WHERE NOME_TURNO = %s
        """, (nome_turno,))

        resultado = cursorSQL.fetchone()

        cursorSQL.close()
        conexaoSQL.close()

        return resultado['IDTURNO'] if resultado else None

    @staticmethod
    def pegar_id_militar(nome_militar):
        
        banco = Banco()
        conexaoSQL= banco.conectar_banco()
        cursorSQL= conexaoSQL.cursor()


        cursorSQL.execute("""
            SELECT IDMILITAR
            FROM EFETIVO
            WHERE NOME_GUERRA = %s
        """, (nome_militar,))

        resultado = cursorSQL.fetchone()

        cursorSQL.close()
        conexaoSQL.close()

        return resultado['IDMILITAR'] if resultado else None
    
class Escala():
    
    def __init__(self):
        pass
    
    def inserir_dia(self):
        
        dia = input("Dia (YYYY-MM-DD): ")
        nome_militar = input("Nome de guerra: ").upper()
        nome_turno = input("Turno (M1, T1, RT...): ").upper()
        
        banco = Banco()

        linha = (dia,banco.pegar_id_militar(nome_militar),banco.pegar_id_turno(nome_turno))
        
        conexaoSQL= banco.conectar_banco()
        cursorSQL= conexaoSQL.cursor()

        query = """
        INSERT INTO ESCALA (DIA, ID_MILITAR, ID_TURNO)
        VALUES (%s, %s, %s)
        """
        cursorSQL.execute(query,linha)
        conexaoSQL.commit()

        conexaoSQL.close()
        cursorSQL.close()

    def pegar_dados_escala(self):
        
        banco = Banco()
        conexaoSQL= banco.conectar_banco()
        cursorSQL= conexaoSQL.cursor()

        cursorSQL.execute("""
        SELECT E.DIA, F.NOME_GUERRA, T.NOME_TURNO
        FROM ESCALA E
        JOIN EFETIVO F ON E.ID_MILITAR = F.IDMILITAR
        JOIN TURNOS T ON E.ID_TURNO = T.IDTURNO
        ORDER BY E.DIA
    """)
        
        resultados = cursorSQL.fetchall()  # lista de dicionários
        cursorSQL.close()
        conexaoSQL.close()
        return resultados
    
    def matriz_escala_dict(escala,ano,mes):

        num_dias = calendar.monthrange(ano, mes)[1]  # número de dias do mês
    
        # defaultdict de dicionário
        matriz = defaultdict(lambda: defaultdict(str))
    
        for linha in escala:
            dia = int(linha['DIA'].day)  # pega o dia do mês
            militar = linha['NOME_GUERRA']
            turno = linha['NOME_TURNO']
            matriz[militar][dia] = turno

        for militar in matriz:
            for d in range(1, num_dias + 1):
                matriz[militar].setdefault(d, "")  # vazio se não tiver turno

        return matriz,num_dias

escala_obj = Escala()

@app.route('/mensal/<int:ano>/<int:mes>')
def mostrar_escala_mensal(ano, mes):
    escala = escala_obj.pegar_dados_escala()
    matriz, num_dias = Escala.matriz_escala_dict(escala, ano, mes)
    return render_template('escala.html', matriz=matriz, num_dias=num_dias)

if __name__ == '__main__':
    app.run(debug=True)

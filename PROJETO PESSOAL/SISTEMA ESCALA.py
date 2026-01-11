import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="sinx0088",
    database="escala_appbr",
    port=3306
)

cursor = conn.cursor()

cursor.execute("""
SELECT 
    e.NOME_GUERRA,
    DAY(es.DIA) AS DIA,
    t.NOME_TURNO
FROM ESCALA es
JOIN EFETIVO e ON e.IDMILITAR = es.ID_MILITAR
JOIN TURNOS t ON t.IDTURNO = es.ID_TURNO
WHERE es.DIA BETWEEN '2026-01-01' AND '2026-01-31'
ORDER BY e.NOME_GUERRA, es.DIA
""")

dados = cursor.fetchall()

# ===============================
# MONTA A ESTRUTURA DA ESCALA
# ===============================
escala = {}

for nome, dia, turno in dados:
    if nome not in escala:
        escala[nome] = {}

    escala[nome][dia] = turno

# ===============================
# CONFIGURAÇÕES DE LAYOUT
# ===============================
LARGURA_NOME = 18     # largura da coluna do nome
LARGURA_DIA = 5       # largura de cada dia

dias = list(range(1, 32))

# ===============================
# CABEÇALHO
# ===============================
print("NOME".ljust(LARGURA_NOME), end="")

for d in dias:
    print(f"{d:02d}".ljust(LARGURA_DIA), end="")

print()

# ===============================
# LINHAS DA ESCALA
# ===============================
for nome in sorted(escala.keys()):
    print(nome.ljust(LARGURA_NOME), end="")

    for d in dias:
        turno = escala[nome].get(d, "-")
        print(turno.ljust(LARGURA_DIA), end="")

    print()

conn.close()

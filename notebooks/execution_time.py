import pandas as pd
import numpy
import matplotlib.pyplot as plt

pd.set_option("display.max_rows", 1000)


df = pd.read_excel(
    "/home/erika.kvalem/Documents/Relecov/relecov_qc_exercise/files/QC_final.xlsx",
    sheet_name="fechas",
)
print(df)

tiempo_ejecuccion = df[
    ["ID", "Tiempo de ejecucion", "Fecha de secuenciacion", "Fecha de recepcion"]
]

tiempo_ejecuccion["Tiempo de ejecucion"].astype(int)

plt.rcdefaults()
fig, ax = plt.subplots()

ax.barh(
    tiempo_ejecuccion["ID"], tiempo_ejecuccion["Fecha de secuenciacion"], align="center"
)
# ax.set_yticks(tiempo_ejecuccion["ID"], labels="ID")
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_ylabel("Laboratories")
ax.set_xlabel("Execution time (days)")
ax.set_title("Execution time (Sequencing date - Reception date) ")


# tiempo_ejecuccion.plot(kind="bar", stacked=True)
plt.show()

from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_all_biblioteche(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM biblioteca"
        cursor.execute(query)

        for row in cursor:
            biblio = Biblioteca(
                id=row["id"],
                nome=row["nome"],
                indirizzo=row["indirizzo"]
            )
            result.append(biblio)

        cursor.close()
        cnx.close()
        return result

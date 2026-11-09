from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_all_generi(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore di connessione al database.")
            return result

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL"
        cursor.execute(query)

        for row in cursor:
            if row["genere"] is not None:
                result.append(row["genere"])

        cursor.close()
        cnx.close()
        return result

    def get_libri_filtrati(self, id_biblioteca, genere):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        cursor = cnx.cursor(dictionary=True)


        query = "SELECT * FROM libro WHERE 1=1"
        param = []

        if id_biblioteca is not None and id_biblioteca != "Nessun filtro":
            query += " AND id_biblioteca = %s"
            param.append(id_biblioteca)

        if genere is not None and genere != "Nessun filtro":
            query += " AND genere = %s"
            param.append(genere)

        cursor.execute(query, param)

        for row in cursor:

            libro = Libro(
                id=row["id"],
                titolo=row["titolo"],
                autore=row["autore"],
                genere=row["genere"],
                id_biblioteca=row["id_biblioteca"],
                anno_pubblicazione = row["anno_pubblicazione"]
            )
            result.append(libro)

        cursor.close()
        cnx.close()
        return result


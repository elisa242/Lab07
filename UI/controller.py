import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
        self.popola_dropdown()

    def popola_dropdown(self):

        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        biblioteche = self._model.get_biblioteche()
        for b in biblioteche:

            self._view.dd_biblioteca.options.append(ft.dropdown.Option(str(b)))

        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        generi = self._model.get_generi()
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(str(g)))

        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def seleziona_biblioteca(self, e):

        if e.control.value == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = e.control.value

    def seleziona_genere(self, e):

        if e.control.value == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra_libri(self, e):

        self._view.list_view.controls.clear()# Puliamo la lista attuale nella view


        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        if not libri:
            # Se nessun libro soddisfa i criteri, mostriamo un alert
            self._view.mostra_alert("Nessun libro trovato con i filtri selezionati.")
            self._view.update()
            return

        for libro in libri:
            self._view.list_view.controls.append(ft.Text(str(libro)))

        self._view.update()

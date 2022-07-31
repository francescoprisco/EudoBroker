import DatabaseManager as DatabaseManager
class DBFunction:
    def __init__(self):
        self.dbm = DatabaseManager.DatabaseManager('141.94.222.38','1433','ADB_Eudorex_Srl', 'Francesco.Prisco', '!CampaniaFelix2022-')
        self.dbm.connect()

    def getOLV(self,Cd_ARPrdClasse):
        parameters = []
        parameters.append(Cd_ARPrdClasse)
        try:
            result = self.dbm.select("SELECT A.Id_DoTes, B.Id_DORig, C.Cd_CF, C.Descrizione, A.Cd_Do, A.NumeroDoc, B.Cd_AR, CAST(B.QtaEvadibile AS INT) AS qt, B.DataConsegna  FROM [dbo].[DOTes] AS A INNER JOIN [dbo].[DORig] AS B ON A.Id_DoTes=B.Id_DOTes INNER JOIN [dbo].[CF] AS C ON A.Cd_CF=C.Cd_CF INNER JOIN [dbo].[AR] AS D ON B.Cd_AR=D.Cd_AR LEFT JOIN [dbo].[ICT_PrdAttivita_Coda] AS E ON B.Id_DORig=E.Id_DORig WHERE E.Id_DORig IS NULL AND B.QtaEvadibile > 0 AND D.Cd_ARPrdClasse LIKE '{}' AND A.Cd_Do LIKE 'OLV' AND A.Esecutivo LIKE 1 AND B.DataConsegna IS NOT NULL ORDER BY B.DataConsegna, B.Cd_AR".format(*parameters))
            print('OLV recuperati con successo')
            return result
        except Exception as e:
            print(e)
            print("Errore: Impossibile recuperare gli OLV")
            self.dbm.close()
            return []

    def getArticoli(self,Cd_ARPrdClasse):
        parameters = []
        parameters.append(Cd_ARPrdClasse)
        try:
            result = self.dbm.select("SELECT Cd_AR, Descrizione FROM [dbo].[AR] WHERE Cd_ARPrdClasse LIKE '{}' AND Obsoleto = 0 ORDER BY Cd_AR".format(*parameters))
            print('Articoli recuperati con successo')
            return result
        except Exception as e:
            print(e)
            print("Errore: Impossibile recuperare gli OLV")
            self.dbm.close()
            return []

    def getDaEvadere(self,Cd_ARPrdClasse):
        parameters = []
        parameters.append(Cd_ARPrdClasse)
        try:
            result = self.dbm.select("SELECT C.Cd_CF, A.Id_DoTes, B.Cd_AR, A.NumeroDoc, B.DataConsegna, CAST(B.QtaEvadibile AS INT) AS qt FROM [dbo].[DOTes] AS A INNER JOIN [dbo].[DORig] AS B ON A.Id_DoTes=B.Id_DOTes INNER JOIN [dbo].[CF] AS C ON A.Cd_CF=C.Cd_CF INNER JOIN [dbo].[AR] AS D ON B.Cd_AR=D.Cd_AR WHERE B.QtaEvadibile > 0 AND D.Cd_ARPrdClasse LIKE '{}' AND A.Cd_Do LIKE 'OLV' AND A.Esecutivo LIKE 1 AND B.DataConsegna IS NOT NULL ORDER BY B.DataConsegna, B.Cd_AR".format(*parameters))
            print('Da evadere recuperati con successo')
            return result
        except Exception as e:
            print(e)
            print("Errore: Impossibile recuperare gli Da Evadere")
            self.dbm.close()
            return []

    def getEvasi(self, Cd_ARPrdClasse):
        parameters = []
        parameters.append(Cd_ARPrdClasse)
        try:
            result = self.dbm.select("SELECT A.NumeroDocRif, A.Id_DoTes, B.Cd_AR, A.NumeroDoc, B.Cd_ARLotto, CAST(B.Qta AS INT) FROM [dbo].[DOTes] AS A INNER JOIN [dbo].[DORig] AS B ON A.Id_DoTes=B.Id_DOTes INNER JOIN [dbo].[CF] AS C ON A.Cd_CF=C.Cd_CF INNER JOIN [dbo].[AR] AS D ON B.Cd_AR=D.Cd_AR WHERE B.Qta > 0 AND D.Cd_ARPrdClasse LIKE '{}' AND A.Cd_Do LIKE 'VLO' ORDER BY A.Id_DoTes DESC".format(*parameters))
            print('Evasi recuperati con successo')
            return result
        except Exception as e:
            print(e)
            print("Errore: Impossibile recuperare gli Evasi")
            self.dbm.close()
            return []

    def evadiOLV(self,id,articolo):
        parameters = []
        parameters.append(id)
        parameters.append(articolo)
        try:
            result = self.dbm.updateInsert("UPDATE [dbo].[DORig] SET QtaEvadibile=0 WHERE Id_DoTes LIKE '{}' AND Cd_AR LIKE '{}}'".format(*parameters))
            print('Evasi aggiornati con successo')
            return result
        except Exception as e:
            print(e)
            print("Errore: Impossibile aggiornare gli Evasi")
            self.dbm.close()
            return []
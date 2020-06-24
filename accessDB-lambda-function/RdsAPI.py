import mysql.connector


class RdsApi:
    def connectRDS(self, host, database, user, password):
        return mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password)

    def addData(self, ne, frequency):
        object = self.connectRDS("serverless-a3.cdvxuztseuhu.us-east-1.rds.amazonaws.com", "serverless-a3", "admin",
                                 "amazonrds")
        cur = object.cursor()
        query = 'INSERT INTO NamedEntities (NamedEntity,Frequency) VALUES ("{0}",{1})'.format(str(ne), frequency)
        cur.execute(query)
        object.commit()
        cur.close()
        object.close()
        print("Row added for {0}".format(ne))

    def checkNameExist(self, ne):
        object = self.connectRDS("serverless-a3.cdvxuztseuhu.us-east-1.rds.amazonaws.com", "serverless-a3", "admin",
                                 "amazonrds")
        cur = object.cursor()
        query = 'select * from NamedEntities where NamedEntity = "{0}";'.format(str(ne))
        cur.execute(query)
        try:
            return cur.fetchall()[0][1]
        except Exception as e:
            print(e)
            return 0
        finally:
            object.commit()
            cur.close()
            object.close()

    def updateName(self, ne, frequency):
        object = self.connectRDS("serverless-a3.cdvxuztseuhu.us-east-1.rds.amazonaws.com", "serverless-a3", "admin",
                                 "amazonrds")
        cur = object.cursor()
        query = 'update NamedEntities set Frequency = "{0}" where NamedEntity = "{1}";'.format(frequency, ne)
        cur.execute(query)
        object.commit()
        cur.close()
        object.close()
        print("Table Updated for {0}".format(ne))
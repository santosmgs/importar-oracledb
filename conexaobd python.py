#importar o driver
import cx_Oracle
#importar oracle database(db)


#create table
def create_table()
    try
        conn = getConnection()
        cursor = conn.cursor()
        sql_query =  CREATE TABLE CEO_DETAILS(
        FIRST_NAME VARCHAR2(50),
        LAST_NAME VARCHAR2(50),
        COMPANY VARCHAR2(50),
        AGE NUMBER
        )
        cursor.execute(sql_query)
        print(Table created successfully)
    except Exception as e
        print(Error occurred while creating the table, e)
    finally
        if(conn)
            cursor.close()
            conn.close()



#criar uma conexao com o BD Oracle
def getConnection()
    try
        connection = cx_Oracle.connect('rm551640', '140105','oracle.fiap.com.brorcl')
        #connction = cx_Oracle.connect(user='rmXXXXX', passowrd = '123456', host= 'oracle.fiap.com.br', port= '1521', service='orcl')
        print('Conexao ', connection.version)
    except Exception as e
        print(f'Erro ao obter a conexao {e}')
    return connection

def insert()
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = INSERT INTO CEO_DE_DETAILS values('Steve', 'Jobs', 'Apple', '50')

    try
        cursor.execute(sql_query)
        conn.commit()
        print(Registro inserido)
    except Exception as e
        print(f'Erro ao inserir o registro  {e}')
    finally
        cursor.close()
        conn.close()

def select()
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = SELECT  FROM CEO_DATAILS WHERE NAME= 'Steve' 
    #sql_query = SELECT  from CEO_DETAILS
    try
        cursor.execute(sql_query)
        for result in cursor
            print(result)
    except Exception as e
        print(f'Erro ao obter registro {e}')
    finally
        cursor.close()
        conn.close()

def uptade()
    conn = getConnection()
    cursor = conn.cursor()
    sql_update = UPDATE CE_DETAILS set AGE = 55 WHERE FIRST_NAME = 'Steve'
    try
        cursor.execute(sql_update)
        conn.commit()
        print(Registro atualizado)
    except Exception as e
        print(f'Erro ao atualizar o registro {e}')
    finally
        cursor.close()
        conn.close()

def delete()
    conn = getConnection()
    cursor = conn.cursor()
    sql_delete = DELETE FROM CEO_DETAILS WHERE FIRST_NAME='Steve'
    try
        cursor.execute(sql_delete)
        conn.commit()
        print(Registro deletado)
    except Exception as e
        conn.rollback()
        print(f'Erro ao deletar o registro {e}')
    finally
        cursor.close()
        conn.close()

#Principal (testes)




def insertParametros(first_name, last_name, company, age)
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = INSERT INTO CEO_DETAILS (first_name, last_name, company, age) VALUES({first_name},{last_name}, {company}, {age})

    '''
    
    data = (
    input(First Name )
    input(Last Name )
    input(Comapany )
    input(Age ))
    )

    '''



    data = (
        first_name,
        last_name,
        company,
        age
    )
    try
        cursor.execute(sql_query, data)
        conn.commit()
        print(Registro inserido)
    finally
        cursor.close()
        conn.close()
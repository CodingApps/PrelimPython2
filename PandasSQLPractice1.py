import sqlite3
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datastamp TEXT, keyword TEXT, value REAL)')

#    def data_entry():
#        c.execute('INSERT INTO stuffToPlot VALUES()')

        
def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1324324423,'2016-01-02', 'Python', 8)")
    conn.commit()
    c.close()
    conn.close()
    
create_table()
data_entry()

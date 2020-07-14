import pandas as pd
import pandasql as ps


def main():
    flights = pd.read_csv("Data_Engineer_test/candidateEvalData/flights.csv")
    airports = pd.read_csv("Data_Engineer_test/candidateEvalData/airports.csv")
    weather = pd.read_csv("Data_Engineer_test/candidateEvalData/weather.csv")
    airlines = pd.read_csv("Data_Engineer_test/candidateEvalData/airlines.csv")

    sql = 'SELECT * from flights'
    result = ps.sqldf(sql)

    sql1 = '''
    SELECT air_time, origin, dest, name from flights INNER JOIN airlines 
    ON  flights.carrier=airlines.carrier 
    '''

    result = ps.sqldf(sql1)
    print(result.head(10))

    sql2 = '''
    SELECT air_time, origin, dest, name from flights INNER JOIN airlines 
    ON  flights.carrier=airlines.carrier 
    WHERE airlines.name LIKE "%JetBlue%"
    '''

    result = ps.sqldf(sql2)
    print(result.head(10))

    # sql3 = '''
    # SELECT air_time, origin, dest, name from flights INNER JOIN airlines
    # ON  flights.carrier=airlines.carrier
    # WHERE airlines.name LIKE "%JetBlue%"
    # ORDER BY origin
    # '''

    sql3 = '''
    SELECT flight, air_time, origin, dest 
    FROM flights
    ORDER BY origin
    '''

    result = ps.sqldf(sql3)
    print(result.head(10))

    sql4 = '''
    SELECT COUNT(origin), flight, air_time, origin, dest 
    FROM flights 
    GROUP BY origin
    HAVING count(origin) > 10000
    ORDER BY origin 
    '''

    result = ps.sqldf(sql4)
    print(result.head(10))


if __name__ == "__main__":
    main()

import psycopg2
from API_interaction import GetMeets

token = "plcOgcreJML2O35Xv0Z6fn3zPMRFtYmX5RzxlXfW5rMVPAIRVrbp9dvWvA843aqr"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  "AppleWebKit/537.36 (KHTML, like Gecko)"
                  "Chrome/84.0.4147.89"
                  "Safari/537.36"}
gm = GetMeets(token, headers)

with psycopg2.connect(dbname='d6qfh4tmk9h4t2',
                      user='xqhkevexwktfkk',
                      password='cb8c1a6070ebed38248446e0960ffe7b3fd8ea4927c0aa3ef4d7e1b630588b3f',
                      host='ec2-34-225-162-157.compute-1.amazonaws.com') as conn:
    with conn.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE b_khalutornykh (
                Id SERIAL PRIMARY KEY,
                Date DATE,
                Bizdev character varying,
                Company character varying,
                Category character varying);
            """
        )
        conn.commit()
        for day in gm.get_days():
            for meets in gm.get_meets(day):
                cursor.execute(
                    """
                    INSERT INTO b_khalutornykh (date, bizdev, company, category) VALUES ('{}', '{}', '{}', '{}')
                    """.format(meets['date'], meets['bizdev'], meets['company'], meets['category'])
                )
        conn.commit()

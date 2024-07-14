import db_connector

cusrsor,conn = db_connector.get_db_connection()

def feed_data():

    # Creating tables
    user_table ="""CREATE TABLE IF NOT EXISTS USER(ID INT PRIMARY KEY, NAME VARCHAR(255), EMAIL VARCHAR(255), AGE INT);"""
    cusrsor.execute(user_table) 
    friend_table ="""CREATE TABLE IF NOT EXISTS FRIEND (ID INT PRIMARY KEY, USER_ID INT, FRIEND_ID INT,FOREIGN KEY (USER_ID) REFERENCES USER(ID),FOREIGN KEY (FRIEND_ID) REFERENCES USER(ID));"""
    cusrsor.execute(friend_table) 

    # List of user data to insert
    users = [
    (1, "John Doe", "john.doe@example.com", 30),
    (2, "Jane Smith", "jane.smith@example.com", 25),
    (3, "Alice Johnson", "alice.johnson@example.com", 28),
    (4, "Bob Brown", "bob.brown@example.com", 35),
    (5, "Carol White", "carol.white@example.com", 22),
    (6, "David Black", "david.black@example.com", 40),
    (7, "Eve Green", "eve.green@example.com", 32),
    (8, "Frank Blue", "frank.blue@example.com", 27),
    (9, "Grace Red", "grace.red@example.com", 24),
    (10, "Hank Yellow", "hank.yellow@example.com", 33),
    (11, "Ivy Purple", "ivy.purple@example.com", 26),
    (12, "Jack Orange", "jack.orange@example.com", 29),
    (13, "Karen Pink", "karen.pink@example.com", 31),
    (14, "Leo Brown", "leo.brown@example.com", 34),
    (15, "Mia White", "mia.white@example.com", 23),
    (16, "Nina Black", "nina.black@example.com", 38),
    (17, "Oscar Green", "oscar.green@example.com", 21),
    (18, "Paul Blue", "paul.blue@example.com", 36),
    (19, "Quinn Red", "quinn.red@example.com", 37),
    (20, "Rachel Yellow", "rachel.yellow@example.com", 20),
    (21, "Sam Purple", "sam.purple@example.com", 41),
    (22, "Tina Orange", "tina.orange@example.com", 39),
    (23, "Uma Pink", "uma.pink@example.com", 42),
    (24, "Vince Brown", "vince.brown@example.com", 43),
    (25, "Wendy White", "wendy.white@example.com", 44),
    (26, "Xander Black", "xander.black@example.com", 45),
    (27, "Yara Green", "yara.green@example.com", 46),
    (28, "Zane Blue", "zane.blue@example.com", 47),
    (29, "Ada Red", "ada.red@example.com", 48),
    (30, "Bill Yellow", "bill.yellow@example.com", 49)
]

    # Execute the query for each user
    try:
        for user in users:
            sql = f"INSERT INTO USER (ID, NAME, EMAIL, AGE) VALUES ({user[0]}, '{user[1]}', '{user[2]}', {user[3]})"
            # print(sql)
            cusrsor.execute(sql)
    except:
        pass

    friends = [(1, 1, 2), (2, 1, 3), (3, 2, 4), (4, 3, 4), (5, 3, 5),
    (6, 4, 6), (7, 5, 7), (8, 6, 8), (9, 7, 9), (10, 8, 10),
    (11, 9, 11), (12, 10, 12), (13, 11, 13), (14, 12, 14), (15, 13, 15),
    (16, 14, 16), (17, 15, 17), (18, 16, 18), (19, 17, 19), (20, 18, 20),
    (21, 29, 1), (22, 30, 2)]

    try:
        for friend in friends:
            sql = f"INSERT INTO FRIEND (ID, USER_ID, FRIEND_ID) VALUES ({friend[0]}, {friend[1]}, {friend[2]})"
            # print(sql)
            cusrsor.execute(sql)
    except:
        pass

    conn.commit()
    cusrsor.close()
    conn.close()

# feed_data()
  
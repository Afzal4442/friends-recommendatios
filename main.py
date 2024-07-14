import db_connector
import feed_data
cusrsor,conn = db_connector.get_db_connection()


def main():
    # Query for getting friend of frind who is not frind of defined user
    # We are taking user id = 1 for our example 
    user_id = 1
    query = f"select user.name, user.email, user.age from user join friend f1 on user.id=f1.user_id join friend f2 on f1.friend_id=f2.user_id where f1.user_id={user_id} and f2.friend_id <> {user_id} AND f2.friend_id NOT IN (SELECT friend_id FROM friend WHERE user_id = {user_id});"
    cusrsor.execute(query)
    friends_suggestions = cusrsor.fetchall()

    print(friends_suggestions)


if __name__ == "__main__":
    main()
from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    #app.run()
    captain = User()
    captain.name = "Ridley"
    captain.surname = 'Scott'
    captain.age = 21
    captain.position = 'captain'
    captain.speciality = 'research engineer'
    captain.address = 'module_1'
    captain.email = 'scott_chief@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(captain)
    db_sess.commit()

    captain1 = User()
    captain1.name = "Tom"
    captain1.surname = 'Mccall'
    captain1.age = 25
    captain1.position = 'not captain'
    captain1.speciality = 'engineer'
    captain1.address = 'module_2'
    captain1.email = 'mccal_eigeneer@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(captain1)
    db_sess.commit()

    captain2 = User()
    captain2.name = "Aonung"
    captain2.surname = 'Baidan'
    captain2.age = 37
    captain2.position = 'not captain'
    captain2.speciality = 'engineer'
    captain2.address = 'module_3'
    captain2.email = 'Baidan_eigineer@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(captain2)
    db_sess.commit()

    captain3 = User()
    captain3.name = "Asick"
    captain3.surname = 'Tomphson'
    captain3.age = 20
    captain3.position = 'not captain'
    captain3.speciality = 'engineer'
    captain3.address = 'module_4'
    captain3.email = 'Tom_eigeneer@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(captain3)
    db_sess.commit()



if __name__ == '__main__':
    main()
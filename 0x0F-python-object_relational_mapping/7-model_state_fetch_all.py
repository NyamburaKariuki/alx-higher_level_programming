#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    eng = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1],
                                                           argv[2], argv[3])
    engine = create_engine(eng)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query and display results
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

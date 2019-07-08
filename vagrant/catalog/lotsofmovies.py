from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Genre, Base, Movie

engine = create_engine('sqlite:///genremovie.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Movie for Action & Adventure
genre1 = Genre(name="Action & Adventure")

session.add(genre1)
session.commit()

movie1 = Movie(name="Jurassic World", description="Owen and Claire return to the ruins of the Jurassic World theme park to rescue the remaining dinosaurs from a looming volcanic extinction",
                     director="J.A. Bayona", starring="Chris Pratt, Bryce Dallas Howard, Rafe Spall", genre=genre1)


session.add(movie1)
session.commit()

movie2 = Movie(name="Venom", description="Tom Hardy stars as the lethal protector and anti-hero Venom - one of Marvel's most enigmatic and complex characters",
                     director="Ruben Fleischer", starring="Michelle Williams, Reid Scott", genre=genre1)

session.add(movie2)
session.commit()

movie3 = Movie(name="Deadpool", description="The Super Duper Cut, now with 15 minutes of brand-new action and jokes lovingly inserted throughout",
                     director="David Leitch", starring="Ryan Reynolds", genre=genre1)

session.add(movie3)
session.commit()




# Movie list for Children & Family
genre2 = Genre(name="Children & Family")

session.add(genre2)
session.commit()


movie1 = Movie(name="Kung Fu Panda", description="Four young pandas go on the adventure of a lifetime",
                     director="John Stevenson", starring="Jack Black, Dustin Hoffman, Angelina Jolie", genre=genre2)

session.add(movie1)
session.commit()

movie2 = Movie(name="Ronja, the Robber's Daughter", description="The daughter of a professional robber, Ronja realizes the complicated nature of her father's profession when she befriends Birk, the child of a rival tribe",
                     director="Goro Miyazaki", starring="Gillian Anderson, Theresa Gallagher", genre=genre2)

session.add(movie2)
session.commit()

movie3 = Movie(name="Teenage Mutant Ninja Turtles", description="The Turtles have been forced to move in with their friend the news reporter April O'Neil, because the Foot Clan knows the whereabouts of their lair in the sewers",
                     director="	Michael Pressman, Michael Pressman", starring="	Paige Turco, David Warner, Michelan Sisti", genre=genre2)

session.add(movie3)
session.commit()
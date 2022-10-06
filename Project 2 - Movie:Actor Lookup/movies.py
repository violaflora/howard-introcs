"""
Do this first!

Adds values to the movie_dict for a new movie name.
If movie name is not in movie_dict, add a new entry.

If the movie_name is already in movie_dict, append the
actors to the existing actors. There should be no
repeat actor names.

Args:
  movie_dict: A movie dictionary.
  movie_name: A string representing the unique name of a movie.
  actors: A list of strings representing the actors in that movie.

Returns the movie_dict.
"""
def add_or_update_a_movie(movie_dict, movie_name, actors):
  if movie_name not in movie_dict:
    movie_dict[movie_name] = actors
  else:
    for ac in actors:
      movie_dict[movie_name].append(ac)
  return movie_dict

"""
Removes an actor from movie_name in a movie_dict object.

Args:
  movie_dict: A movie dictionary.
  movie_name: A string representing the unique name of a movie.
  actors: A list of strings representing the actors in that movie.

Returns the movie_dict.
"""
def remove_actor_from_movie(movie_dict, movie_name, actors):
  movie_dict[movie_name] = [i for i in movie_dict[movie_name] if i not in actors]
  return movie_dict

"""
Given a movie dictionary, returns the movie with the most actors.
In the case of a tie, any single movie is acceptable.

Args:
  movie_dict: A movie dictionary.

Returns a string.
"""
def find_movie_with_most_actors(movie_dict):
  mostActors = 0
  mostActorsMovie = ""
  for key,value in movie_dict.items():
    if len(value) > mostActors:
      mostActors = len(value)
      mostActorsMovie = key
  return mostActorsMovie

"""
Given two actors, returns an array of movie names in which both
actors appear.

Args:
  actor_1: {str} Name of first actor.
  actor_2: {str} Name of second actor.

Returns an array of strings.
"""
similarMovies = []
def find_similar_movies(movie_dict, actor1, actor2):
  for key,value in movie_dict.items():
    if actor1 in value and actor2 in value:
      similarMovies.append(key)
  return similarMovies

"""
Given a movie dictionary, returns the actor which has been in
the most movies.

Args:
  movie_dict: A movie dictionary.

Returns a string.
"""
def find_actor_with_most_movies(movie_dict):
  actors = {}
  for movie in movie_dict:
    for ac in movie_dict[movie]:
      if ac not in actors:
        actors[ac] = 1
      else:
        actors[ac] += 1
  mostMovies = 0
  mostMoviesActor = ""
  for key,value in actors.items():
    if actors[key] > mostMovies:
      mostMovies = value
      mostMoviesActor = key
  return mostMoviesActor

"""
Opens a file named movie_filename. Each line in this
file is formatted as follows:

movie_1,actor_a,actor_b,actor_c,.....
movie_2,actor_d,actor_e,actor_a
movie_3,actor_e,....
...

This function returns a movie dictionary with the
correct mappings from the given file.
"""
def parse_movie_text_file(movie_filename):
  dictionary = {}
  f = open(movie_filename, "r")
  lines = f.readlines()
  for line in lines:
    entry = line.split(",")
    key = entry[0]
    value = entry[1:]
    dictionary[key] = value
  f.close()
  return dictionary

"""
Extra credit!

The six degrees of Kevin Bacon is a game which
attempts to find how many movies apart a given actor
is to Kevin Bacon. If they have been in a movie with
Kevin Bacon, they are one degree from Kevin Bacon. If
the actor has been in a movie with an actor who has
been in a movie with Kevin Bacon, then they are two
degrees away from Kevin Bacon.

https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon

Write a function which when given two actors, returns 
the number of degrees between actor1 and actor2.

Args:
  actor_1: {str} Name of first actor.
  actor_2: {str} Name of second actor.

Returns an integer.
"""
def degrees_between(actor1, actor2):
    pass


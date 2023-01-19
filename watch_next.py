import spacy
nlp = spacy.load('en_core_web_md')

# The description of Planet Hulk
planet_hulk= nlp('Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,\
    the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can \
    live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.')

def watch_next(planet_hulk):
    # Read file
    # f = open('movies.txt', 'r+')
    with open('movies.txt', 'r+') as f:
        movie_list = []
        similarity_list = []
        for line in f:
            movie_list.append(line)
            description = line.split()[1]
            tokens = nlp(description)
            similarity = planet_hulk.similarity(tokens)
            similarity_list.append(similarity)
    # Find the largest similarity and the index
    index = similarity_list.index(max(similarity_list))
    # get the movie title
    movie_title = movie_list[index].split()[0] + ' ' + movie_list[index].split()[1]
    print(movie_title)
    return(movie_title)

watch_next(planet_hulk)
# print first and last movie in the from list 

movies = []

for i in range(3):

    movie = input(f"\n Enter {i+1} movie name: ")

    if movie == "":
        print("\n Movie name can not be emputy")
        continue
    movie = movie.strip().title()
    movies.append(movie)

print("\n ==== Movies ====")

for movie in movies:
    print(f"\n {movie}")

if len(movies) > 0:
    print(f"\n 1⃣ First movie {movies[0]}")
    print(f"\n 2⃣  Second movie {movies[-1]}")

else:
    print("\n Movies were not saved")
 

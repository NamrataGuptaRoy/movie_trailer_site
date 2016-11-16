import fresh_tomatoes
import media
dhamal=media.Movie("Dhamal","Comedy","http://static.koimoi.com/wp-content/new-galleries/2014/02/bollywoods-best-7-road-movie-3.jpg","https://www.youtube.com/watch?v=LKNHVDPKy7g")
babys_day_out=media.Movie("Baby's Day Out","Adventure of a kid","https://images-na.ssl-images-amazon.com/images/I/51P1VQ7X1BL.jpg","https://www.youtube.com/watch?v=7V6XjKJx1HM")
kahani=media.Movie("Kahani2","Thriller","https://humptydumptyonawall.files.wordpress.com/2013/01/vidya-balan-kahaani-movie-poster.jpg","https://www.youtube.com/watch?v=Ez4mXaeSKuk")
ajab_prem=media.Movie("Ajab prem ki gazab kahani","Romantic","https://i.ytimg.com/vi/j0Yx8BLkox4/maxresdefault.jpg","https://www.youtube.com/watch?v=j0Yx8BLkox4")


movies=[dhamal,babys_day_out,kahani,ajab_prem]
fresh_tomatoes.open_movies_page(movies)

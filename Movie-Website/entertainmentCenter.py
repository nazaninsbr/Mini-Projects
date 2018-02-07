import media
import fresh_tomatoes

if __name__ == '__main__':
	avatar = media.Movie("Avatar", "./avatar.jpg", "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved.","https://www.youtube.com/watch?v=uZNHIU3uHT4")
	toystory = media.Movie("Toy Story", "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450", "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen) action figure.", "https://www.youtube.com/watch?v=gFTXLCCPPCs")
	saveTheLastDance = media.Movie("Save the Last Dance", "http://www.gstatic.com/tv/thumb/movieposters/26927/p26927_p_v8_aa.jpg", "Sara (Julia Stiles) is moved from a small Midwestern town to the south side of Chicago when her mother dies in a car accident, and must live with her father.", "https://www.youtube.com/watch?v=dhAxDeSxYbQ")

	movies = [avatar, toystory, saveTheLastDance]

	fresh_tomatoes.open_movies_page(movies)
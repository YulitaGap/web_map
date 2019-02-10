Lab №2 - readme.txt

How To Run:
    run module web_mapping.py with python 3.6

Files Included With This Project:
    
    web_mapping.py          Map_World_War.html
    locations.list          locations.csv
    Map_ 1909film.html      Map_2000.html
    requirements.txt        rating.csv


Main module,block of functions : 

                                 - reads files, 
                                 - takes needed info about 1939 and 1945 years cinematography,
                                 - decodes filming location into geographical longitude and latitude , 
                                 - creates a web_map,
                                 - counts amount of filmed movies for all locations and defines top 50,
                                 - adds 3 layers to map
                                 - adds markers and circles to map according to data received by functions

                    

Project Issues:
        
        1)This map was created in purpose to show how cinematography
        has been developing  during the II World War.
        (The result is shown on 2 layers of map)   
        
        2)The 2nd issue was to get top 50 locations by amount of movies filmed there.
        (The result of full research for all locations is in file.csv)

        
        Therefore 3 layers were created on map:        
        1)"Start of 2 world war" - shows all locations where in 1939 were filmed movies.
        2)"Middle of 2 world war" - shows all locations where in 1945 were filmed movies.
        3)"Most popular" - shows top 50 locations with maximal amount of movies filmed there.

        I also upload examples of how this map could be build for other years,user may need(1909,2000)

Profiling Results: 

    summary of films in 1939 is 2973 and 1265 in 1945.
    If to compare with other periods, cinematography has always been growing, but here we can see the result of
    how war influences on cultural regress.
    Also we can see that mainly the amount of movies has been reduced for territories involved in II World War
    (South and North America, Europe, China and Australia)


Analysis Results: 
                  
                  if to take in consideration the list of top 50 locations we can see that :
                  1-3 places take Great Britain(London,Leicester Leicestershire England UK)
                                  USA(Los Angeles, New York,Hollywood Nashville,Chicago)
                                  Canada(Toronto,London Ontario,Vancouver)
                  Other popular places are in Argentina,Germany,Hungary and Australia.
                  On the map you can see:
                  darkred - the most filmed locations
                  red - locations,where 20 000 - 30 000 movies where filmed
                  orange - 10 000 - 20 000 movies filmed there
                  light orange - less then 10 000 movies but in top 50.

Description of result html file:
 Tags included:
 1) \<!DOCTYPE html>- defines the type of our document as HTML ;

 2) \<head> - defines tech information about document, is a container for all the head elements,
             including scripts, styles, meta information
 3) \<meta> - defines meta-tags, which  store the service information for browsers and search engines(http-equid,content,name)

 4) \<script> - is used to define a client-side script (async,type charset defer)

 5) \<link> - defines relation with outward document

 6) \<style> - defines styles of different elements of web-page(type, media, scoped)

 7) \<div> - defines chapter(part, block in document)

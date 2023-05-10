from apis import spotify
from apis import sendgrid

genres= spotify.get_genres_abridged()

counter = 0

#genre lists
user_genres_num =[]
user_genres_num_list =[]
user_genre_list=['NONE SELECTED']
genre_list=[]

#artist lists
user_artists_num =[]
user_artists_num_list =[]
user_artist_list=['NONE SELECTED']
artist_list=[]

user_artist_id = []
user_artist_id_num_list = []
user_artist_id_list=['NONE SELECTED']
artist_id_list =[]

#track lists
user_tracks_num =[]
user_tracks_num_list =[]
user_track_list=['NONE SELECTED']
track_list=[]

def make_setting_browse_options():
    print('-' * 60)
    print('Setting/Browse Options')
    print('-' * 60)
    print('1 - Select your favorite genres', '         ', user_genre_list)
    print('2 - Select your favorite artists','        ', user_artist_list)
    print('3 - Discover new music')
    print('4 - Quit')
    print('-' * 60)

def get_user_choice():
    while True:
        try:
            user_choice=int(input('What would you like to do?'))
            if user_choice == 4:
                return 4
        except:
            print('Please enter a number.')
            continue
        if user_choice < 1 or user_choice > 4:
            print('Your number must be between 1 and 4.')
            continue
        return user_choice
        
while True:
    make_setting_browse_options()
    user_choice= get_user_choice()
    
    ####### Selecting genres #######
    if user_choice == 1:
        for genre in genres:
            counter +=1
            genre_number = str(counter)+' '+genre
            genre_list.append(genre_number)
            if counter < 10:  
                print(' '+ str(counter)+'.', genre)
            elif counter < 26:
                print(str(counter)+'.', genre)
        counter =0
        print()
        
        user_genres = input('Please select up to 3 genres as a comma-delimited list of numbers (no spaces please). Order numbers from least to greatest. Type "clear" to clear out genres:')
        user_genres_num.append(user_genres)
        
        user_genres_num_list=user_genres_num[0].split(',')
        

        print(user_genres_num)
        print(user_genres_num_list)
        
        user_genre_list.clear()
        for item in genre_list:
            if len(user_genres_num_list) == 1:
                if int(item.split()[0]) == int(user_genres_num_list[0]):
                    user_genre_list.append(item.split()[1])
            elif len(user_genres_num_list) == 2:
                if int(item.split()[0]) == int(user_genres_num_list[0]):
                    user_genre_list.append(item.split()[1])
                elif int(item.split()[0]) == int(user_genres_num_list[1]):
                    user_genre_list.append(item.split()[1])
            elif len(user_genres_num_list) == 3:
                if int(item.split()[0]) == int(user_genres_num_list[0]):
                    user_genre_list.append(item.split()[1])
                elif int(item.split()[0]) == int(user_genres_num_list[1]):
                    user_genre_list.append(item.split()[1])
                elif int(item.split()[0]) == int(user_genres_num_list[2]):
                    user_genre_list.append(item.split()[1])
                
        if user_genres == 'clear':
            counter=0
            user_genres_num.clear()
            user_genres_num_list.clear()
            user_genre_list.clear()
            genre_list.clear()
            user_genre_list.append('NONE SELECTED')

            
    ####### Selecting artists #######
    elif user_choice == 2:
        user_artist=input('Enter the name of an artist')
        artists = spotify.get_artists(user_artist)
        print()
        print('The folllowing artists were found...')
        print()
        
        for artist in artists:
            counter +=1
            artist_number = str(counter)+'.'+ artist.get('name')
            artist_id = str(counter)+'.'+ artist.get('id')
            artist_list.append(artist_number)
            artist_id_list.append(artist_id)
            if counter < 10:
                print(' '+ str(counter)+'.', artist.get('name'))
            elif counter < 30:
                print(str(counter)+'.', artist.get('name'))
        counter=0
        print()

        user_artists = input('Please select up to 3 artist as a comma-delimited list of numbers (no spaces please). Type "clear" to clear out artists:')
        user_artists_num.append(user_artists)
        user_artists_num_list=user_artists_num[0].split(',')
        
        user_artist_id.append(user_artists)
        user_artist_id_list=user_artists_num[0].split(',')

        user_artist_list.clear()
        for item in artist_list:
            if len(user_artists_num_list) == 1:
                if int(item.split('.')[0]) == int(user_artists_num_list[0]):
                    user_artist_list.append(item.split('.')[1])
            elif len(user_artists_num_list) == 2:
                if int(item.split('.')[0]) == int(user_artists_num_list[0]):
                    user_artist_list.append(item.split('.')[1])
                elif int(item.split('.')[0]) == int(user_artists_num_list[1]):
                    user_artist_list.append(item.split('.')[1])
            elif len(user_artists_num_list) == 3:
                if int(item.split('.')[0]) == int(user_artists_num_list[0]):
                    user_artist_list.append(item.split('.')[1])
                elif int(item.split('.')[0]) == int(user_artists_num_list[1]):
                    user_artist_list.append(item.split('.')[1])
                elif int(item.split('.')[0]) == int(user_artists_num_list[2]):
                    user_artist_list.append(item.split('.')[1])

        user_artist_id_list.clear()
        for item in artist_id_list:
            if len(user_artists_num_list) == 1:
                if int(item.split('.')[0]) == int(user_artists_num_list[0]):
                    user_artist_id_list.append(item.split('.')[1])
            elif len(user_artists_num_list) == 2:
                if int(item.split('.')[0]) == int(user_artists_num_list[0]):
                    user_artist_id_list.append(item.split('.')[1])
                elif int(item.split('.')[0]) == int(user_artists_num_list[1]):
                    user_artist_id_list.append(item.split('.')[1])
            elif len(user_artists_num_list) == 3:
                if int(item.split('.')[0]) == int(user_artists_num_list[0]):
                    user_artist_id_list.append(item.split('.')[1])
                elif int(item.split('.')[0]) == int(user_artists_num_list[1]):
                    user_artist_id_list.append(item.split('.')[1])
                elif int(item.split('.')[0]) == int(user_artists_num_list[2]):
                    user_artist_id_list.append(item.split('.')[1])

        if user_artists == 'clear':
            counter=0
            user_artists_num.clear()
            user_artists_num_list.clear()
            user_artist_list.clear()
            artist_list.clear()
            user_artist_id.clear()
            user_artist_id_num_list.clear()
            user_artist_id_list.clear()
            artist_id_list.clear()
            user_artist_list.append('NONE SELECTED')


    ##### Discover new music/email recommendations ######
    elif user_choice == 3:
        track_recommendations = spotify.get_similar_tracks(artist_ids=user_artist_id_list, genres=user_genre_list)
        spotify.print_formatted_tracklist_table(track_recommendations)
        email_choice=input('Would you like to email this list to a friend? (y/n)')
        if email_choice.lower() == 'n':
            continue
        elif email_choice.lower() == 'y':
            sender_email=input('What is your email address?')
            recipient_email= input('Whose would you like to send the email to?')
            message=input('What would you like to say about this playlist?')
            email_subject = 'Playlist Recommendation from Spotify: '+message
            email_message=spotify.get_formatted_tracklist_table_html(track_recommendations)
            sendgrid.send_mail(
                sender_email,
                recipient_email,
                email_subject,
                email_message)
        
    ##### Quit program#######        
    elif user_choice == 4:
        print('Quitting the program...')
        break





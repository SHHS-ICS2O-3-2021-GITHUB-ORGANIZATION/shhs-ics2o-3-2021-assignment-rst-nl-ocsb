# NAME OF AUTHOR: Nyandea Lansana
# NAME OF THE PROGRAM: Lit Trivia Game 
# DATE OF CREATION: Jan. 28, 2022- Feb. 02, 2022.
# PURPOSE OF PROGRAM: To create a fun and engaging trivia game with different sections. 

# Program Title
print ("✦𝕷𝖎𝖙 𝕿𝖗𝖎𝖛𝖎𝖆✦")


# Importing a random and time module so the questions can be randomize
# and that the game runs smoothly
import random
import time


# Created a dictionary of questions for each sections and it's correct 
# answers, in addition to that, a dictionary of answers to all the questions 
hist_geo_dict = {
    "\nWhich 20th Century conflict led US soldiers to die for a tie?" : "C", 
    "\nWhat is the birthplace of Napoleon Bonaparte?" : "A", 
    "\nMumbai, Chennai and Kolkata are major cities in which country?" : "E", 
    "\nWhat is the tallest mountain in the world?" : "D",
    "\nWhich Italian city is famous for its canals?" : "B",
    "\nWhat are the only two countries to have a land border with the US?" : "E",
    "\nIn 1930, which was also called the tragic year, how many Americans were unemployed?" : "A" ,
    "\nName the Filipino who was nicknamed the Iron Butterfly." : "B",
    "\nIn opposition to World War I, what grew popular in the 1920s?" : "E",
    "\nThe British Raj lasted how many years in India?" : "C",
    "\nWhat was the first country to use postcards?" : "A",
    "\nFrom 1933 to 1945, which country maintained an official state of emergency?" : "D", 
    "\nWinston Churchill was held captive as a prisoner during which war?" : "B",
    "\nHow many states are there in the United States?" : "A",
    "\nWhat country has the most natural lakes?" : "E",
    "\nWhat is the name of the river that flows through the Brazil rainforest?" : "D",
    "\nWhat is the official currency of the United Kingdom?" : "C",
    "\nWhat razor-thin country accounts for more than half of the western coastline of South America?" : "E",
    "\nWhat is the only sea without any coasts?" : "C",
    "\nWhat percentage of the River Nile is located in Egypt?" : "A",
    "\nWhat is the driest place on Earth?" : "B",
    "\nWhich African nation has the most pyramids?" : "D",
    "\nWhat is the oldest city in the world?" : "A",
    "\nWhat country is home to Kangaroo Island?" : "C",
    "\nWhat continent is located at Latitude 90° S Longitude 0.00° E?" : "A",
    "\nRiyadh is the capital of what Middle-Eastern country?" : "E",
    "\nWhich of these African nations is not landlocked?" : "E",
    "\nWhat is the smallest independent country on Earth?" : "A",
  }

hist_geo_list = [["A. The Boer War", "B. Kosovo War" ,"C. The Korean War", "D. Vietnam War", "E. Third Afghan War"], 
          ["A. Corsica, France", "B. Mexico City, Mexico", "C. Halifax, Nova Scotia", "D. Paris, France", "E. Bordeaux, France"], 
          ["A. Russia", "B. Soudi Arabia", "C. Bangladesh","D. Philippines", "E. India"],
          ["A. Mount Kangchenjunga", "B. Mount Kilimanjaro", "C. Mount Kailish", "D. Mount Everest", "E. Mount Lhotse"],
          ["A. Rome", "B. Venice", "C. Florence", "D. Naples", "E. Milan"],
          ["A. Denmark and Germany", "B. Mexico and Spain", "C. Haiti and France", "D. United Kingdom and Ireland", "E. Canada and Mexico"],
          ["A. More than 7 million", "B. One million", "C. More than twenty million", "D. One Hundred thousand", "E. More than twelve million"],
          ["A. Teodoro Agoncillo", "B. Imelda Marcos", "C. Encarnación Alzona", "D. Nicolas Zafra", "E. Ricardo Manapat"], 
          ["A. Poetry", "B. Songwriting", "C. Fashion","D. Movie Industry", "E. Jazz and dancing"],
          ["A. 100 years", "B. 5 weeks", "C. 90 years", "D. 12 Months", "E. 60 years"],
          ["A. Austria", "B. Spain", "C. United States", "D. France", "E. China"],
          ["A. France", "B. United States", "C. United Kingdom", "D. Germany", "E. Jamaica"],
          ["A. World War II", "B. The Boer War", "C. Arab Revolt in Palestine", "D. Jewish insurgency in Mandatory Palestine", "E. Kosovo War"],
          ["A. 50 states", "B. 30 states", "C. 13 states", "D. 40 states", "E. 55 states"],
          ["A. South Asia", "B. Philippines", "C. Italy", "D. France", "E. Canada"], 
          ["A. Rio Negro", "B. Paraguay River", "C. Parnaíba River","D. Amazon River", "E. Tocantins River"],
          ["A. Leones", "B. U.S Dollars", "C. Pound Sterling", "D. Euro", "E. Swiss Franc"],
          ["A. Ecuador", "B. Peru", "C. Argentina", "D. Bolivia", "E. Chile"],
          ["A. The Celebes Sea", "B. The Adriatic Sea", "C. The Sargasso Sea ", "D. The Mediterranean Sea", "E. The Red Sea"],
          ["A. 22 percent", "B. 100 percent", "C. 9 percent", "D. 83 percent", "E. 10 percent"],
          ["A. Atacama Desert", "B. McMurdo, Antarctica", "C. Sahara Desert", "D. Kufra, Libya", "E. Aoulef, Algeria"], 
          ["A. Libya", "B. Soudi Arabia", "C. Egypt","D. Sudan", "E. Algeria"],
          ["A. Damascus", "B. Jerusalem", "C. Athens", "D. Greece", "E. Jericho"],
          ["A. South Africa", "B. Great Britain", "C. Australia", "D. France", "E. Japan"],
          ["A. Antarctica", "B. Sierra Leone", "C. South America", "D. Asia", "E. Australia"],
          ["A. Yemen", "B. Iraq", "C. Syria", "D. Lesotho", "E. Saudi Arabia"],
          ["A. Nigeria", "B. Burkina Faso", "C. Chad", "D. Niger", "E. Congo"], 
          ["A. Vatican City", "B. Monaco", "C. Nauru","D. Grenada", "E. Dubai"]]

slang_dic_dict = {
    "\nIf something is 'fire', that means it is what? " : "E", 
    "\nWhat does 'spill the tea' mean?" : "B", 
    "\nWhat does GOAT stand for?" : "A", 
    "\nWhat is the meaning of the word 'fleek' ?": "D",
    "\nWhen someone says 'DM Me', that means what?" : "A",
    "\nIf someone is 'boujee', what does that mean?" : "E",
    "\nWhen someone says they're the 'CEO' of dancing, what does that mean?" : "B",
    "\nA snack is a term you might use to describe a person that you find?" : "D",
    "\nYou use this word when you’re so embarrased?" : "B",
    "\nIf you feel salty, it means that you are what?" : "A",
    "\n'Finna' is short for saying what?" : "D",
    "\nAnother word for a car is what?" : "E",
    "\nWhich of this terms convey being real, authentic, and truthful?" : "D",
    "\nWhat term do you use to describe throwing something away with high velocity?" : "E",
    "\nIf someone is 'Low Key', they're what?" : "A",
    "\nTFW is an abbreviation for?" : "D",
    "\n---------- refers to political awareness." : "C",
    "\n---------- is a term for agreement or approval." : "A",
    "\n----------- is a cool sense of style. It can refer to clothes or the way someone carries themselves." : "B",
    "\nIt's an act where someone stops communicating with a person." : "A",
    "\nIf you go through a positive physical, mental, or spiritual change, what does that mean?" : "D",
    "\nThis term is used to describe something that stands out from the rest or makes you feel different compared to other things.?" : "E",
    "\nWhat expression do you use when you find something hilarious?" : "A",
    "\nWhen someone says you're the 'main character', it means what?" : "B",
    "\nWhat does the word “periodt” mean?" : "C",
    "\nIf you're being mad or upset about something, you're what?" : "C",
    "\nThis is a term to describe how funny you find something." : "E",
    "\nAn adjective that describes how great something is" : "A",
  }          

slang_dic_list = [["A. It's burning", "B. It's shining really bright" ,"C. It's on fire", "D. Refers to combustion", "E. It's great or lit"], 
          ["A. You dropped your tea", "B. To tell the latest (gossip)", "C. To make a tea", "D. To go to a tea party", "E. To drink tea"], 
          ["A. Greatest of all times", "B. A big goat", "C. Going out at twelve","D. Get out and try", "E. Game of all thrones."],
          ["A. Being awful", "B. Acting out of anger", "C. Lame", "D. Flawless", "E. A person who lacks wisdom"],
          ["A. Direct Message", "B. Don't mention me", "C. Don't get married", "D. Come to my house", "E. Dinner at my place"],
          ["A. Someone who likes ugly things", "B. A place to sit and sing", "C. A difficult test", "D. Best friend", "E. Loves fancy and extravagant things"],
          ["A. Chief Executive Officer", "B. It means they are the very best at it or have mastered it", "C. It means they have a high rank in the dancing industry", "D. It means they're very important in dancing", "E. They invented dancing"],
          ["A. Funny", "B. Ugly", "C. Dumb", "D. Beautiful or attractive", "E. Ignorant"],
          ["A. Yikes", "B. Big Yikes", "C. Oh hell naw", "D. I'm so dead", "E. Ewwwwww"],
          ["A. Jealous", "B. Salty", "C. Picky", "D. Sad", "E. Happy"],
          ["A. About to", "B. Laying down", "C. Stepping out", "D. Going to", "E. Running to"],
          ["A. Splash", "B. Cool", "C. Sic", "D. Gorg", "E. Whip"],
          ["A. No hat", "B. No fax", "C. No pun intended", "D. No cap", "E. No lies"],
          ["A. Throw", "B. Drop", "C. Drag", "D. Fallen", "E. Yeet"],
          ["A. Calm or secretive", "B. Hyper and nice", "C. Outgoing and loud", "D. Quiet and unhappy", "E. Mean and bully"],
          ["A. That face when", "B. That friend woke", "C. That falling when", "D. That feeling when", "E. That fight well"],
          ["A. Aware", "B. Smark", "C. Woke", "D. Active", "E. Seeker"],
          ["A. Bet", "B. Agree", "C. Sign me up", "D. Double yes", "E. For sure"],
          ["A. Grip", "B. Drip", "C. Trip", "D. Whip", "E. Amazing"],
          ["A. Ghosting", "B. Blocking", "C. Disappearing", "D. Basic", "E. Dank"],
          ["A. Grow up", "B. Woke", "C. Educated", "D. A glow up", "E. Upgrade"],
          ["A. Real good", "B. For real", "C. The best", "D. Can't top this", "E. Hits different"],
          ["A. I'm dead", "B. I'm laughing so hard", "C. My eyes are watering", "D. OMGGGG", "E. I can't even"],
          ["A. It means you're amazing", "B. It means you have a natural charismatic energy", "C. Friendly", "D. Open-minded", "E. Brilliant"],
          ["A. A new version of period", "B. Period", "C. To add emphasis to something", "D. To say no", "E. To decline"],
          ["A. Irked", "B. Real deep", "C. Pressed", "D. Big L", "E. Stank"],
          ["A. Leaving me", "B. You lost me", "C. Chile, no", "D. Yooooooo", "E. Sending me"],
          ["A. Slaps", "B. Little", "C. Mid", "D. Whole breed", "E. Next level"]]

meme_quotes_dict= {
    "\nWho said; 'Mr. Vice President, I'm speaking.'" : "E", 
    "\n'Is that a chicken?' Is a 'heartfelt' word from who?" : "B", 
    "\nFinish the saying; 'My head, it don't move. You what -----------? " : "A", 
    "\nWho said 'That's suspicious...That's weird.'?": "D",
    "\n'Oh you look so cute sitting there doing -----------! Finish the famous words from Spencer." : "A",
    "\nComplete the saying; 'Oh no, our table, ----------.'" : "E",
    "\nWho said; 'So you just gonna bring me a birthday gift on my birthday to my birthday party on my birthday with a birthday gift.'?" : "B" ,
    "\nFinish the quote; “Are you not ashamed of yourself? Are you not embarrazzed?”" : "B", 
    "\nTakis are seriously --------?" : "E",
    "\nFinish the quote; “Can I get woah, can I get another woah, give me another one; woah." : "A",
    "\nWho said; “She can beat me, but she cannot beat my outfit.”?" : "D",
    "\nHi, I'm John Quinones, and this is -------------?" : "C",
    "\n“Where you silent or where you ----------?”" : "A",
    "\n“Waking up in the morning thinking about so many things. --------------”?" : "D",
    "\n“Don't you dare disobey me caroline. -----------------”?" : "A",
    "\n“Listen, you not a different breed. You just different! ----------------”?" : "A",
    "\n“I know I'm smiling right now, but the light inside of me is -----------”" : "B",
    "\n“So yeah, they hit me with that one. Doesn't even hurt, at this point I'm numb, there's no ----------”?" : "E",
    "\nA bug happened at the ending of this quote; “I don't see how you can hate from the outside of the club”, fix the ending?" : "C",
    "\n“Baby I'm not even here, --------------”?" : "D",
    "\n“Call an ambulance, call an ambulance, -------------”?" : "E",
    "\n“But imagine how tired we are, --------------”" : "D",
    "\n“It must be nice, I'm tryna get -----------”" : "A",
    "\nWho said; “It was supposed to give, but it didn't give.”?" : "D",
    "\n“That is very much ---------”" : "C",
    "\n“Ladies and gentlemen, the volume inside this bus, is ------------”" : "B",
    "\nFinish the iconic quote; “One eyes open when I'm sleeping, ----------.”" : "C",
    "\n“ARGHH!! Stop, I could have dropped my ----------”" : "A",
 }
        
meme_quotes_list = [["A. Donald Trump", "B. Melania Trump" ,"C. Khabane Lame", "D. Kim Kardashian", "E. Kamala Harris"], 
          ["A. Larri", "B. Kylie Jenner", "C. Nicki Minaj", "D. King Bach", "E. Lele Pons"], 
          ["A. I'm telling you", "B. I'm singing", "C. I'm being for real","D. It's worth, it won't move", "E. I give up."],
          ["A. Nicki Minaj", "B. Ariana Grande", "C. Megan Thee Stallion", "D. Cardi B", "E. Rico Nasty"],
          ["A. Absolutely nothing", "B. Doing duets and singing that song", "C. Nothing", "D. Something", "E. Stalking, are you happy"],
          ["A. It's cracked", "B. I don't like it", "C. We need a new one", "D. It hurt the dog", "E. It's broken"],
          ["A. Doja Cat", "B. Tyler, the Creator", "C. Hannah Stockings", "D. SZA", "E. Travis Scott"],
          ["A. I'm speechless", "B. This is really embarrazzing? ", "C. You need help", "D. This is bad", "E. I feel bad for you"],
          ["A. Awful", "B. Spicy", "C. The best", "D. Amazing", "E. Intense"],
          ["A. Call the ambulance, woah woah woah. ", "B. Woah Woah", "C. Now dance", "D. Hit the woah", "E. Let's go"],
          ["A. Saweetie", "B. Cardi B", "C. Mulatto", "D. Rihanna", "E. Normani"],
          ["A. Welcome back to the show", "B. Is my friend Johnny", "C. What would you do", "D. Today is the day", "E. This is my show"],
          ["A. Silenced", "B. Interrupted", "C. Stopped", "D. Threatened", "E. Paranoid"],
          ["A. I cried", "B. I just want money", "C. With no money", "D. I just wish things would get better", "E. Please help me"],
          ["A. Arghhhh Eeugh", "B. Come back here", "C. Listen to me", "D. Put it back", "E. I'm coming for you"],
          ["A. You weird, Goofball", "B. You're abnormal", "C. You're a cool breed", "D. You're from Area 51", "E. You're sick"],
          ["A. Shininggg", "B. Dyingggg", "C. Sparklinggg", "D. Happyyyy", "E. Burninggg"],
          ["A. Musicccc", "B. Lifeee", "C. Familyyy", "D. Moneyyyy", "E. Feelingsss"],
          ["A. When you like hating", "B. When you don't have money", "C. When you can't even get in.", "D. When you're broke", "E. Hahaaa"],
          ["A. You're not welcome", "B. Have a good day", "C. Goodbye", "D. I'm hallucination", "E. I'm dead"],
          ["A. Someone is hurt", "B. Please", "C. Help", "D. This guy is going to need it", "E. But not for me."],
          ["A. Imagine", "B. Don't say things like that", "C. True word", "D. Imagine how tired we are of it.", "E. Think about it"],
          ["A. Like you my boy.", "B. Like you my friend", "C. Like you mama", "D. Like you fam", "E. Like you shawty"],
          ["A. Beyonce", "B. Mariah Carey", "C. H.E.R", "D. Doja Cat", "E. Summer Walker"],
          ["A. Accurate", "B. Cringe", "C. Adequate", "D. Bad", "E. True"],
          ["A. Annoying", "B. Astronomical", "C. High", "D. Very much so inappropriate", "E. Rude"],
          ["A. My eyes would be close", "B. Two eye open when I'm sleeping", "C. One eyeeee", "D. No eyes open", "E. Okay good byeeee"],
          ["A. Croissant", "B. Phone", "C. Drink", "D. The water", "E. The baby"]]

movie_ent_dict= {
    "\nKim Kardashian was Paris Hilton's what?" : "A", 
    "\nAriana Grande got her start on what kids' TV show?" : "D", 
    "\nMariah Carey had her latest No.1 song with which single?" : "A", 
    "\nWhich tech entrepreneur named his son  X Æ A-12?": "C",
    "\nWhat is the name of Michelle Obama's 2018 memoir?" : "E",
    "\nWhat was the name of the boat in Jaw?" : "A",
    "\nWhich film written, directed, and produced by James Cameron went on to become the highest-grossing film of its time?" : "B" ,
    "\nWhat are the names of the stepsisters from Disney's Cinderalla?": "C",
    "\nWho is the oldest Kardashian sister?" : "E",
    "\nWhat is Rihanna's real name?" : "C",
    "\nWhich artist made history in 2020 as the youngest winner of the Grammy's four main categories?" : "B" ,
    "\nOn Lip Sync Battle, Tom Holland lip-synced to what song?": "A",
    "\nWhich film has Zendaya not performed in?" : "E",
    "\nWhich One Direction star created the 2019 hit 'Watermelon Sugar'?" : "E",
    "\nZendaya competed on what reality Show?": "B",
    "\nWho was the first African American to win an Academy Award for best actor?" : "C",
    "\nWhat was the first feature-length animated movie ever released?" : "D",
    "\nIn The Matrix, what was the colour of the pill Neo took?" : "C",
    "\nFor what movie did Tom Hanks score his first Academy Award nomination?" : "A",
    "\nWhat flavor of Pop Tarts does Buddy the Elf use in his spaghetti in Elf? " : "A",
    "\nWhat pop vocal group performs at the wedding in Bridesmaids?" : "B",
    "\nIn what 1950 drama does Bette Davis say, “Fasten your seatbelts; it’s going to be a bumpy night”?" : "C",
    "\nWho played park owner John Hammond in Jurassic Park?" : "D",
    "\nFor what movie did Steven Spielberg win his first Oscar for Best Director?" : "B",
  }
        
movie_ent_list = [["A. Closet Organizer", "B. Assistant" ,"C. Video Editor", "D. Campaign Manager", "E. Fashion Designer"], 
          ["A. Sam and Cat", "B. Don't Look Up", "C. Wicked", "D. Victorious", "E. Winx Club"], 
          ["A. All I Want For Christmas Is You", "B. Without You", "C. Oh Santa!","D. Fantasy", "E. My All"],
          ["A. Jeff Bezos", "B. Jack Dorsey", "C. Elon Musk", "D. Drew Houston", "E. Brian Chesky"],
          ["A. Will", "B. When Breath Becomes Air", "C. Night", "D. A Promised Land", "E. Becoming"],
          ["A. Orca", "B. Dexter", "C. Captain Ron", "D. Gone Fission", "E. The Inferno"],
          ["A. Avatar", "B. Titanic", "C. Romeo and Juliet", "D. Rambo", "E. Merchant of Venice"],
          ["A. Anna and Elsa", "B. Lilo and Stitch", "C. Anastasia and Drizella", "D. Andrina and Ariel", "E. Attina and Arista"], 
          ["A. Kim", "B. Khloe", "C. Kendall","D. Kylie", "E. Kourtney"],
          ["A. Onika Maraj", "B. Belcalis Almánzar", "C. Robyn Fenty", "D. Amala Dlamini", "E. Solána Rowe"],
          ["A. Dua Lipa", "B. Billie Eilish", "C. Olivia Rodrigo ", "D. Sabrina Carpenter", "E. Bhad Bhabie"],
          ["A. Umbrella", "B. Rain On Me", "C. 24K Magic", "D. Fair Trade", "E. Bad Guy"],
          ["A. The Greatest Showman", "B. Smallfoot", "C. Spider-Man: Homecoming", "D. Euphoria", "E. Hunger Games"],
          ["A. Liam Payne", "B. Zayn", "C. Louis Tomlinson", "D. Niall Horan", "E. Harry Styles"], 
          ["A. Dance Moms", "B. Dancing With The Stars ", "C. World of Dance","D. Bring It", "E. Legendary"],
          ["A. Denzel Washington", "B. Morgan Freeman", "C. Sidney Poitier", "D. Viola Davis", "E. Samuel L. Jackson"],
          ["A. Rapunzel", "B. Barney", "C. Beauty and the Beast", "D. Snow White and the Seven Dwarfs", "E. Dune"],
          ["A. Yellow", "B. Blue", "C. Red", "D. White", "E. Black"],
          ["A. Big", "B. Small", "C. Tiny", "D. Slim", "E. Wide"],
          ["A. Chocolate", "B. Strawberry", "C. Mint", "D. Blueberry", "E. Buttered Pecan"],
          ["A. Shane Filan", "B. Wilson Phillips", "C. Justin Timberlake", "D. Ringo Starr", "E. John Lennon"],
          ["A. Squid Game", "B. The Sleepover", "C. All About Eve", "D. Harry Potter", "E. Jaws"],
          ["A. Sam Neill", "B. Ariana Richards", "C. Ty Simpkins", "D. Richard Attenborough", "E. Jeff Goldblum"],
          ["A. Tenet", "B. Little Woman ", "C. The Father", "D. Another Round", "E. The Lord of the Rings"]]

riddles_dict= {
    "\nI am an odd number. Take away a letter and I become even. What number am I?" : "C", 
    "\nIf two’s company, and three’s a crowd, what are four and five?" : "A", 
    "\nWhat three numbers, none of which is zero, give the same result whether they’re added or multiplied?" : "D", 
    "\nWhat begins with an “e” and only contains one letter?" : "E",
    "\nWhat would you find in the middle of Toronto?" : "B",
    "\nYou see me once in June, twice in November and not at all in May. What am I?" : "A",
    "\nWhat word is pronounced the same if you take away four of its five letters?" : "C" ,
    "\nWhat is so fragile that saying its name breaks it?" : "A",
    "\nSpeaking of rivers, a man calls his dog from the opposite side of the river. The dog crosses the river without getting wet, and without using a bridge or boat. How?" : "D",
    "\nWhat can fill a room but takes up no space?" : "B",
    "\nIf you drop me, I’m sure to crack, but give me a smile and I’ll always smile back. What am I?" : "E",
    "\nWhat can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?" : "B",
    "\nMary has four daughters, and each of her daughters has a brother. How many children does Mary have?" : "E",
    "\nI can be entertaining until you realize some pieces have been lost. What am I?" : "C",
    "\nI live in the corn, and my job is to deter. Free from pests your crops I assure. What am I?" : "A",
    "\nWhat can you hold in your left hand and not in your right?" : "B",
    "\nIf an electric train is traveling south, which way is the smoke going?" : "C",
    "\nWhat is the end of everything?" : "E",
    "\nI speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?" : "B",
    "\nYou measure my life in hours and I serve you by expiring. I’m quick when I’m thin and slow when I’m fat. The wind is my enemy. What am I?" : "A",
    "\nI have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?" : "E",
    "\nWhat English word has three consecutive double letters?" : "B",
  }
        
riddles_list = [["A. Fourteen", "B. Seventeen" ,"C. Seven", "D. Five", "E. Three"], 
          ["A. Nine", "B. Four's a party and five's preparing to leave the group.", "C. Seven", "D. Four and five are too many", "E. Six"], 
          ["A. One, one, and one", "B. Three, four, and one", "C. Three, and three","D. One, two, and three", "E. Two, two, and one"],
          ["A. Evan", "B. Evening", "C. Ever", "D. Emoji message", "E. Envelope"],
          ["A. Yonge", "B. The letter “o”", "C. Bloor", "D. CN Tower", "E.Tour Casa Loma"],
          ["A. The letter “e”", "B. Rain", "C. Sunshine", "D. Snow", "E. The letter “a”"],
          ["A. Empty", "B. Check", "C. Queue", "D. Hail", "E. Ray"],
          ["A. Silence", "B. Sound", "C. Wave","D. An Echo", "E. Glass"],
          ["A. Someone carried the dog", "B. There was no river", "C. The river had a canoe", "D. The river was frozen", "E. The dog was a super dog"],
          ["A. Camera", "B. Light", "C. A human", "D. A wall", "E. Footsteps"],
          ["A. A puddle of water", "B. Refraction", "C. A transparent wall", "D. A phone", "E. A mirror"],
          ["A. A snake", "B. A river", "C. A car", "D. A tap", "E. A timer"],
          ["A. Six", "B. Sixteen", "C. Twelve","D. Seven", "E. Five"],
          ["A. A phone", "B. A car", "C. A puzzle", "D. Money", "E. A book"],
          ["A. A scarecrow", "B. A cat", "C. Repellers", "D. Containers", "E. Sound system"],
          ["A. Your left hand", "B. Your Right Elbow", "C. Your right hand", "D. Your left fingers", "E. Your right fingers"],
          ["A. East", "B. West", "C. There's no smoke", "D. North", "E. South"],
          ["A. Everthing", "B. A new thing", "C.The letters “ing”","D. The end", "E. The letter “g”"],
          ["A. Wind", "B. An echo", "C. Footsteps", "D. Shadow", "E. Water droplets"],
          ["A. A candle", "B. Hair", "C. Paint", "D. Grass", "E. Ladder"],
          ["A. A place", "B. A street", "C. A forest", "D. A haunted house", "E. A map"],
          ["A. Book man", "B. Bookkeeper", "C. Bookshelf", "D. Ending", "E. Beginning"]]

# Defined different functions to run the game
def play_another_round():
    # Asking for input if the user wants to play the game again
    response = input("Do you want to play again? Enter in yes or no: ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# Creating a function that displays the score to the user
def display_score(num_correct_ans, num_questions):
  score = int((num_correct_ans/num_questions)*100)
  print("\nYour score is: "+str(score)+"%")

# Defining the game sections throughout the game 
def hist_geo_game():
    answers = []
    questions = []
     
    # Get a list of random numbers to randomize the questions
    # Randomizing the questions, but only outputting ten questions
    random_num_list = random.sample(range(0, len(hist_geo_dict)), 10)
    random_num_list.sort()

    size_of_random_array = len(random_num_list)

    dict_index = 0
    for quest, ans in hist_geo_dict.items():
        if dict_index in random_num_list:
          questions.append(quest)
          answers.append(ans)
        dict_index +=1

    correct_answers = 0
    quest_ans_index = 0
    for rand_num in random_num_list:
      print(questions[quest_ans_index])
      for multiple_choice in hist_geo_list[rand_num]:
        print(multiple_choice)
  
      # Let it known to the user how to answer the questions. 
      user_input = input("Answer the question by entering A, B, C, D, or E")
      user_input = user_input.upper()
      if user_input == answers[quest_ans_index]:
        # Incrementing everytime 
        correct_answers += 1
        print("Correct!")
      else:
        # When the user doesn't get the correct answer, display the correct answers
        print("Incorrect! Correct answer is: " + answers[quest_ans_index])
      quest_ans_index +=1
    display_score(correct_answers, size_of_random_array)

def slang_dic_game():
    answers = []
    questions = []
     
    # Get a list of random numbers to randomize the questions
    random_num_list = random.sample(range(0, len(slang_dic_dict)), 10)
    random_num_list.sort()

    size_of_random_array = len(random_num_list)

    dict_index = 0
    for quest, ans in slang_dic_dict.items():
        if dict_index in random_num_list:
          questions.append(quest)
          answers.append(ans)
        dict_index +=1

    correct_answers = 0
    quest_ans_index = 0
    for rand_num in random_num_list:
      print(questions[quest_ans_index])
      for multiple_choice in slang_dic_list[rand_num]:
        print(multiple_choice)
  

      user_input = input("Answer the questions by entering A, B, C, D, or E")
      user_input = user_input.upper()
      if user_input == answers[quest_ans_index]:
        correct_answers += 1
        print("Correct!")
      else:
        print("Incorrect! Correct answer is: " + answers[quest_ans_index])
      quest_ans_index +=1
    display_score(correct_answers, size_of_random_array)

def meme_quotes_game():
    answers = []
    questions = []
     
    # Get a list of random numbers to randomize the questions
    random_num_list = random.sample(range(0, len(meme_quotes_dict)), 10)
    random_num_list.sort()

    size_of_random_array = len(random_num_list)

    dict_index = 0
    for quest, ans in meme_quotes_dict.items():
        if dict_index in random_num_list:
          questions.append(quest)
          answers.append(ans)
        dict_index +=1

    correct_answers = 0
    quest_ans_index = 0
    for rand_num in random_num_list:
      print(questions[quest_ans_index])
      for multiple_choice in meme_quotes_list[rand_num]:
        print(multiple_choice)
  

      user_input = input("Answer the questions by entering A, B, C, D, or E")
      user_input = user_input.upper()
      if user_input == answers[quest_ans_index]:
        correct_answers += 1
        print("Correct!")
      else:
        print("Incorrect! Correct answer is: " + answers[quest_ans_index])
      quest_ans_index +=1
    display_score(correct_answers, size_of_random_array)

def movie_ent_game():
    answers = []
    questions = []
     
    # Get a list of random numbers to randomize the questions
    random_num_list = random.sample(range(0, len(movie_ent_dict)), 10)
    random_num_list.sort()

    size_of_random_array = len(random_num_list)

    dict_index = 0
    for quest, ans in movie_ent_dict.items():
        if dict_index in random_num_list:
          questions.append(quest)
          answers.append(ans)
        dict_index +=1

    correct_answers = 0
    quest_ans_index = 0
    for rand_num in random_num_list:
      print(questions[quest_ans_index])
      for multiple_choice in movie_ent_list[rand_num]:
        print(multiple_choice)
  

      user_input = input("Answer the questions by entering A, B, C, D, or E")
      user_input = user_input.upper()
      if user_input == answers[quest_ans_index]:
        correct_answers += 1
        print("Correct!")
      else:
        print("Incorrect! Correct answer is: " + answers[quest_ans_index])
      quest_ans_index +=1
    display_score(correct_answers, size_of_random_array)
   
def riddles_game():
    answers = []
    questions = []
     
    # Get a list of random numbers to randomize the questions
    random_num_list = random.sample(range(0, len(riddles_dict)), 10)
    random_num_list.sort()

    size_of_random_array = len(random_num_list)

    dict_index = 0
    for quest, ans in riddles_dict.items():
        if dict_index in random_num_list:
          questions.append(quest)
          answers.append(ans)
        dict_index +=1

    correct_answers = 0
    quest_ans_index = 0
    for rand_num in random_num_list:
      print(questions[quest_ans_index])
      for multiple_choice in riddles_list[rand_num]:
        print(multiple_choice)

      user_input = input("Answer the questions by entering A, B, C, D, or E")
      user_input = user_input.upper()
      if user_input == answers[quest_ans_index]:
        correct_answers += 1
        print("Correct!")
      else:
        print("Incorrect! Correct answer is: " + answers[quest_ans_index])
      quest_ans_index += 1
    display_score(correct_answers, size_of_random_array)    
    
# INPUT
# Friendly user prompt
username = input("\nWhat's your name?")
# When their name is number, display an error prompt
while not username.isalpha():
    print("Invalid name!")
    username = input("Please enter your name: ")
    time.sleep(1)

# Telling the user about the sections and which one they would like to try.
welcome_string = "Hello " + str(username) + ", Welcome to Lit Trivia! What section of the trivia would you like to do?\n"
welcome_string += "There's world History and Geography, Slang Dictionary, Meme Quotes, Movie and Entertainment, and Riddles.\n"
print(welcome_string)

time.sleep(5)

# The start of the game
while True:
  option_string  = "\nPlease enter:\n1 for History and Geography\n"
  option_string += "2 for Slang Dictionary\n"
  option_string += "3 for Meme Quotes\n"
  option_string += "4 for Movie and Entertainment\n"
  option_string += "5 for Riddles\n"
  option_string += "Or enter in any other number to exit program\n"
  options = int(input(option_string))

  # If and Elif statements to decide what the user want to do
  # From here, the program loops back to the top whenever a section
  # comes to an end
  if options == 1:
      time.sleep(1)
      hist_geo_info_string = "\nWelcome to Lit Trivia's section on History and Geography. "
      hist_geo_info_string += "Have fun, and let's put your knowledge of History and Geography to the test.\n"
      print(hist_geo_info_string)
      time.sleep(4)
      hist_geo_game()

  elif options == 2:
      time.sleep(1)
      slang_dic_info_string = "\nWelcome " + str(username) +", it appears that you're interested in Lit Trivia's Slang Dictionary. "
      slang_dic_info_string += "However, this isn't your typical dictionary. "
      slang_dic_info_string += "I'd like to introduce you to the GenZ slang Dictionary. "
      slang_dic_info_string += "Have a good time and let's see how well you know your stuff.\n"
      print(slang_dic_info_string)
      time.sleep(7)
      slang_dic_game()
  
  elif options == 3:
      time.sleep(1)
      meme_quotes_info_string = "\nGreetings, and welcome to the Meme Quotes of Lit Trivia. "
      meme_quotes_info_string += "This, my friend, isn't your normal everyday quote collection. "
      meme_quotes_info_string += "The Memes Quotes are from well-known memes, Tiktoks, vines, and celebrities. "
      meme_quotes_info_string += "Have fun and see how much you can remember.\n"
      print(meme_quotes_info_string)
      time.sleep(7)
      meme_quotes_game()

  elif options == 4:
      time.sleep(1)
      print("Hey, and let's get Lit! Have fun and let's test your knowledge on movies and the entertainment industry.")
      time.sleep(4)
      movie_ent_game()

  elif options == 5:
      time.sleep(1)
      print("Say hello to Lit Trivia's riddles! Have fun, and fingers cross that you don't give up on these tough riddles.")
      time.sleep(4)
      riddles_game()

  if play_another_round():
    continue
  else:
    print("Well that was fun! Thanks for trying, bye.")
    break
exit(0)
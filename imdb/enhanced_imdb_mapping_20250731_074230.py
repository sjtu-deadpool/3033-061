#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MovieLens 100k IMDB ID Mapping (Enhanced Version)
Generated on: 2025-07-31 07:42:30
Progress: 27/1682 (1.6%)
Using enhanced Gemini API with natural language queries
"""

# MovieLens 100k IMDB ID Mapping
# Total verified IDs: 27

KNOWN_IMDB_IDS = {
    1: "0114709",    # Toy Story (1995) - animation, children's
    2: "0113189",    # GoldenEye (1995) - action, adventure
    3: "0113189",    # Four Rooms (1995) - thriller
    4: "0113161",    # Get Shorty (1995) - action, comedy
    5: "0112722",    # Copycat (1995) - crime, drama
    6: "0114948",    # Shanghai Triad (Yao a yao yao dao waipo qiao) (1995) - drama
    7: "0114746",    # Twelve Monkeys (1995) - drama, sci-fi
    8: "0112462",    # Babe (1995) - children's, comedy
    9: "0112818",    # Dead Man Walking (1995) - drama
    10: "0114279",    # Richard III (1995) - drama, war
    11: "0114369",    # Seven (Se7en) (1995) - crime, thriller
    12: "0114814",    # Usual Suspects, The (1995) - crime, thriller
    13: "0113851",    # Mighty Aphrodite (1995) - comedy
    14: "0110877",    # Postino, Il (1994) - drama, romance
    15: "0113824",    # Mr. Holland's Opus (1995) - drama
    16: "0113165",    # French Twist (Gazon maudit) (1995) - comedy, romance
    17: "0116367",    # From Dusk Till Dawn (1996) - action, comedy
    18: "0112443",    # White Balloon, The (1995) - drama
    19: "0112379",    # Antonia's Line (1995) - drama
    20: "0112377",    # Angels and Insects (1995) - drama, romance
    21: "0117110",    # Muppet Treasure Island (1996) - action, adventure
    22: "0112573",    # Braveheart (1995) - action, drama
    23: "0075314",    # Taxi Driver (1976) - drama, thriller
    24: "0114214",    # Rumble in the Bronx (1995) - action, adventure
    25: "0115685",    # Birdcage, The (1996) - comedy
    26: "0112585",    # Brothers McMullen, The (1995) - comedy
    27: "0109026",    # Bad Boys (1995) - action
}

# Complete movie list format
IMDB_LIST = [
    "0114709",  # 1. Toy Story (1995) - VERIFIED
    "0113189",  # 2. GoldenEye (1995) - VERIFIED
    "0113189",  # 3. Four Rooms (1995) - VERIFIED
    "0113161",  # 4. Get Shorty (1995) - VERIFIED
    "0112722",  # 5. Copycat (1995) - VERIFIED
    "0114948",  # 6. Shanghai Triad (Yao a yao yao dao waipo qiao) (1995) - VERIFIED
    "0114746",  # 7. Twelve Monkeys (1995) - VERIFIED
    "0112462",  # 8. Babe (1995) - VERIFIED
    "0112818",  # 9. Dead Man Walking (1995) - VERIFIED
    "0114279",  # 10. Richard III (1995) - VERIFIED
    "0114369",  # 11. Seven (Se7en) (1995) - VERIFIED
    "0114814",  # 12. Usual Suspects, The (1995) - VERIFIED
    "0113851",  # 13. Mighty Aphrodite (1995) - VERIFIED
    "0110877",  # 14. Postino, Il (1994) - VERIFIED
    "0113824",  # 15. Mr. Holland's Opus (1995) - VERIFIED
    "0113165",  # 16. French Twist (Gazon maudit) (1995) - VERIFIED
    "0116367",  # 17. From Dusk Till Dawn (1996) - VERIFIED
    "0112443",  # 18. White Balloon, The (1995) - VERIFIED
    "0112379",  # 19. Antonia's Line (1995) - VERIFIED
    "0112377",  # 20. Angels and Insects (1995) - VERIFIED
    "0117110",  # 21. Muppet Treasure Island (1996) - VERIFIED
    "0112573",  # 22. Braveheart (1995) - VERIFIED
    "0075314",  # 23. Taxi Driver (1976) - VERIFIED
    "0114214",  # 24. Rumble in the Bronx (1995) - VERIFIED
    "0115685",  # 25. Birdcage, The (1996) - VERIFIED
    "0112585",  # 26. Brothers McMullen, The (1995) - VERIFIED
    "0109026",  # 27. Bad Boys (1995) - VERIFIED
    "0000028",  # 28. Apollo 13 (1995) - PLACEHOLDER
    "0000029",  # 29. Batman Forever (1995) - PLACEHOLDER
    "0000030",  # 30. Belle de jour (1967) - PLACEHOLDER
    "0000031",  # 31. Crimson Tide (1995) - PLACEHOLDER
    "0000032",  # 32. Crumb (1994) - PLACEHOLDER
    "0000033",  # 33. Desperado (1995) - PLACEHOLDER
    "0000034",  # 34. Doom Generation, The (1995) - PLACEHOLDER
    "0000035",  # 35. Free Willy 2: The Adventure Home (1995) - PLACEHOLDER
    "0000036",  # 36. Mad Love (1995) - PLACEHOLDER
    "0000037",  # 37. Nadja (1994) - PLACEHOLDER
    "0000038",  # 38. Net, The (1995) - PLACEHOLDER
    "0000039",  # 39. Strange Days (1995) - PLACEHOLDER
    "0000040",  # 40. To Wong Foo, Thanks for Everything! Julie Newmar (1995) - PLACEHOLDER
    "0000041",  # 41. Billy Madison (1995) - PLACEHOLDER
    "0000042",  # 42. Clerks (1994) - PLACEHOLDER
    "0000043",  # 43. Disclosure (1994) - PLACEHOLDER
    "0000044",  # 44. Dolores Claiborne (1994) - PLACEHOLDER
    "0000045",  # 45. Eat Drink Man Woman (1994) - PLACEHOLDER
    "0000046",  # 46. Exotica (1994) - PLACEHOLDER
    "0000047",  # 47. Ed Wood (1994) - PLACEHOLDER
    "0000048",  # 48. Hoop Dreams (1994) - PLACEHOLDER
    "0000049",  # 49. I.Q. (1994) - PLACEHOLDER
    "0000050",  # 50. Star Wars (1977) - PLACEHOLDER
    "0000051",  # 51. Legends of the Fall (1994) - PLACEHOLDER
    "0000052",  # 52. Madness of King George, The (1994) - PLACEHOLDER
    "0000053",  # 53. Natural Born Killers (1994) - PLACEHOLDER
    "0000054",  # 54. Outbreak (1995) - PLACEHOLDER
    "0000055",  # 55. Professional, The (1994) - PLACEHOLDER
    "0000056",  # 56. Pulp Fiction (1994) - PLACEHOLDER
    "0000057",  # 57. Priest (1994) - PLACEHOLDER
    "0000058",  # 58. Quiz Show (1994) - PLACEHOLDER
    "0000059",  # 59. Three Colors: Red (1994) - PLACEHOLDER
    "0000060",  # 60. Three Colors: Blue (1993) - PLACEHOLDER
    "0000061",  # 61. Three Colors: White (1994) - PLACEHOLDER
    "0000062",  # 62. Stargate (1994) - PLACEHOLDER
    "0000063",  # 63. Santa Clause, The (1994) - PLACEHOLDER
    "0000064",  # 64. Shawshank Redemption, The (1994) - PLACEHOLDER
    "0000065",  # 65. What's Eating Gilbert Grape (1993) - PLACEHOLDER
    "0000066",  # 66. While You Were Sleeping (1995) - PLACEHOLDER
    "0000067",  # 67. Ace Ventura: Pet Detective (1994) - PLACEHOLDER
    "0000068",  # 68. Crow, The (1994) - PLACEHOLDER
    "0000069",  # 69. Forrest Gump (1994) - PLACEHOLDER
    "0000070",  # 70. Four Weddings and a Funeral (1994) - PLACEHOLDER
    "0000071",  # 71. Lion King, The (1994) - PLACEHOLDER
    "0000072",  # 72. Mask, The (1994) - PLACEHOLDER
    "0000073",  # 73. Maverick (1994) - PLACEHOLDER
    "0000074",  # 74. Faster Pussycat! Kill! Kill! (1965) - PLACEHOLDER
    "0000075",  # 75. Brother Minister: The Assassination of Malcolm X (1994) - PLACEHOLDER
    "0000076",  # 76. Carlito's Way (1993) - PLACEHOLDER
    "0000077",  # 77. Firm, The (1993) - PLACEHOLDER
    "0000078",  # 78. Free Willy (1993) - PLACEHOLDER
    "0000079",  # 79. Fugitive, The (1993) - PLACEHOLDER
    "0000080",  # 80. Hot Shots! Part Deux (1993) - PLACEHOLDER
    "0000081",  # 81. Hudsucker Proxy, The (1994) - PLACEHOLDER
    "0000082",  # 82. Jurassic Park (1993) - PLACEHOLDER
    "0000083",  # 83. Much Ado About Nothing (1993) - PLACEHOLDER
    "0000084",  # 84. Robert A. Heinlein's The Puppet Masters (1994) - PLACEHOLDER
    "0000085",  # 85. Ref, The (1994) - PLACEHOLDER
    "0000086",  # 86. Remains of the Day, The (1993) - PLACEHOLDER
    "0000087",  # 87. Searching for Bobby Fischer (1993) - PLACEHOLDER
    "0000088",  # 88. Sleepless in Seattle (1993) - PLACEHOLDER
    "0000089",  # 89. Blade Runner (1982) - PLACEHOLDER
    "0000090",  # 90. So I Married an Axe Murderer (1993) - PLACEHOLDER
    "0000091",  # 91. Nightmare Before Christmas, The (1993) - PLACEHOLDER
    "0000092",  # 92. True Romance (1993) - PLACEHOLDER
    "0000093",  # 93. Welcome to the Dollhouse (1995) - PLACEHOLDER
    "0000094",  # 94. Home Alone (1990) - PLACEHOLDER
    "0000095",  # 95. Aladdin (1992) - PLACEHOLDER
    "0000096",  # 96. Terminator 2: Judgment Day (1991) - PLACEHOLDER
    "0000097",  # 97. Dances with Wolves (1990) - PLACEHOLDER
    "0000098",  # 98. Silence of the Lambs, The (1991) - PLACEHOLDER
    "0000099",  # 99. Snow White and the Seven Dwarfs (1937) - PLACEHOLDER
    "0000100",  # 100. Fargo (1996) - PLACEHOLDER
    "0000101",  # 101. Heavy Metal (1981) - PLACEHOLDER
    "0000102",  # 102. Aristocats, The (1970) - PLACEHOLDER
    "0000103",  # 103. All Dogs Go to Heaven 2 (1996) - PLACEHOLDER
    "0000104",  # 104. Theodore Rex (1995) - PLACEHOLDER
    "0000105",  # 105. Sgt. Bilko (1996) - PLACEHOLDER
    "0000106",  # 106. Diabolique (1996) - PLACEHOLDER
    "0000107",  # 107. Moll Flanders (1996) - PLACEHOLDER
    "0000108",  # 108. Kids in the Hall: Brain Candy (1996) - PLACEHOLDER
    "0000109",  # 109. Mystery Science Theater 3000: The Movie (1996) - PLACEHOLDER
    "0000110",  # 110. Operation Dumbo Drop (1995) - PLACEHOLDER
    "0000111",  # 111. Truth About Cats & Dogs, The (1996) - PLACEHOLDER
    "0000112",  # 112. Flipper (1996) - PLACEHOLDER
    "0000113",  # 113. Horseman on the Roof, The (Hussard sur le toit, Le) (1995) - PLACEHOLDER
    "0000114",  # 114. Wallace & Gromit: The Best of Aardman Animation (1996) - PLACEHOLDER
    "0000115",  # 115. Haunted World of Edward D. Wood Jr., The (1995) - PLACEHOLDER
    "0000116",  # 116. Cold Comfort Farm (1995) - PLACEHOLDER
    "0000117",  # 117. Rock, The (1996) - PLACEHOLDER
    "0000118",  # 118. Twister (1996) - PLACEHOLDER
    "0000119",  # 119. Maya Lin: A Strong Clear Vision (1994) - PLACEHOLDER
    "0000120",  # 120. Striptease (1996) - PLACEHOLDER
    "0000121",  # 121. Independence Day (ID4) (1996) - PLACEHOLDER
    "0000122",  # 122. Cable Guy, The (1996) - PLACEHOLDER
    "0000123",  # 123. Frighteners, The (1996) - PLACEHOLDER
    "0000124",  # 124. Lone Star (1996) - PLACEHOLDER
    "0000125",  # 125. Phenomenon (1996) - PLACEHOLDER
    "0000126",  # 126. Spitfire Grill, The (1996) - PLACEHOLDER
    "0000127",  # 127. Godfather, The (1972) - PLACEHOLDER
    "0000128",  # 128. Supercop (1992) - PLACEHOLDER
    "0000129",  # 129. Bound (1996) - PLACEHOLDER
    "0000130",  # 130. Kansas City (1996) - PLACEHOLDER
    "0000131",  # 131. Breakfast at Tiffany's (1961) - PLACEHOLDER
    "0000132",  # 132. Wizard of Oz, The (1939) - PLACEHOLDER
    "0000133",  # 133. Gone with the Wind (1939) - PLACEHOLDER
    "0000134",  # 134. Citizen Kane (1941) - PLACEHOLDER
    "0000135",  # 135. 2001: A Space Odyssey (1968) - PLACEHOLDER
    "0000136",  # 136. Mr. Smith Goes to Washington (1939) - PLACEHOLDER
    "0000137",  # 137. Big Night (1996) - PLACEHOLDER
    "0000138",  # 138. D3: The Mighty Ducks (1996) - PLACEHOLDER
    "0000139",  # 139. Love Bug, The (1969) - PLACEHOLDER
    "0000140",  # 140. Homeward Bound: The Incredible Journey (1993) - PLACEHOLDER
    "0000141",  # 141. 20,000 Leagues Under the Sea (1954) - PLACEHOLDER
    "0000142",  # 142. Bedknobs and Broomsticks (1971) - PLACEHOLDER
    "0000143",  # 143. Sound of Music, The (1965) - PLACEHOLDER
    "0000144",  # 144. Die Hard (1988) - PLACEHOLDER
    "0000145",  # 145. Lawnmower Man, The (1992) - PLACEHOLDER
    "0000146",  # 146. Unhook the Stars (1996) - PLACEHOLDER
    "0000147",  # 147. Long Kiss Goodnight, The (1996) - PLACEHOLDER
    "0000148",  # 148. Ghost and the Darkness, The (1996) - PLACEHOLDER
    "0000149",  # 149. Jude (1996) - PLACEHOLDER
    "0000150",  # 150. Swingers (1996) - PLACEHOLDER
    "0000151",  # 151. Willy Wonka and the Chocolate Factory (1971) - PLACEHOLDER
    "0000152",  # 152. Sleeper (1973) - PLACEHOLDER
    "0000153",  # 153. Fish Called Wanda, A (1988) - PLACEHOLDER
    "0000154",  # 154. Monty Python's Life of Brian (1979) - PLACEHOLDER
    "0000155",  # 155. Dirty Dancing (1987) - PLACEHOLDER
    "0000156",  # 156. Reservoir Dogs (1992) - PLACEHOLDER
    "0000157",  # 157. Platoon (1986) - PLACEHOLDER
    "0000158",  # 158. Weekend at Bernie's (1989) - PLACEHOLDER
    "0000159",  # 159. Basic Instinct (1992) - PLACEHOLDER
    "0000160",  # 160. Glengarry Glen Ross (1992) - PLACEHOLDER
    "0000161",  # 161. Top Gun (1986) - PLACEHOLDER
    "0000162",  # 162. On Golden Pond (1981) - PLACEHOLDER
    "0000163",  # 163. Return of the Pink Panther, The (1974) - PLACEHOLDER
    "0000164",  # 164. Abyss, The (1989) - PLACEHOLDER
    "0000165",  # 165. Jean de Florette (1986) - PLACEHOLDER
    "0000166",  # 166. Manon of the Spring (Manon des sources) (1986) - PLACEHOLDER
    "0000167",  # 167. Private Benjamin (1980) - PLACEHOLDER
    "0000168",  # 168. Monty Python and the Holy Grail (1974) - PLACEHOLDER
    "0000169",  # 169. Wrong Trousers, The (1993) - PLACEHOLDER
    "0000170",  # 170. Cinema Paradiso (1988) - PLACEHOLDER
    "0000171",  # 171. Delicatessen (1991) - PLACEHOLDER
    "0000172",  # 172. Empire Strikes Back, The (1980) - PLACEHOLDER
    "0000173",  # 173. Princess Bride, The (1987) - PLACEHOLDER
    "0000174",  # 174. Raiders of the Lost Ark (1981) - PLACEHOLDER
    "0000175",  # 175. Brazil (1985) - PLACEHOLDER
    "0000176",  # 176. Aliens (1986) - PLACEHOLDER
    "0000177",  # 177. Good, The Bad and The Ugly, The (1966) - PLACEHOLDER
    "0000178",  # 178. 12 Angry Men (1957) - PLACEHOLDER
    "0000179",  # 179. Clockwork Orange, A (1971) - PLACEHOLDER
    "0000180",  # 180. Apocalypse Now (1979) - PLACEHOLDER
    "0000181",  # 181. Return of the Jedi (1983) - PLACEHOLDER
    "0000182",  # 182. GoodFellas (1990) - PLACEHOLDER
    "0000183",  # 183. Alien (1979) - PLACEHOLDER
    "0000184",  # 184. Army of Darkness (1993) - PLACEHOLDER
    "0000185",  # 185. Psycho (1960) - PLACEHOLDER
    "0000186",  # 186. Blues Brothers, The (1980) - PLACEHOLDER
    "0000187",  # 187. Godfather: Part II, The (1974) - PLACEHOLDER
    "0000188",  # 188. Full Metal Jacket (1987) - PLACEHOLDER
    "0000189",  # 189. Grand Day Out, A (1992) - PLACEHOLDER
    "0000190",  # 190. Henry V (1989) - PLACEHOLDER
    "0000191",  # 191. Amadeus (1984) - PLACEHOLDER
    "0000192",  # 192. Raging Bull (1980) - PLACEHOLDER
    "0000193",  # 193. Right Stuff, The (1983) - PLACEHOLDER
    "0000194",  # 194. Sting, The (1973) - PLACEHOLDER
    "0000195",  # 195. Terminator, The (1984) - PLACEHOLDER
    "0000196",  # 196. Dead Poets Society (1989) - PLACEHOLDER
    "0000197",  # 197. Graduate, The (1967) - PLACEHOLDER
    "0000198",  # 198. Nikita (La Femme Nikita) (1990) - PLACEHOLDER
    "0000199",  # 199. Bridge on the River Kwai, The (1957) - PLACEHOLDER
    "0000200",  # 200. Shining, The (1980) - PLACEHOLDER
    "0000201",  # 201. Evil Dead II (1987) - PLACEHOLDER
    "0000202",  # 202. Groundhog Day (1993) - PLACEHOLDER
    "0000203",  # 203. Unforgiven (1992) - PLACEHOLDER
    "0000204",  # 204. Back to the Future (1985) - PLACEHOLDER
    "0000205",  # 205. Patton (1970) - PLACEHOLDER
    "0000206",  # 206. Akira (1988) - PLACEHOLDER
    "0000207",  # 207. Cyrano de Bergerac (1990) - PLACEHOLDER
    "0000208",  # 208. Young Frankenstein (1974) - PLACEHOLDER
    "0000209",  # 209. This Is Spinal Tap (1984) - PLACEHOLDER
    "0000210",  # 210. Indiana Jones and the Last Crusade (1989) - PLACEHOLDER
    "0000211",  # 211. M*A*S*H (1970) - PLACEHOLDER
    "0000212",  # 212. Unbearable Lightness of Being, The (1988) - PLACEHOLDER
    "0000213",  # 213. Room with a View, A (1986) - PLACEHOLDER
    "0000214",  # 214. Pink Floyd - The Wall (1982) - PLACEHOLDER
    "0000215",  # 215. Field of Dreams (1989) - PLACEHOLDER
    "0000216",  # 216. When Harry Met Sally... (1989) - PLACEHOLDER
    "0000217",  # 217. Bram Stoker's Dracula (1992) - PLACEHOLDER
    "0000218",  # 218. Cape Fear (1991) - PLACEHOLDER
    "0000219",  # 219. Nightmare on Elm Street, A (1984) - PLACEHOLDER
    "0000220",  # 220. Mirror Has Two Faces, The (1996) - PLACEHOLDER
    "0000221",  # 221. Breaking the Waves (1996) - PLACEHOLDER
    "0000222",  # 222. Star Trek: First Contact (1996) - PLACEHOLDER
    "0000223",  # 223. Sling Blade (1996) - PLACEHOLDER
    "0000224",  # 224. Ridicule (1996) - PLACEHOLDER
    "0000225",  # 225. 101 Dalmatians (1996) - PLACEHOLDER
    "0000226",  # 226. Die Hard 2 (1990) - PLACEHOLDER
    "0000227",  # 227. Star Trek VI: The Undiscovered Country (1991) - PLACEHOLDER
    "0000228",  # 228. Star Trek: The Wrath of Khan (1982) - PLACEHOLDER
    "0000229",  # 229. Star Trek III: The Search for Spock (1984) - PLACEHOLDER
    "0000230",  # 230. Star Trek IV: The Voyage Home (1986) - PLACEHOLDER
    "0000231",  # 231. Batman Returns (1992) - PLACEHOLDER
    "0000232",  # 232. Young Guns (1988) - PLACEHOLDER
    "0000233",  # 233. Under Siege (1992) - PLACEHOLDER
    "0000234",  # 234. Jaws (1975) - PLACEHOLDER
    "0000235",  # 235. Mars Attacks! (1996) - PLACEHOLDER
    "0000236",  # 236. Citizen Ruth (1996) - PLACEHOLDER
    "0000237",  # 237. Jerry Maguire (1996) - PLACEHOLDER
    "0000238",  # 238. Raising Arizona (1987) - PLACEHOLDER
    "0000239",  # 239. Sneakers (1992) - PLACEHOLDER
    "0000240",  # 240. Beavis and Butt-head Do America (1996) - PLACEHOLDER
    "0000241",  # 241. Last of the Mohicans, The (1992) - PLACEHOLDER
    "0000242",  # 242. Kolya (1996) - PLACEHOLDER
    "0000243",  # 243. Jungle2Jungle (1997) - PLACEHOLDER
    "0000244",  # 244. Smilla's Sense of Snow (1997) - PLACEHOLDER
    "0000245",  # 245. Devil's Own, The (1997) - PLACEHOLDER
    "0000246",  # 246. Chasing Amy (1997) - PLACEHOLDER
    "0000247",  # 247. Turbo: A Power Rangers Movie (1997) - PLACEHOLDER
    "0000248",  # 248. Grosse Pointe Blank (1997) - PLACEHOLDER
    "0000249",  # 249. Austin Powers: International Man of Mystery (1997) - PLACEHOLDER
    "0000250",  # 250. Fifth Element, The (1997) - PLACEHOLDER
    "0000251",  # 251. Shall We Dance? (1996) - PLACEHOLDER
    "0000252",  # 252. Lost World: Jurassic Park, The (1997) - PLACEHOLDER
    "0000253",  # 253. Pillow Book, The (1995) - PLACEHOLDER
    "0000254",  # 254. Batman & Robin (1997) - PLACEHOLDER
    "0000255",  # 255. My Best Friend's Wedding (1997) - PLACEHOLDER
    "0000256",  # 256. When the Cats Away (Chacun cherche son chat) (1996) - PLACEHOLDER
    "0000257",  # 257. Men in Black (1997) - PLACEHOLDER
    "0000258",  # 258. Contact (1997) - PLACEHOLDER
    "0000259",  # 259. George of the Jungle (1997) - PLACEHOLDER
    "0000260",  # 260. Event Horizon (1997) - PLACEHOLDER
    "0000261",  # 261. Air Bud (1997) - PLACEHOLDER
    "0000262",  # 262. In the Company of Men (1997) - PLACEHOLDER
    "0000263",  # 263. Steel (1997) - PLACEHOLDER
    "0000264",  # 264. Mimic (1997) - PLACEHOLDER
    "0000265",  # 265. Hunt for Red October, The (1990) - PLACEHOLDER
    "0000266",  # 266. Kull the Conqueror (1997) - PLACEHOLDER
    "0000267",  # 267. unknown () - PLACEHOLDER
    "0000268",  # 268. Chasing Amy (1997) - PLACEHOLDER
    "0000269",  # 269. Full Monty, The (1997) - PLACEHOLDER
    "0000270",  # 270. Gattaca (1997) - PLACEHOLDER
    "0000271",  # 271. Starship Troopers (1997) - PLACEHOLDER
    "0000272",  # 272. Good Will Hunting (1997) - PLACEHOLDER
    "0000273",  # 273. Heat (1995) - PLACEHOLDER
    "0000274",  # 274. Sabrina (1995) - PLACEHOLDER
    "0000275",  # 275. Sense and Sensibility (1995) - PLACEHOLDER
    "0000276",  # 276. Leaving Las Vegas (1995) - PLACEHOLDER
    "0000277",  # 277. Restoration (1995) - PLACEHOLDER
    "0000278",  # 278. Bed of Roses (1996) - PLACEHOLDER
    "0000279",  # 279. Once Upon a Time... When We Were Colored (1995) - PLACEHOLDER
    "0000280",  # 280. Up Close and Personal (1996) - PLACEHOLDER
    "0000281",  # 281. River Wild, The (1994) - PLACEHOLDER
    "0000282",  # 282. Time to Kill, A (1996) - PLACEHOLDER
    "0000283",  # 283. Emma (1996) - PLACEHOLDER
    "0000284",  # 284. Tin Cup (1996) - PLACEHOLDER
    "0000285",  # 285. Secrets & Lies (1996) - PLACEHOLDER
    "0000286",  # 286. English Patient, The (1996) - PLACEHOLDER
    "0000287",  # 287. Marvin's Room (1996) - PLACEHOLDER
    "0000288",  # 288. Scream (1996) - PLACEHOLDER
    "0000289",  # 289. Evita (1996) - PLACEHOLDER
    "0000290",  # 290. Fierce Creatures (1997) - PLACEHOLDER
    "0000291",  # 291. Absolute Power (1997) - PLACEHOLDER
    "0000292",  # 292. Rosewood (1997) - PLACEHOLDER
    "0000293",  # 293. Donnie Brasco (1997) - PLACEHOLDER
    "0000294",  # 294. Liar Liar (1997) - PLACEHOLDER
    "0000295",  # 295. Breakdown (1997) - PLACEHOLDER
    "0000296",  # 296. Promesse, La (1996) - PLACEHOLDER
    "0000297",  # 297. Ulee's Gold (1997) - PLACEHOLDER
    "0000298",  # 298. Face/Off (1997) - PLACEHOLDER
    "0000299",  # 299. Hoodlum (1997) - PLACEHOLDER
    "0000300",  # 300. Air Force One (1997) - PLACEHOLDER
    "0000301",  # 301. In & Out (1997) - PLACEHOLDER
    "0000302",  # 302. L.A. Confidential (1997) - PLACEHOLDER
    "0000303",  # 303. Ulee's Gold (1997) - PLACEHOLDER
    "0000304",  # 304. Fly Away Home (1996) - PLACEHOLDER
    "0000305",  # 305. Ice Storm, The (1997) - PLACEHOLDER
    "0000306",  # 306. Mrs. Brown (Her Majesty, Mrs. Brown) (1997) - PLACEHOLDER
    "0000307",  # 307. Devil's Advocate, The (1997) - PLACEHOLDER
    "0000308",  # 308. FairyTale: A True Story (1997) - PLACEHOLDER
    "0000309",  # 309. Deceiver (1997) - PLACEHOLDER
    "0000310",  # 310. Rainmaker, The (1997) - PLACEHOLDER
    "0000311",  # 311. Wings of the Dove, The (1997) - PLACEHOLDER
    "0000312",  # 312. Midnight in the Garden of Good and Evil (1997) - PLACEHOLDER
    "0000313",  # 313. Titanic (1997) - PLACEHOLDER
    "0000314",  # 314. 3 Ninjas: High Noon At Mega Mountain (1998) - PLACEHOLDER
    "0000315",  # 315. Apt Pupil (1998) - PLACEHOLDER
    "0000316",  # 316. As Good As It Gets (1997) - PLACEHOLDER
    "0000317",  # 317. In the Name of the Father (1993) - PLACEHOLDER
    "0000318",  # 318. Schindler's List (1993) - PLACEHOLDER
    "0000319",  # 319. Everyone Says I Love You (1996) - PLACEHOLDER
    "0000320",  # 320. Paradise Lost: The Child Murders at Robin Hood Hills (1996) - PLACEHOLDER
    "0000321",  # 321. Mother (1996) - PLACEHOLDER
    "0000322",  # 322. Murder at 1600 (1997) - PLACEHOLDER
    "0000323",  # 323. Dante's Peak (1997) - PLACEHOLDER
    "0000324",  # 324. Lost Highway (1997) - PLACEHOLDER
    "0000325",  # 325. Crash (1996) - PLACEHOLDER
    "0000326",  # 326. G.I. Jane (1997) - PLACEHOLDER
    "0000327",  # 327. Cop Land (1997) - PLACEHOLDER
    "0000328",  # 328. Conspiracy Theory (1997) - PLACEHOLDER
    "0000329",  # 329. Desperate Measures (1998) - PLACEHOLDER
    "0000330",  # 330. 187 (1997) - PLACEHOLDER
    "0000331",  # 331. Edge, The (1997) - PLACEHOLDER
    "0000332",  # 332. Kiss the Girls (1997) - PLACEHOLDER
    "0000333",  # 333. Game, The (1997) - PLACEHOLDER
    "0000334",  # 334. U Turn (1997) - PLACEHOLDER
    "0000335",  # 335. How to Be a Player (1997) - PLACEHOLDER
    "0000336",  # 336. Playing God (1997) - PLACEHOLDER
    "0000337",  # 337. House of Yes, The (1997) - PLACEHOLDER
    "0000338",  # 338. Bean (1997) - PLACEHOLDER
    "0000339",  # 339. Mad City (1997) - PLACEHOLDER
    "0000340",  # 340. Boogie Nights (1997) - PLACEHOLDER
    "0000341",  # 341. Critical Care (1997) - PLACEHOLDER
    "0000342",  # 342. Man Who Knew Too Little, The (1997) - PLACEHOLDER
    "0000343",  # 343. Alien: Resurrection (1997) - PLACEHOLDER
    "0000344",  # 344. Apostle, The (1997) - PLACEHOLDER
    "0000345",  # 345. Deconstructing Harry (1997) - PLACEHOLDER
    "0000346",  # 346. Jackie Brown (1997) - PLACEHOLDER
    "0000347",  # 347. Wag the Dog (1997) - PLACEHOLDER
    "0000348",  # 348. Desperate Measures (1998) - PLACEHOLDER
    "0000349",  # 349. Hard Rain (1998) - PLACEHOLDER
    "0000350",  # 350. Fallen (1998) - PLACEHOLDER
    "0000351",  # 351. Prophecy II, The (1998) - PLACEHOLDER
    "0000352",  # 352. Spice World (1997) - PLACEHOLDER
    "0000353",  # 353. Deep Rising (1998) - PLACEHOLDER
    "0000354",  # 354. Wedding Singer, The (1998) - PLACEHOLDER
    "0000355",  # 355. Sphere (1998) - PLACEHOLDER
    "0000356",  # 356. Client, The (1994) - PLACEHOLDER
    "0000357",  # 357. One Flew Over the Cuckoo's Nest (1975) - PLACEHOLDER
    "0000358",  # 358. Spawn (1997) - PLACEHOLDER
    "0000359",  # 359. Assignment, The (1997) - PLACEHOLDER
    "0000360",  # 360. Wonderland (1997) - PLACEHOLDER
    "0000361",  # 361. Incognito (1997) - PLACEHOLDER
    "0000362",  # 362. Blues Brothers 2000 (1998) - PLACEHOLDER
    "0000363",  # 363. Sudden Death (1995) - PLACEHOLDER
    "0000364",  # 364. Ace Ventura: When Nature Calls (1995) - PLACEHOLDER
    "0000365",  # 365. Powder (1995) - PLACEHOLDER
    "0000366",  # 366. Dangerous Minds (1995) - PLACEHOLDER
    "0000367",  # 367. Clueless (1995) - PLACEHOLDER
    "0000368",  # 368. Bio-Dome (1996) - PLACEHOLDER
    "0000369",  # 369. Black Sheep (1996) - PLACEHOLDER
    "0000370",  # 370. Mary Reilly (1996) - PLACEHOLDER
    "0000371",  # 371. Bridges of Madison County, The (1995) - PLACEHOLDER
    "0000372",  # 372. Jeffrey (1995) - PLACEHOLDER
    "0000373",  # 373. Judge Dredd (1995) - PLACEHOLDER
    "0000374",  # 374. Mighty Morphin Power Rangers: The Movie (1995) - PLACEHOLDER
    "0000375",  # 375. Showgirls (1995) - PLACEHOLDER
    "0000376",  # 376. Houseguest (1994) - PLACEHOLDER
    "0000377",  # 377. Heavyweights (1994) - PLACEHOLDER
    "0000378",  # 378. Miracle on 34th Street (1994) - PLACEHOLDER
    "0000379",  # 379. Tales From the Crypt Presents: Demon Knight (1995) - PLACEHOLDER
    "0000380",  # 380. Star Trek: Generations (1994) - PLACEHOLDER
    "0000381",  # 381. Muriel's Wedding (1994) - PLACEHOLDER
    "0000382",  # 382. Adventures of Priscilla, Queen of the Desert, The (1994) - PLACEHOLDER
    "0000383",  # 383. Flintstones, The (1994) - PLACEHOLDER
    "0000384",  # 384. Naked Gun 33 1/3: The Final Insult (1994) - PLACEHOLDER
    "0000385",  # 385. True Lies (1994) - PLACEHOLDER
    "0000386",  # 386. Addams Family Values (1993) - PLACEHOLDER
    "0000387",  # 387. Age of Innocence, The (1993) - PLACEHOLDER
    "0000388",  # 388. Beverly Hills Cop III (1994) - PLACEHOLDER
    "0000389",  # 389. Black Beauty (1994) - PLACEHOLDER
    "0000390",  # 390. Fear of a Black Hat (1993) - PLACEHOLDER
    "0000391",  # 391. Last Action Hero (1993) - PLACEHOLDER
    "0000392",  # 392. Man Without a Face, The (1993) - PLACEHOLDER
    "0000393",  # 393. Mrs. Doubtfire (1993) - PLACEHOLDER
    "0000394",  # 394. Radioland Murders (1994) - PLACEHOLDER
    "0000395",  # 395. Robin Hood: Men in Tights (1993) - PLACEHOLDER
    "0000396",  # 396. Serial Mom (1994) - PLACEHOLDER
    "0000397",  # 397. Striking Distance (1993) - PLACEHOLDER
    "0000398",  # 398. Super Mario Bros. (1993) - PLACEHOLDER
    "0000399",  # 399. Three Musketeers, The (1993) - PLACEHOLDER
    "0000400",  # 400. Little Rascals, The (1994) - PLACEHOLDER
    "0000401",  # 401. Brady Bunch Movie, The (1995) - PLACEHOLDER
    "0000402",  # 402. Ghost (1990) - PLACEHOLDER
    "0000403",  # 403. Batman (1989) - PLACEHOLDER
    "0000404",  # 404. Pinocchio (1940) - PLACEHOLDER
    "0000405",  # 405. Mission: Impossible (1996) - PLACEHOLDER
    "0000406",  # 406. Thinner (1996) - PLACEHOLDER
    "0000407",  # 407. Spy Hard (1996) - PLACEHOLDER
    "0000408",  # 408. Close Shave, A (1995) - PLACEHOLDER
    "0000409",  # 409. Jack (1996) - PLACEHOLDER
    "0000410",  # 410. Kingpin (1996) - PLACEHOLDER
    "0000411",  # 411. Nutty Professor, The (1996) - PLACEHOLDER
    "0000412",  # 412. Very Brady Sequel, A (1996) - PLACEHOLDER
    "0000413",  # 413. Tales from the Crypt Presents: Bordello of Blood (1996) - PLACEHOLDER
    "0000414",  # 414. My Favorite Year (1982) - PLACEHOLDER
    "0000415",  # 415. Apple Dumpling Gang, The (1975) - PLACEHOLDER
    "0000416",  # 416. Old Yeller (1957) - PLACEHOLDER
    "0000417",  # 417. Parent Trap, The (1961) - PLACEHOLDER
    "0000418",  # 418. Cinderella (1950) - PLACEHOLDER
    "0000419",  # 419. Mary Poppins (1964) - PLACEHOLDER
    "0000420",  # 420. Alice in Wonderland (1951) - PLACEHOLDER
    "0000421",  # 421. William Shakespeare's Romeo and Juliet (1996) - PLACEHOLDER
    "0000422",  # 422. Aladdin and the King of Thieves (1996) - PLACEHOLDER
    "0000423",  # 423. E.T. the Extra-Terrestrial (1982) - PLACEHOLDER
    "0000424",  # 424. Children of the Corn: The Gathering (1996) - PLACEHOLDER
    "0000425",  # 425. Bob Roberts (1992) - PLACEHOLDER
    "0000426",  # 426. Transformers: The Movie, The (1986) - PLACEHOLDER
    "0000427",  # 427. To Kill a Mockingbird (1962) - PLACEHOLDER
    "0000428",  # 428. Harold and Maude (1971) - PLACEHOLDER
    "0000429",  # 429. Day the Earth Stood Still, The (1951) - PLACEHOLDER
    "0000430",  # 430. Duck Soup (1933) - PLACEHOLDER
    "0000431",  # 431. Highlander (1986) - PLACEHOLDER
    "0000432",  # 432. Fantasia (1940) - PLACEHOLDER
    "0000433",  # 433. Heathers (1989) - PLACEHOLDER
    "0000434",  # 434. Forbidden Planet (1956) - PLACEHOLDER
    "0000435",  # 435. Butch Cassidy and the Sundance Kid (1969) - PLACEHOLDER
    "0000436",  # 436. American Werewolf in London, An (1981) - PLACEHOLDER
    "0000437",  # 437. Amityville 1992: It's About Time (1992) - PLACEHOLDER
    "0000438",  # 438. Amityville 3-D (1983) - PLACEHOLDER
    "0000439",  # 439. Amityville: A New Generation (1993) - PLACEHOLDER
    "0000440",  # 440. Amityville II: The Possession (1982) - PLACEHOLDER
    "0000441",  # 441. Amityville Horror, The (1979) - PLACEHOLDER
    "0000442",  # 442. Amityville Curse, The (1990) - PLACEHOLDER
    "0000443",  # 443. Birds, The (1963) - PLACEHOLDER
    "0000444",  # 444. Blob, The (1958) - PLACEHOLDER
    "0000445",  # 445. Body Snatcher, The (1945) - PLACEHOLDER
    "0000446",  # 446. Burnt Offerings (1976) - PLACEHOLDER
    "0000447",  # 447. Carrie (1976) - PLACEHOLDER
    "0000448",  # 448. Omen, The (1976) - PLACEHOLDER
    "0000449",  # 449. Star Trek: The Motion Picture (1979) - PLACEHOLDER
    "0000450",  # 450. Star Trek V: The Final Frontier (1989) - PLACEHOLDER
    "0000451",  # 451. Grease (1978) - PLACEHOLDER
    "0000452",  # 452. Jaws 2 (1978) - PLACEHOLDER
    "0000453",  # 453. Jaws 3-D (1983) - PLACEHOLDER
    "0000454",  # 454. Bastard Out of Carolina (1996) - PLACEHOLDER
    "0000455",  # 455. Jackie Chan's First Strike (1996) - PLACEHOLDER
    "0000456",  # 456. Beverly Hills Ninja (1997) - PLACEHOLDER
    "0000457",  # 457. Free Willy 3: The Rescue (1997) - PLACEHOLDER
    "0000458",  # 458. Nixon (1995) - PLACEHOLDER
    "0000459",  # 459. Cry, the Beloved Country (1995) - PLACEHOLDER
    "0000460",  # 460. Crossing Guard, The (1995) - PLACEHOLDER
    "0000461",  # 461. Smoke (1995) - PLACEHOLDER
    "0000462",  # 462. Like Water For Chocolate (Como agua para chocolate) (1992) - PLACEHOLDER
    "0000463",  # 463. Secret of Roan Inish, The (1994) - PLACEHOLDER
    "0000464",  # 464. Vanya on 42nd Street (1994) - PLACEHOLDER
    "0000465",  # 465. Jungle Book, The (1994) - PLACEHOLDER
    "0000466",  # 466. Red Rock West (1992) - PLACEHOLDER
    "0000467",  # 467. Bronx Tale, A (1993) - PLACEHOLDER
    "0000468",  # 468. Rudy (1993) - PLACEHOLDER
    "0000469",  # 469. Short Cuts (1993) - PLACEHOLDER
    "0000470",  # 470. Tombstone (1993) - PLACEHOLDER
    "0000471",  # 471. Courage Under Fire (1996) - PLACEHOLDER
    "0000472",  # 472. Dragonheart (1996) - PLACEHOLDER
    "0000473",  # 473. James and the Giant Peach (1996) - PLACEHOLDER
    "0000474",  # 474. Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1963) - PLACEHOLDER
    "0000475",  # 475. Trainspotting (1996) - PLACEHOLDER
    "0000476",  # 476. First Wives Club, The (1996) - PLACEHOLDER
    "0000477",  # 477. Matilda (1996) - PLACEHOLDER
    "0000478",  # 478. Philadelphia Story, The (1940) - PLACEHOLDER
    "0000479",  # 479. Vertigo (1958) - PLACEHOLDER
    "0000480",  # 480. North by Northwest (1959) - PLACEHOLDER
    "0000481",  # 481. Apartment, The (1960) - PLACEHOLDER
    "0000482",  # 482. Some Like It Hot (1959) - PLACEHOLDER
    "0000483",  # 483. Casablanca (1942) - PLACEHOLDER
    "0000484",  # 484. Maltese Falcon, The (1941) - PLACEHOLDER
    "0000485",  # 485. My Fair Lady (1964) - PLACEHOLDER
    "0000486",  # 486. Sabrina (1954) - PLACEHOLDER
    "0000487",  # 487. Roman Holiday (1953) - PLACEHOLDER
    "0000488",  # 488. Sunset Blvd. (1950) - PLACEHOLDER
    "0000489",  # 489. Notorious (1946) - PLACEHOLDER
    "0000490",  # 490. To Catch a Thief (1955) - PLACEHOLDER
    "0000491",  # 491. Adventures of Robin Hood, The (1938) - PLACEHOLDER
    "0000492",  # 492. East of Eden (1955) - PLACEHOLDER
    "0000493",  # 493. Thin Man, The (1934) - PLACEHOLDER
    "0000494",  # 494. His Girl Friday (1940) - PLACEHOLDER
    "0000495",  # 495. Around the World in 80 Days (1956) - PLACEHOLDER
    "0000496",  # 496. It's a Wonderful Life (1946) - PLACEHOLDER
    "0000497",  # 497. Bringing Up Baby (1938) - PLACEHOLDER
    "0000498",  # 498. African Queen, The (1951) - PLACEHOLDER
    "0000499",  # 499. Cat on a Hot Tin Roof (1958) - PLACEHOLDER
    "0000500",  # 500. Fly Away Home (1996) - PLACEHOLDER
    "0000501",  # 501. Dumbo (1941) - PLACEHOLDER
    "0000502",  # 502. Bananas (1971) - PLACEHOLDER
    "0000503",  # 503. Candidate, The (1972) - PLACEHOLDER
    "0000504",  # 504. Bonnie and Clyde (1967) - PLACEHOLDER
    "0000505",  # 505. Dial M for Murder (1954) - PLACEHOLDER
    "0000506",  # 506. Rebel Without a Cause (1955) - PLACEHOLDER
    "0000507",  # 507. Streetcar Named Desire, A (1951) - PLACEHOLDER
    "0000508",  # 508. People vs. Larry Flynt, The (1996) - PLACEHOLDER
    "0000509",  # 509. My Left Foot (1989) - PLACEHOLDER
    "0000510",  # 510. Magnificent Seven, The (1954) - PLACEHOLDER
    "0000511",  # 511. Lawrence of Arabia (1962) - PLACEHOLDER
    "0000512",  # 512. Wings of Desire (1987) - PLACEHOLDER
    "0000513",  # 513. Third Man, The (1949) - PLACEHOLDER
    "0000514",  # 514. Annie Hall (1977) - PLACEHOLDER
    "0000515",  # 515. Boot, Das (1981) - PLACEHOLDER
    "0000516",  # 516. Local Hero (1983) - PLACEHOLDER
    "0000517",  # 517. Manhattan (1979) - PLACEHOLDER
    "0000518",  # 518. Miller's Crossing (1990) - PLACEHOLDER
    "0000519",  # 519. Treasure of the Sierra Madre, The (1948) - PLACEHOLDER
    "0000520",  # 520. Great Escape, The (1963) - PLACEHOLDER
    "0000521",  # 521. Deer Hunter, The (1978) - PLACEHOLDER
    "0000522",  # 522. Down by Law (1986) - PLACEHOLDER
    "0000523",  # 523. Cool Hand Luke (1967) - PLACEHOLDER
    "0000524",  # 524. Great Dictator, The (1940) - PLACEHOLDER
    "0000525",  # 525. Big Sleep, The (1946) - PLACEHOLDER
    "0000526",  # 526. Ben-Hur (1959) - PLACEHOLDER
    "0000527",  # 527. Gandhi (1982) - PLACEHOLDER
    "0000528",  # 528. Killing Fields, The (1984) - PLACEHOLDER
    "0000529",  # 529. My Life as a Dog (Mitt liv som hund) (1985) - PLACEHOLDER
    "0000530",  # 530. Man Who Would Be King, The (1975) - PLACEHOLDER
    "0000531",  # 531. Shine (1996) - PLACEHOLDER
    "0000532",  # 532. Kama Sutra: A Tale of Love (1996) - PLACEHOLDER
    "0000533",  # 533. Daytrippers, The (1996) - PLACEHOLDER
    "0000534",  # 534. Traveller (1997) - PLACEHOLDER
    "0000535",  # 535. Addicted to Love (1997) - PLACEHOLDER
    "0000536",  # 536. Ponette (1996) - PLACEHOLDER
    "0000537",  # 537. My Own Private Idaho (1991) - PLACEHOLDER
    "0000538",  # 538. Anastasia (1997) - PLACEHOLDER
    "0000539",  # 539. Mouse Hunt (1997) - PLACEHOLDER
    "0000540",  # 540. Money Train (1995) - PLACEHOLDER
    "0000541",  # 541. Mortal Kombat (1995) - PLACEHOLDER
    "0000542",  # 542. Pocahontas (1995) - PLACEHOLDER
    "0000543",  # 543. Misérables, Les (1995) - PLACEHOLDER
    "0000544",  # 544. Things to Do in Denver when You're Dead (1995) - PLACEHOLDER
    "0000545",  # 545. Vampire in Brooklyn (1995) - PLACEHOLDER
    "0000546",  # 546. Broken Arrow (1996) - PLACEHOLDER
    "0000547",  # 547. Young Poisoner's Handbook, The (1995) - PLACEHOLDER
    "0000548",  # 548. NeverEnding Story III, The (1994) - PLACEHOLDER
    "0000549",  # 549. Rob Roy (1995) - PLACEHOLDER
    "0000550",  # 550. Die Hard: With a Vengeance (1995) - PLACEHOLDER
    "0000551",  # 551. Lord of Illusions (1995) - PLACEHOLDER
    "0000552",  # 552. Species (1995) - PLACEHOLDER
    "0000553",  # 553. Walk in the Clouds, A (1995) - PLACEHOLDER
    "0000554",  # 554. Waterworld (1995) - PLACEHOLDER
    "0000555",  # 555. White Man's Burden (1995) - PLACEHOLDER
    "0000556",  # 556. Wild Bill (1995) - PLACEHOLDER
    "0000557",  # 557. Farinelli: il castrato (1994) - PLACEHOLDER
    "0000558",  # 558. Heavenly Creatures (1994) - PLACEHOLDER
    "0000559",  # 559. Interview with the Vampire (1994) - PLACEHOLDER
    "0000560",  # 560. Kid in King Arthur's Court, A (1995) - PLACEHOLDER
    "0000561",  # 561. Mary Shelley's Frankenstein (1994) - PLACEHOLDER
    "0000562",  # 562. Quick and the Dead, The (1995) - PLACEHOLDER
    "0000563",  # 563. Stephen King's The Langoliers (1995) - PLACEHOLDER
    "0000564",  # 564. Tales from the Hood (1995) - PLACEHOLDER
    "0000565",  # 565. Village of the Damned (1995) - PLACEHOLDER
    "0000566",  # 566. Clear and Present Danger (1994) - PLACEHOLDER
    "0000567",  # 567. Wes Craven's New Nightmare (1994) - PLACEHOLDER
    "0000568",  # 568. Speed (1994) - PLACEHOLDER
    "0000569",  # 569. Wolf (1994) - PLACEHOLDER
    "0000570",  # 570. Wyatt Earp (1994) - PLACEHOLDER
    "0000571",  # 571. Another Stakeout (1993) - PLACEHOLDER
    "0000572",  # 572. Blown Away (1994) - PLACEHOLDER
    "0000573",  # 573. Body Snatchers (1993) - PLACEHOLDER
    "0000574",  # 574. Boxing Helena (1993) - PLACEHOLDER
    "0000575",  # 575. City Slickers II: The Legend of Curly's Gold (1994) - PLACEHOLDER
    "0000576",  # 576. Cliffhanger (1993) - PLACEHOLDER
    "0000577",  # 577. Coneheads (1993) - PLACEHOLDER
    "0000578",  # 578. Demolition Man (1993) - PLACEHOLDER
    "0000579",  # 579. Fatal Instinct (1993) - PLACEHOLDER
    "0000580",  # 580. Englishman Who Went Up a Hill, But Came Down a Mountain, The (1995) - PLACEHOLDER
    "0000581",  # 581. Kalifornia (1993) - PLACEHOLDER
    "0000582",  # 582. Piano, The (1993) - PLACEHOLDER
    "0000583",  # 583. Romeo Is Bleeding (1993) - PLACEHOLDER
    "0000584",  # 584. Secret Garden, The (1993) - PLACEHOLDER
    "0000585",  # 585. Son in Law (1993) - PLACEHOLDER
    "0000586",  # 586. Terminal Velocity (1994) - PLACEHOLDER
    "0000587",  # 587. Hour of the Pig, The (1993) - PLACEHOLDER
    "0000588",  # 588. Beauty and the Beast (1991) - PLACEHOLDER
    "0000589",  # 589. Wild Bunch, The (1969) - PLACEHOLDER
    "0000590",  # 590. Hellraiser: Bloodline (1996) - PLACEHOLDER
    "0000591",  # 591. Primal Fear (1996) - PLACEHOLDER
    "0000592",  # 592. True Crime (1995) - PLACEHOLDER
    "0000593",  # 593. Stalingrad (1993) - PLACEHOLDER
    "0000594",  # 594. Heavy (1995) - PLACEHOLDER
    "0000595",  # 595. Fan, The (1996) - PLACEHOLDER
    "0000596",  # 596. Hunchback of Notre Dame, The (1996) - PLACEHOLDER
    "0000597",  # 597. Eraser (1996) - PLACEHOLDER
    "0000598",  # 598. Big Squeeze, The (1996) - PLACEHOLDER
    "0000599",  # 599. Police Story 4: Project S (Chao ji ji hua) (1993) - PLACEHOLDER
    "0000600",  # 600. Daniel Defoe's Robinson Crusoe (1996) - PLACEHOLDER
    "0000601",  # 601. For Whom the Bell Tolls (1943) - PLACEHOLDER
    "0000602",  # 602. American in Paris, An (1951) - PLACEHOLDER
    "0000603",  # 603. Rear Window (1954) - PLACEHOLDER
    "0000604",  # 604. It Happened One Night (1934) - PLACEHOLDER
    "0000605",  # 605. Meet Me in St. Louis (1944) - PLACEHOLDER
    "0000606",  # 606. All About Eve (1950) - PLACEHOLDER
    "0000607",  # 607. Rebecca (1940) - PLACEHOLDER
    "0000608",  # 608. Spellbound (1945) - PLACEHOLDER
    "0000609",  # 609. Father of the Bride (1950) - PLACEHOLDER
    "0000610",  # 610. Gigi (1958) - PLACEHOLDER
    "0000611",  # 611. Laura (1944) - PLACEHOLDER
    "0000612",  # 612. Lost Horizon (1937) - PLACEHOLDER
    "0000613",  # 613. My Man Godfrey (1936) - PLACEHOLDER
    "0000614",  # 614. Giant (1956) - PLACEHOLDER
    "0000615",  # 615. 39 Steps, The (1935) - PLACEHOLDER
    "0000616",  # 616. Night of the Living Dead (1968) - PLACEHOLDER
    "0000617",  # 617. Blue Angel, The (Blaue Engel, Der) (1930) - PLACEHOLDER
    "0000618",  # 618. Picnic (1955) - PLACEHOLDER
    "0000619",  # 619. Extreme Measures (1996) - PLACEHOLDER
    "0000620",  # 620. Chamber, The (1996) - PLACEHOLDER
    "0000621",  # 621. Davy Crockett, King of the Wild Frontier (1955) - PLACEHOLDER
    "0000622",  # 622. Swiss Family Robinson (1960) - PLACEHOLDER
    "0000623",  # 623. Angels in the Outfield (1994) - PLACEHOLDER
    "0000624",  # 624. Three Caballeros, The (1945) - PLACEHOLDER
    "0000625",  # 625. Sword in the Stone, The (1963) - PLACEHOLDER
    "0000626",  # 626. So Dear to My Heart (1949) - PLACEHOLDER
    "0000627",  # 627. Robin Hood: Prince of Thieves (1991) - PLACEHOLDER
    "0000628",  # 628. Sleepers (1996) - PLACEHOLDER
    "0000629",  # 629. Victor/Victoria (1982) - PLACEHOLDER
    "0000630",  # 630. Great Race, The (1965) - PLACEHOLDER
    "0000631",  # 631. Crying Game, The (1992) - PLACEHOLDER
    "0000632",  # 632. Sophie's Choice (1982) - PLACEHOLDER
    "0000633",  # 633. Christmas Carol, A (1938) - PLACEHOLDER
    "0000634",  # 634. Microcosmos: Le peuple de l'herbe (1996) - PLACEHOLDER
    "0000635",  # 635. Fog, The (1980) - PLACEHOLDER
    "0000636",  # 636. Escape from New York (1981) - PLACEHOLDER
    "0000637",  # 637. Howling, The (1981) - PLACEHOLDER
    "0000638",  # 638. Return of Martin Guerre, The (Retour de Martin Guerre, Le) (1982) - PLACEHOLDER
    "0000639",  # 639. Tin Drum, The (Blechtrommel, Die) (1979) - PLACEHOLDER
    "0000640",  # 640. Cook the Thief His Wife & Her Lover, The (1989) - PLACEHOLDER
    "0000641",  # 641. Paths of Glory (1957) - PLACEHOLDER
    "0000642",  # 642. Grifters, The (1990) - PLACEHOLDER
    "0000643",  # 643. The Innocent (1994) - PLACEHOLDER
    "0000644",  # 644. Thin Blue Line, The (1988) - PLACEHOLDER
    "0000645",  # 645. Paris Is Burning (1990) - PLACEHOLDER
    "0000646",  # 646. Once Upon a Time in the West (1969) - PLACEHOLDER
    "0000647",  # 647. Ran (1985) - PLACEHOLDER
    "0000648",  # 648. Quiet Man, The (1952) - PLACEHOLDER
    "0000649",  # 649. Once Upon a Time in America (1984) - PLACEHOLDER
    "0000650",  # 650. Seventh Seal, The (Sjunde inseglet, Det) (1957) - PLACEHOLDER
    "0000651",  # 651. Glory (1989) - PLACEHOLDER
    "0000652",  # 652. Rosencrantz and Guildenstern Are Dead (1990) - PLACEHOLDER
    "0000653",  # 653. Touch of Evil (1958) - PLACEHOLDER
    "0000654",  # 654. Chinatown (1974) - PLACEHOLDER
    "0000655",  # 655. Stand by Me (1986) - PLACEHOLDER
    "0000656",  # 656. M (1931) - PLACEHOLDER
    "0000657",  # 657. Manchurian Candidate, The (1962) - PLACEHOLDER
    "0000658",  # 658. Pump Up the Volume (1990) - PLACEHOLDER
    "0000659",  # 659. Arsenic and Old Lace (1944) - PLACEHOLDER
    "0000660",  # 660. Fried Green Tomatoes (1991) - PLACEHOLDER
    "0000661",  # 661. High Noon (1952) - PLACEHOLDER
    "0000662",  # 662. Somewhere in Time (1980) - PLACEHOLDER
    "0000663",  # 663. Being There (1979) - PLACEHOLDER
    "0000664",  # 664. Paris, Texas (1984) - PLACEHOLDER
    "0000665",  # 665. Alien 3 (1992) - PLACEHOLDER
    "0000666",  # 666. Blood For Dracula (Andy Warhol's Dracula) (1974) - PLACEHOLDER
    "0000667",  # 667. Audrey Rose (1977) - PLACEHOLDER
    "0000668",  # 668. Blood Beach (1981) - PLACEHOLDER
    "0000669",  # 669. Body Parts (1991) - PLACEHOLDER
    "0000670",  # 670. Body Snatchers (1993) - PLACEHOLDER
    "0000671",  # 671. Bride of Frankenstein (1935) - PLACEHOLDER
    "0000672",  # 672. Candyman (1992) - PLACEHOLDER
    "0000673",  # 673. Cape Fear (1962) - PLACEHOLDER
    "0000674",  # 674. Cat People (1982) - PLACEHOLDER
    "0000675",  # 675. Nosferatu (Nosferatu, eine Symphonie des Grauens) (1922) - PLACEHOLDER
    "0000676",  # 676. Crucible, The (1996) - PLACEHOLDER
    "0000677",  # 677. Fire on the Mountain (1996) - PLACEHOLDER
    "0000678",  # 678. Volcano (1997) - PLACEHOLDER
    "0000679",  # 679. Conan the Barbarian (1981) - PLACEHOLDER
    "0000680",  # 680. Kull the Conqueror (1997) - PLACEHOLDER
    "0000681",  # 681. Wishmaster (1997) - PLACEHOLDER
    "0000682",  # 682. I Know What You Did Last Summer (1997) - PLACEHOLDER
    "0000683",  # 683. Rocket Man (1997) - PLACEHOLDER
    "0000684",  # 684. In the Line of Fire (1993) - PLACEHOLDER
    "0000685",  # 685. Executive Decision (1996) - PLACEHOLDER
    "0000686",  # 686. Perfect World, A (1993) - PLACEHOLDER
    "0000687",  # 687. McHale's Navy (1997) - PLACEHOLDER
    "0000688",  # 688. Leave It to Beaver (1997) - PLACEHOLDER
    "0000689",  # 689. Jackal, The (1997) - PLACEHOLDER
    "0000690",  # 690. Seven Years in Tibet (1997) - PLACEHOLDER
    "0000691",  # 691. Dark City (1998) - PLACEHOLDER
    "0000692",  # 692. American President, The (1995) - PLACEHOLDER
    "0000693",  # 693. Casino (1995) - PLACEHOLDER
    "0000694",  # 694. Persuasion (1995) - PLACEHOLDER
    "0000695",  # 695. Kicking and Screaming (1995) - PLACEHOLDER
    "0000696",  # 696. City Hall (1996) - PLACEHOLDER
    "0000697",  # 697. Basketball Diaries, The (1995) - PLACEHOLDER
    "0000698",  # 698. Browning Version, The (1994) - PLACEHOLDER
    "0000699",  # 699. Little Women (1994) - PLACEHOLDER
    "0000700",  # 700. Miami Rhapsody (1995) - PLACEHOLDER
    "0000701",  # 701. Wonderful, Horrible Life of Leni Riefenstahl, The (1993) - PLACEHOLDER
    "0000702",  # 702. Barcelona (1994) - PLACEHOLDER
    "0000703",  # 703. Widows' Peak (1994) - PLACEHOLDER
    "0000704",  # 704. House of the Spirits, The (1993) - PLACEHOLDER
    "0000705",  # 705. Singin' in the Rain (1952) - PLACEHOLDER
    "0000706",  # 706. Bad Moon (1996) - PLACEHOLDER
    "0000707",  # 707. Enchanted April (1991) - PLACEHOLDER
    "0000708",  # 708. Sex, Lies, and Videotape (1989) - PLACEHOLDER
    "0000709",  # 709. Strictly Ballroom (1992) - PLACEHOLDER
    "0000710",  # 710. Better Off Dead... (1985) - PLACEHOLDER
    "0000711",  # 711. Substance of Fire, The (1996) - PLACEHOLDER
    "0000712",  # 712. Tin Men (1987) - PLACEHOLDER
    "0000713",  # 713. Othello (1995) - PLACEHOLDER
    "0000714",  # 714. Carrington (1995) - PLACEHOLDER
    "0000715",  # 715. To Die For (1995) - PLACEHOLDER
    "0000716",  # 716. Home for the Holidays (1995) - PLACEHOLDER
    "0000717",  # 717. Juror, The (1996) - PLACEHOLDER
    "0000718",  # 718. In the Bleak Midwinter (1995) - PLACEHOLDER
    "0000719",  # 719. Canadian Bacon (1994) - PLACEHOLDER
    "0000720",  # 720. First Knight (1995) - PLACEHOLDER
    "0000721",  # 721. Mallrats (1995) - PLACEHOLDER
    "0000722",  # 722. Nine Months (1995) - PLACEHOLDER
    "0000723",  # 723. Boys on the Side (1995) - PLACEHOLDER
    "0000724",  # 724. Circle of Friends (1995) - PLACEHOLDER
    "0000725",  # 725. Exit to Eden (1994) - PLACEHOLDER
    "0000726",  # 726. Fluke (1995) - PLACEHOLDER
    "0000727",  # 727. Immortal Beloved (1994) - PLACEHOLDER
    "0000728",  # 728. Junior (1994) - PLACEHOLDER
    "0000729",  # 729. Nell (1994) - PLACEHOLDER
    "0000730",  # 730. Queen Margot (Reine Margot, La) (1994) - PLACEHOLDER
    "0000731",  # 731. Corrina, Corrina (1994) - PLACEHOLDER
    "0000732",  # 732. Dave (1993) - PLACEHOLDER
    "0000733",  # 733. Go Fish (1994) - PLACEHOLDER
    "0000734",  # 734. Made in America (1993) - PLACEHOLDER
    "0000735",  # 735. Philadelphia (1993) - PLACEHOLDER
    "0000736",  # 736. Shadowlands (1993) - PLACEHOLDER
    "0000737",  # 737. Sirens (1994) - PLACEHOLDER
    "0000738",  # 738. Threesome (1994) - PLACEHOLDER
    "0000739",  # 739. Pretty Woman (1990) - PLACEHOLDER
    "0000740",  # 740. Jane Eyre (1996) - PLACEHOLDER
    "0000741",  # 741. Last Supper, The (1995) - PLACEHOLDER
    "0000742",  # 742. Ransom (1996) - PLACEHOLDER
    "0000743",  # 743. Crow: City of Angels, The (1996) - PLACEHOLDER
    "0000744",  # 744. Michael Collins (1996) - PLACEHOLDER
    "0000745",  # 745. Ruling Class, The (1972) - PLACEHOLDER
    "0000746",  # 746. Real Genius (1985) - PLACEHOLDER
    "0000747",  # 747. Benny & Joon (1993) - PLACEHOLDER
    "0000748",  # 748. Saint, The (1997) - PLACEHOLDER
    "0000749",  # 749. MatchMaker, The (1997) - PLACEHOLDER
    "0000750",  # 750. Amistad (1997) - PLACEHOLDER
    "0000751",  # 751. Tomorrow Never Dies (1997) - PLACEHOLDER
    "0000752",  # 752. Replacement Killers, The (1998) - PLACEHOLDER
    "0000753",  # 753. Burnt By the Sun (1994) - PLACEHOLDER
    "0000754",  # 754. Red Corner (1997) - PLACEHOLDER
    "0000755",  # 755. Jumanji (1995) - PLACEHOLDER
    "0000756",  # 756. Father of the Bride Part II (1995) - PLACEHOLDER
    "0000757",  # 757. Across the Sea of Time (1995) - PLACEHOLDER
    "0000758",  # 758. Lawnmower Man 2: Beyond Cyberspace (1996) - PLACEHOLDER
    "0000759",  # 759. Fair Game (1995) - PLACEHOLDER
    "0000760",  # 760. Screamers (1995) - PLACEHOLDER
    "0000761",  # 761. Nick of Time (1995) - PLACEHOLDER
    "0000762",  # 762. Beautiful Girls (1996) - PLACEHOLDER
    "0000763",  # 763. Happy Gilmore (1996) - PLACEHOLDER
    "0000764",  # 764. If Lucy Fell (1996) - PLACEHOLDER
    "0000765",  # 765. Boomerang (1992) - PLACEHOLDER
    "0000766",  # 766. Man of the Year (1995) - PLACEHOLDER
    "0000767",  # 767. Addiction, The (1995) - PLACEHOLDER
    "0000768",  # 768. Casper (1995) - PLACEHOLDER
    "0000769",  # 769. Congo (1995) - PLACEHOLDER
    "0000770",  # 770. Devil in a Blue Dress (1995) - PLACEHOLDER
    "0000771",  # 771. Johnny Mnemonic (1995) - PLACEHOLDER
    "0000772",  # 772. Kids (1995) - PLACEHOLDER
    "0000773",  # 773. Mute Witness (1994) - PLACEHOLDER
    "0000774",  # 774. Prophecy, The (1995) - PLACEHOLDER
    "0000775",  # 775. Something to Talk About (1995) - PLACEHOLDER
    "0000776",  # 776. Three Wishes (1995) - PLACEHOLDER
    "0000777",  # 777. Castle Freak (1995) - PLACEHOLDER
    "0000778",  # 778. Don Juan DeMarco (1995) - PLACEHOLDER
    "0000779",  # 779. Drop Zone (1994) - PLACEHOLDER
    "0000780",  # 780. Dumb & Dumber (1994) - PLACEHOLDER
    "0000781",  # 781. French Kiss (1995) - PLACEHOLDER
    "0000782",  # 782. Little Odessa (1994) - PLACEHOLDER
    "0000783",  # 783. Milk Money (1994) - PLACEHOLDER
    "0000784",  # 784. Beyond Bedlam (1993) - PLACEHOLDER
    "0000785",  # 785. Only You (1994) - PLACEHOLDER
    "0000786",  # 786. Perez Family, The (1995) - PLACEHOLDER
    "0000787",  # 787. Roommates (1995) - PLACEHOLDER
    "0000788",  # 788. Relative Fear (1994) - PLACEHOLDER
    "0000789",  # 789. Swimming with Sharks (1995) - PLACEHOLDER
    "0000790",  # 790. Tommy Boy (1995) - PLACEHOLDER
    "0000791",  # 791. Baby-Sitters Club, The (1995) - PLACEHOLDER
    "0000792",  # 792. Bullets Over Broadway (1994) - PLACEHOLDER
    "0000793",  # 793. Crooklyn (1994) - PLACEHOLDER
    "0000794",  # 794. It Could Happen to You (1994) - PLACEHOLDER
    "0000795",  # 795. Richie Rich (1994) - PLACEHOLDER
    "0000796",  # 796. Speechless (1994) - PLACEHOLDER
    "0000797",  # 797. Timecop (1994) - PLACEHOLDER
    "0000798",  # 798. Bad Company (1995) - PLACEHOLDER
    "0000799",  # 799. Boys Life (1995) - PLACEHOLDER
    "0000800",  # 800. In the Mouth of Madness (1995) - PLACEHOLDER
    "0000801",  # 801. Air Up There, The (1994) - PLACEHOLDER
    "0000802",  # 802. Hard Target (1993) - PLACEHOLDER
    "0000803",  # 803. Heaven & Earth (1993) - PLACEHOLDER
    "0000804",  # 804. Jimmy Hollywood (1994) - PLACEHOLDER
    "0000805",  # 805. Manhattan Murder Mystery (1993) - PLACEHOLDER
    "0000806",  # 806. Menace II Society (1993) - PLACEHOLDER
    "0000807",  # 807. Poetic Justice (1993) - PLACEHOLDER
    "0000808",  # 808. Program, The (1993) - PLACEHOLDER
    "0000809",  # 809. Rising Sun (1993) - PLACEHOLDER
    "0000810",  # 810. Shadow, The (1994) - PLACEHOLDER
    "0000811",  # 811. Thirty-Two Short Films About Glenn Gould (1993) - PLACEHOLDER
    "0000812",  # 812. Andre (1994) - PLACEHOLDER
    "0000813",  # 813. Celluloid Closet, The (1995) - PLACEHOLDER
    "0000814",  # 814. Great Day in Harlem, A (1994) - PLACEHOLDER
    "0000815",  # 815. One Fine Day (1996) - PLACEHOLDER
    "0000816",  # 816. Candyman: Farewell to the Flesh (1995) - PLACEHOLDER
    "0000817",  # 817. Frisk (1995) - PLACEHOLDER
    "0000818",  # 818. Girl 6 (1996) - PLACEHOLDER
    "0000819",  # 819. Eddie (1996) - PLACEHOLDER
    "0000820",  # 820. Space Jam (1996) - PLACEHOLDER
    "0000821",  # 821. Mrs. Winterbourne (1996) - PLACEHOLDER
    "0000822",  # 822. Faces (1968) - PLACEHOLDER
    "0000823",  # 823. Mulholland Falls (1996) - PLACEHOLDER
    "0000824",  # 824. Great White Hype, The (1996) - PLACEHOLDER
    "0000825",  # 825. Arrival, The (1996) - PLACEHOLDER
    "0000826",  # 826. Phantom, The (1996) - PLACEHOLDER
    "0000827",  # 827. Daylight (1996) - PLACEHOLDER
    "0000828",  # 828. Alaska (1996) - PLACEHOLDER
    "0000829",  # 829. Fled (1996) - PLACEHOLDER
    "0000830",  # 830. Power 98 (1995) - PLACEHOLDER
    "0000831",  # 831. Escape from L.A. (1996) - PLACEHOLDER
    "0000832",  # 832. Bogus (1996) - PLACEHOLDER
    "0000833",  # 833. Bulletproof (1996) - PLACEHOLDER
    "0000834",  # 834. Halloween: The Curse of Michael Myers (1995) - PLACEHOLDER
    "0000835",  # 835. Gay Divorcee, The (1934) - PLACEHOLDER
    "0000836",  # 836. Ninotchka (1939) - PLACEHOLDER
    "0000837",  # 837. Meet John Doe (1941) - PLACEHOLDER
    "0000838",  # 838. In the Line of Duty 2 (1987) - PLACEHOLDER
    "0000839",  # 839. Loch Ness (1995) - PLACEHOLDER
    "0000840",  # 840. Last Man Standing (1996) - PLACEHOLDER
    "0000841",  # 841. Glimmer Man, The (1996) - PLACEHOLDER
    "0000842",  # 842. Pollyanna (1960) - PLACEHOLDER
    "0000843",  # 843. Shaggy Dog, The (1959) - PLACEHOLDER
    "0000844",  # 844. Freeway (1996) - PLACEHOLDER
    "0000845",  # 845. That Thing You Do! (1996) - PLACEHOLDER
    "0000846",  # 846. To Gillian on Her 37th Birthday (1996) - PLACEHOLDER
    "0000847",  # 847. Looking for Richard (1996) - PLACEHOLDER
    "0000848",  # 848. Murder, My Sweet (1944) - PLACEHOLDER
    "0000849",  # 849. Days of Thunder (1990) - PLACEHOLDER
    "0000850",  # 850. Perfect Candidate, A (1996) - PLACEHOLDER
    "0000851",  # 851. Two or Three Things I Know About Her (1966) - PLACEHOLDER
    "0000852",  # 852. Bloody Child, The (1996) - PLACEHOLDER
    "0000853",  # 853. Braindead (1992) - PLACEHOLDER
    "0000854",  # 854. Bad Taste (1987) - PLACEHOLDER
    "0000855",  # 855. Diva (1981) - PLACEHOLDER
    "0000856",  # 856. Night on Earth (1991) - PLACEHOLDER
    "0000857",  # 857. Paris Was a Woman (1995) - PLACEHOLDER
    "0000858",  # 858. Amityville: Dollhouse (1996) - PLACEHOLDER
    "0000859",  # 859. April Fool's Day (1986) - PLACEHOLDER
    "0000860",  # 860. Believers, The (1987) - PLACEHOLDER
    "0000861",  # 861. Nosferatu a Venezia (1986) - PLACEHOLDER
    "0000862",  # 862. Jingle All the Way (1996) - PLACEHOLDER
    "0000863",  # 863. Garden of Finzi-Contini, The (Giardino dei Finzi-Contini, Il) (1970) - PLACEHOLDER
    "0000864",  # 864. My Fellow Americans (1996) - PLACEHOLDER
    "0000865",  # 865. Ice Storm, The (1997) - PLACEHOLDER
    "0000866",  # 866. Michael (1996) - PLACEHOLDER
    "0000867",  # 867. Whole Wide World, The (1996) - PLACEHOLDER
    "0000868",  # 868. Hearts and Minds (1996) - PLACEHOLDER
    "0000869",  # 869. Fools Rush In (1997) - PLACEHOLDER
    "0000870",  # 870. Touch (1997) - PLACEHOLDER
    "0000871",  # 871. Vegas Vacation (1997) - PLACEHOLDER
    "0000872",  # 872. Love Jones (1997) - PLACEHOLDER
    "0000873",  # 873. Picture Perfect (1997) - PLACEHOLDER
    "0000874",  # 874. Career Girls (1997) - PLACEHOLDER
    "0000875",  # 875. She's So Lovely (1997) - PLACEHOLDER
    "0000876",  # 876. Money Talks (1997) - PLACEHOLDER
    "0000877",  # 877. Excess Baggage (1997) - PLACEHOLDER
    "0000878",  # 878. That Darn Cat! (1997) - PLACEHOLDER
    "0000879",  # 879. Peacemaker, The (1997) - PLACEHOLDER
    "0000880",  # 880. Soul Food (1997) - PLACEHOLDER
    "0000881",  # 881. Money Talks (1997) - PLACEHOLDER
    "0000882",  # 882. Washington Square (1997) - PLACEHOLDER
    "0000883",  # 883. Telling Lies in America (1997) - PLACEHOLDER
    "0000884",  # 884. Year of the Horse (1997) - PLACEHOLDER
    "0000885",  # 885. Phantoms (1998) - PLACEHOLDER
    "0000886",  # 886. Life Less Ordinary, A (1997) - PLACEHOLDER
    "0000887",  # 887. Eve's Bayou (1997) - PLACEHOLDER
    "0000888",  # 888. One Night Stand (1997) - PLACEHOLDER
    "0000889",  # 889. Tango Lesson, The (1997) - PLACEHOLDER
    "0000890",  # 890. Mortal Kombat: Annihilation (1997) - PLACEHOLDER
    "0000891",  # 891. Bent (1997) - PLACEHOLDER
    "0000892",  # 892. Flubber (1997) - PLACEHOLDER
    "0000893",  # 893. For Richer or Poorer (1997) - PLACEHOLDER
    "0000894",  # 894. Home Alone 3 (1997) - PLACEHOLDER
    "0000895",  # 895. Scream 2 (1997) - PLACEHOLDER
    "0000896",  # 896. Sweet Hereafter, The (1997) - PLACEHOLDER
    "0000897",  # 897. Time Tracers (1995) - PLACEHOLDER
    "0000898",  # 898. Postman, The (1997) - PLACEHOLDER
    "0000899",  # 899. Winter Guest, The (1997) - PLACEHOLDER
    "0000900",  # 900. Kundun (1997) - PLACEHOLDER
    "0000901",  # 901. Mr. Magoo (1997) - PLACEHOLDER
    "0000902",  # 902. Big Lebowski, The (1998) - PLACEHOLDER
    "0000903",  # 903. Afterglow (1997) - PLACEHOLDER
    "0000904",  # 904. Ma vie en rose (My Life in Pink) (1997) - PLACEHOLDER
    "0000905",  # 905. Great Expectations (1998) - PLACEHOLDER
    "0000906",  # 906. Oscar & Lucinda (1997) - PLACEHOLDER
    "0000907",  # 907. Vermin (1998) - PLACEHOLDER
    "0000908",  # 908. Half Baked (1998) - PLACEHOLDER
    "0000909",  # 909. Dangerous Beauty (1998) - PLACEHOLDER
    "0000910",  # 910. Nil By Mouth (1997) - PLACEHOLDER
    "0000911",  # 911. Twilight (1998) - PLACEHOLDER
    "0000912",  # 912. U.S. Marshalls (1998) - PLACEHOLDER
    "0000913",  # 913. Love and Death on Long Island (1997) - PLACEHOLDER
    "0000914",  # 914. Wild Things (1998) - PLACEHOLDER
    "0000915",  # 915. Primary Colors (1998) - PLACEHOLDER
    "0000916",  # 916. Lost in Space (1998) - PLACEHOLDER
    "0000917",  # 917. Mercury Rising (1998) - PLACEHOLDER
    "0000918",  # 918. City of Angels (1998) - PLACEHOLDER
    "0000919",  # 919. City of Lost Children, The (1995) - PLACEHOLDER
    "0000920",  # 920. Two Bits (1995) - PLACEHOLDER
    "0000921",  # 921. Farewell My Concubine (1993) - PLACEHOLDER
    "0000922",  # 922. Dead Man (1995) - PLACEHOLDER
    "0000923",  # 923. Raise the Red Lantern (1991) - PLACEHOLDER
    "0000924",  # 924. White Squall (1996) - PLACEHOLDER
    "0000925",  # 925. Unforgettable (1996) - PLACEHOLDER
    "0000926",  # 926. Down Periscope (1996) - PLACEHOLDER
    "0000927",  # 927. Flower of My Secret, The (Flor de mi secreto, La) (1995) - PLACEHOLDER
    "0000928",  # 928. Craft, The (1996) - PLACEHOLDER
    "0000929",  # 929. Harriet the Spy (1996) - PLACEHOLDER
    "0000930",  # 930. Chain Reaction (1996) - PLACEHOLDER
    "0000931",  # 931. Island of Dr. Moreau, The (1996) - PLACEHOLDER
    "0000932",  # 932. First Kid (1996) - PLACEHOLDER
    "0000933",  # 933. Funeral, The (1996) - PLACEHOLDER
    "0000934",  # 934. Preacher's Wife, The (1996) - PLACEHOLDER
    "0000935",  # 935. Paradise Road (1997) - PLACEHOLDER
    "0000936",  # 936. Brassed Off (1996) - PLACEHOLDER
    "0000937",  # 937. Thousand Acres, A (1997) - PLACEHOLDER
    "0000938",  # 938. Smile Like Yours, A (1997) - PLACEHOLDER
    "0000939",  # 939. Murder in the First (1995) - PLACEHOLDER
    "0000940",  # 940. Airheads (1994) - PLACEHOLDER
    "0000941",  # 941. With Honors (1994) - PLACEHOLDER
    "0000942",  # 942. What's Love Got to Do with It (1993) - PLACEHOLDER
    "0000943",  # 943. Killing Zoe (1994) - PLACEHOLDER
    "0000944",  # 944. Renaissance Man (1994) - PLACEHOLDER
    "0000945",  # 945. Charade (1963) - PLACEHOLDER
    "0000946",  # 946. Fox and the Hound, The (1981) - PLACEHOLDER
    "0000947",  # 947. Big Blue, The (Grand bleu, Le) (1988) - PLACEHOLDER
    "0000948",  # 948. Booty Call (1997) - PLACEHOLDER
    "0000949",  # 949. How to Make an American Quilt (1995) - PLACEHOLDER
    "0000950",  # 950. Georgia (1995) - PLACEHOLDER
    "0000951",  # 951. Indian in the Cupboard, The (1995) - PLACEHOLDER
    "0000952",  # 952. Blue in the Face (1995) - PLACEHOLDER
    "0000953",  # 953. Unstrung Heroes (1995) - PLACEHOLDER
    "0000954",  # 954. Unzipped (1995) - PLACEHOLDER
    "0000955",  # 955. Before Sunrise (1995) - PLACEHOLDER
    "0000956",  # 956. Nobody's Fool (1994) - PLACEHOLDER
    "0000957",  # 957. Pushing Hands (1992) - PLACEHOLDER
    "0000958",  # 958. To Live (Huozhe) (1994) - PLACEHOLDER
    "0000959",  # 959. Dazed and Confused (1993) - PLACEHOLDER
    "0000960",  # 960. Naked (1993) - PLACEHOLDER
    "0000961",  # 961. Orlando (1993) - PLACEHOLDER
    "0000962",  # 962. Ruby in Paradise (1993) - PLACEHOLDER
    "0000963",  # 963. Some Folks Call It a Sling Blade (1993) - PLACEHOLDER
    "0000964",  # 964. Month by the Lake, A (1995) - PLACEHOLDER
    "0000965",  # 965. Funny Face (1957) - PLACEHOLDER
    "0000966",  # 966. Affair to Remember, An (1957) - PLACEHOLDER
    "0000967",  # 967. Little Lord Fauntleroy (1936) - PLACEHOLDER
    "0000968",  # 968. Inspector General, The (1949) - PLACEHOLDER
    "0000969",  # 969. Winnie the Pooh and the Blustery Day (1968) - PLACEHOLDER
    "0000970",  # 970. Hear My Song (1991) - PLACEHOLDER
    "0000971",  # 971. Mediterraneo (1991) - PLACEHOLDER
    "0000972",  # 972. Passion Fish (1992) - PLACEHOLDER
    "0000973",  # 973. Grateful Dead (1995) - PLACEHOLDER
    "0000974",  # 974. Eye for an Eye (1996) - PLACEHOLDER
    "0000975",  # 975. Fear (1996) - PLACEHOLDER
    "0000976",  # 976. Solo (1996) - PLACEHOLDER
    "0000977",  # 977. Substitute, The (1996) - PLACEHOLDER
    "0000978",  # 978. Heaven's Prisoners (1996) - PLACEHOLDER
    "0000979",  # 979. Trigger Effect, The (1996) - PLACEHOLDER
    "0000980",  # 980. Mother Night (1996) - PLACEHOLDER
    "0000981",  # 981. Dangerous Ground (1997) - PLACEHOLDER
    "0000982",  # 982. Maximum Risk (1996) - PLACEHOLDER
    "0000983",  # 983. Rich Man's Wife, The (1996) - PLACEHOLDER
    "0000984",  # 984. Shadow Conspiracy (1997) - PLACEHOLDER
    "0000985",  # 985. Blood & Wine (1997) - PLACEHOLDER
    "0000986",  # 986. Turbulence (1997) - PLACEHOLDER
    "0000987",  # 987. Underworld (1997) - PLACEHOLDER
    "0000988",  # 988. Beautician and the Beast, The (1997) - PLACEHOLDER
    "0000989",  # 989. Cats Don't Dance (1997) - PLACEHOLDER
    "0000990",  # 990. Anna Karenina (1997) - PLACEHOLDER
    "0000991",  # 991. Keys to Tulsa (1997) - PLACEHOLDER
    "0000992",  # 992. Head Above Water (1996) - PLACEHOLDER
    "0000993",  # 993. Hercules (1997) - PLACEHOLDER
    "0000994",  # 994. Last Time I Committed Suicide, The (1997) - PLACEHOLDER
    "0000995",  # 995. Kiss Me, Guido (1997) - PLACEHOLDER
    "0000996",  # 996. Big Green, The (1995) - PLACEHOLDER
    "0000997",  # 997. Stuart Saves His Family (1995) - PLACEHOLDER
    "0000998",  # 998. Cabin Boy (1994) - PLACEHOLDER
    "0000999",  # 999. Clean Slate (1994) - PLACEHOLDER
    "0001000",  # 1000. Lightning Jack (1994) - PLACEHOLDER
    "0001001",  # 1001. Stupids, The (1996) - PLACEHOLDER
    "0001002",  # 1002. Pest, The (1997) - PLACEHOLDER
    "0001003",  # 1003. That Darn Cat! (1997) - PLACEHOLDER
    "0001004",  # 1004. Geronimo: An American Legend (1993) - PLACEHOLDER
    "0001005",  # 1005. Double vie de Véronique, La (Double Life of Veronique, The) (1991) - PLACEHOLDER
    "0001006",  # 1006. Until the End of the World (Bis ans Ende der Welt) (1991) - PLACEHOLDER
    "0001007",  # 1007. Waiting for Guffman (1996) - PLACEHOLDER
    "0001008",  # 1008. I Shot Andy Warhol (1996) - PLACEHOLDER
    "0001009",  # 1009. Stealing Beauty (1996) - PLACEHOLDER
    "0001010",  # 1010. Basquiat (1996) - PLACEHOLDER
    "0001011",  # 1011. 2 Days in the Valley (1996) - PLACEHOLDER
    "0001012",  # 1012. Private Parts (1997) - PLACEHOLDER
    "0001013",  # 1013. Anaconda (1997) - PLACEHOLDER
    "0001014",  # 1014. Romy and Michele's High School Reunion (1997) - PLACEHOLDER
    "0001015",  # 1015. Shiloh (1997) - PLACEHOLDER
    "0001016",  # 1016. Con Air (1997) - PLACEHOLDER
    "0001017",  # 1017. Trees Lounge (1996) - PLACEHOLDER
    "0001018",  # 1018. Tie Me Up! Tie Me Down! (1990) - PLACEHOLDER
    "0001019",  # 1019. Die xue shuang xiong (Killer, The) (1989) - PLACEHOLDER
    "0001020",  # 1020. Gaslight (1944) - PLACEHOLDER
    "0001021",  # 1021. 8 1/2 (1963) - PLACEHOLDER
    "0001022",  # 1022. Fast, Cheap & Out of Control (1997) - PLACEHOLDER
    "0001023",  # 1023. Fathers' Day (1997) - PLACEHOLDER
    "0001024",  # 1024. Mrs. Dalloway (1997) - PLACEHOLDER
    "0001025",  # 1025. Fire Down Below (1997) - PLACEHOLDER
    "0001026",  # 1026. Lay of the Land, The (1997) - PLACEHOLDER
    "0001027",  # 1027. Shooter, The (1995) - PLACEHOLDER
    "0001028",  # 1028. Grumpier Old Men (1995) - PLACEHOLDER
    "0001029",  # 1029. Jury Duty (1995) - PLACEHOLDER
    "0001030",  # 1030. Beverly Hillbillies, The (1993) - PLACEHOLDER
    "0001031",  # 1031. Lassie (1994) - PLACEHOLDER
    "0001032",  # 1032. Little Big League (1994) - PLACEHOLDER
    "0001033",  # 1033. Homeward Bound II: Lost in San Francisco (1996) - PLACEHOLDER
    "0001034",  # 1034. Quest, The (1996) - PLACEHOLDER
    "0001035",  # 1035. Cool Runnings (1993) - PLACEHOLDER
    "0001036",  # 1036. Drop Dead Fred (1991) - PLACEHOLDER
    "0001037",  # 1037. Grease 2 (1982) - PLACEHOLDER
    "0001038",  # 1038. Switchback (1997) - PLACEHOLDER
    "0001039",  # 1039. Hamlet (1996) - PLACEHOLDER
    "0001040",  # 1040. Two if by Sea (1996) - PLACEHOLDER
    "0001041",  # 1041. Forget Paris (1995) - PLACEHOLDER
    "0001042",  # 1042. Just Cause (1995) - PLACEHOLDER
    "0001043",  # 1043. Rent-a-Kid (1995) - PLACEHOLDER
    "0001044",  # 1044. Paper, The (1994) - PLACEHOLDER
    "0001045",  # 1045. Fearless (1993) - PLACEHOLDER
    "0001046",  # 1046. Malice (1993) - PLACEHOLDER
    "0001047",  # 1047. Multiplicity (1996) - PLACEHOLDER
    "0001048",  # 1048. She's the One (1996) - PLACEHOLDER
    "0001049",  # 1049. House Arrest (1996) - PLACEHOLDER
    "0001050",  # 1050. Ghost and Mrs. Muir, The (1947) - PLACEHOLDER
    "0001051",  # 1051. Associate, The (1996) - PLACEHOLDER
    "0001052",  # 1052. Dracula: Dead and Loving It (1995) - PLACEHOLDER
    "0001053",  # 1053. Now and Then (1995) - PLACEHOLDER
    "0001054",  # 1054. Mr. Wrong (1996) - PLACEHOLDER
    "0001055",  # 1055. Simple Twist of Fate, A (1994) - PLACEHOLDER
    "0001056",  # 1056. Cronos (1992) - PLACEHOLDER
    "0001057",  # 1057. Pallbearer, The (1996) - PLACEHOLDER
    "0001058",  # 1058. War, The (1994) - PLACEHOLDER
    "0001059",  # 1059. Don't Be a Menace to South Central While Drinking Your Juice in the Hood (1996) - PLACEHOLDER
    "0001060",  # 1060. Adventures of Pinocchio, The (1996) - PLACEHOLDER
    "0001061",  # 1061. Evening Star, The (1996) - PLACEHOLDER
    "0001062",  # 1062. Four Days in September (1997) - PLACEHOLDER
    "0001063",  # 1063. Little Princess, A (1995) - PLACEHOLDER
    "0001064",  # 1064. Crossfire (1947) - PLACEHOLDER
    "0001065",  # 1065. Koyaanisqatsi (1983) - PLACEHOLDER
    "0001066",  # 1066. Balto (1995) - PLACEHOLDER
    "0001067",  # 1067. Bottle Rocket (1996) - PLACEHOLDER
    "0001068",  # 1068. Star Maker, The (Uomo delle stelle, L') (1995) - PLACEHOLDER
    "0001069",  # 1069. Amateur (1994) - PLACEHOLDER
    "0001070",  # 1070. Living in Oblivion (1995) - PLACEHOLDER
    "0001071",  # 1071. Party Girl (1995) - PLACEHOLDER
    "0001072",  # 1072. Pyromaniac's Love Story, A (1995) - PLACEHOLDER
    "0001073",  # 1073. Shallow Grave (1994) - PLACEHOLDER
    "0001074",  # 1074. Reality Bites (1994) - PLACEHOLDER
    "0001075",  # 1075. Man of No Importance, A (1994) - PLACEHOLDER
    "0001076",  # 1076. Pagemaster, The (1994) - PLACEHOLDER
    "0001077",  # 1077. Love and a .45 (1994) - PLACEHOLDER
    "0001078",  # 1078. Oliver & Company (1988) - PLACEHOLDER
    "0001079",  # 1079. Joe's Apartment (1996) - PLACEHOLDER
    "0001080",  # 1080. Celestial Clockwork (1994) - PLACEHOLDER
    "0001081",  # 1081. Curdled (1996) - PLACEHOLDER
    "0001082",  # 1082. Female Perversions (1996) - PLACEHOLDER
    "0001083",  # 1083. Albino Alligator (1996) - PLACEHOLDER
    "0001084",  # 1084. Anne Frank Remembered (1995) - PLACEHOLDER
    "0001085",  # 1085. Carried Away (1996) - PLACEHOLDER
    "0001086",  # 1086. It's My Party (1995) - PLACEHOLDER
    "0001087",  # 1087. Bloodsport 2 (1995) - PLACEHOLDER
    "0001088",  # 1088. Double Team (1997) - PLACEHOLDER
    "0001089",  # 1089. Speed 2: Cruise Control (1997) - PLACEHOLDER
    "0001090",  # 1090. Sliver (1993) - PLACEHOLDER
    "0001091",  # 1091. Pete's Dragon (1977) - PLACEHOLDER
    "0001092",  # 1092. Dear God (1996) - PLACEHOLDER
    "0001093",  # 1093. Live Nude Girls (1995) - PLACEHOLDER
    "0001094",  # 1094. Thin Line Between Love and Hate, A (1996) - PLACEHOLDER
    "0001095",  # 1095. High School High (1996) - PLACEHOLDER
    "0001096",  # 1096. Commandments (1997) - PLACEHOLDER
    "0001097",  # 1097. Hate (Haine, La) (1995) - PLACEHOLDER
    "0001098",  # 1098. Flirting With Disaster (1996) - PLACEHOLDER
    "0001099",  # 1099. Red Firecracker, Green Firecracker (1994) - PLACEHOLDER
    "0001100",  # 1100. What Happened Was... (1994) - PLACEHOLDER
    "0001101",  # 1101. Six Degrees of Separation (1993) - PLACEHOLDER
    "0001102",  # 1102. Two Much (1996) - PLACEHOLDER
    "0001103",  # 1103. Trust (1990) - PLACEHOLDER
    "0001104",  # 1104. C'est arrivé près de chez vous (1992) - PLACEHOLDER
    "0001105",  # 1105. Firestorm (1998) - PLACEHOLDER
    "0001106",  # 1106. Newton Boys, The (1998) - PLACEHOLDER
    "0001107",  # 1107. Beyond Rangoon (1995) - PLACEHOLDER
    "0001108",  # 1108. Feast of July (1995) - PLACEHOLDER
    "0001109",  # 1109. Death and the Maiden (1994) - PLACEHOLDER
    "0001110",  # 1110. Tank Girl (1995) - PLACEHOLDER
    "0001111",  # 1111. Double Happiness (1994) - PLACEHOLDER
    "0001112",  # 1112. Cobb (1994) - PLACEHOLDER
    "0001113",  # 1113. Mrs. Parker and the Vicious Circle (1994) - PLACEHOLDER
    "0001114",  # 1114. Faithful (1996) - PLACEHOLDER
    "0001115",  # 1115. Twelfth Night (1996) - PLACEHOLDER
    "0001116",  # 1116. Mark of Zorro, The (1940) - PLACEHOLDER
    "0001117",  # 1117. Surviving Picasso (1996) - PLACEHOLDER
    "0001118",  # 1118. Up in Smoke (1978) - PLACEHOLDER
    "0001119",  # 1119. Some Kind of Wonderful (1987) - PLACEHOLDER
    "0001120",  # 1120. I'm Not Rappaport (1996) - PLACEHOLDER
    "0001121",  # 1121. Umbrellas of Cherbourg, The (Parapluies de Cherbourg, Les) (1964) - PLACEHOLDER
    "0001122",  # 1122. They Made Me a Criminal (1939) - PLACEHOLDER
    "0001123",  # 1123. Last Time I Saw Paris, The (1954) - PLACEHOLDER
    "0001124",  # 1124. Farewell to Arms, A (1932) - PLACEHOLDER
    "0001125",  # 1125. Innocents, The (1961) - PLACEHOLDER
    "0001126",  # 1126. Old Man and the Sea, The (1958) - PLACEHOLDER
    "0001127",  # 1127. Truman Show, The (1998) - PLACEHOLDER
    "0001128",  # 1128. Heidi Fleiss: Hollywood Madam (1995)  (1995) - PLACEHOLDER
    "0001129",  # 1129. Chungking Express (1994) - PLACEHOLDER
    "0001130",  # 1130. Jupiter's Wife (1994) - PLACEHOLDER
    "0001131",  # 1131. Safe (1995) - PLACEHOLDER
    "0001132",  # 1132. Feeling Minnesota (1996) - PLACEHOLDER
    "0001133",  # 1133. Escape to Witch Mountain (1975) - PLACEHOLDER
    "0001134",  # 1134. Get on the Bus (1996) - PLACEHOLDER
    "0001135",  # 1135. Doors, The (1991) - PLACEHOLDER
    "0001136",  # 1136. Ghosts of Mississippi (1996) - PLACEHOLDER
    "0001137",  # 1137. Beautiful Thing (1996) - PLACEHOLDER
    "0001138",  # 1138. Best Men (1997) - PLACEHOLDER
    "0001139",  # 1139. Hackers (1995) - PLACEHOLDER
    "0001140",  # 1140. Road to Wellville, The (1994) - PLACEHOLDER
    "0001141",  # 1141. War Room, The (1993) - PLACEHOLDER
    "0001142",  # 1142. When We Were Kings (1996) - PLACEHOLDER
    "0001143",  # 1143. Hard Eight (1996) - PLACEHOLDER
    "0001144",  # 1144. Quiet Room, The (1996) - PLACEHOLDER
    "0001145",  # 1145. Blue Chips (1994) - PLACEHOLDER
    "0001146",  # 1146. Calendar Girl (1993) - PLACEHOLDER
    "0001147",  # 1147. My Family (1995) - PLACEHOLDER
    "0001148",  # 1148. Tom & Viv (1994) - PLACEHOLDER
    "0001149",  # 1149. Walkabout (1971) - PLACEHOLDER
    "0001150",  # 1150. Last Dance (1996) - PLACEHOLDER
    "0001151",  # 1151. Original Gangstas (1996) - PLACEHOLDER
    "0001152",  # 1152. In Love and War (1996) - PLACEHOLDER
    "0001153",  # 1153. Backbeat (1993) - PLACEHOLDER
    "0001154",  # 1154. Alphaville (1965) - PLACEHOLDER
    "0001155",  # 1155. Rendezvous in Paris (Rendez-vous de Paris, Les) (1995) - PLACEHOLDER
    "0001156",  # 1156. Cyclo (1995) - PLACEHOLDER
    "0001157",  # 1157. Relic, The (1997) - PLACEHOLDER
    "0001158",  # 1158. Fille seule, La (A Single Girl) (1995) - PLACEHOLDER
    "0001159",  # 1159. Stalker (1979) - PLACEHOLDER
    "0001160",  # 1160. Love! Valour! Compassion! (1997) - PLACEHOLDER
    "0001161",  # 1161. Palookaville (1996) - PLACEHOLDER
    "0001162",  # 1162. Phat Beach (1996) - PLACEHOLDER
    "0001163",  # 1163. Portrait of a Lady, The (1996) - PLACEHOLDER
    "0001164",  # 1164. Zeus and Roxanne (1997) - PLACEHOLDER
    "0001165",  # 1165. Big Bully (1996) - PLACEHOLDER
    "0001166",  # 1166. Love & Human Remains (1993) - PLACEHOLDER
    "0001167",  # 1167. Sum of Us, The (1994) - PLACEHOLDER
    "0001168",  # 1168. Little Buddha (1993) - PLACEHOLDER
    "0001169",  # 1169. Fresh (1994) - PLACEHOLDER
    "0001170",  # 1170. Spanking the Monkey (1994) - PLACEHOLDER
    "0001171",  # 1171. Wild Reeds (1994) - PLACEHOLDER
    "0001172",  # 1172. Women, The (1939) - PLACEHOLDER
    "0001173",  # 1173. Bliss (1997) - PLACEHOLDER
    "0001174",  # 1174. Caught (1996) - PLACEHOLDER
    "0001175",  # 1175. Hugo Pool (1997) - PLACEHOLDER
    "0001176",  # 1176. Welcome To Sarajevo (1997) - PLACEHOLDER
    "0001177",  # 1177. Dunston Checks In (1996) - PLACEHOLDER
    "0001178",  # 1178. Major Payne (1994) - PLACEHOLDER
    "0001179",  # 1179. Man of the House (1995) - PLACEHOLDER
    "0001180",  # 1180. I Love Trouble (1994) - PLACEHOLDER
    "0001181",  # 1181. Low Down Dirty Shame, A (1994) - PLACEHOLDER
    "0001182",  # 1182. Cops and Robbersons (1994) - PLACEHOLDER
    "0001183",  # 1183. Cowboy Way, The (1994) - PLACEHOLDER
    "0001184",  # 1184. Endless Summer 2, The (1994) - PLACEHOLDER
    "0001185",  # 1185. In the Army Now (1994) - PLACEHOLDER
    "0001186",  # 1186. Inkwell, The (1994) - PLACEHOLDER
    "0001187",  # 1187. Switchblade Sisters (1975) - PLACEHOLDER
    "0001188",  # 1188. Young Guns II (1990) - PLACEHOLDER
    "0001189",  # 1189. Prefontaine (1997) - PLACEHOLDER
    "0001190",  # 1190. That Old Feeling (1997) - PLACEHOLDER
    "0001191",  # 1191. Letter From Death Row, A (1998) - PLACEHOLDER
    "0001192",  # 1192. Boys of St. Vincent, The (1993) - PLACEHOLDER
    "0001193",  # 1193. Before the Rain (Pred dozhdot) (1994) - PLACEHOLDER
    "0001194",  # 1194. Once Were Warriors (1994) - PLACEHOLDER
    "0001195",  # 1195. Strawberry and Chocolate (Fresa y chocolate) (1993) - PLACEHOLDER
    "0001196",  # 1196. Savage Nights (Nuits fauves, Les) (1992) - PLACEHOLDER
    "0001197",  # 1197. Family Thing, A (1996) - PLACEHOLDER
    "0001198",  # 1198. Purple Noon (1960) - PLACEHOLDER
    "0001199",  # 1199. Cemetery Man (Dellamorte Dellamore) (1994) - PLACEHOLDER
    "0001200",  # 1200. Kim (1950) - PLACEHOLDER
    "0001201",  # 1201. Marlene Dietrich: Shadow and Light (1996)  (1996) - PLACEHOLDER
    "0001202",  # 1202. Maybe, Maybe Not (Bewegte Mann, Der) (1994) - PLACEHOLDER
    "0001203",  # 1203. Top Hat (1935) - PLACEHOLDER
    "0001204",  # 1204. To Be or Not to Be (1942) - PLACEHOLDER
    "0001205",  # 1205. Secret Agent, The (1996) - PLACEHOLDER
    "0001206",  # 1206. Amos & Andrew (1993) - PLACEHOLDER
    "0001207",  # 1207. Jade (1995) - PLACEHOLDER
    "0001208",  # 1208. Kiss of Death (1995) - PLACEHOLDER
    "0001209",  # 1209. Mixed Nuts (1994) - PLACEHOLDER
    "0001210",  # 1210. Virtuosity (1995) - PLACEHOLDER
    "0001211",  # 1211. Blue Sky (1994) - PLACEHOLDER
    "0001212",  # 1212. Flesh and Bone (1993) - PLACEHOLDER
    "0001213",  # 1213. Guilty as Sin (1993) - PLACEHOLDER
    "0001214",  # 1214. In the Realm of the Senses (Ai no corrida) (1976) - PLACEHOLDER
    "0001215",  # 1215. Barb Wire (1996) - PLACEHOLDER
    "0001216",  # 1216. Kissed (1996) - PLACEHOLDER
    "0001217",  # 1217. Assassins (1995) - PLACEHOLDER
    "0001218",  # 1218. Friday (1995) - PLACEHOLDER
    "0001219",  # 1219. Goofy Movie, A (1995) - PLACEHOLDER
    "0001220",  # 1220. Higher Learning (1995) - PLACEHOLDER
    "0001221",  # 1221. When a Man Loves a Woman (1994) - PLACEHOLDER
    "0001222",  # 1222. Judgment Night (1993) - PLACEHOLDER
    "0001223",  # 1223. King of the Hill (1993) - PLACEHOLDER
    "0001224",  # 1224. Scout, The (1994) - PLACEHOLDER
    "0001225",  # 1225. Angus (1995) - PLACEHOLDER
    "0001226",  # 1226. Night Falls on Manhattan (1997) - PLACEHOLDER
    "0001227",  # 1227. Awfully Big Adventure, An (1995) - PLACEHOLDER
    "0001228",  # 1228. Under Siege 2: Dark Territory (1995) - PLACEHOLDER
    "0001229",  # 1229. Poison Ivy II (1995) - PLACEHOLDER
    "0001230",  # 1230. Ready to Wear (Pret-A-Porter) (1994) - PLACEHOLDER
    "0001231",  # 1231. Marked for Death (1990) - PLACEHOLDER
    "0001232",  # 1232. Madonna: Truth or Dare (1991) - PLACEHOLDER
    "0001233",  # 1233. Nénette et Boni (1996) - PLACEHOLDER
    "0001234",  # 1234. Chairman of the Board (1998) - PLACEHOLDER
    "0001235",  # 1235. Big Bang Theory, The (1994) - PLACEHOLDER
    "0001236",  # 1236. Other Voices, Other Rooms (1997) - PLACEHOLDER
    "0001237",  # 1237. Twisted (1996) - PLACEHOLDER
    "0001238",  # 1238. Full Speed (1996) - PLACEHOLDER
    "0001239",  # 1239. Cutthroat Island (1995) - PLACEHOLDER
    "0001240",  # 1240. Ghost in the Shell (Kokaku kidotai) (1995) - PLACEHOLDER
    "0001241",  # 1241. Van, The (1996) - PLACEHOLDER
    "0001242",  # 1242. Old Lady Who Walked in the Sea, The (Vieille qui marchait dans la mer, La) (1991) - PLACEHOLDER
    "0001243",  # 1243. Night Flier (1997) - PLACEHOLDER
    "0001244",  # 1244. Metro (1997) - PLACEHOLDER
    "0001245",  # 1245. Gridlock'd (1997) - PLACEHOLDER
    "0001246",  # 1246. Bushwhacked (1995) - PLACEHOLDER
    "0001247",  # 1247. Bad Girls (1994) - PLACEHOLDER
    "0001248",  # 1248. Blink (1994) - PLACEHOLDER
    "0001249",  # 1249. For Love or Money (1993) - PLACEHOLDER
    "0001250",  # 1250. Best of the Best 3: No Turning Back (1995) - PLACEHOLDER
    "0001251",  # 1251. A Chef in Love (1996) - PLACEHOLDER
    "0001252",  # 1252. Contempt (Mépris, Le) (1963) - PLACEHOLDER
    "0001253",  # 1253. Tie That Binds, The (1995) - PLACEHOLDER
    "0001254",  # 1254. Gone Fishin' (1997) - PLACEHOLDER
    "0001255",  # 1255. Broken English (1996) - PLACEHOLDER
    "0001256",  # 1256. Designated Mourner, The (1997) - PLACEHOLDER
    "0001257",  # 1257. Designated Mourner, The (1997) - PLACEHOLDER
    "0001258",  # 1258. Trial and Error (1997) - PLACEHOLDER
    "0001259",  # 1259. Pie in the Sky (1995) - PLACEHOLDER
    "0001260",  # 1260. Total Eclipse (1995) - PLACEHOLDER
    "0001261",  # 1261. Run of the Country, The (1995) - PLACEHOLDER
    "0001262",  # 1262. Walking and Talking (1996) - PLACEHOLDER
    "0001263",  # 1263. Foxfire (1996) - PLACEHOLDER
    "0001264",  # 1264. Nothing to Lose (1994) - PLACEHOLDER
    "0001265",  # 1265. Star Maps (1997) - PLACEHOLDER
    "0001266",  # 1266. Bread and Chocolate (Pane e cioccolata) (1973) - PLACEHOLDER
    "0001267",  # 1267. Clockers (1995) - PLACEHOLDER
    "0001268",  # 1268. Bitter Moon (1992) - PLACEHOLDER
    "0001269",  # 1269. Love in the Afternoon (1957) - PLACEHOLDER
    "0001270",  # 1270. Life with Mikey (1993) - PLACEHOLDER
    "0001271",  # 1271. North (1994) - PLACEHOLDER
    "0001272",  # 1272. Talking About Sex (1994) - PLACEHOLDER
    "0001273",  # 1273. Color of Night (1994) - PLACEHOLDER
    "0001274",  # 1274. Robocop 3 (1993) - PLACEHOLDER
    "0001275",  # 1275. Killer (Bulletproof Heart) (1994) - PLACEHOLDER
    "0001276",  # 1276. Sunset Park (1996) - PLACEHOLDER
    "0001277",  # 1277. Set It Off (1996) - PLACEHOLDER
    "0001278",  # 1278. Selena (1997) - PLACEHOLDER
    "0001279",  # 1279. Wild America (1997) - PLACEHOLDER
    "0001280",  # 1280. Gang Related (1997) - PLACEHOLDER
    "0001281",  # 1281. Manny & Lo (1996) - PLACEHOLDER
    "0001282",  # 1282. Grass Harp, The (1995) - PLACEHOLDER
    "0001283",  # 1283. Out to Sea (1997) - PLACEHOLDER
    "0001284",  # 1284. Before and After (1996) - PLACEHOLDER
    "0001285",  # 1285. Princess Caraboo (1994) - PLACEHOLDER
    "0001286",  # 1286. Shall We Dance? (1937) - PLACEHOLDER
    "0001287",  # 1287. Ed (1996) - PLACEHOLDER
    "0001288",  # 1288. Denise Calls Up (1995) - PLACEHOLDER
    "0001289",  # 1289. Jack and Sarah (1995) - PLACEHOLDER
    "0001290",  # 1290. Country Life (1994) - PLACEHOLDER
    "0001291",  # 1291. Celtic Pride (1996) - PLACEHOLDER
    "0001292",  # 1292. Simple Wish, A (1997) - PLACEHOLDER
    "0001293",  # 1293. Star Kid (1997) - PLACEHOLDER
    "0001294",  # 1294. Ayn Rand: A Sense of Life (1997) - PLACEHOLDER
    "0001295",  # 1295. Kicked in the Head (1997) - PLACEHOLDER
    "0001296",  # 1296. Indian Summer (1996) - PLACEHOLDER
    "0001297",  # 1297. Love Affair (1994) - PLACEHOLDER
    "0001298",  # 1298. Band Wagon, The (1953) - PLACEHOLDER
    "0001299",  # 1299. Penny Serenade (1941) - PLACEHOLDER
    "0001300",  # 1300. 'Til There Was You (1997) - PLACEHOLDER
    "0001301",  # 1301. Stripes (1981) - PLACEHOLDER
    "0001302",  # 1302. Late Bloomers (1996) - PLACEHOLDER
    "0001303",  # 1303. Getaway, The (1994) - PLACEHOLDER
    "0001304",  # 1304. New York Cop (1996) - PLACEHOLDER
    "0001305",  # 1305. National Lampoon's Senior Trip (1995) - PLACEHOLDER
    "0001306",  # 1306. Delta of Venus (1994) - PLACEHOLDER
    "0001307",  # 1307. Carmen Miranda: Bananas Is My Business (1994) - PLACEHOLDER
    "0001308",  # 1308. Babyfever (1994) - PLACEHOLDER
    "0001309",  # 1309. Very Natural Thing, A (1974) - PLACEHOLDER
    "0001310",  # 1310. Walk in the Sun, A (1945) - PLACEHOLDER
    "0001311",  # 1311. Waiting to Exhale (1995) - PLACEHOLDER
    "0001312",  # 1312. Pompatus of Love, The (1996) - PLACEHOLDER
    "0001313",  # 1313. Palmetto (1998) - PLACEHOLDER
    "0001314",  # 1314. Surviving the Game (1994) - PLACEHOLDER
    "0001315",  # 1315. Inventing the Abbotts (1997) - PLACEHOLDER
    "0001316",  # 1316. Horse Whisperer, The (1998) - PLACEHOLDER
    "0001317",  # 1317. Journey of August King, The (1995) - PLACEHOLDER
    "0001318",  # 1318. Catwalk (1995) - PLACEHOLDER
    "0001319",  # 1319. Neon Bible, The (1995) - PLACEHOLDER
    "0001320",  # 1320. Homage (1995) - PLACEHOLDER
    "0001321",  # 1321. Open Season (1996) - PLACEHOLDER
    "0001322",  # 1322. Metisse (Café au Lait) (1993) - PLACEHOLDER
    "0001323",  # 1323. Wooden Man's Bride, The (Wu Kui) (1994) - PLACEHOLDER
    "0001324",  # 1324. Loaded (1994) - PLACEHOLDER
    "0001325",  # 1325. August (1996) - PLACEHOLDER
    "0001326",  # 1326. Boys (1996) - PLACEHOLDER
    "0001327",  # 1327. Captives (1994) - PLACEHOLDER
    "0001328",  # 1328. Of Love and Shadows (1994) - PLACEHOLDER
    "0001329",  # 1329. Low Life, The (1994) - PLACEHOLDER
    "0001330",  # 1330. An Unforgettable Summer (1994) - PLACEHOLDER
    "0001331",  # 1331. Last Klezmer: Leopold Kozlowski, His Life and Music, The (1995) - PLACEHOLDER
    "0001332",  # 1332. My Life and Times With Antonin Artaud (En compagnie d'Antonin Artaud) (1993) - PLACEHOLDER
    "0001333",  # 1333. Midnight Dancers (Sibak) (1994) - PLACEHOLDER
    "0001334",  # 1334. Somebody to Love (1994) - PLACEHOLDER
    "0001335",  # 1335. American Buffalo (1996) - PLACEHOLDER
    "0001336",  # 1336. Kazaam (1996) - PLACEHOLDER
    "0001337",  # 1337. Larger Than Life (1996) - PLACEHOLDER
    "0001338",  # 1338. Two Deaths (1995) - PLACEHOLDER
    "0001339",  # 1339. Stefano Quantestorie (1993) - PLACEHOLDER
    "0001340",  # 1340. Crude Oasis, The (1995) - PLACEHOLDER
    "0001341",  # 1341. Hedd Wyn (1992) - PLACEHOLDER
    "0001342",  # 1342. Convent, The (Convento, O) (1995) - PLACEHOLDER
    "0001343",  # 1343. Lotto Land (1995) - PLACEHOLDER
    "0001344",  # 1344. Story of Xinghua, The (1993) - PLACEHOLDER
    "0001345",  # 1345. Day the Sun Turned Cold, The (Tianguo niezi) (1994) - PLACEHOLDER
    "0001346",  # 1346. Dingo (1992) - PLACEHOLDER
    "0001347",  # 1347. Ballad of Narayama, The (Narayama Bushiko) (1958) - PLACEHOLDER
    "0001348",  # 1348. Every Other Weekend (1990) - PLACEHOLDER
    "0001349",  # 1349. Mille bolle blu (1993) - PLACEHOLDER
    "0001350",  # 1350. Crows and Sparrows (1949) - PLACEHOLDER
    "0001351",  # 1351. Lover's Knot (1996) - PLACEHOLDER
    "0001352",  # 1352. Shadow of Angels (Schatten der Engel) (1976) - PLACEHOLDER
    "0001353",  # 1353. 1-900 (1994) - PLACEHOLDER
    "0001354",  # 1354. Venice/Venice (1992) - PLACEHOLDER
    "0001355",  # 1355. Infinity (1996) - PLACEHOLDER
    "0001356",  # 1356. Ed's Next Move (1996) - PLACEHOLDER
    "0001357",  # 1357. For the Moment (1994) - PLACEHOLDER
    "0001358",  # 1358. The Deadly Cure (1996) - PLACEHOLDER
    "0001359",  # 1359. Boys in Venice (1996) - PLACEHOLDER
    "0001360",  # 1360. Sexual Life of the Belgians, The (1994) - PLACEHOLDER
    "0001361",  # 1361. Search for One-eye Jimmy, The (1996) - PLACEHOLDER
    "0001362",  # 1362. American Strays (1996) - PLACEHOLDER
    "0001363",  # 1363. Leopard Son, The (1996) - PLACEHOLDER
    "0001364",  # 1364. Bird of Prey (1996) - PLACEHOLDER
    "0001365",  # 1365. Johnny 100 Pesos (1993) - PLACEHOLDER
    "0001366",  # 1366. JLG/JLG - autoportrait de décembre (1994) - PLACEHOLDER
    "0001367",  # 1367. Faust (1994) - PLACEHOLDER
    "0001368",  # 1368. Mina Tannenbaum (1994) - PLACEHOLDER
    "0001369",  # 1369. Forbidden Christ, The (Cristo proibito, Il) (1950) - PLACEHOLDER
    "0001370",  # 1370. I Can't Sleep (J'ai pas sommeil) (1994) - PLACEHOLDER
    "0001371",  # 1371. Machine, The (1994) - PLACEHOLDER
    "0001372",  # 1372. Stranger, The (1994) - PLACEHOLDER
    "0001373",  # 1373. Good Morning (1971) - PLACEHOLDER
    "0001374",  # 1374. Falling in Love Again (1980) - PLACEHOLDER
    "0001375",  # 1375. Cement Garden, The (1993) - PLACEHOLDER
    "0001376",  # 1376. Meet Wally Sparks (1997) - PLACEHOLDER
    "0001377",  # 1377. Hotel de Love (1996) - PLACEHOLDER
    "0001378",  # 1378. Rhyme & Reason (1997) - PLACEHOLDER
    "0001379",  # 1379. Love and Other Catastrophes (1996) - PLACEHOLDER
    "0001380",  # 1380. Hollow Reed (1996) - PLACEHOLDER
    "0001381",  # 1381. Losing Chase (1996) - PLACEHOLDER
    "0001382",  # 1382. Bonheur, Le (1965) - PLACEHOLDER
    "0001383",  # 1383. Second Jungle Book: Mowgli & Baloo, The (1997) - PLACEHOLDER
    "0001384",  # 1384. Squeeze (1996) - PLACEHOLDER
    "0001385",  # 1385. Roseanna's Grave (For Roseanna) (1997) - PLACEHOLDER
    "0001386",  # 1386. Tetsuo II: Body Hammer (1992) - PLACEHOLDER
    "0001387",  # 1387. Fall (1997) - PLACEHOLDER
    "0001388",  # 1388. Gabbeh (1996) - PLACEHOLDER
    "0001389",  # 1389. Mondo (1996) - PLACEHOLDER
    "0001390",  # 1390. Innocent Sleep, The (1995) - PLACEHOLDER
    "0001391",  # 1391. For Ever Mozart (1996) - PLACEHOLDER
    "0001392",  # 1392. Locusts, The (1997) - PLACEHOLDER
    "0001393",  # 1393. Stag (1997) - PLACEHOLDER
    "0001394",  # 1394. Swept from the Sea (1997) - PLACEHOLDER
    "0001395",  # 1395. Hurricane Streets (1998) - PLACEHOLDER
    "0001396",  # 1396. Stonewall (1995) - PLACEHOLDER
    "0001397",  # 1397. Of Human Bondage (1934) - PLACEHOLDER
    "0001398",  # 1398. Anna (1996) - PLACEHOLDER
    "0001399",  # 1399. Stranger in the House (1997) - PLACEHOLDER
    "0001400",  # 1400. Picture Bride (1995) - PLACEHOLDER
    "0001401",  # 1401. M. Butterfly (1993) - PLACEHOLDER
    "0001402",  # 1402. Ciao, Professore! (1993) - PLACEHOLDER
    "0001403",  # 1403. Caro Diario (Dear Diary) (1994) - PLACEHOLDER
    "0001404",  # 1404. Withnail and I (1987) - PLACEHOLDER
    "0001405",  # 1405. Boy's Life 2 (1997) - PLACEHOLDER
    "0001406",  # 1406. When Night Is Falling (1995) - PLACEHOLDER
    "0001407",  # 1407. Specialist, The (1994) - PLACEHOLDER
    "0001408",  # 1408. Gordy (1995) - PLACEHOLDER
    "0001409",  # 1409. Swan Princess, The (1994) - PLACEHOLDER
    "0001410",  # 1410. Harlem (1993) - PLACEHOLDER
    "0001411",  # 1411. Barbarella (1968) - PLACEHOLDER
    "0001412",  # 1412. Land Before Time III: The Time of the Great Giving (1995) (V) (1995) - PLACEHOLDER
    "0001413",  # 1413. Street Fighter (1994) - PLACEHOLDER
    "0001414",  # 1414. Coldblooded (1995) - PLACEHOLDER
    "0001415",  # 1415. Next Karate Kid, The (1994) - PLACEHOLDER
    "0001416",  # 1416. No Escape (1994) - PLACEHOLDER
    "0001417",  # 1417. Turning, The (1992) - PLACEHOLDER
    "0001418",  # 1418. Joy Luck Club, The (1993) - PLACEHOLDER
    "0001419",  # 1419. Highlander III: The Sorcerer (1994) - PLACEHOLDER
    "0001420",  # 1420. Gilligan's Island: The Movie (1998) - PLACEHOLDER
    "0001421",  # 1421. My Crazy Life (Mi vida loca) (1993) - PLACEHOLDER
    "0001422",  # 1422. Suture (1993) - PLACEHOLDER
    "0001423",  # 1423. Walking Dead, The (1995) - PLACEHOLDER
    "0001424",  # 1424. I Like It Like That (1994) - PLACEHOLDER
    "0001425",  # 1425. I'll Do Anything (1994) - PLACEHOLDER
    "0001426",  # 1426. Grace of My Heart (1996) - PLACEHOLDER
    "0001427",  # 1427. Drunks (1995) - PLACEHOLDER
    "0001428",  # 1428. SubUrbia (1997) - PLACEHOLDER
    "0001429",  # 1429. Sliding Doors (1998) - PLACEHOLDER
    "0001430",  # 1430. Ill Gotten Gains (1997) - PLACEHOLDER
    "0001431",  # 1431. Legal Deceit (1997) - PLACEHOLDER
    "0001432",  # 1432. Mighty, The (1998) - PLACEHOLDER
    "0001433",  # 1433. Men of Means (1998) - PLACEHOLDER
    "0001434",  # 1434. Shooting Fish (1997) - PLACEHOLDER
    "0001435",  # 1435. Steal Big, Steal Little (1995) - PLACEHOLDER
    "0001436",  # 1436. Mr. Jones (1993) - PLACEHOLDER
    "0001437",  # 1437. House Party 3 (1994) - PLACEHOLDER
    "0001438",  # 1438. Panther (1995) - PLACEHOLDER
    "0001439",  # 1439. Jason's Lyric (1994) - PLACEHOLDER
    "0001440",  # 1440. Above the Rim (1994) - PLACEHOLDER
    "0001441",  # 1441. Moonlight and Valentino (1995) - PLACEHOLDER
    "0001442",  # 1442. Scarlet Letter, The (1995) - PLACEHOLDER
    "0001443",  # 1443. 8 Seconds (1994) - PLACEHOLDER
    "0001444",  # 1444. That Darn Cat! (1965) - PLACEHOLDER
    "0001445",  # 1445. Ladybird Ladybird (1994) - PLACEHOLDER
    "0001446",  # 1446. Bye Bye, Love (1995) - PLACEHOLDER
    "0001447",  # 1447. Century (1993) - PLACEHOLDER
    "0001448",  # 1448. My Favorite Season (1993) - PLACEHOLDER
    "0001449",  # 1449. Pather Panchali (1955) - PLACEHOLDER
    "0001450",  # 1450. Golden Earrings (1947) - PLACEHOLDER
    "0001451",  # 1451. Foreign Correspondent (1940) - PLACEHOLDER
    "0001452",  # 1452. Lady of Burlesque (1943) - PLACEHOLDER
    "0001453",  # 1453. Angel on My Shoulder (1946) - PLACEHOLDER
    "0001454",  # 1454. Angel and the Badman (1947) - PLACEHOLDER
    "0001455",  # 1455. Outlaw, The (1943) - PLACEHOLDER
    "0001456",  # 1456. Beat the Devil (1954) - PLACEHOLDER
    "0001457",  # 1457. Love Is All There Is (1996) - PLACEHOLDER
    "0001458",  # 1458. Damsel in Distress, A (1937) - PLACEHOLDER
    "0001459",  # 1459. Madame Butterfly (1995) - PLACEHOLDER
    "0001460",  # 1460. Sleepover (1995) - PLACEHOLDER
    "0001461",  # 1461. Here Comes Cookie (1935) - PLACEHOLDER
    "0001462",  # 1462. Thieves (Voleurs, Les) (1996) - PLACEHOLDER
    "0001463",  # 1463. Boys, Les (1997) - PLACEHOLDER
    "0001464",  # 1464. Stars Fell on Henrietta, The (1995) - PLACEHOLDER
    "0001465",  # 1465. Last Summer in the Hamptons (1995) - PLACEHOLDER
    "0001466",  # 1466. Margaret's Museum (1995) - PLACEHOLDER
    "0001467",  # 1467. Saint of Fort Washington, The (1993) - PLACEHOLDER
    "0001468",  # 1468. Cure, The (1995) - PLACEHOLDER
    "0001469",  # 1469. Tom and Huck (1995) - PLACEHOLDER
    "0001470",  # 1470. Gumby: The Movie (1995) - PLACEHOLDER
    "0001471",  # 1471. Hideaway (1995) - PLACEHOLDER
    "0001472",  # 1472. Visitors, The (Visiteurs, Les) (1993) - PLACEHOLDER
    "0001473",  # 1473. Little Princess, The (1939) - PLACEHOLDER
    "0001474",  # 1474. Nina Takes a Lover (1994) - PLACEHOLDER
    "0001475",  # 1475. Bhaji on the Beach (1993) - PLACEHOLDER
    "0001476",  # 1476. Raw Deal (1948) - PLACEHOLDER
    "0001477",  # 1477. Nightwatch (1997) - PLACEHOLDER
    "0001478",  # 1478. Dead Presidents (1995) - PLACEHOLDER
    "0001479",  # 1479. Reckless (1995) - PLACEHOLDER
    "0001480",  # 1480. Herbie Rides Again (1974) - PLACEHOLDER
    "0001481",  # 1481. S.F.W. (1994) - PLACEHOLDER
    "0001482",  # 1482. Gate of Heavenly Peace, The (1995) - PLACEHOLDER
    "0001483",  # 1483. Man in the Iron Mask, The (1998) - PLACEHOLDER
    "0001484",  # 1484. Jerky Boys, The (1994) - PLACEHOLDER
    "0001485",  # 1485. Colonel Chabert, Le (1994) - PLACEHOLDER
    "0001486",  # 1486. Girl in the Cadillac (1995) - PLACEHOLDER
    "0001487",  # 1487. Even Cowgirls Get the Blues (1993) - PLACEHOLDER
    "0001488",  # 1488. Germinal (1993) - PLACEHOLDER
    "0001489",  # 1489. Chasers (1994) - PLACEHOLDER
    "0001490",  # 1490. Fausto (1993) - PLACEHOLDER
    "0001491",  # 1491. Tough and Deadly (1995) - PLACEHOLDER
    "0001492",  # 1492. Window to Paris (1994) - PLACEHOLDER
    "0001493",  # 1493. Modern Affair, A (1995) - PLACEHOLDER
    "0001494",  # 1494. Mostro, Il (1994) - PLACEHOLDER
    "0001495",  # 1495. Flirt (1995) - PLACEHOLDER
    "0001496",  # 1496. Carpool (1996) - PLACEHOLDER
    "0001497",  # 1497. Line King: Al Hirschfeld, The (1996) - PLACEHOLDER
    "0001498",  # 1498. Farmer & Chase (1995) - PLACEHOLDER
    "0001499",  # 1499. Grosse Fatigue (1994) - PLACEHOLDER
    "0001500",  # 1500. Santa with Muscles (1996) - PLACEHOLDER
    "0001501",  # 1501. Prisoner of the Mountains (Kavkazsky Plennik) (1996) - PLACEHOLDER
    "0001502",  # 1502. Naked in New York (1994) - PLACEHOLDER
    "0001503",  # 1503. Gold Diggers: The Secret of Bear Mountain (1995) - PLACEHOLDER
    "0001504",  # 1504. Bewegte Mann, Der (1994) - PLACEHOLDER
    "0001505",  # 1505. Killer: A Journal of Murder (1995) - PLACEHOLDER
    "0001506",  # 1506. Nelly & Monsieur Arnaud (1995) - PLACEHOLDER
    "0001507",  # 1507. Three Lives and Only One Death (1996) - PLACEHOLDER
    "0001508",  # 1508. Babysitter, The (1995) - PLACEHOLDER
    "0001509",  # 1509. Getting Even with Dad (1994) - PLACEHOLDER
    "0001510",  # 1510. Mad Dog Time (1996) - PLACEHOLDER
    "0001511",  # 1511. Children of the Revolution (1996) - PLACEHOLDER
    "0001512",  # 1512. World of Apu, The (Apur Sansar) (1959) - PLACEHOLDER
    "0001513",  # 1513. Sprung (1997) - PLACEHOLDER
    "0001514",  # 1514. Dream With the Fishes (1997) - PLACEHOLDER
    "0001515",  # 1515. Wings of Courage (1995) - PLACEHOLDER
    "0001516",  # 1516. Wedding Gift, The (1994) - PLACEHOLDER
    "0001517",  # 1517. Race the Sun (1996) - PLACEHOLDER
    "0001518",  # 1518. Losing Isaiah (1995) - PLACEHOLDER
    "0001519",  # 1519. New Jersey Drive (1995) - PLACEHOLDER
    "0001520",  # 1520. Fear, The (1995) - PLACEHOLDER
    "0001521",  # 1521. Mr. Wonderful (1993) - PLACEHOLDER
    "0001522",  # 1522. Trial by Jury (1994) - PLACEHOLDER
    "0001523",  # 1523. Good Man in Africa, A (1994) - PLACEHOLDER
    "0001524",  # 1524. Kaspar Hauser (1993) - PLACEHOLDER
    "0001525",  # 1525. Object of My Affection, The (1998) - PLACEHOLDER
    "0001526",  # 1526. Witness (1985) - PLACEHOLDER
    "0001527",  # 1527. Senseless (1998) - PLACEHOLDER
    "0001528",  # 1528. Nowhere (1997) - PLACEHOLDER
    "0001529",  # 1529. Underground (1995) - PLACEHOLDER
    "0001530",  # 1530. Jefferson in Paris (1995) - PLACEHOLDER
    "0001531",  # 1531. Far From Home: The Adventures of Yellow Dog (1995) - PLACEHOLDER
    "0001532",  # 1532. Foreign Student (1994) - PLACEHOLDER
    "0001533",  # 1533. I Don't Want to Talk About It (De eso no se habla) (1993) - PLACEHOLDER
    "0001534",  # 1534. Twin Town (1997) - PLACEHOLDER
    "0001535",  # 1535. Enfer, L' (1994) - PLACEHOLDER
    "0001536",  # 1536. Aiqing wansui (1994) - PLACEHOLDER
    "0001537",  # 1537. Cosi (1996) - PLACEHOLDER
    "0001538",  # 1538. All Over Me (1997) - PLACEHOLDER
    "0001539",  # 1539. Being Human (1993) - PLACEHOLDER
    "0001540",  # 1540. Amazing Panda Adventure, The (1995) - PLACEHOLDER
    "0001541",  # 1541. Beans of Egypt, Maine, The (1994) - PLACEHOLDER
    "0001542",  # 1542. Scarlet Letter, The (1926) - PLACEHOLDER
    "0001543",  # 1543. Johns (1996) - PLACEHOLDER
    "0001544",  # 1544. It Takes Two (1995) - PLACEHOLDER
    "0001545",  # 1545. Frankie Starlight (1995) - PLACEHOLDER
    "0001546",  # 1546. Shadows (Cienie) (1988) - PLACEHOLDER
    "0001547",  # 1547. Show, The (1995) - PLACEHOLDER
    "0001548",  # 1548. The Courtyard (1995) - PLACEHOLDER
    "0001549",  # 1549. Dream Man (1995) - PLACEHOLDER
    "0001550",  # 1550. Destiny Turns on the Radio (1995) - PLACEHOLDER
    "0001551",  # 1551. Glass Shield, The (1994) - PLACEHOLDER
    "0001552",  # 1552. Hunted, The (1995) - PLACEHOLDER
    "0001553",  # 1553. Underneath, The (1995) - PLACEHOLDER
    "0001554",  # 1554. Safe Passage (1994) - PLACEHOLDER
    "0001555",  # 1555. Secret Adventures of Tom Thumb, The (1993) - PLACEHOLDER
    "0001556",  # 1556. Condition Red (1995) - PLACEHOLDER
    "0001557",  # 1557. Yankee Zulu (1994) - PLACEHOLDER
    "0001558",  # 1558. Aparajito (1956) - PLACEHOLDER
    "0001559",  # 1559. Hostile Intentions (1994) - PLACEHOLDER
    "0001560",  # 1560. Clean Slate (Coup de Torchon) (1981) - PLACEHOLDER
    "0001561",  # 1561. Tigrero: A Film That Was Never Made (1994) - PLACEHOLDER
    "0001562",  # 1562. Eye of Vichy, The (Oeil de Vichy, L') (1993) - PLACEHOLDER
    "0001563",  # 1563. Promise, The (Versprechen, Das) (1994) - PLACEHOLDER
    "0001564",  # 1564. To Cross the Rubicon (1991) - PLACEHOLDER
    "0001565",  # 1565. Daens (1992) - PLACEHOLDER
    "0001566",  # 1566. Man from Down Under, The (1943) - PLACEHOLDER
    "0001567",  # 1567. Careful (1992) - PLACEHOLDER
    "0001568",  # 1568. Vermont Is For Lovers (1992) - PLACEHOLDER
    "0001569",  # 1569. Vie est belle, La (Life is Rosey) (1987) - PLACEHOLDER
    "0001570",  # 1570. Quartier Mozart (1992) - PLACEHOLDER
    "0001571",  # 1571. Touki Bouki (Journey of the Hyena) (1973) - PLACEHOLDER
    "0001572",  # 1572. Wend Kuuni (God's Gift) (1982) - PLACEHOLDER
    "0001573",  # 1573. Spirits of the Dead (Tre passi nel delirio) (1968) - PLACEHOLDER
    "0001574",  # 1574. Pharaoh's Army (1995) - PLACEHOLDER
    "0001575",  # 1575. I, Worst of All (Yo, la peor de todas) (1990) - PLACEHOLDER
    "0001576",  # 1576. Hungarian Fairy Tale, A (1987) - PLACEHOLDER
    "0001577",  # 1577. Death in the Garden (Mort en ce jardin, La) (1956) - PLACEHOLDER
    "0001578",  # 1578. Collectionneuse, La (1967) - PLACEHOLDER
    "0001579",  # 1579. Baton Rouge (1988) - PLACEHOLDER
    "0001580",  # 1580. Liebelei (1933) - PLACEHOLDER
    "0001581",  # 1581. Woman in Question, The (1950) - PLACEHOLDER
    "0001582",  # 1582. T-Men (1947) - PLACEHOLDER
    "0001583",  # 1583. Invitation, The (Zaproszenie) (1986) - PLACEHOLDER
    "0001584",  # 1584. Symphonie pastorale, La (1946) - PLACEHOLDER
    "0001585",  # 1585. American Dream (1990) - PLACEHOLDER
    "0001586",  # 1586. Lashou shentan (1992) - PLACEHOLDER
    "0001587",  # 1587. Terror in a Texas Town (1958) - PLACEHOLDER
    "0001588",  # 1588. Salut cousin! (1996) - PLACEHOLDER
    "0001589",  # 1589. Schizopolis (1996) - PLACEHOLDER
    "0001590",  # 1590. To Have, or Not (1995) - PLACEHOLDER
    "0001591",  # 1591. Duoluo tianshi (1995) - PLACEHOLDER
    "0001592",  # 1592. Magic Hour, The (1998) - PLACEHOLDER
    "0001593",  # 1593. Death in Brunswick (1991) - PLACEHOLDER
    "0001594",  # 1594. Everest (1998) - PLACEHOLDER
    "0001595",  # 1595. Shopping (1994) - PLACEHOLDER
    "0001596",  # 1596. Nemesis 2: Nebula (1995) - PLACEHOLDER
    "0001597",  # 1597. Romper Stomper (1992) - PLACEHOLDER
    "0001598",  # 1598. City of Industry (1997) - PLACEHOLDER
    "0001599",  # 1599. Someone Else's America (1995) - PLACEHOLDER
    "0001600",  # 1600. Guantanamera (1994) - PLACEHOLDER
    "0001601",  # 1601. Office Killer (1997) - PLACEHOLDER
    "0001602",  # 1602. Price Above Rubies, A (1998) - PLACEHOLDER
    "0001603",  # 1603. Angela (1995) - PLACEHOLDER
    "0001604",  # 1604. He Walked by Night (1948) - PLACEHOLDER
    "0001605",  # 1605. Love Serenade (1996) - PLACEHOLDER
    "0001606",  # 1606. Deceiver (1997) - PLACEHOLDER
    "0001607",  # 1607. Hurricane Streets (1998) - PLACEHOLDER
    "0001608",  # 1608. Buddy (1997) - PLACEHOLDER
    "0001609",  # 1609. B*A*P*S (1997) - PLACEHOLDER
    "0001610",  # 1610. Truth or Consequences, N.M. (1997) - PLACEHOLDER
    "0001611",  # 1611. Intimate Relations (1996) - PLACEHOLDER
    "0001612",  # 1612. Leading Man, The (1996) - PLACEHOLDER
    "0001613",  # 1613. Tokyo Fist (1995) - PLACEHOLDER
    "0001614",  # 1614. Reluctant Debutante, The (1958) - PLACEHOLDER
    "0001615",  # 1615. Warriors of Virtue (1997) - PLACEHOLDER
    "0001616",  # 1616. Desert Winds (1995) - PLACEHOLDER
    "0001617",  # 1617. Hugo Pool (1997) - PLACEHOLDER
    "0001618",  # 1618. King of New York (1990) - PLACEHOLDER
    "0001619",  # 1619. All Things Fair (1996) - PLACEHOLDER
    "0001620",  # 1620. Sixth Man, The (1997) - PLACEHOLDER
    "0001621",  # 1621. Butterfly Kiss (1995) - PLACEHOLDER
    "0001622",  # 1622. Paris, France (1993) - PLACEHOLDER
    "0001623",  # 1623. Cérémonie, La (1995) - PLACEHOLDER
    "0001624",  # 1624. Hush (1998) - PLACEHOLDER
    "0001625",  # 1625. Nightwatch (1997) - PLACEHOLDER
    "0001626",  # 1626. Nobody Loves Me (Keiner liebt mich) (1994) - PLACEHOLDER
    "0001627",  # 1627. Wife, The (1995) - PLACEHOLDER
    "0001628",  # 1628. Lamerica (1994) - PLACEHOLDER
    "0001629",  # 1629. Nico Icon (1995) - PLACEHOLDER
    "0001630",  # 1630. Silence of the Palace, The (Saimt el Qusur) (1994) - PLACEHOLDER
    "0001631",  # 1631. Slingshot, The (1993) - PLACEHOLDER
    "0001632",  # 1632. Land and Freedom (Tierra y libertad) (1995) - PLACEHOLDER
    "0001633",  # 1633. Á köldum klaka (Cold Fever) (1994) - PLACEHOLDER
    "0001634",  # 1634. Etz Hadomim Tafus (Under the Domin Tree) (1994) - PLACEHOLDER
    "0001635",  # 1635. Two Friends (1986)  (1986) - PLACEHOLDER
    "0001636",  # 1636. Brothers in Trouble (1995) - PLACEHOLDER
    "0001637",  # 1637. Girls Town (1996) - PLACEHOLDER
    "0001638",  # 1638. Normal Life (1996) - PLACEHOLDER
    "0001639",  # 1639. Bitter Sugar (Azucar Amargo) (1996) - PLACEHOLDER
    "0001640",  # 1640. Eighth Day, The (1996) - PLACEHOLDER
    "0001641",  # 1641. Dadetown (1995) - PLACEHOLDER
    "0001642",  # 1642. Some Mother's Son (1996) - PLACEHOLDER
    "0001643",  # 1643. Angel Baby (1995) - PLACEHOLDER
    "0001644",  # 1644. Sudden Manhattan (1996) - PLACEHOLDER
    "0001645",  # 1645. Butcher Boy, The (1998) - PLACEHOLDER
    "0001646",  # 1646. Men With Guns (1997) - PLACEHOLDER
    "0001647",  # 1647. Hana-bi (1997) - PLACEHOLDER
    "0001648",  # 1648. Niagara, Niagara (1997) - PLACEHOLDER
    "0001649",  # 1649. Big One, The (1997) - PLACEHOLDER
    "0001650",  # 1650. Butcher Boy, The (1998) - PLACEHOLDER
    "0001651",  # 1651. Spanish Prisoner, The (1997) - PLACEHOLDER
    "0001652",  # 1652. Temptress Moon (Feng Yue) (1996) - PLACEHOLDER
    "0001653",  # 1653. Entertaining Angels: The Dorothy Day Story (1996) - PLACEHOLDER
    "0001654",  # 1654. Chairman of the Board (1998) - PLACEHOLDER
    "0001655",  # 1655. Favor, The (1994) - PLACEHOLDER
    "0001656",  # 1656. Little City (1998) - PLACEHOLDER
    "0001657",  # 1657. Target (1995) - PLACEHOLDER
    "0001658",  # 1658. Substance of Fire, The (1996) - PLACEHOLDER
    "0001659",  # 1659. Getting Away With Murder (1996) - PLACEHOLDER
    "0001660",  # 1660. Small Faces (1995) - PLACEHOLDER
    "0001661",  # 1661. New Age, The (1994) - PLACEHOLDER
    "0001662",  # 1662. Rough Magic (1995) - PLACEHOLDER
    "0001663",  # 1663. Nothing Personal (1995) - PLACEHOLDER
    "0001664",  # 1664. 8 Heads in a Duffel Bag (1997) - PLACEHOLDER
    "0001665",  # 1665. Brother's Kiss, A (1997) - PLACEHOLDER
    "0001666",  # 1666. Ripe (1996) - PLACEHOLDER
    "0001667",  # 1667. Next Step, The (1995) - PLACEHOLDER
    "0001668",  # 1668. Wedding Bell Blues (1996) - PLACEHOLDER
    "0001669",  # 1669. MURDER and murder (1996) - PLACEHOLDER
    "0001670",  # 1670. Tainted (1998) - PLACEHOLDER
    "0001671",  # 1671. Further Gesture, A (1996) - PLACEHOLDER
    "0001672",  # 1672. Kika (1993) - PLACEHOLDER
    "0001673",  # 1673. Mirage (1995) - PLACEHOLDER
    "0001674",  # 1674. Mamma Roma (1962) - PLACEHOLDER
    "0001675",  # 1675. Sunchaser, The (1996) - PLACEHOLDER
    "0001676",  # 1676. War at Home, The (1996) - PLACEHOLDER
    "0001677",  # 1677. Sweet Nothing (1995) - PLACEHOLDER
    "0001678",  # 1678. Mat' i syn (1997) - PLACEHOLDER
    "0001679",  # 1679. B. Monkey (1998) - PLACEHOLDER
    "0001680",  # 1680. Sliding Doors (1998) - PLACEHOLDER
    "0001681",  # 1681. You So Crazy (1994) - PLACEHOLDER
    "0001682",  # 1682. Scream of Stone (Schrei aus Stein) (1991) - PLACEHOLDER
]

if __name__ == "__main__":
    print(f"Total movies: 1682")
    print(f"Verified IDs: 27")
    print(f"Progress: 1.6%")

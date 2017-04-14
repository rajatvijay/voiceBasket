LANGUAGE_OPTIONS = [
    'Afrikaans',
    'Arabic',
    'Albenian',
    'Bahasa-Indonesian',
    'Bahasa-Malaysian',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    'Cambodian',
    'Caribbean',
    'Catalan',
    'Chinese-Cantonese',
    'Chinese-Mandrin',
    'Croatian',
    'czech',
    'Danish',
    'Dutch',
    'English-Indian',
    'English-US',
    'English-UK',
    'English-Australian'
    'English-Latin American',
    'English-South African',
    'English-Asian',
    'Finnish,'
    'Flemish,',
    'French-Canadian',
    'French-European',
    'Georgeon',
    'German',
    'Greek',
    'Gujarati',
    'Hebrew',
    'Hindi',
    'Hungarian',
    'Icelandic',
    'Indonesian',
    'Italian',
    'Irish',
    'Japanese',
    'Kannada',
    'Korean',
    'Kurdish',
    'Latvian',
    'Malayalam',
    'Marathi',
    'Maltese',
    'Malay',
    'Norwegian',
    'Oriya',
    'Persian',
    'Polish',
    'Portugese-Brazil',
    'Portugese-Europe',
    'Punjabi',
    'Romanian',
    'Russian',
    'Sanskrit',
    'Serbian',
    'Slovak',
    'Slovanian',
    'Spanish-Latin American',
    'Spanish-Europe',
    'Swahili',
    'Swedish',
    'Tagalog',
    'Tamil',
    'Telugu',
    'Thai',
    'Turkish',
    'Urudu',
    'Ukranian',
    'Vietnamese'
]

VOICE_OVER_TYPE = [
    'Radio & TV Commercials',
    'Infomercials & Explainer Videos',
    'Corporate Videos & Presentations',
    'Cartoon/Animation Videos',
    'Documentaries',
    'Audio-books',
    'IVR'
]

GENDER_OPTIONS = ['Male', 'Female', 'Male & Female']

AGE_TYPE = [
    'Teenage',
    'Young Adult',
    'Middle Age',
    'Senior'
]

REQUEST_TYPE = [
    'Commercial',
    'Infomercials & Explainer Videos',
    'Corporate Videos & Presentations',
    'Cartoon / Animation Videos',
    'Documentaries',
    'Audio-books',
    'IVR',

]

ADMIN_EMAIL = 'admin@admin.com'

ARTIST_PASSWORD = '123456'

ARTIST_MOBILE = 8888888888

ARTIST_COMPANY_NAME = 'Voice Basket'

def make_choices(options):
    return map(lambda x: (x, x), options)

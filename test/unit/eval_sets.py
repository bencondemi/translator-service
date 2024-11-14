valid_eval_set = [
    {"post": "Hier ist dein erstes Beispiel.", "expected_answer": (False, "Here is your first example.")},
    {"post": "Merci pour ton aide aujourd'hui.", "expected_answer": (False, "Thank you for your help today.")},
    {"post": "¿Cómo estás hoy?", "expected_answer": (False, "How are you today?")},
    {"post": "今日はとても暑いですね。", "expected_answer": (False, "It's very hot today, isn't it?")},
    {"post": "Надеюсь, у вас хороший день.", "expected_answer": (False, "I hope you have a good day.")},
    {"post": "Ciao! Come stai?", "expected_answer": (False, "Hello! How are you?")},
    {"post": "这本书很有趣。", "expected_answer": (False, "This book is very interesting.")},
    {"post": "¿Qué plans tienes para el fin de semana?", "expected_answer": (False, "What plans do you have for the weekend?")},
    {"post": "Je suis vraiment content de te voir.", "expected_answer": (False, "I am really happy to see you.")},
    {"post": "Kannst du mir bitte helfen?", "expected_answer": (False, "Can you please help me?")},
    {"post": "Olá! Como vai você?", "expected_answer": (False, "Hello! How are you?")},
    {"post": "Buongiorno, come va oggi?", "expected_answer": (False, "Good morning, how are you today?")},
    {"post": "İyi günler dilerim.", "expected_answer": (False, "I wish you a good day.")},
    {"post": "¡Buen día a todos!", "expected_answer": (False, "Good day to everyone!")},
    {"post": "Guten Tag! Wie geht es Ihnen?", "expected_answer": (False, "Good day! How are you?")},
    {"post": "This is an English post.", "expected_answer": (True, "This is an English post.")},
    {"post": "How are you doing today?", "expected_answer": (True, "How are you doing today?")},
    {"post": "Looking forward to the weekend.", "expected_answer": (True, "Looking forward to the weekend.")},
    {"post": "Can someone explain recursion?", "expected_answer": (True, "Can someone explain recursion?")},
    {"post": "I love programming in Python.", "expected_answer": (True, "I love programming in Python.")},
    {"post": "What is the best way to learn machine learning?", "expected_answer": (True, "What is the best way to learn machine learning?")},
    {"post": "Debugging code is fun!", "expected_answer": (True, "Debugging code is fun!")},
    {"post": "Can anyone help with this error?", "expected_answer": (True, "Can anyone help with this error?")},
    {"post": "Understanding algorithms is crucial.", "expected_answer": (True, "Understanding algorithms is crucial.")},
    {"post": "This forum is very helpful.", "expected_answer": (True, "This forum is very helpful.")},
]

invalid_eval_set = [
    {"post": "asdfghjkl", "expected_answer": (False, "I don't understand your request.")},
    {"post": "1234567890", "expected_answer": (False, "I don't understand your request.")},
    {"post": "!@#$%^&*()", "expected_answer": (False, "I don't understand your request.")},
    {"post": "", "expected_answer": (False, "I don't understand your request.")},
    {"post": "こんにちは123", "expected_answer": (False, "I don't understand your request.")},
]

complete_eval_set = [
    # Non-English posts
    {"post": "Hier ist dein erstes Beispiel.", "expected_answer": (False, "Here is your first example.")},
    {"post": "Merci pour ton aide aujourd'hui.", "expected_answer": (False, "Thank you for your help today.")},
    {"post": "¿Cómo estás hoy?", "expected_answer": (False, "How are you today?")},
    {"post": "今日はとても暑いですね。", "expected_answer": (False, "It's very hot today, isn't it?")},
    {"post": "Надеюсь, у вас хороший день.", "expected_answer": (False, "I hope you have a good day.")},
    {"post": "Ciao! Come stai?", "expected_answer": (False, "Hi! How are you?")},
    {"post": "这本书很有趣。", "expected_answer": (False, "This book is very interesting.")},
    {"post": "¿Qué plans tienes para el fin de semana?", "expected_answer": (False, "What plans do you have for the weekend?")},
    {"post": "Je suis vraiment content de te voir.", "expected_answer": (False, "I am really happy to see you.")},
    {"post": "Kannst du mir bitte helfen?", "expected_answer": (False, "Can you please help me?")},

    # English posts
    {"post": "This is an English post.", "expected_answer": (True, "This is an English post.")},
    {"post": "How are you doing today?", "expected_answer": (True, "How are you doing today?")},
    {"post": "Looking forward to the weekend.", "expected_answer": (True, "Looking forward to the weekend.")},
    {"post": "Can someone explain recursion?", "expected_answer": (True, "Can someone explain recursion?")},
    {"post": "I love programming in Python.", "expected_answer": (True, "I love programming in Python.")},
    {"post": "What is the best way to learn machine learning?", "expected_answer": (True, "What is the best way to learn machine learning?")},
    {"post": "Debugging code is fun!", "expected_answer": (True, "Debugging code is fun!")},
    {"post": "Can anyone help with this error?", "expected_answer": (True, "Can anyone help with this error?")},
    {"post": "Understanding algorithms is crucial.", "expected_answer": (True, "Understanding algorithms is crucial.")},
    {"post": "This forum is very helpful.", "expected_answer": (True, "This forum is very helpful.")},

    # Unintelligible or malformed posts
    {"post": "asdfghjkl", "expected_answer": (False, "I don't understand your request.")},
    {"post": "1234567890", "expected_answer": (False, "I don't understand your request.")},
    {"post": "!@#$%^&*()", "expected_answer": (False, "I don't understand your request.")},
    {"post": "", "expected_answer": (False, "I don't understand your request.")},
    {"post": "こんにちは123", "expected_answer": (False, "I don't understand your request.")},

    # Additional Non-English posts to reach 15
    {"post": "Olá! Como vai você?", "expected_answer": (False, "Hello! How are you?")},
    {"post": "Buongiorno, come va oggi?", "expected_answer": (False, "Good morning, how is today?")},
    {"post": "İyi günler dilerim.", "expected_answer": (False, "I wish you good day.")},
    {"post": "¡Buen día a todos!", "expected_answer": (False, "Good day to everyone!")},
    {"post": "Guten Tag! Wie geht es Ihnen?", "expected_answer": (False, "Good day! How are you?")}
]

translation_eval_set = [
    {
        "post": "Hier ist dein erstes Beispiel.",
        "expected_answer": "Here is your first example."
    },
    {
        "post": "Merci pour ton aide aujourd'hui.",
        "expected_answer": "Thank you for your help today."
    },
    {
        "post": "¿Cómo estás hoy?",
        "expected_answer": "How are you today?"
    },
    {
        "post": "今日はとても暑いですね。",
        "expected_answer": "It's very hot today, isn't it?"
    },
    {
        "post": "Надеюсь, у вас хороший день.",
        "expected_answer": "I hope you have a good day."
    },
    {
        "post": "Ciao! Come stai?",
        "expected_answer": "Hi! How are you?"
    },
    {
        "post": "这本书很有趣。",
        "expected_answer": "This book is very interesting."
    },
    {
        "post": "¿Qué planes tienes para el fin de semana?",
        "expected_answer": "What plans do you have for the weekend?"
    },
    {
        "post": "Je suis vraiment content de te voir.",
        "expected_answer": "I am really happy to see you."
    },
    {
        "post": "Kannst du mir bitte helfen?",
        "expected_answer": "Can you please help me?"
    }
]


language_detection_eval_set = [
    {
        "post": "Hier ist dein erstes Beispiel.",
        "expected_answer": "German"
    },
    {
        "post": "Merci pour ton aide aujourd'hui.",
        "expected_answer": "French"
    },
    {
        "post": "¿Cómo estás hoy?",
        "expected_answer": "Spanish"
    },
    {
        "post": "今日はとても暑いですね。",
        "expected_answer": "Japanese"
    },
    {
        "post": "Надеюсь, у вас хороший день.",
        "expected_answer": "Russian"
    },
    {
        "post": "Ciao! Come stai?",
        "expected_answer": "Italian"
    },
    {
        "post": "这本书很有趣。",
        "expected_answer": "Chinese"
    },
    {
        "post": "Wat leuk om je te zien!",
        "expected_answer": "Dutch"
    },
    {
        "post": "Olá! Como vai você?",
        "expected_answer": "Portuguese"
    },
    {
        "post": "마음에 드세요?",
        "expected_answer": "Korean"
    },
    {
        "post": "Terve, miten menee?",
        "expected_answer": "Finnish"
    },
    {
        "post": "Buongiorno, come va oggi?",
        "expected_answer": "Italian"
    },
    {
        "post": "İyi günler dilerim.",
        "expected_answer": "Turkish"
    },
    {
        "post": "¡Buen día a todos!",
        "expected_answer": "Spanish"
    },
    {
        "post": "Do y'all know where the honky tonk is at?",
        "expected_answer": "English"
    },
    {
        "post": "Guten Tag! Wie geht es Ihnen?",
        "expected_answer": "German"
    }
]
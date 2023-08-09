raw = {
    "Health and Wellness": {
        "morning yoga routine": "🌅🧘‍♂️✨",
        "healthy meal preparation": "🥗👩‍🍳💪",
        "stress relief meditation": "😫🧘‍♀️☺️",
        "alternative herbal therapy": "🌿💆‍♂️🌱",
    },
    "Education and Learning": {
        "graduation celebration": "🎓🎉📚",
        "online learning platform": "💻📖🎓",
        "exploring art history": "🖼️📚🎨",
        "science laboratory experiments": "🔬🧪🧠",
    },
    "Travel and Adventure": {
        "tropical island getaway": "🏝️✈️🍹",
        "cross-country road trip": "🚗🗺️🛣️",
        "exploring local culture": "🌐🎭🏺",
        "sustainable eco-tourism": "🌍🌱🏕️",
    },
    "Family and Life Stages": {
        "newborn baby joy": "👶🎉💕",
        "wedding day bliss": "💑💍🎊",
        "teenager's first car": "🚗👦🔑",
        "caring for elderly parents": "👴💕👩‍⚕️",
    },
    "Business and Entrepreneurship": {
        "launching a startup": "🚀💼📈",
        "branding and logo design": "✏️🎨🏢",
        "investing in the stock market": "💲📈📊",
        "business networking event": "🤝💼🏢",
    },
    "Science and Discovery": {
        "groundbreaking research": "🔬💡📘",
        "protecting the environment": "🌍🛡️🌿",
        "space telescope exploration": "🪐🔭🌌",
        "innovative medical treatment": "💊🏥💡",
    },
    "Hobbies and Recreation": {
        "playing a musical instrument": "🎹🎼🎵",
        "painting a masterpiece": "🎨🖼️✨",
        "mountain biking adventure": "🚵‍♀️⛰️🌲",
        "gardening and landscaping": "🌻🏡🌳",
    },
    "Culture and Society": {
        "women's rights movement": "♀️✊💪",
        "traditional dance festival": "💃🥁🎉",
        "high fashion runway": "👗👠📸",
        "binge-watching favorite series": "📺🍿😃",
    },
    "Nature and Environment": {
        "bird watching in the forest": "🦉🌲🔭",
        "sunset beach walk": "🌅🏖️👣",
        "snow-capped mountain hike": "🏔️🥾❄️",
        "urban rooftop garden": "🏙️🌷🍅",
    },
    "Spirituality and Philosophy": {
        "praying in a temple": "🙏⛩️🕊️",
        "mindfulness meditation practice": "🧘‍♀️☮️🕉️",
        "debating ethical issues": "💭⚖️🗣️",
        "exploring existential thoughts": "🌌🤔💭",
    },
}
concepts = [
    {"category": category, "concept": concept, "emoji": emoji}
    for category, concepts in raw.items()
    for concept, emoji in concepts.items()
]

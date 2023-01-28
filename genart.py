import json
import requests
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "https://zoociety.xyz",
    "http://localhost",
    "http://localhost:3000",
    "https://lilfarmboy.xyz"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Zoociety AI"}


API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/dreamlike-art/dreamlike-photoreal-2.0"

headers = {"Authorization": f"Bearer {API_TOKEN}"}


@app.get("/promptimize")
def chat(prompt: str):

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/microsoft/Promptist",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    print(output.content)

    return output.content


@app.get("/dialogue")
def chat(prompt: str):

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    print(output.content)

    return output.content


@app.get("/chat")
def chat(prompt: str):

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    print(output.content)

    return output.content


@app.get("/cotlin")
def chat(prompt: str):
    data = ({
        "inputs": {
            "question": prompt,
            "context": "Lil Farm Boy is an NFT collection in the Ethereum network with 5,999 supply and has more than 240 unique traits such as background, clothing, ears, eyes, headgear, mouth, nose and skin. There are also extremely unique NFTs or what we call one-of-one’s such as God, Cyborg, Nude, Golden and Alien. There are multiple ways to get whitelisted for you to be able to mint the NFT. First is the easiest way, simply let us know more about you! Share with us your talent and contributions in web3. Answer the form in the website. Second,  Give your insights about art and tech in the NFT space. Let us know about your thoughts on various integrations of art, web3 and AI! Are you pro or anti AI art? How do you think AI will affect the current NFT space? Thirdly, Participate in discussions, contribute to forums and provide suggestions of what we can improve on and what you want to see in our community. Fourth, engage on our twitter and join our collabs' Lil Pass giveaways. You can also provide solid collabs and you're automatically whitelisted. Lastly, join our activities and games. One of the goals of the project is to build an exclusive community that is crazy about art, web3 and AI while offering tools for its holders. Aside from building an exclusive community, the project’s roadmap also includes building collaborations and integrations with third-party tools to give more value to the NFT and at the same time, to build Cotlin — an in-house ecosystem of tools which consists of AI and Web3 tools for NFTs, Discord bots, browser extensions and more — which will also help the project in terms of sustaining revenue even after the minting phase since the tools will be paid for non-holders of the NFT and will be free for NFT holders. Lil Farm Boy will also have a lore where the story is about someone, who at some point, were undervalued and unappreciated for their passion at their current environment and community; who needed someone and somewhere to belong to. The lore also explains how the Lil Farm Boy meets Cotlin, his robot companion, who teaches him more about technology, especially AI, to be used for his art. The lore includes the Lil Farm Boy’s adventure to The City of Innovative Arts where he learns about technology, and that it can be used to upgrade his art in beyond his imagination. The roadmap for Lil Farm Boy also includes an exclusive merchandise for its holders and a marketplace for non-holders to avail of the said merchandise which will be internationally available. To make the NFT have a more interactive and immersive experience, the team at The Howdy Studios will build NFT Augmented Reality applications so the NFT holders can make use of their assets as their avatars. Above all this, the team will build token-gated decentralized applications and games that NFT holders will surely enjoy with the rest of the community. The Lil Farm Boy is a collaboration project by three organizations: The Howdy Studios, Level Art and Zoociety. Explore and grow with an amazing community that appreciates. Art by Level Art — 150+ artists DAO. Web3 by The Howdy Studios — a web3 dev house. AI tools by Zoociety — ecosystem of AI and other tech tools. The Howdy Studios is a startup web3 dev studio building since 2021, that has built and catered several NFT projects, both small and big collections. The founders have vast experience in startup and web app building for almost a decade. And now, they’re taking their skills to the next level by exploring the possibilities of blockchain, smart contracts, cryptocurrencies and NFTs through continuous building and progressive learning. Level Art is a community of empowered artists helping Web3 founders and builders bring their dream projects to life through quality art that has a vision of becoming the leading Web3 art community. Zoociety is a next-generation one-stop ecosystem that leverages the power of emerging technologies to bring a wide range of tools, resources, and services to create a more connected and creative world in a new, innovative way. Aside from these three organizations, the team will be handpicking elite community members who contributed real value to the community and they will be called Councils — one for art and one for tech. Councils are special roles in the community divided between art and tech. They are the key leaders at the City of Innovative Arts that highly contributes to the community. Only holders of 5 NFTs and up may be qualified to be part of this elite group who will be orchestrating decisions and plans for the community together with the Lil Team. Few ways to be summoned as a council are: contribute to forum topics, participate in twitter spaces, talk about art, web3 and AI, join activities, offer suggestions. So people should HODL or hold a Lil Farm Boy NFT so that they are in the front seat of an exclusive community, all contributing towards one goal — to explore art, web3 and AI, and be able to bridge them all together. Most tools that the Lil Farm Boy Team will build are token-gated for holders only. Special perks and privileges await those who become Lil Angels and Lil Heroes (10+ NFTs). To learn more about the project, people can ask Cotlin — our friendly robot AI that will guide you every step of the way. If you have questions, tasks for him to do, or simply want someone to talk to, he’s the guy! He’s also the one who taught the Lil Farm Boy about AI!"
        },
    })
    print(data)
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/bert-large-uncased-whole-word-masking-finetuned-squad",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(data),
    )

    return output.json()

# OUTPUT: {
#   "score": 0.4456194043159485,
#   "start": 16,
#   "end": 57,
#   "answer": "an NFT collection in the Ethereum network"
# }


@app.get("/q&a")
def chat(prompt: str, context: str):
    data = ({
        "inputs": {
            "question": prompt,
            "context": context
        },
    })
    print(data)
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/bert-large-uncased-whole-word-masking-finetuned-squad",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(data),
    )

    return output.json()

# TEXT MASKING


@app.get("/tachyon")
def chat(prompt: str):
    data = ({
        "inputs": {
            "question": prompt,
            "context": "Zoociety is a next-generation one-stop ecosystem that leverages the power of emerging technologies to bring a wide range of tools, resources, and services to create a more connected and creative world in a new, innovative way. One of Zoociety's main objectives is to solve the problem of monetizing creative works. Billions of artists, writers, and creators struggle to find platforms that allow them to monetize their skillsets and creations. The secret of getting these people on board is a seamless one-stop ecosystem with zero required knowledge about the latest emerging technologies. Zoociety's Ecosystem focuses on exploration, tokenization and monetization by providing users with platforms that can easily create, manage, and monetize their tokenized assets with intuitive UI/UX, low transaction fees, and fast settlement of decentralized transactions. Zoociety also aims to improve the process of finding and sharing relevant contents or results in a snap. With so much information available online, it can be difficult to sift through and find high-quality, reliable sources. Zoociety's Research Lab and its Intelligent Units help users discover valuable content and find the most reliable answers to their problems in a few clicks. In addition, Zoociety seeks to address issues such as isolation, limited access to emerging technologies, complex file management, data permanence, lack of transparency and trust in online interactions and transactions, inefficient use of time and resources, inappropriate or offensive content, lack of privacy and security, difficulty connecting with like-minded individuals, limited customization and personalization opportunities, and lack of access to professional development. By providing a comprehensive ecosystem that combines all the power of technologies like AI, Blockchain Technology, and Quantum Computing, Zoociety helps users to solve real-world web problems, at least in one-sitting. Our vision is to become the premier platform for innovation, collaboration, and creativity. By building a comprehensive ecosystem that combines the best of emerging technologies, we believe we can create a platform that is unparalleled in its ability to connect and empower users from all walks of digital life. We envision a future where everyone, from casual users to professionals and experts, has the tools and resources they need to achieve their full potential and contribute to a more connected and creative world of our society. Our mission is to provide a platform that empowers users to connect, create, and collaborate in innovative ways. By leveraging emerging technologies, we seek to create a comprehensive ecosystem that meets the needs of users across the spectrum. We believe that by bringing people together and providing them with the necessary tools and resources, we can foster creativity, collaboration, and innovation on a global scale. Our goal is to create a user-friendly, intuitive, and accessible platform that meets the needs of both casual users and experts. By prioritizing ease of use and user experience, we aim to create a platform that is attractive to a wide range of users. We also strive to continuously improve and evolve the Zoociety Ecosystem in response to user feedback and changing market conditions, in order to provide the best possible experience for our users. Zoociety is created, owned, founded, and developed by raldblox. Raldblox is so cute and smart."
        },
    })
    print(data)
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/bert-large-uncased-whole-word-masking-finetuned-squad",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(data),
    )

    return output.json()


@app.get("/bert")
def mask(prompt: str):

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/bert-large-cased-whole-word-masking",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    print(output.content)

    return output.content


# IMAGE CAPTIONING
@app.get("/caption")
def mask(prompt: str):

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    print(output.content)

    return output.content


@app.get("/anime")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/hakurei/waifu-diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@app.get("/cyberpunk")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/DGSpitzer/Cyberpunk-Anime-Diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@app.get("/pencil")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/yehiaserag/anime-pencil-diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@app.get("/photoreal")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/dreamlike-art/dreamlike-photoreal-2.0",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@app.get("/tts")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="audio/flac")


@app.get("/image")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@app.get("/imagepro")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@app.get("/animepro")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/andite/anything-v4.0",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@app.get("/animepro2")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/gsdf/Counterfeit-V2.0",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@app.get("/illustrate")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/WarriorMama777/OrangeMixs",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")

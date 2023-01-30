import json
import requests
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, FileResponse
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


@app.get("/dialog")
def chat(lastInput: str, lastResponse: str, newInput: str):

    data = ({
        "inputs": {
            "past_user_inputs": [lastInput],
            "generated_responses": [lastResponse],
            "text": newInput
        },
        "parameters": {"wait_for_model": True},
    })

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(data),
    )

    result = output.json()
    filtered = result.get("generated_text")
    answer = json.dumps({"answer": filtered})

    return answer


@app.get("/dialog2")
def chat(lastInput: str, lastResponse: str, newInput: str):

    data = ({
        "inputs": {
            "past_user_inputs": [lastInput],
            "generated_responses": [lastResponse],
            "text": newInput
        },
    })

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(data),
    )

    result = output.json()
    filtered = result.get("generated_text")
    answer = json.dumps({"answer": filtered})

    return answer


@app.get("/dialog3")
def chat(lastInput: str, lastResponse: str, newInput: str):

    data = ({
        "inputs": {
            "past_user_inputs": [lastInput],
            "generated_responses": [lastResponse],
            "text": newInput
        },
    })

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/microsoft/GODEL-v1_1-large-seq2seq",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(data),
    )

    result = output.json()
    filtered = result.get("generated_text")
    answer = json.dumps({"answer": filtered})

    return answer


@app.get("/chat")
def chat(prompt: str):

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    result = output.json()
    filtered = result.get("generated_text")
    answer = json.dumps({"answer": filtered})

    return answer


@ app.get("/conversational")
def chat(lastInput: str, lastResponse: str, newInput: str):
    data = ({
        "inputs": {
            "past_user_inputs": [lastInput],
            "generated_responses": [lastResponse],
            "text": newInput
        },
    })
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(data),
    )

    result = output.json()
    filtered = result.get("generated_text")
    answer = json.dumps({"response": filtered})

    return answer


@ app.get("/conversational2")
def chat(lastInput: str, lastResponse: str, newInput: str):
    data = ({
        "inputs": {
            "past_user_inputs": [lastInput],
            "generated_responses": [lastResponse],
            "text": newInput
        },
    })
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/facebook/blenderbot-3B",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(data),
    )

    result = output.json()
    filtered = result.get("generated_text")
    answer = json.dumps({"response": filtered})

    return answer


@app.get("/cotlin")
def chat(prompt: str):
    data = ({
        "inputs": {
            "question": prompt,
            "context": "Lil Farm Boy is an NFT collection in the Ethereum network with 5,999 supply and has more than 240 unique traits such as background, clothing, ears, eyes, headgear, mouth, nose and skin. There are also extremely unique NFT or what we call one-of-one’s such as God, Cyborg, Nude, Golden and Alien. Lil Farm Boy is a fresh restart and pivot from the team who revived Honest Farmer Club, an NFT project in Polygon with GameFi and DeFi utilities. After a year of continuously building HFC, Th3o (Lil Farm Boy’s founder), wants to build his own exclusive community from the ground up that talks about art, web3 and AI. The goal is to build an elite community of smart, like-minded people and an ecosystem of tools for the them to enjoy towards having a fun and decentralized future filled with art and tech. There are multiple ways to get whitelisted for you to be able to mint the NFT. First is the easiest way, simply let us know more about you! Share with us your talent and contributions in web3. Answer the form in the website. Second,  Give your insights about art and tech in the NFT space. Let us know about your thoughts on various integrations of art, web3 and AI! Are you pro or anti AI art? How do you think AI will affect the current NFT space? Thirdly, Participate in discussions, contribute to forums and provide suggestions of what we can improve on and what you want to see in our community. Fourth, engage on our twitter and join our collaborations' Lil Pass (whitelist) giveaways. You can also provide solid collaborations and you're automatically whitelisted. Lastly, join our activities and games. One of the goals of the project is to build an exclusive community that is crazy about art, web3 and AI while offering tools for its holders. Aside from building an exclusive community, the project’s roadmap also includes building collaborations and integrations with third-party tools to give more value to the NFT and at the same time, to build Cotlin — an in-house ecosystem of tools which consists of AI and Web3 tools for NFTs, Discord bots, browser extensions and more — which will also help the project in terms of sustaining revenue even after the minting phase since the tools will be paid for non-holders of the NFT and will be free for NFT holders. Lil Farm Boy will also have a lore where the story is about someone, who at some point, were undervalued and unappreciated for their passion at their current environment and community; who needed someone and somewhere to belong to. The lore also explains how the Lil Farm Boy meets Cotlin, his robot companion, who teaches him more about technology, especially AI, to be used for his art. The lore includes the Lil Farm Boy’s adventure to The City of Innovative Arts where he learns about technology, and that it can be used to upgrade his art in beyond his imagination. The roadmap for Lil Farm Boy also includes an exclusive merchandise for its holders and a marketplace for non-holders to avail of the said merchandise which will be internationally available. To make the NFT have a more interactive and immersive experience, the team at The Howdy Studios will build NFT Augmented Reality applications so the NFT holders can make use of their assets as their avatars. Above all this, the team will build token-gated decentralized applications and games that NFT holders will surely enjoy with the rest of the community. The Lil Farm Boy is a collaboration project by three organizations: The Howdy Studios, Level Art and Zoociety. Explore and grow with an amazing community that appreciates. Art by Level Art — 150+ artists DAO. Web3 by The Howdy Studios — a web3 dev house. AI tools by Zoociety — ecosystem of AI and other tech tools. The Howdy Studios is a startup web3 dev studio building since 2021, that has built and catered several NFT projects, both small and big collections. The founders have vast experience in startup and web app building for almost a decade. And now, they’re taking their skills to the next level by exploring the possibilities of blockchain, smart contracts, cryptocurrencies and NFTs through continuous building and progressive learning. Level Art is a community of empowered artists helping Web3 founders and builders bring their dream projects to life through quality art that has a vision of becoming the leading Web3 art community. Zoociety is a next-generation one-stop ecosystem that leverages the power of emerging technologies to bring a wide range of tools, resources, and services to create a more connected and creative world in a new, innovative way. Aside from these three organizations, the team will be handpicking elite community members who contributed real value to the community and they will be called Councils — one for art and one for tech. Councils are special roles in the community divided between art and tech. They are the key leaders at the City of Innovative Arts that highly contributes to the community. Only holders of 5 NFTs and up may be qualified to be part of this elite group who will be orchestrating decisions and plans for the community together with the Lil Team. Few ways to be summoned as a council are: contribute to forum topics, participate in twitter spaces, talk about art, web3 and AI, join activities, offer suggestions. So people should HODL or hold a Lil Farm Boy NFT so that they are in the front seat of an exclusive community, all contributing towards one goal — to explore art, web3 and AI, and be able to bridge them all together. Most tools that the Lil Farm Boy Team will build are token-gated for holders only. Special perks and privileges await those who become Lil Angels and Lil Heroes (10+ NFTs). To learn more about the project, people can ask Cotlin — our friendly robot AI that will guide you every step of the way. If you have questions, tasks for him to do, or simply want someone to talk to, he’s the guy! He’s also the one who taught the Lil Farm Boy about AI! Web3 refers to the third generation of the World Wide Web, which is built on decentralized technology such as blockchain and aims to give users more control over their data and online interactions. Blockchain is a decentralized, digital ledger that records transactions across a network of computers. Each block in the chain contains a number of transactions, and once recorded, the data in a block cannot be altered. Smart Contract is a computer program that automates the execution of a contract. Smart contracts are self-executing and self-enforcing, meaning that they can automatically enforce the rules and penalties of an agreement. Decentralized Application (dApp) is an application that runs on a decentralized network, typically using smart contracts to automate its functionality. dApps are built on top of blockchain technology and are decentralized, meaning that they do not have a central point of control or ownership. Non-Fungible Token, NFT is a digital asset that represents ownership of a unique item or piece of content, such as a digital collectible or a virtual real estate. NFTs are stored on a blockchain and are not interchangeable with other tokens of the same type. DeFi is a decentralized finance, refers to a movement that aims to build financial applications on top of decentralized infrastructure, such as smart contracts on the Ethereum blockchain. These apps can include lending and borrowing platforms, stablecoins, and prediction markets. Ethereum is an open-source, blockchain-based, decentralized computing platform that enables the creation of smart contracts and decentralized applications (dApps). It was first proposed in 2013 by Vitalik Buterin, a programmer and researcher in the field of cryptocurrency. A cryptocurrency is a digital or virtual currency that uses cryptography for security. Cryptocurrencies are decentralized and operate on a blockchain, which is a distributed ledger technology that records and verifies transactions. Polygon (previously known as Matic Network) is a layer 2 scaling solution for Ethereum. It uses a system of sidechains that are secured by a network of validators, which allows for faster and cheaper transactions than on the main Ethereum blockchain. Artificial Intelligence (AI) is a branch of computer science that deals with the creation of intelligent machines that can perform tasks that typically require human intelligence, such as understanding natural language, recognizing images and speech, and making decisions. Augmented Reality (AR) is a technology that enhances the user's perception of the real world by overlaying digital information, such as images, videos, or 3D models, on top of the user's view of the real world. DAO stands for Decentralized Autonomous Organization. It is a digital organization that is run by a set of rules encoded on a blockchain, rather than being controlled by a central authority or group of individuals. HODL is a term that originated in the cryptocurrency community as a misspelling of the word hold in a 2013 forum post. The term HODL has since been adopted as an acronym that stands for Hold On for Dear Life. It is used to describe the strategy of buying and holding a cryptocurrency long-term, rather than trading it frequently. Gamefi, also known as GameFi or Game-Fi, is a term that refers to the intersection of gaming and finance. It is a term used to describe the use of blockchain technology, smart contracts, and decentralized finance (DeFi) protocols to create new financial products, services and experiences for gamers. Discord is a communication platform that is popular among gamers and communities. It provides text, voice, and video chat functionality, as well as the ability to share files, images, and videos. Discord also includes a wide range of additional features, such as the ability to create and join servers (also known as channels), create and manage roles, and use a variety of bots to enhance the functionality of the platform. Decentralized refers to a system or network that operates on a distributed model, rather than a centralized one. In a centralized system, there is a central point of control, such as a single server or database, that manages and coordinates all the operations. In a decentralized system, there is no central point of control, and the operations are managed by multiple nodes or participants that are distributed across the network. Cryptography is the practice of secure communication and the science of techniques for secure communication. Cryptography is used to protect sensitive information, such as personal data and financial transactions, from unauthorized access, alteration, or disclosure. A stablecoin is a type of cryptocurrency that is pegged to the value of a fiat currency, commodity, or other cryptocurrency. The idea behind stablecoins is to provide a digital asset that maintains a relatively stable value, unlike other cryptocurrencies like Bitcoin or Ethereum which can be highly volatile. A sidechain is a separate blockchain that is attached to a main blockchain using a two-way peg. This allows for assets to be transferred between the two chains, effectively allowing the sidechain to have its own set of rules and uses while still being able to utilize the security provided by the parent chain. Twitter is a social media platform that allows users to post short messages, called tweets, which can include text, images, and links. Tweets are limited to 280 characters, and users can follow other users to see their tweets in their own timeline."
        },
    })

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/bert-large-uncased-whole-word-masking-finetuned-squad",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(data),
    )

    result = output.json()
    filtered = result.get("answer")
    answer = json.dumps({"response": filtered})
    return answer


@ app.get("/q&a")
def chat(question: str, context: str):
    data = ({
        "inputs": {
            "question": question,
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

    result = output.json()
    filtered = result.get("answer")
    answer = json.dumps({"response": filtered})

    return answer

# TEXT MASKING


@ app.get("/tachyon")
def chat(prompt: str):
    data = ({
        "inputs": {
            "question": prompt,
            "context": "Zoociety is a next-generation one-stop ecosystem that leverages the power of emerging technologies to bring a wide range of tools, resources, and services to create a more connected and creative world in a new, innovative way. One of Zoociety's main objectives is to solve the problem of monetizing creative works. Billions of artists, writers, and creators struggle to find platforms that allow them to monetize their skillsets and creations. The secret of getting these people on board is a seamless one-stop ecosystem with zero required knowledge about the latest emerging technologies. Zoociety's Ecosystem focuses on exploration, tokenization and monetization by providing users with platforms that can easily create, manage, and monetize their tokenized assets with intuitive UI/UX, low transaction fees, and fast settlement of decentralized transactions. Zoociety also aims to improve the process of finding and sharing relevant contents or results in a snap. With so much information available online, it can be difficult to sift through and find high-quality, reliable sources. Zoociety's Research Lab and its Intelligent Units help users discover valuable content and find the most reliable answers to their problems in a few clicks. In addition, Zoociety seeks to address issues such as isolation, limited access to emerging technologies, complex file management, data permanence, lack of transparency and trust in online interactions and transactions, inefficient use of time and resources, inappropriate or offensive content, lack of privacy and security, difficulty connecting with like-minded individuals, limited customization and personalization opportunities, and lack of access to professional development. By providing a comprehensive ecosystem that combines all the power of technologies like AI, Blockchain Technology, and Quantum Computing, Zoociety helps users to solve real-world web problems, at least in one-sitting. Our vision is to become the premier platform for innovation, collaboration, and creativity. By building a comprehensive ecosystem that combines the best of emerging technologies, we believe we can create a platform that is unparalleled in its ability to connect and empower users from all walks of digital life. We envision a future where everyone, from casual users to professionals and experts, has the tools and resources they need to achieve their full potential and contribute to a more connected and creative world of our society. Our mission is to provide a platform that empowers users to connect, create, and collaborate in innovative ways. By leveraging emerging technologies, we seek to create a comprehensive ecosystem that meets the needs of users across the spectrum. We believe that by bringing people together and providing them with the necessary tools and resources, we can foster creativity, collaboration, and innovation on a global scale. Our goal is to create a user-friendly, intuitive, and accessible platform that meets the needs of both casual users and experts. By prioritizing ease of use and user experience, we aim to create a platform that is attractive to a wide range of users. We also strive to continuously improve and evolve the Zoociety Ecosystem in response to user feedback and changing market conditions, in order to provide the best possible experience for our users. Zoociety is created, owned, founded, and developed by raldblox. Raldblox is so cute and smart."
        },
    })
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/bert-large-uncased-whole-word-masking-finetuned-squad",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(data),
    )

    return output.json()


@ app.get("/wordmask")
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


@ app.get("/imagecaption/{_:path}")
def image(request: Request):

    with open(url, "rb") as f:
        data = f.read()

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=data,
    )

    return output.content


@ app.get("/waifu")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/hakurei/waifu-diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/cyberpunk")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/DGSpitzer/Cyberpunk-Anime-Diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/pencil")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/yehiaserag/anime-pencil-diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/photoreal")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/dreamlike-art/dreamlike-photoreal-2.0",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/arcane")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/nitrosocke/Nitro-Diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(
            f"{prompt}, arcane style"),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/disney")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/nitrosocke/Nitro-Diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(
            f"{prompt}, modern disney style"),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/portrait")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/prompthero/openjourney",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(f"portrait+ {prompt}"),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/redshift")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/nitrosocke/redshift-diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(f"redshift style {prompt}"),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/analog")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/wavymulder/Analog-Diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(f"analog style {prompt}"),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/japan")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/aipicasso/cool-japan-diffusion-2-1-0",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(f"{prompt}, official art, 4k, detailed"),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/futurecharacter")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/nitrosocke/Future-Diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(
            f"future style {prompt} Negative Prompt: duplicate heads bad anatomy"),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/futurelandscape")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/nitrosocke/Future-Diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(
            f"future style {prompt} Negative Prompt: blurry fog soft"),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/epic")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/johnslegers/epic-diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(
            f"future style {prompt} Negative Prompt: blurry fog soft"),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/journey")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/prompthero/openjourney",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/journey2")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/prompthero/openjourney-v2",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/tts")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="audio/flac")


@ app.get("/image")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/imagepro")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/anime")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/andite/anything-v4.0",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/anime2")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/gsdf/Counterfeit-V2.0",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/cyberanime")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/DGSpitzer/Cyberpunk-Anime-Diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(F"{prompt} in dgs illustration style"),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/inkpunk")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/Envvi/Inkpunk-Diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(F"nvinkpunk {prompt}"),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/eldenring")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/nitrosocke/elden-ring-diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(F"elden ring style {prompt}"),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/illustrate")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/WarriorMama777/OrangeMixs",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@ app.get("/taylor")
def chat(pastinput: str, response: str, newinput: str):
    data = ({
        "inputs": {
            "past_user_inputs": [f"{pastinput}"],
            "generated_responses": [f"{response}"],
            "text": newinput
        },
    })
    print(data)
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(data),
    )

    # result = output.json()
    # filtered = result.get("answer")
    # answer = json.dumps({"answer": filtered})
    # return answer

    return output.json()


@ app.get("/grammar")
def checkGrammar(propmt: str):

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/pszemraj/flan-t5-large-grammar-synthesis",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(propmt),
    )

    return output.json()


@ app.get("/grammar2")
def checkGrammar(propmt: str):

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/vennify/t5-base-grammar-correction",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(propmt),
    )

    return output.json()


@ app.get("/summarizer")
def summarize(propmt: str):

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/philschmid/bart-large-cnn-samsum",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(propmt),
    )

    result = output.json()
    filter = result[0].get("summary_text")
    summary = json.dumps({"result": filter})

    return summary

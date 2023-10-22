import pinecone
from doc_vec import convert_vec

input = [{
        "Agent`s first name": "John",
        "Agent`s Last name": "Smith",
        "Agent`s brokerage": "TEstestt brokerage",
        "Agent`s title": "Broker",
        "Agent`s licensed since": "2020-06-09",
        "Agent`s website": "testwebsite.com",
        "Agent`s headline1": "I can help you sell your house.",
        "Agent`s headline2": "Don`t buy an houses without me.",
        "Agent`s description": """Initiatives
I am a real estate agent who shows initiative and takes the lead in marketing my services. I utilize various strategies and provide my clients with the best support and the most current knowledge of the rules and regulations.
Humor
I believe in the power of a good sense of humor, especially when it comes to the negotiation process. I strive to make sure that my clients never feel uncomfortable during the process, and that they are always given a chance to laugh and enjoy it.
Multiple Solutions
I pride myself on providing multiple solutions to my clients` problems. No matter the situation, I always strive to come up with a few options that I believe are the best for the particular situation at hand.
Commission Fees
I understand that commission fees are important, and I am willing to negotiate fees with my clients in order to get the best outcome for all parties. This includes making sure that I am fairly compensated for the work I do.
Communication
I respect my client`s time and always strive to respond as quickly as possible. This ensures that the process is kept as efficient and stress-free as possible. Additionally, I also keep my clients informed on any progress and changes that happen throughout the process.
Experience
I understand the importance of experience when it comes to real estate, and I prioritize working with agents who have a considerable amount of clients. This allows me to continually develop and improve my skills and knowledge, and provide the highest quality service to my clients.
""",
        "Agent`s second Language": "15",
        "Agent`s personalty profile": "I shows initiatives. I provide my own marketing strategy. I provide a good knowledge of the rules. I believe that a good send of humor can help. I provide multiple solutions to a problem. In regards to the commissions fees, I do not mind negotiating my commission fees. I respond as soon as possible. I prefer an agent who has lots of clients to gain more experience. ",
        "The most common type of property that this agent has helped with is": "Detatached Houses",
        "The second most common type of property that this agent has helped with is": "Semi Detached Houses",
        "This agent has the following charactstics": {
            "Year of Experience": "3",
            "Year of License": "4",
            "Year of first listing": "5",
            "Year of last listing": "6",
            "Year of first property sold for a client": "7",
            "Year of first property bought for a client": "8",
            "Year of last property sold for a client": "9",
            "Year of last property bought for a client": "10",
            "Total properties listed on MLS": "11",
            "Total properties sold for clients": "12",
            "Total properties bought for clients": "13",
            "Total properties sold over price": "14",
            "Total properties sold under price": "15",
            "Total properties bought over price": "16",
            "Total properties bought under price": "17"
        },
        "This agent has the following case histories": {
            "Case History 1 Title": "Case History: How I Helped a Client Buy or Sell a Property",
            "Case History 1 Description": """Initiative
Responding to a situation quickly and effectively, I was able to pursue a potential client for a property. I sought out the necessary information needed to ensure that the client had the most accurate information to make a purchase decision.
Marketing Strategy
I was able to create an effective marketing strategy for the client. By utilizing different promotions and advertising platforms, I was able to create a comprehensive way to increase the exposure of the property and gain more interest.
Negotiating Commission Fees
In order to keep the client`s costs low, I chose to negotiate the commission fees. By doing so, I was able to build trust with the client, while also providing them with a better price overall for their purchase or sale.
""",
            "Case History 2 Title": "Providing a good knowledge of the rules and multiple solutions to a problem",
            "Case History 2 Description": """Background
A client came to me looking for a property to purchase in a certain neighbourhood in the city. The neighbourhood is known for its complex and ever changing zoning rules.
My Actions
I provided my client with a comprehensive overview of the zoning rules of the neighbourhood and ensured that they understood the effects the rules could have on their purchase price and development plans.
Results
I was able to provide multiple solutions to the client that would allow them to purchase the property without having to worry about the complex and ever changing zoning rules, and they were able to purchase the property at a price that was lower than they had expected.
""",
            "Case History 3 Title": "Real Estate Agent Helps Client Purchase Property",
            "Case History 3 Description": """Initiative & Strategy
I showed initiative by researching the local real estate market and presented the client with a detailed marketing strategy tailored to their specific needs.
Rules & Negotiations
I provided the client with a comprehensive knowledge of the rules regulating the local real estate market and was able to successfully negotiate the commission fees.
Humor & Solutions
Throughout the process, I showed a good sense of humor and provided multiple solutions to the challenges encountered along the way.
""",
            "Case History 4 Title": "Providing a Solutions-Oriented Approach to Help a Client Buy or ",
            "Case History 4 Description": """Showing Initiative
Recently, I was able to help a client who was interested in buying a property. I showed initiative by having done research in advance about the area that he was interested in. This allowed me to present him with an array of potential properties that fit his criteria.
Providing My Own Marketing Strategy
I also provided my own marketing strategy when helping the client with his purchase. This included utilizing various online listing services, advertising the property in local newspapers and organizing open houses. As a result, my client was able to find a suitable property quickly.
Negotiating Commission Fees
Ultimately, I was able to close the deal by negotiating commission fees on behalf of my client. By using my knowledge of real estate rules, I was able to prove to the seller that my client was in a strong position, which allowed me to negotiate a lower fee for my client.
"""
        }
},
{
        "Agent`s first name": "Sergei",
        "Agent`s Last name": "Danilov",
        "Agent`s brokerage": "Broker",
        "Agent`s title": "dfdsfdsfsd",
        "Agent`s licensed since": "0000-00-00",
        "Agent`s website": "fdsfdsf",
        "Agent`s headline1": "fdsfds",
        "Agent`s headline2": "dfdsfd",
        "Agent`s description": "Initiatives. As a real estate agent I always take initiative. I never miss out on an opportunity to provide my own successful marketing strategy to ensure the best results.Knowledge of Rules. Good understanding of the rules is needed in the real estate profession and I provide just that. You can count on me to make sure that everything is done according to the rules and regulations of the area.Humor. I believe that having a good sense of humor in this profession is essential. It helps to lighten up the situation and creates a friendly and comfortable environment for everyone.Multiple Solutions. When a problem arises, I always look for multiple solutions before making a final decision. I believe that this approach results in better decisions for all involved parties.Fees Negotiations. I understand that when it comes to commission fees, it is important to be able to negotiate. I am open to discussing fees and finding a reasonable solution that works for everyone.Quick Response. When a potential client needs something, I always make sure to respond as soon as possible. This is essential for providing excellent customer service and ensuring that the client`s needs are met quickly.Experience With Clients. I have a lot of experience with clients, which is always valuable for a successful real estate career. I am always looking for new ways to expand my client base and provide them with the best possible experience.",
        "Agent`s second Language": "2",
        "Agent`s personalty profile": "I shows initiatives. I provide my own marketing strategy. I provide a good knowledge of the rules. I believe that a good send of humor can help. I provide multiple solutions to a problem. In regards to the commissions fees, I do not mind negotiating my commission fees. I respond as soon as possible. I prefer an agent who has lots of clients to gain more experience. ",
        "The most common type of property that this agent has helped with is": "Detatached Houses",
        "The second most common type of property that this agent has helped with is": "Detatached Houses",
        "This agent has the following charactstics": {
            "Year of Experience": "12",
            "Year of License": "12",
            "Year of first listing": "2",
            "Year of last listing": "2",
            "Year of first property sold for a client": "2",
            "Year of first property bought for a client": "2",
            "Year of last property sold for a client": "2",
            "Year of last property bought for a client": "2",
            "Total properties listed on MLS": "12",
            "Total properties sold for clients": "2",
            "Total properties bought for clients": "2",
            "Total properties sold over price": "12",
            "Total properties sold under price": "2",
            "Total properties bought over price": "2",
            "Total properties bought under price": "2"
        },
        "This agent has the following case histories": {
            "Case History 1 Title": "Real Estate Agent Provided Innovative Solutions and Negotiated Commission Fees for a Client",
            "Case History 1 Description": "Initiative Showed 10. I recently worked with a client to buy a property. With the client\u2019s budget, I went beyond the traditional search methods and utilized my own marketing strategies, such as researching lesser-known marketplace listing sites that had properties below the budget and providing information about developer incentives that the buyer could leverage.Knows the Rules. I was also able to ensure that the client was knowledgeable in the nuances of the deal, making sure to explain all applicable rules to the client so that they were well informed and there were no surprises during the actual transaction.Negotiated Commission Fees. Finally, given the pricing parameters, I was able to save the client money by negotiating the commission fees down. Through a combination of my initiative, knowledge of the rules, and ability to negotiate, the client was able to purchase the property without breaking their budget.",
            "Case History 2 Title": "Real Estate Agent Helps Client Purchase\/Sell Property",
            "Case History 2 Description": "Initiative. The real estate agent recognized the client`s needs and took initiative to provide an effective marketing strategy to ensure the property was properly advertised. The agent was also proactive in addressing the client`s questions and concerns for the duration of the process.Knowledge of Rules and Regulations. The agent was well versed in all of the rules and regulations involved in the property purchase\/sale and utilized this knowledge to ensure the transaction was conducted ethically and legally.Humor. The agent was able to lighten the mood and reassure the client through his affable demeanor and friendly sense of humor during challenging times in the process.",
            "Case History 3 Title": "I Help a Client Purchase a Property",
            "Case History 3 Description": "I Take Initiative. I take the initiative of researching the area and the property to get the best price for my client. I put together an extensive packet of information about the area and the specific property, such as crime rates, market reports, local businesses, public transportation, and schools. This helps my client to make an informed decision.I Provide My Own Marketing Strategy. I create an effective marketing strategy so that my client`s property is seen by the ideal buyers. This includes strategically placed advertisements, professionally designed flyers, and utilizing social media for maximum exposure.I Negotiate with Buyers. I work hard to negotiate the best possible price for my client. I use my knowledge of the local market, as well as my sharp negotiation skills, to get my client the best deal possible.",
            "Case History 4 Title": "Real Estate Agent Usefulness Case",
            "Case History 4 Description": "Showing Initiative. When a client contacted me with the goal of finding a property, I proactively scoured the market and gathered a collection of potential properties for them to review. Even in a tight market, I was able to come up with a list of likely prospects for them to visit.Applying The Rules. Knowing the rules of the industry and the area is important for any real estate agent, and I had a good understanding of the rules and regulations that applied to the property the client was interested in. I was able to explain the regulations in an easy to understand manner, helping the client make an educated decision on their purchase.Negotiating Commission Fees. When it came time to negotiate commission fees, I was upfront and honest with the client. I explained the market rate for brokers and was willing to negotiate the commission rate in order to come to an agreeable solution. In the end, the client was satisfied with the commission rate."
        }
    },
]

str_ = []
for i in range(len(input)):
    str__ = ""
    # str__ = str__ + "Agent`s brokerage"
    # str__ = str__ + input[i]["Agent`s brokerage"]
    print(len(input[i]["Agent`s brokerage"]))
    # str__ = str__ +"Agent`s title"
    # str__ = str__ + input[i]["Agent`s title"]
    print(len(input[i]["Agent`s title"]))
    # str__ = str__ +"Agent`s licensed since"
    # str__ = str__ + input[i]["Agent`s licensed since"]
    print(len(input[i]["Agent`s licensed since"]))
    # str__ = str__ +"headline1"
    # str__ = str__ + input[i]["Agent`s headline1"]
    print(len(input[i]["Agent`s headline1"]))
    # str__ = str__ +"Agent`s headline2"
    # str__ = str__ + input[i]["Agent`s headline2"]
    print(len(input[i]["Agent`s headline2"]))
    str__ = str__ +"description"
    str__ = str__ + input[i]["Agent`s description"]
    print(len(input[i]["Agent`s description"]))
    # str__ = str__ +"Agent`s personalty profile"
    # str__ = str__ + input["Agent`s personalty profile"]
    print(len(input[i]["Agent`s personalty profile"]))
    # str__ = str__ +"This agent has the following case histories"
    str__ = str__ +"Case History"
    str__ = str__ + input[i]["This agent has the following case histories"]["Case History 1 Title"]
    print(len(input[i]["This agent has the following case histories"]["Case History 1 Title"]))
    str__ = str__ +"Case History 1 Description"
    str__ = str__ + input[i]["This agent has the following case histories"]["Case History 1 Description"]
    print(len(input[i]["This agent has the following case histories"]["Case History 1 Description"]))
    # str__ = str__ +"Case History 2 Title"
    # str__ = str__ + input["This agent has the following case histories"]["Case History 2 Title"]
    # str__ = str__ +"Case History 2 Description"
    # str__ = str__ + input["This agent has the following case histories"]["Case History 2 Description"]
    # str__ = str__ +
    # str__ = str__ + input[]
    str_.append(str__)



pinecone_key = "42c8108f-1798-4fc2-b43b-320d619c9207"
pinecone.init(api_key=pinecone_key, environment="northamerica-northeast1-gcp")

index = pinecone.Index(index_name = "docscorer")

for st in str_:
    input = convert_vec(st)
    print(input)
    items = [{"id": str(i), "values": input[i].tolist()} for i in range(input.shape[0])]
    index.upsert(vectors = items)

print(index.describe_index_stats())
query = "I am looking for a real estate agent who experience in selling detached home and has listed at least 2 homes in the past 2 years"
index.delete(delete_all=True)
query_embedding = convert_vec(query)[0].tolist()

results = index.query(
    top_k = 6,
    include_values = True,
    vector = query_embedding
)

for i in range(len(str_)):
    print(results["matches"][i]["score"])

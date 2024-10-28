from web3 import Web3
from api_url import API_URLS
# Connect to Ethereum Sepolia testnet via Alchemy
alchemy_url = "https://eth-sepolia.g.alchemy.com/v2/W6pTG4cOiva7Ri0dyyI6t_WS92YONNz3"
web3 = Web3(Web3.HTTPProvider(alchemy_url))
# Check connection
if not web3.is_connected():
    print("Failed to connect to the Ethereum network.")
    exit()
# Contract address and ABI
contract_address = "0xc15873e0b3128658fEa1AE75661DF7c068B8932E"
contract_abi = API_URLS
# Instantiate contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)
def get_options_and_votes(round_id):
    """
    Fetches all options' descriptions and vote counts for a specific round.
    Calls getAllVotes first, then fetches each option's details.
    """
    try:
        # Get the vote counts for all options in this round
        vote_counts = contract.functions.getAllVotes(round_id).call()
    except Exception as e:
        print(f"Error fetching votes for round {round_id}: {e}")
        return None
    # Fetch each option's description using getOptionDetails
    options_data = []
    for i in range(len(vote_counts)):
        try:
            description, _ = contract.functions.getOptionDetails(round_id, i).call()
            options_data.append({"Candidate": description, "votes": vote_counts[i]})
        except Exception as e:
            print(f"Error fetching option details for option {i} in round {round_id}: {e}")
            return None
    return options_data
def get_all_rounds_data():
    """
    Fetches and prints all options and votes for each round.
    """
    try:
        # Get the total number of rounds
        total_rounds = contract.functions.currentRoundId().call()
        print(f"Total Rounds: {total_rounds}")
    except Exception as e:
        print(f"Error fetching total rounds: {e}")
        return
    # Iterate over each round and fetch options and votes
    voting_results = {}
    for round_id in range(total_rounds):
        voting_results[f'round_{round_id}'] = get_options_and_votes(round_id)
    return voting_results
# Run the function to print all rounds data
get_all_rounds_data()
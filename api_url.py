API_URLS = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"roundId","type":"uint256"},{"indexed":True,"internalType":"address","name":"voter","type":"address"},{"indexed":False,"internalType":"uint256","name":"optionIndex","type":"uint256"}],"name":"Voted","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"roundId","type":"uint256"}],"name":"VotingEnded","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"roundId","type":"uint256"},{"indexed":False,"internalType":"string[]","name":"optionDescriptions","type":"string[]"},{"indexed":False,"internalType":"uint256","name":"endTime","type":"uint256"}],"name":"VotingRoundCreated","type":"event"},{"inputs":[{"internalType":"string[]","name":"optionDescriptions","type":"string[]"},{"internalType":"uint256","name":"_durationInMinutes","type":"uint256"}],"name":"createVotingRound","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"currentRoundId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"roundId","type":"uint256"}],"name":"endVoting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"roundId","type":"uint256"}],"name":"getAllVotes","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"roundId","type":"uint256"},{"internalType":"uint256","name":"optionIndex","type":"uint256"}],"name":"getOptionDetails","outputs":[{"internalType":"string","name":"description","type":"string"},{"internalType":"uint256","name":"voteCount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"roundId","type":"uint256"},{"internalType":"uint256","name":"optionIndex","type":"uint256"}],"name":"vote","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"votingRounds","outputs":[{"internalType":"bool","name":"active","type":"bool"},{"internalType":"uint256","name":"endTime","type":"uint256"}],"stateMutability":"view","type":"function"}]
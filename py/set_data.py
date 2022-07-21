import json

obj = {
        "name": {
            "first": "Milad",
            "last": "Green",
            },
        "contact": {
            "email": "5r33ns@gmail.com",
            "twitter": "miladgr33n",
            },
        "profession": {
            "name": "programmer",
            "present": "web3.0 DeFi",
            "future": "decentralized world",
            "briefHistory": [
                "input raw data; (ML, DM) combo to predict on a specific axis; output its future and related probability",
                "P2P live-stream for over 200 nodes over a single session",
                "financial programming framework",
                ],
            "spaces": {
                "web3.0": {
                    "languages": [
                        "Solidity",
                        "Python",
                        "JavaScript",
                        "TypeScript",
                        ],
                    "smartContractTools": [
                        "ChainLink",
                        "OpenZeppelin", 
                        ],
                    "deploymentAndTesting": [
                        "Brownie",
                        "Remix",
                        ],
                    "wallets": "MetaMask",
                    "blockExplorers": "Etherscan",
                    "layerOneConnection": [
                        "Alchemy",
                        "Infura",
                        "Moralis",
                        ],
                    "frontEnd": [
                        "web3.js",
                        "ethers.js",
                        "Moralis",
                        ],
                    "securityAudits": [
                        "Trail of Bits",
                        "Slither",
                        "fuzzing",
                        ],
                    "monitoring": [
                        "OpenZeppelin Defender",
                        "tenderly",
                        ],
                    },
                "web2.0": [
                    "C",
                    "C++",
                    "Python",
                    "PHP",
                    "Java",
                    "SQL",
                    "JavaScript",
                    "Bash",
                    "HTML/CSS",
                    "C#",
                    ],
                }
            }
        }
json_obj = json.dumps(obj, indent=4)
with open('data.json', 'w') as f:
    f.write(json_obj)


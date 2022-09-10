


    const { ethers } = require("ethers");


    window.generateBasic = async() => {
      const result =  await formFinished();
      if(result){
        connect();
        execute();  
      }
      
      
    }

    

    window.connect = async () => {
      if (typeof window.ethereum !== "undefined") {
        try {
          await ethereum.request({ method: "eth_requestAccounts" });
        } catch (error) {
          console.log(error);
        }
        console.log("Connected")
        const accounts = await ethereum.request({ method: "eth_accounts" });
        console.log(accounts);
       
      } else {
        console.log("Please install MetaMask");
      }
    } 
    window.execute = async() => {
      if (typeof window.ethereum !== "undefined") {
        contractAddress = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512";
        const abi = [
          {
            "inputs": [],
            "stateMutability": "payable",
            "type": "constructor"
          },
          {
            "anonymous": false,
            "inputs": [
              {
                "indexed": false,
                "internalType": "bool",
                "name": "isBought",
                "type": "bool"
              }
            ],
            "name": "bought",
            "type": "event"
          },
          {
            "inputs": [],
            "name": "advancedPrice",
            "outputs": [
              {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
              }
            ],
            "stateMutability": "view",
            "type": "function"
          },
          {
            "inputs": [],
            "name": "buySomething",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function"
          },
          {
            "inputs": [
              {
                "internalType": "uint256",
                "name": "newPrice",
                "type": "uint256"
              }
            ],
            "name": "changeFee",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
          },
          {
            "inputs": [
              {
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
              }
            ],
            "name": "changeOwner",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
          },
          {
            "inputs": [],
            "name": "checkVault",
            "outputs": [
              {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
              }
            ],
            "stateMutability": "view",
            "type": "function"
          },
          {
            "inputs": [],
            "name": "emptyVault",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
          },
          {
            "inputs": [],
            "name": "getFee",
            "outputs": [
              {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
              }
            ],
            "stateMutability": "view",
            "type": "function"
          },
          {
            "inputs": [],
            "name": "owner",
            "outputs": [
              {
                "internalType": "address payable",
                "name": "",
                "type": "address"
              }
            ],
            "stateMutability": "view",
            "type": "function"
          }
        ];

        //From metamask get basic info
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const contract = new ethers.Contract(contractAddress, abi, signer);

        try {
          //get feeprice from contract and format it 
          const advancedPrice = await contract.getFee();
          const ethAdvancedPrice = ethers.utils.formatEther(advancedPrice);

          //call metamask and call functon on contract
          const options ={value: ethers.utils.parseEther(ethAdvancedPrice.toString())}; 
          var recipt = await contract.buySomething(options);

          //waits for the contract to be confirmed
          await recipt.wait(1);
          
          //listne for emit event from contract and puts return ammount in the variable "isbought"
          //once only lstnes for it once
          contract.once("bought", (isBought) => {
              const obj = saveData();

              //send back "javascript_data" to python
              const response = $.post( "/postmethod", {
                javascript_data: "yaaaa they finally made a transaction",
                soulMetaData: JSON.stringify(obj),
              })
              .done(function() {
                location.href= '/download'
              });
    
          });

          //send to download page after everyting is done
          //
          

        } catch (error) {
          console.log(error);
        }
      } else {
        console.log("Please install MetaMask")
      }
    }

    module.exports = {
      connect,
      execute,
    };



    
    window.saveData = () => {
      let solMeta = {
        "type": 1,
        "name":"Pizza", 
        "symbol":"PZA", 
        "supply": 1000,
        "advanced": true,
        "tax": true,
        "user_tax": 15,
        "owner_tax": 0,
        "max_tax":15,  
        "distribution": [
            {
                "name":"Development",
                "percent":25,
                "address":"<Wallet Address>"
            },
            {
                "name":"Marketing",
                "percent":25,
                "address":"<Wallet Address>"
            },
            {
                "name":"Rewards",
                "percent":25,
                "address":"<Wallet Address>"
            },
            {
                "name":"Liquidity",
                "percent":25,
                "address":"<Wallet Address>"
            }
        ],
        "mintable": false,
        "burnable": false,
        "random_coments":false,
        "random_code":false,
        "scam_fo_sho":false,
        "custom_code":false,
        "code":""
        }
        
        solMeta.name = $("#tname").val();
        solMeta.symbol = $("#tsymbol").val();
        solMeta.supply = $("#tsupply").val();
        let myString = JSON.stringify(solMeta);
        const obj = JSON.parse(myString);
        console.log(obj.name)
        return solMeta;
    }
    





    
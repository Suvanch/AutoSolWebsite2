from copyreg import constructor
import json
import os
import shutil


fullFileExtenstion = "c:\\Users\\suvan\\Desktop\\AutoSolWebsite2\\website\\"
baseContractExtension = fullFileExtenstion + "autoSol\\baseContracts\\"
staticExtension = fullFileExtenstion + "static\\contract\\"

class distribution:
    name = ""
    percent = 0
    address = ""
    #add check for low pwecent/name or no address 
    def __init__(self, name, percent,address):
        
        #if name == "":
        #    print("Name cant be empty. Try again!")
        #    return
        #if percent <= 0: 
        #    print("Percent cant be empty. Try again!")
        #    return
        #if address == "":
        #    print("Wallet address cant be empty. Try again!")
        #    return

        self.name = name
        self.percent = percent
        self.address = address

    def changeAddress(self,address):
        if address == "":
            print("Wallet address cant be empty. Try again!")
            return
        
        self.address = address
    
    def changePercent(self, percent):
        if percent <= 0: 
            print("Percent cant be empty. Try again!")
            return
        self.percent = percent

    def changeName(self, name):
        if name == "":
            print("Name cant be empty. Try again!")
            return
        self.name = name

class contractData:
    type = 0
    name = ""
    symbol = "" 
    supply = 0
    advanced = False
    tax = False
    taxBurn = False
    user_tax = 0
    owner_tax = 0
    max_tax = 0
    mintable = False
    burnable = False
    random_coments = False
    random_code = False
    scam_fo_sho = False
    custom_code = False
    code = ""
    distribution = []
    # thislist.append("orange")
    def __init__(self, name, symbol, supply):
        self.name = name
        self.symbol = symbol
        self.supply = supply

def readJson():
    file = open(fullFileExtenstion+'autosol\\solMeta.json')
    try:
        data = json.load(file)
    except:
        print("An exception occurred") 

    contract = contractData(data['name'],data['symbol'],data['supply'])
    contract.type = data['type']
    contract.advanced = data['advanced']
    contract.tax = data['tax']
    contract.user_tax = data['user_tax']
    contract.owner_tax = data['owner_tax']
    contract.max_tax = data['max_tax']
    contract.mintable = data['mintable']
    contract.burnable = data['burnable']
    contract.random_coments = data['random_coments']
    contract.random_code = data['random_code']
    contract.scam_fo_sho = data['scam_fo_sho']
    contract.custom_code = data['custom_code']


    sumOfDistro = 0
    for i in data['distribution']:
        newDist = distribution(i['name'],i['percent'],i['address'])
        contract.distribution.append(newDist) 
        sumOfDistro += i['percent']
        if i["name"] == "Burn":
            contract.taxBurn = True

    if sumOfDistro > 100:
        print("The sum of all your dstribution go over a 100%. \nThis will cause the contract to take a higher tax than expected and might cause errors when deploying.")
        print("Change the percents and regenerate make contract")
    file.close()
    return contract

def createContract(contract):

    #check if the folder still exists, if not make a new folder
    if os.path.exists(fullFileExtenstion+"static\\contract"):
        print("contract file was not deleted")
        shutil.rmtree(fullFileExtenstion+"static\\contract")
    else:
        os.makedirs(fullFileExtenstion+"static\\contract")

    

    if contract.advanced:
        advancedContract(contract)
    else:
        basicContract(contract) 
    
    #zip up folder
    #delete folder and all its contenets
    shutil.make_archive(fullFileExtenstion+"static\\contract", 'zip', fullFileExtenstion+"static\\contract")
    shutil.rmtree(fullFileExtenstion+"static\\contract")


def advancedContract(contract):
    #Creates new contract based on old contract
    newFileName = contract.symbol +".sol"
    
    if contract.tax:
        with open(baseContractExtension + 'advancedTaxBaseContract.txt','r') as firstfile, open(staticExtension+newFileName,'a') as secondfile:
            for line in firstfile:
                secondfile.write(line)
    else:
        with open(baseContractExtension + 'advancedBaseContract.txt','r') as firstfile, open(staticExtension+newFileName,'a') as secondfile:
            for line in firstfile:
                secondfile.write(line)
        

    #Editing Contract
    with open(staticExtension+newFileName, 'r') as file :
        filedata = file.read()

    filedata = filedata.replace('<contract name>', contract.name)
    filedata = filedata.replace('<contract symbol>', contract.symbol)
    filedata = filedata.replace('<contract supply>', str(contract.supply))
    filedata = filedata.replace('<maxTax>', str(contract.max_tax))
    if contract.type == 0:
        filedata = filedata.replace('<type>', "ERC20")
    elif contract.type == 1:
        filedata = filedata.replace('<type>', "BEP20")

    
    if contract.mintable:
        filedata = mint(filedata)
    else:
        filedata = filedata.replace('<mint>', "")

    if contract.burnable:
        filedata = burn(filedata)
    else:
        filedata = filedata.replace('<burn>', "")

    if contract.scam_fo_sho:
        filedata = scam_fo_sho(filedata,contract)
    #else:
        #filedata = filedata.replace('<>', "")

    if contract.custom_code:
        filedata = coustom_code(filedata,contract)
    else:
        filedata = filedata.replace('<custom code>', "")

    if contract.tax:
        filedata = addTax(filedata,contract)



    #if contract.random_code:
        #filedata = randCode(filedata)

    
    with open(staticExtension+newFileName, 'w') as file:
        file.write(filedata)

def basicContract(contract):
    #Creates new contract based on old contract
    newFileName = contract.symbol +".sol"
    with open(baseContractExtension + 'basicBaseContract.txt','r') as firstfile, open(staticExtension+newFileName,'a') as secondfile:
        for line in firstfile:
             secondfile.write(line)


    #Editing Contract
    with open(staticExtension+newFileName, 'r') as file :
        filedata = file.read()

    filedata = filedata.replace('<contract name>', contract.name)
    filedata = filedata.replace('<contract symbol>', contract.symbol)
    filedata = filedata.replace('<contract supply>', str(contract.supply))

    
    with open(staticExtension+newFileName, 'w') as file:
        file.write(filedata)



def mint(filedata):
    function = """
        \tfunction mint(address account,uint256 amount) public onlyOwner{
        \t\t_mint(account, amount);}
        \n"""
    filedata = filedata.replace('<mint>', function)
    return filedata

def burn(filedata):
    function = """
        \tfunction burn(address account, uint256 amount) public onlyOwner {
        \t\t_burn(account, amount);}
        \n"""
    filedata = filedata.replace('<burn>', function)
    return filedata

def addDistrbution(filedata,contract):
    #setting golval variables for walet addresses
    proposeFeeDistroSet = ""
    globalOwnerWalletAddressVariable = "" #address public _developerWallet;
    globalOwnerWalletPercentVariable = "" #uint256 public _developerWalletFeePercent;
    globalPendingOwnerPercentVariable = "" #uint256 public _pendingDeveloperWalletFeePercent;
    constructorOwnerAddressVariable = "" #address developerWallet,
    constructorSetGlobal = "" #_developerWallet = developerWallet;
    constructorSetWalletPercent = "" #_developerWalletFeePercent = 45e16; //44%
    constructorBurnPercet = "" #_burnPercent = 0e16; //0%
    constructorAddOwnerWhitelist = "" #addWhitelistAddress(_developerWallet);
    transferWfeesOwnerAmountVariable = "" #uint256 toDeveloper,
    transferWfeesCall = "" #_transfer(sender, _MarketingWallet, toMarketing);
    getCurrentFeeDistroNumReturns = "" #uint256,
    getCurrentFeeDistroReturns = "" #_developerWalletFeePercent,
    getPendingFeeNumReturns = "" #uint256,
    getPendingFeeReturn = "" #_pendingDeveloperWalletFeePercent,
    calcFeeDistroInputVariables = "" #uint256 toDeveloper,
    calcFeeDistroCalc = "" #toDeveloper = amount.mul(_developerWalletFeePercent).div(1e18);
    calcFeeDistroBurn = "" #toBurn = amount.sub(toDeveloper).sub(toLand).sub(toMarketing).sub(toLiquidity);
    proposeFeeDistroInput = "" #uint256 developerWalletFeePercent,
    proposeFeeDistroRequire = "" #.add(developerWalletFeePercent)
    proposeFeeDistroSet = "" 
    setFeeDistroSet = "" #_developerWalletFeePercent = _pendingDeveloperWalletFeePercent;
    setWalletAddressFunction = "" 
    
    
    
    if contract.taxBurn:
        calcFeeDistroBurn += "\t\ttoBurn = amount"
    
    count = len(contract.distribution)
    first = contract.distribution[0].name
    for x in contract.distribution:
        
        transferWfeesOwnerAmountVariable += "\t\t\t\tuint256 to"+x.name+",\n"
        getCurrentFeeDistroNumReturns += "\t\t\tuint256,\n"
        getPendingFeeNumReturns += "\t\t\tuint256,\n"
        proposeFeeDistroInput += "\t\t\tuint256 "+x.name+"WalletFeePercent,\n" 
        calcFeeDistroInputVariables += "\t\t\tuint256 to"+x.name+",\n"

        if x.name == first:
            proposeFeeDistroRequire += "\t\t\t\t"+x.name+"WalletFeePercent\n"
        else:
            proposeFeeDistroRequire += "\t\t\t\t.add("+x.name+"WalletFeePercent)\n"


        if x.name == "Burn":
            globalOwnerWalletPercentVariable += "\tuint256 public _"+ x.name+"FeePercent;\n"
            globalPendingOwnerPercentVariable += "\tuint256 public _pending"+x.name+"FeePercent;\n"
            constructorSetWalletPercent += "\t\t_"+x.name+"FeePercent = "+str(x.percent)+"e16; //"+str(x.percent)+"%\n"
            setFeeDistroSet += "\t\t\t_"+x.name+"FeePercent = _pending"+x.name+"FeePercent;\n"
            getCurrentFeeDistroReturns += "\t\t\t_"+x.name+"FeePercent,\n"
            getPendingFeeReturn += "\t\t\t_pending" + x.name + "FeePercent,\n"
            proposeFeeDistroSet += "\t\t\t_pending"+x.name+"FeePercent = _"+x.name+"FeePercent;\n" 
            transferWfeesCall += "\t\t\t_transfer(sender, 0x000000000000000000000000000000000000dEaD, to"+x.name+");\n"

          

               
        else:
            if contract.taxBurn:
                calcFeeDistroBurn += ".sub(to"+x.name+")"
            calcFeeDistroCalc += "\t\tto"+x.name+" = amount.mul(_"+x.name+"WalletFeePercent).div(1e18);\n"
            constructorOwnerAddressVariable += "\t\taddress "+x.name+"Wallet,\n"
            globalOwnerWalletAddressVariable += "\taddress public _"+ x.name +"Wallet;\n" 
            globalOwnerWalletPercentVariable += "\tuint256 public _"+ x.name+"WalletFeePercent;\n"
            globalPendingOwnerPercentVariable += "\tuint256 public _pending"+x.name+"WalletFeePercent;\n"
            constructorSetGlobal += "\t\t_"+x.name+"Wallet = "+x.name+"Wallet;\n"
            constructorSetWalletPercent += "\t\t_"+x.name+"WalletFeePercent = "+str(x.percent)+"e16; //"+str(x.percent)+"%\n"
            constructorAddOwnerWhitelist += "\t\taddWhitelistAddress(_"+x.name+"Wallet);\n"
            transferWfeesCall += "\t\t\t_transfer(sender, _"+x.name+"Wallet, to"+x.name+");\n"
            setFeeDistroSet += "\t\t\t_"+x.name+"WalletFeePercent = _pending"+x.name+"WalletFeePercent;\n"
            getCurrentFeeDistroReturns += "\t\t\t_"+x.name+"WalletFeePercent,\n"
            getPendingFeeReturn += "\t\t\t_pending" + x.name + "WalletFeePercent,\n"
            proposeFeeDistroSet += "\t\t\t_pending"+x.name+"WalletFeePercent = _"+x.name+"WalletFeePercent;\n"           
            #add this for scam<scam>
            setWalletAddressFunction += "\tfunction set"+x.name+"WalletAddress(address "+x.name+"Address) public onlyOwner {\n\trequire(\n\t\t"+x.name+"Address != address(0),\n\t\t\""+contract.symbol+": "+x.name+"Address cannot be zero address\"\n\t);\n\t_"+x.name+"Wallet = "+x.name+"Address;\n}\n"


    constructorOwnerAddressVariable = constructorOwnerAddressVariable[:-2]
    transferWfeesOwnerAmountVariable = transferWfeesOwnerAmountVariable[:-2]
    calcFeeDistroInputVariables = calcFeeDistroInputVariables[:-2]
    getCurrentFeeDistroNumReturns = getCurrentFeeDistroNumReturns[:-2]
    getCurrentFeeDistroReturns = getCurrentFeeDistroReturns[:-2]
    getPendingFeeNumReturns = getPendingFeeNumReturns[:-2]
    getPendingFeeReturn = getPendingFeeReturn[:-2]
    proposeFeeDistroInput = proposeFeeDistroInput[:-2]
    transferWfeesCall = transferWfeesCall[:-1]
    proposeFeeDistroRequire = proposeFeeDistroRequire[:-1]
    if contract.taxBurn:
        calcFeeDistroBurn += ";"
        constructorAddOwnerWhitelist += "\t\taddWhitelistAddress(0x000000000000000000000000000000000000dEaD);\n"

    

    filedata = filedata.replace('<globalOwnerWalletAddressVariable>', globalOwnerWalletAddressVariable)
    filedata = filedata.replace('<globalOwnerWalletPercentVariable>', globalOwnerWalletPercentVariable)
    filedata = filedata.replace('<globalPendingOwnerPercentVariable>', globalPendingOwnerPercentVariable)
    filedata = filedata.replace('<constructorOwnerAddressVariable>', constructorOwnerAddressVariable)
    filedata = filedata.replace('<constructorSetGlobal>', constructorSetGlobal)
    filedata = filedata.replace('<constructorSetWalletPercent>', constructorSetWalletPercent)
    filedata = filedata.replace('<constructorBurnPercet>', constructorBurnPercet)
    filedata = filedata.replace('<constructorAddOwnerWhitelist>', constructorAddOwnerWhitelist)
    filedata = filedata.replace('<transferWfeesOwnerAmountVariable>', transferWfeesOwnerAmountVariable)
    filedata = filedata.replace('<transferWfeesCall>', transferWfeesCall)
    filedata = filedata.replace('<getCurrentFeeDistroNumReturns>', getCurrentFeeDistroNumReturns)
    filedata = filedata.replace('<getCurrentFeeDistroReturns>', getCurrentFeeDistroReturns)
    filedata = filedata.replace('<getPendingFeeNumReturns>', getPendingFeeNumReturns)
    filedata = filedata.replace('<getPendingFeeReturn>', getPendingFeeReturn)
    filedata = filedata.replace('<calcFeeDistroInputVariables>', calcFeeDistroInputVariables)
    filedata = filedata.replace('<calcFeeDistroCalc>', calcFeeDistroCalc)
    filedata = filedata.replace('<calcFeeDistroBurn>', calcFeeDistroBurn)
    filedata = filedata.replace('<proposeFeeDistroInput>', proposeFeeDistroInput)
    filedata = filedata.replace('<proposeFeeDistroRequire>', proposeFeeDistroRequire)
    filedata = filedata.replace('<proposeFeeDistroSet>', proposeFeeDistroSet)
    filedata = filedata.replace('<setFeeDistroSet>', setFeeDistroSet)
    filedata = filedata.replace('<setWalletAddressFunction>', setWalletAddressFunction)
    
    return filedata

def removeDistrbution(filedata,contract):
    filedata = filedata.replace('<globalOwnerWalletAddressVariable>', "")
    filedata = filedata.replace('<globalOwnerWalletPercentVariable>', "")
    filedata = filedata.replace('<globalPendingOwnerPercentVariable>', "")
    filedata = filedata.replace('<constructorOwnerAddressVariable>', "")
    filedata = filedata.replace('<constructorSetGlobal>', "")
    filedata = filedata.replace('<constructorSetWalletPercent>', "")
    filedata = filedata.replace('<constructorBurnPercet>', "")
    filedata = filedata.replace('<constructorAddOwnerWhitelist>', "")
    filedata = filedata.replace('<transferWfeesOwnerAmountVariable>', "")
    filedata = filedata.replace('<transferWfeesCall>', "")
    filedata = filedata.replace('<getCurrentFeeDistroNumReturns>', "")
    filedata = filedata.replace('<getCurrentFeeDistroReturns>', "")
    filedata = filedata.replace('<getPendingFeeNumReturns>', "")
    filedata = filedata.replace('<getPendingFeeReturn>', "")
    filedata = filedata.replace('<calcFeeDistroInputVariables>', "")
    filedata = filedata.replace('<calcFeeDistroCalc>', "")
    filedata = filedata.replace('<calcFeeDistroBurn>', "")
    filedata = filedata.replace('<proposeFeeDistroInput>', "")
    filedata = filedata.replace('<proposeFeeDistroRequire>', "")
    filedata = filedata.replace('<proposeFeeDistroSet>', "")
    filedata = filedata.replace('<setFeeDistroSet>', "")
    filedata = filedata.replace('<setWalletAddressFunction>', "")
    return filedata

#THIS DOESENT DO ANYTHING NO SCAM
def scam_fo_sho(filedata,contract):
    str = "\tfunction set"+"Burn"+"WalletAddress(address "+"Burn"+"Address) public onlyOwner {\n\trequire(\n\t\t"+"Burn"+"Address != address(0),\n\t\t\"<contract symbol>: "+"Burn"+"Address cannot be zero address\"\n\t);\n\t_"+"Burn"+"Wallet = "+"Burn"+"Address;\n}\n"
    filedata = filedata.replace('<scam>', str)
    str1 = "replace with scam warning" #add <scam info> to line 3 of baseContract.sol
    filedata = filedata.replace('<scam info>', str) #add<scam> to ln320 but you also have to change some other stuff for it to work 
    return filedata

def coustom_code(filedata,contract):
    filedata = filedata.replace('<custom code>', contract.code)
    return filedata

def addTax(filedata,contract):
    if contract.user_tax > 0:
        filedata = filedata.replace('<user_tax>', "\t\t_transactionFeePercent = "+str(contract.user_tax)+"e16; // "+str(contract.user_tax)+"%")
    else:
        filedata = filedata.replace('<user_tax>',"")
    if contract.owner_tax > 0:
        filedata = filedata.replace('<owner_tax>', "\t\t_transactionFeePercentOwner = "+str(contract.owner_tax)+"e16; // "+str(contract.owner_tax)+"%")
    else:
        filedata = filedata.replace('<owner_tax>',"")

    #if there is a coustom distribution
    count = len(contract.distribution)
    if count > 0:
        filedata = addDistrbution(filedata,contract)
    else:
        print("You need to send the tax somewhere. Add distribution and try again. Im not building this contract")
        filedata = ""
        #filedata = removeDistrbution(filedata,contract)


    return filedata

contract = readJson()
createContract(contract)

def uc():
    contract = readJson()
    createContract(contract)


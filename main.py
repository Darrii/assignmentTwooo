from adriano import PCMCFrom

cryptoname = input("Enter the name of the CryptoCurrency:").lower()
parse = PCMCFrom.PCMCFrom(cryptoname, cryptoname + '.html')

parse.parseFromCMC()
from txt2csv import txt2csv
from data2json import dataSequence2jsonFormat
from postLib import postJson, postDossier
import os



# Séquence 1

# Convertir le fichier brut en csv
# name="95476D_S1"
# txt2csv(name)

# Appeler la fonction sur Matlab avec cette commande
# dataPreProcessing("95476D_S1","2023-09-22_10-39-22",[2655, 5019, 7384])



# Convertir les fichiers csv traités en json  
# dataFileName="95476D_S1_1_2023-09-22_10-39-22"
# data=dataSequence2jsonFormat(dataFileName,"00:07:80:65:DF:D1","MONTEE",16,50,"Montée de 4 étages",["INDEX", "RESP_THORAX", "RESP_ABDOMEN", "ACC_VERTICAL", "ACC_HORIZONTAL"])

# dataFileName="95476D_S1_2_2023-09-22_10-40-15"
# data=dataSequence2jsonFormat(dataFileName,"00:07:80:65:DF:D1","DESCENTE",16,50,"Descente de 4 étages après une montée de 4 étages",["INDEX", "RESP_THORAX", "RESP_ABDOMEN", "ACC_VERTICAL", "ACC_HORIZONTAL"])


# dataFileName="95476D_S1_3_2023-09-22_10-41-02"
# data=dataSequence2jsonFormat(dataFileName,"00:07:80:65:DF:D1","MONTEE",16,50,"Montée de 4 étages après une descente et une montée de 4 étages",["INDEX", "RESP_THORAX", "RESP_ABDOMEN", "ACC_VERTICAL", "ACC_HORIZONTAL"])

# dataFileName="95476D_S1_4_2023-09-22_10-41-49"
# data=dataSequence2jsonFormat(dataFileName,"00:07:80:65:DF:D1","REPOS",16,50,"Repos après deux montées et une descente de 4 étages",["INDEX", "RESP_THORAX", "RESP_ABDOMEN", "ACC_VERTICAL", "ACC_HORIZONTAL"])

# Séquence 2

# Convertir le fichier brut en csv
# name="95476D_S2"
# txt2csv(name)

# Appeler la fonction sur Matlab avec cette commande
# dataPreProcessing("95476D_S2","2023-09-22_10-45-12",[2216, 4949, 7250, 9892])



# Convertir les fichiers csv traités en json      
# dataFileName="95476D_S2_1_2023-09-22_10-45-12"
# data=dataSequence2jsonFormat(dataFileName,"00:07:80:65:DF:D1","DESCENTE",16,50,"Descente de 4 étages",["INDEX", "RESP_THORAX", "RESP_ABDOMEN", "ACC_VERTICAL", "ACC_HORIZONTAL"])

# dataFileName="95476D_S2_2_2023-09-22_10-45-56"
# data=dataSequence2jsonFormat(dataFileName,"00:07:80:65:DF:D1","MONTEE",16,50,"Montée de 4 étages après une descente de 4 étages",["INDEX", "RESP_THORAX", "RESP_ABDOMEN", "ACC_VERTICAL", "ACC_HORIZONTAL"])

# dataFileName="95476D_S2_3_2023-09-22_10-46-50"
# data=dataSequence2jsonFormat(dataFileName,"00:07:80:65:DF:D1","DESCENTE",16,50,"Descente de 4 étages après une descente et une montée de 4 étages",["INDEX", "RESP_THORAX", "RESP_ABDOMEN", "ACC_VERTICAL", "ACC_HORIZONTAL"])

# dataFileName="95476D_S2_4_2023-09-22_10-47-37"
# data=dataSequence2jsonFormat(dataFileName,"00:07:80:65:DF:D1","MONTEE",16,50,"Montée de 4 étages après une montée et deux descentes de 4 étages",["INDEX", "RESP_THORAX", "RESP_ABDOMEN", "ACC_VERTICAL", "ACC_HORIZONTAL"])

# dataFileName="95476D_S2_5_2023-09-22_10-48-29"
# data=dataSequence2jsonFormat(dataFileName,"00:07:80:65:DF:D1","REPOS",16,50,"Repos après deux montées et deux descentes de 4 étages",["INDEX", "RESP_THORAX", "RESP_ABDOMEN", "ACC_VERTICAL", "ACC_HORIZONTAL"])

# Poste l'intégralité des fichiers du dossier data_json sur le serveur
# postDossier(r'data_json')
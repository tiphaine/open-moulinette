ECHO_SUCCESS=@echo " \033[1;32m✔\033[0m  "

all: install download convert

install:
	pip install -r requirements.txt

download:
	@rm -rf data
	@mkdir data
	# https://www.insee.fr/fr/statistiques/1893259
	@curl --output data/equip-serv-commerce-infra-16.zip https://www.insee.fr/fr/statistiques/fichier/1893259/equip-serv-commerce-infra-2016.zip
	@unzip data/equip-serv-commerce-infra-16.zip -d data/
	# https://www.insee.fr/fr/statistiques/1893257
	@curl --output data/equip-sport-loisir-socio-infra-16.zip https://www.insee.fr/fr/statistiques/fichier/1893257/equip-sport-loisir-socio-infra-2016.zip
	@unzip data/equip-sport-loisir-socio-infra-16.zip -d data/
	# https://www.insee.fr/fr/statistiques/1893261
	@curl --output data/equip-serv-ens-1er-degre-infra-16.zip https://www.insee.fr/fr/statistiques/fichier/1893261/equip-serv-ens-1er-degre-infra-2016.zip
	@unzip data/equip-serv-ens-1er-degre-infra-16.zip -d data/
	# https://www.insee.fr/fr/statistiques/1893263
	@curl --output data/equip-serv-ens-2eme-degre-infra-16.zip https://www.insee.fr/fr/statistiques/fichier/1893263/equip-serv-ens-2e-degre-infra-2016.zip
	@unzip data/equip-serv-ens-2eme-degre-infra-16.zip -d data/
	# https://www.insee.fr/fr/statistiques/1893265
	@curl --output data/equip-serv-ens-sup-form-serv-infra-16.zip https://www.insee.fr/fr/statistiques/fichier/1893265/equip-serv-ens-sup-form-serv-infra-2016.zip
	@unzip data/equip-serv-ens-sup-form-serv-infra-16.zip -d data/
	# https://www.insee.fr/fr/statistiques/1893301
	# 4 files for this insee'files
	@curl --output data/structure-distrib-revenus-iris-2011.zip https://www.insee.fr/fr/statistiques/fichier/1893301/structure-distrib-revenus-iris-2011.zip
	@unzip data/structure-distrib-revenus-iris-2011.zip -d data/
	# https://www.insee.fr/fr/statistiques/1893249
	@curl --output data/equip-serv-action-sociale-infra-16.zip https://www.insee.fr/fr/statistiques/fichier/1893249/equip-serv-action-sociale-infra-2016.zip
	@unzip data/equip-serv-action-sociale-infra-16.zip -d data/
	# https://www.insee.fr/fr/statistiques/1893247
	@curl --output data/equip-serv-sante-infra-16.zip https://www.insee.fr/fr/statistiques/fichier/1893247/equip-serv-sante-infra-2016.zip
	@unzip data/equip-serv-sante-infra-16.zip -d data/
	# https://www.insee.fr/fr/statistiques/1893251
	@curl --output data/equip-serv-medical-para-infra-16.zip https://www.insee.fr/fr/statistiques/fichier/1893251/equip-serv-medical-para-infra-2016.zip
	@unzip data/equip-serv-medical-para-infra-16.zip -d data/
	# https://www.insee.fr/fr/statistiques/1896402
	@curl --output data/equip-serv-particuliers-infra-16.zip https://www.insee.fr/fr/statistiques/fichier/1896402/equip-serv-particuliers-infra-2016.zip
	@unzip data/equip-serv-particuliers-infra-16.zip -d data/
	# https://www.insee.fr/fr/statistiques/1893234
	@curl --output data/equip-tour-transp-infra-16.zip https://www.insee.fr/fr/statistiques/fichier/1893234/equip-tour-transp-infra-2016.zip
	@unzip data/equip-tour-transp-infra-16.zip -d data/
	# https://www.insee.fr/fr/statistiques/2028271
	@curl --output data/base-ic-logement-2010.xls https://www.insee.fr/fr/statistiques/fichier/2028271/base-ic-logement-2010.xls
	# https://www.insee.fr/fr/statistiques/2028269
	@curl --output data/infra-logement-2011.zip https://www.insee.fr/fr/statistiques/fichier/2028269/infra-logement-2011.zip
	@unzip data/infra-logement-2011.zip -d data/
	# https://www.insee.fr/fr/statistiques/2028267
	@curl --output data/infra-logement-2012.zip https://www.insee.fr/fr/statistiques/fichier/2028267/infra-logement-2012.zip
	@unzip data/infra-logement-2012.zip -d data/
	# https://www.insee.fr/fr/statistiques/2386703
	@curl --output data/infra-logement-2013.zip https://www.insee.fr/fr/statistiques/fichier/2386703/base-ic-logement-2013.zip
	@unzip data/infra-logement-2013.zip -d data/
	# https://www.insee.fr/fr/statistiques/2028259
	@curl --output data/base-ic-diplomes-formation-2010.xls https://www.insee.fr/fr/statistiques/fichier/2028259/base-ic-diplomes-formation-2010.xls
	# https://www.insee.fr/fr/statistiques/2028261
	@curl --output data/infra-formation-2011.zip https://www.insee.fr/fr/statistiques/fichier/2028261/infra-formation-2011.zip
	@unzip data/infra-formation-2011.zip -d data/
	# https://www.insee.fr/fr/statistiques/2028265
	@curl --output data/infra-formation-2012.zip https://www.insee.fr/fr/statistiques/fichier/2028265/infra-formation-2012.zip
	@unzip data/infra-formation-2012.zip -d data/
	# https://www.insee.fr/fr/statistiques/2386698
	@curl --output data/infra-formation-2013.zip https://www.insee.fr/fr/statistiques/fichier/2386698/base-ic-diplomes-formation-2013.zip
	@unzip data/infra-formation-2013.zip -d data/
	# https://www.insee.fr/fr/statistiques/2028571
	@curl --output data/base-ic-couples-familles-menages-2010.zip https://www.insee.fr/fr/statistiques/fichier/2028571/base-ic-couples-familles-menages-2010.zip
	@unzip data/base-ic-couples-familles-menages-2010.zip -d data/
	# https://www.insee.fr/fr/statistiques/2386664
	@curl --output data/infra-famille-2011.zip https://www.insee.fr/fr/statistiques/fichier/2028567/infra-famille-2011.zip
	@unzip data/infra-famille-2011.zip -d data/
	# https://www.insee.fr/fr/statistiques/2028569
	@curl --output data/infra-famille-2012.zip https://www.insee.fr/fr/statistiques/fichier/2028569/infra-famille-2012.zip
	@unzip data/infra-famille-2012.zip -d data/
	# https://www.insee.fr/fr/statistiques/2386664
	@curl --output data/base-ic-couples-familles-menages-2013.xls https://www.insee.fr/fr/statistiques/fichier/2386664/base-ic-couples-familles-menages-2013.xls
	# https://www.insee.fr/fr/statistiques/2028604
	@curl --output data/infra-population-2010.zip https://www.insee.fr/fr/statistiques/fichier/2028604/infra-population-2010.zip
	@unzip data/infra-population-2010.zip -d data/
	# https://www.insee.fr/fr/statistiques/2028584
	@curl --output data/infra-population-2011.zip https://www.insee.fr/fr/statistiques/fichier/2028584/infra-population-2011.zip
	@unzip data/infra-population-2011.zip -d data/
	# https://www.insee.fr/fr/statistiques/2028582
	@curl --output data/infra-population-2012.zip https://www.insee.fr/fr/statistiques/fichier/2028582/infra-population-2012.zip
	@unzip data/infra-population-2012.zip -d data/
	# https://www.insee.fr/fr/statistiques/2386737
	@curl --output data/infra-population-2013.zip https://www.insee.fr/fr/statistiques/fichier/2386737/base-ic-evol-struct-pop-2013.zip
	@unzip data/infra-population-2013.zip -d data/
	# https://www.insee.fr/fr/statistiques/2028670
	@curl --output data/infra-activite-resident-2010.zip https://www.insee.fr/fr/statistiques/fichier/2028670/infra-activite-resident-10.zip
	@unzip data/infra-activite-resident-2010.zip -d data/
	# https://www.insee.fr/fr/statistiques/2028668
	@curl --output data/infra-activite-resident-2011.zip https://www.insee.fr/fr/statistiques/fichier/2028668/infra-activite-resident-2011.zip
	@unzip data/infra-activite-resident-2011.zip -d data/
	# https://www.insee.fr/fr/statistiques/2028654
	@curl --output data/infra-activite-resident-2012.zip https://www.insee.fr/fr/statistiques/fichier/2028654/infra-activite-resident-2012.zip
	@unzip data/infra-activite-resident-2012.zip -d data/
	# https://www.insee.fr/fr/statistiques/2386631
	@curl --output data/infra-activite-resident-2013.zip https://www.insee.fr/fr/statistiques/fichier/2386631/base-ic-activite-residents-2013.zip
	@unzip data/infra-activite-resident-2013.zip -d data/

convert:
	python mk_data.py

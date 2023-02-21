# See ../makefile


.PHONY: dotenv-install-from-example ## instantiate the dotenv-file (no override)
# cp --backup   creates .env~, but will overwrite this next time
# safest way, is to not overwrite existing .env-files, manual intervention needed.
dotenv-install-from-example:
	@echo -e "Copying .env.example to .env" ;\
	cp -n .env.example .env ;\
	echo "Please review any credentials in the .env-file."


.PHONY: dotenv-set-basedir ## replace placeholder __CDW__ with current working directory
dotenv-set-basedir:
	@echo -e "Replacing string __CWD__ -> $(PWD)" ;\
	$(SED) -i 's@__CWD__@'"$(PWD)"'@'  .env
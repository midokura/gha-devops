# Env & Vars --------------------------------------------------------

# Tasks -------------------------------------------------------------

## # Help task ------------------------------------------------------
##

## help		Print project tasks help
help: Makefile
	@echo "\n midokura gha devops project tasks:\n";
	@sed -n 's/^##/	/p' $<;
	@echo "\n";

## gen-docs	Generate docs
gen-docs:
	@echo "\n> Generate GitHub Actions docs";
	@docker build --no-cache -t gha-docs:local .;
	@docker image prune --force || true;
	@echo "\n> Generating docs:\n";
	@for gha in *; do \
		if [ -d "$$gha" ] && [ ! -L "$$gha" ]; then \
			echo "- GitHub Action: $$gha"; \
			docker run -v `pwd`/$$gha:/gha:rw --rm gha-docs:local; \
		fi; \
	done;

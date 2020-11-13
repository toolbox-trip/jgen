NAME = jgen
BASE = snail.azurecr.io


version:
	@docker build --tag ${BASE}/$(NAME):$(VERSION) ./src

pre_latest:
override VERSION = latest

latest: pre_latest version

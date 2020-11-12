NAME = jgen


version:
	@docker build --tag snail.azurecr.io/$(NAME):$(VERSION) ./src

pre_latest:
override VERSION = latest

latest: pre_latest version

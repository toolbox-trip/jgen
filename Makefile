NAME = jgen
BASE = "localhost"


version:
	@docker build --tag ${BASE}/$(NAME):$(VERSION) ./src

pre_latest:
override VERSION = latest

latest: pre_latest version

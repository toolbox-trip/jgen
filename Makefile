NAME = jgen
BASE = "localhost"
VERSION = latest


version:
	@docker build --tag ${BASE}/$(NAME):$(VERSION) ./src

DOCKER=podman
#DOCKER=docker
#DOCKER=sudo docker

ROOT_DIR:=$(realpath $(dir $(firstword $(MAKEFILE_LIST))))

.PHONY: run sharescreen
run:
	$(DOCKER) run --rm -p 1948:1948 -p 35729:35729 \
	-v $(ROOT_DIR)/slides:/slides \
	docker.io/webpronl/reveal-md:latest /slides \
	--css css/style.css \
	 --highlight-theme github \
	--watch

sharescreen:
	x11vnc -forever \
		-display :0 \
		-clip xinerama1 \
		-shared \
		-localhost \
		-ncache 10 \
		-nopw \
		-noxdamage \
		-nocursorshape -nocursorpos \
		-nobell \
		-nosel \
		-viewonly

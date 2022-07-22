FROM python:3

ARG UID_USER
ARG USERNAME
ARG GID_GROUP
ARG GROUPNAME

ENV UID_USER=${UID_USER}
ENV USERNAME=${USERNAME}
ENV GID_GROUP=${GID_GROUP}
ENV GROUPNAME=${GROUPNAME}
ADD .env-docker /.env-docker

RUN addgroup -gid $(cat /.env-docker) docker

RUN useradd -d /home/$USERNAME -u "$UID_USER" "$USERNAME"
RUN mkdir -p /home/$USERNAME
RUN usermod -aG docker ${USERNAME}

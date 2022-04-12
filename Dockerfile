# syntax=docker/dockerfile:1

FROM node:16-alpine

RUN npm install -g action-docs

RUN mkdir -p /gha

WORKDIR /gha

ENTRYPOINT ["action-docs", "-a", "action.yaml", "--no-banner", "--update-readme"]
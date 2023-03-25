# See ../makefile

# Add virtualenv to PATH, same effect as activating the virtualenv
VENV_BIN_DIR := $(shell pwd)/.venv/bin
export PATH := $(VENV_BIN_DIR):$(PATH)


# Source .env.example, because.env might not yet exist.
-include .env.example

# Source .env, if it exists. This Overrides any env-vars sourced in .env.example.
-include .env

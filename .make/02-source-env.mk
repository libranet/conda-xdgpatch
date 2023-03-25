# See ../makefile

# Source .env.example, because .env might not yet exist.
-include .env.example

# Source .env, if it exists. This Overrides any env-vars sourced in .env.example.
-include .env

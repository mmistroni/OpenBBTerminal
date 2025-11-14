This example directory contains files that allow you to work on OpenBB Terminal repo via codespaces.
The codespace is being built using Dockerfile  <OpenBBTerminal>/build/docker/platforjm_dockerfile

Since it spins off a docker en, there will be 
- no github config (which normally is associated by default to yourself once you create a codespace for your repo)
- no environment variables for OBB

## PREREQUISITED
1. You must fork out the OpenBB Terminal repo
2. in your GigHub Settings-->Codespaces you will need to configure the following variables
   2.1 GIT_USER_NAME : this is your git username, I
   2.2 GIT_USER_EMAIL: this is your git user email
   2.3 OPENBB_ENV_VARS: this is a JSON that contains all the openbb keys you have. This variable will be read by the corresponding populate_env.py script which is invoked while the codespace is being built. This script read OPENBB_ENV_VARS and create all the related
   openbb keys you have, like in the example below
            {"benzinga_api_key":"<your bz key>",
             "fmp_api_key":"<your fmp key>",
             "fred_api_key":"<your fred key>"
             }

### SETUP
You will need to :
1 - Create a .devcontainer directory under OpenBBTerminal
2 - Put  devcontainer.json and populate_env.py under this directory

### TESTING YOUR SETUP
Once your codespace is setup, you can test it by running the script  OpenBBTerminal\examples\github_codespaces\cot.py, which exercises
fmp_api_key so as to prove your setup is correct.

### LIMITATIONS
Once your codespace is running you might have issues with git commits.. You will get errors when committing files  related to your gpg
keys. I am still figuring out how to address this, but you can get around this problem by entering this command in the terminal

git config --global commit.gpgsign false



# Zombies Randomizer
A Discord bot to randomly select a Black Ops 3 Zombies map.

## Usage
This bot can be added to your server by following [these instructions](https://discordpy.readthedocs.io/en/latest/discord.html).

Run locally by creating a `.env` file:
```
$ echo DISCORD_TOKEN={ API_key } > .env
```
Where `{ API_key }` should be replaed with your API key. Then, simply run `./bot.py` for a local instance. See the section below for instructions on deploying to Heroku.

Commands are invoked prefixed by the `!` character. Here is a description of the commands:
```
!add    Adds a given map to the pool
!help   Shows this message
!list   List the current maps in the pool
!map    Randomly selects a map from the pool
!pop    Remove most recently inserted map from pool
!remove Remove given map from pool
!reset  Resets the pool to the original list of Black Ops 3 maps
```

## Deployment
I used the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) tool to deploy the Dockerized bot.

Login to Heroku. Note this needs to be done with `sudo` as we need to access the Docker daemon.
```
# heroku login
# heroku container:login
```

Create the app:
```
$ heroku create zombies-randomizer
```

Set the API key as a Heroku config var:
```
$ heroku config:set DISCORD_TOKEN={ API_key }
```
Where `{ API_key }` should be replaed with your API key. Then, push and deploy the container:
```
# heroku container:push worker --app zombies-randomizer
# heroku container:release worker --app zombies-randomizer
```

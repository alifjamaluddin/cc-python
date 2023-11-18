# Write your own IRC CLIENT

## Run this program

Setup docker image

```bash
docker build -t ccirc -f ../zero/Dockerfile.basic .
```

Run example

```bash
docker run --rm -it ccirc
```

## Available commands

- JOIN: to join channel
- PART: to leave channel
- CHANNELS: to list joined channels
- NICK: to change nickname
- QUIT: to quit program

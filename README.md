# swisspair HTTP API

A dockerized HTTP API for https://github.com/karlosss/swisspair - Algorithm to pair players according to the Swiss system (not only) for Magic: The Gathering.

## Installation

- Install and run `docker`
- clone the repository
- `cd` into the cloned repository
- `docker build .`
- `docker run -p 5000:5000 IMAGE_ID`, where `IMAGE_ID` is the ID of the image built by the previous command.

Then, `POST localhost:5000/pair` will respond. For a working example, see `test_curl.txt`.


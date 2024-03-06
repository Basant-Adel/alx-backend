# 0x03. Queuing System in JS

**`Back-end`** **`JavaScript`** **`ES6`** **`Redis`** **`NodeJS`** **`ExpressJS`** **`Kue`**

## Resources

### Read or watch:

* [Redis quick start](https://redis.io/docs/getting-started/tutorial/)
* [Redis client interface](https://redis.io/docs/manual/cli/)
* [Redis client for Node JS](https://github.com/redis/node-redis)
* [Kue](https://github.com/Automattic/kue) deprecated but still use in the industry

## Tasks

### **Install a redis instance**

Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - [https://redis.io/download/](https://redis.io/download/)):

```bash
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
```

* Start Redis in the background with `src/redis-server`

```bash
$ src/redis-server &
```

* Make sure that the server is working with a ping `src/redis-cli ping`

```bash
PONG
```

* Using the Redis client again, set the value `School` for the key `Holberton`

```bash
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
```

* Kill the server with the process id of the redis-server (hint: use `ps` and `grep`)

```bash
$ kill [PID_OF_Redis_Server]
```
<br>

Copy the `dump.rdb` from the `redis-5.0.7` directory into the root of the Queuing project.

### Requirements:

* Running `get Holberton` in the client, should return `School`

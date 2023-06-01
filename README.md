
# Grow Green




## Deployment

To Run this project you need **Redis**.
Redis is only available for Unix Systems. In order to use it on windows
you need to enable Window Subsytem for Linux. You can read more [here](https://learn.microsoft.com/en-us/windows/wsl/install) about how to enable 
it. 
Or you can use [docker image](https://hub.docker.com/_/redis) of **Redis**

To run redis server :
```bash
  service redis-server start
```

You can check if it service is successfully started or not by typing :
 ```bash
  redis-cli
  127.0.0.1:6379> ping
```
If working fine you will get this output:
```bash
PONG
```

Be carefull while installing these : 
```bash
  pip install channels
  pip install dephane
  pip install channels-redis

```

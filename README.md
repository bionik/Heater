# heater
Daemon / client for controlling gpio outputs.

I needed a daemon for controlling a heater with a timer to shut it off. I decided to go with a daemon/client model so that the daemon could be run as root and the client justs sends messages to the daemon and doesn't need to be run as root. The message is sent over an UNIX socket.

When heater is turned on, timer is started to shut the heater off after a while. This is to prevent the heater being on all the time. This feature is easily removed, if you need to leave the gpio on all the time. If you resend the on command while timer has not yet been triggered, the timer is restarted. This way tou can extend the time. Off command will also always stop the timer.

I will also call the off command from cron every midnight, since I wont be needing the heating at night.

When I need to put the heater on, I just run the client like this:
```
python client.py on
```

To shut off the heater:
```
python client.py off
```

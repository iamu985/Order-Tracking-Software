# Order-Tracking-Software
Order tracking and receipt prinitng software.

## Development SetUp
In order to run the application you need to have docker installed. If you are not aware of how to install it then check out the [docs](https://docs.docker.com/get-docker/).

1. Make sure your terminal shows Dockerfile in your filesystem.
2. To build your app run this command `docker build -t ellora/ots:dev .`
3. In linux the command in 2 needs sudo to run. You can remove to use sudo by following this [guide](https://docs.docker.com/engine/install/linux-postinstall/). 

The initial build might require some time depending on your internet speed and system.

To run the app after build run the following command:
`docker run -p 8000:8000 --privileged --device /dev/bus/usb ellora/ots:dev` 
the --device part is for linux to have usb access. 

The usb access is not yet tested and so is not implemented. It is in our todo list.

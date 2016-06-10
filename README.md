# micropython-examples

```sh
sudo minicom -s # setup -> select /dev/ttyUSB0
sudo minicom
# quit from minicom -> a -> q
```

```sh
python /git/esptool/esptool.py -p /dev/ttyUSB0 --baud 460800 write_flash --flash_size=8m 0 /git/micropython/esp8266/build/firmware-combined.bin
```
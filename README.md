# Biblioteka do sensora CO2
--> [SCD4x](SCD4x/)

Sensor potrzebuje w µPythonie zainicjalizowanej magistrali I2C:
```
from machine import Pin,I2C
i2c = I2C(0,scl=Pin(numer_pinu_scl), sda=Pin(numer_pinu_sda),freq=400_000)
```

Potem tworzy się nowy obiekt sensora:

```
import scd4x
scd41 = scd4x.SCD4X(i2c)
```
i już można poczekać sobie na nowy pomiar i odczytać jego dane:
```
while not scd.data_ready:
    pass
t = scd.temperature
rh = scd.relative_humidity
co2 = scd.CO2
print(f"Poziom CO2: {co2}ppm, temperatura: {t}°C, wilgotność: {rh}%Rh")
```

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
# Biblioteka do sterowania serwem modelarskim
--> [Servo](Servo/)

Serwo potrzebuje tylko podania pinu, do którego podłączony jest przewód z sygnałem sterującym (zazwyczaj żółty).
```
from machine import Pin
from Servo import Servo

servo = Servo(Pin(numer_pinu))
```

potem można już po prostu pisać:

```
servo.duty_us(500) # Czas impulsu jest w mikrosekundach! 1500 = środek
```

# Biblioteka do obsługi czujnika temperatury i wilgotności AHT21 / AHT10 (na zapas)

--> [ahtx0](ahtx0/)

Dostępny sensor (SHT31) obsługiwany jest przezuniwersalną bibliotekę ahtx0

Znowu, potrzeba najpierw zainicjować szynę I2C:
```
from machine import Pin,I2C
i2c = I2C(0,scl=Pin(numer_pinu_scl), sda=Pin(numer_pinu_sda),freq=400_000)
```
A potem utworzyć obiekt odpowiedzialny za komunikację z sensorem:
```
from ahtx0 import AHT20
aht10  = AHT10(i2c,address=0x38)
```

i czytać wartości:
```
rh10 = aht10.relative_humidity
t10  = aht10.temperature
```
# Kilka sensorów na jednym połączeniu I2C

Do jednej szyny I2C można na raz podłączyć więcej niż jeden sensor / układ. Wystarczy ją wtedy też zainicjować tylko raz i użyć tego samego obiektu `i2c` dla wszystkich sensorów.

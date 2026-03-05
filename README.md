# Utworzenie nowego połączenia I2C w µPythonie

```
from machine import Pin,I2C
i2c = I2C(0,scl=Pin(numer_pinu_scl), sda=Pin(numer_pinu_sda),freq=400_000)
```
Domyślnie piny SDA i SCL to piny 0 i 1 mikrokontrolera. Jeśli użyjemy ich, to wystarczy:
```
from machine import I2C
i2c = I2C()
```
i magistrala I2C zostaje "otwarta"

# Kilka sensorów na jednym połączeniu I2C

Do jednej szyny I2C można na raz podłączyć więcej niż jeden sensor / układ. Wystarczy ją wtedy też zainicjować tylko raz i użyć tego samego obiektu `i2c` dla wszystkich sensorów.

# Biblioteka do sensora CO2
--> [SCD4x](SCD4x/)

Sensor potrzebuje w µPythonie zainicjalizowanej magistrali I2C.
Potem tworzy się nowy obiekt sensora:

```
import scd4x
scd41 = scd4x.SCD4X(i2c)
```
Potem trzeba mu "powiedzieć", że ma mierzyć (można mu mierzenie przerywać, żeby nie zużywał prądu, jeśli się na przykład pracuje z baterii):
```
scd41.start_periodic_measurement()
```
i już można poczekać sobie na nowy pomiar i odczytać jego dane:
```
while not scd41.data_ready:
    pass
t = scd41.temperature
rh = scd41.relative_humidity
co2 = scd41.CO2
print(f"Poziom CO2: {co2}ppm, temperatura: {t}°C, wilgotność: {rh}%Rh")
```


# Biblioteka do obsługi czujnika temperatury i wilgotności SHT31 (zamontowany w "ptaśku")

--> [sht30](sht30/)

Zamontowany sensor to SHT31, ale od strony mikrokontrolera zachowują się tak samo, więc używa się tej samej biblioteki.

Znowu, potrzeba najpierw zainicjować szynę I2C:
```
from machine import Pin,I2C
i2c = I2C(0,scl=Pin(numer_pinu_scl), sda=Pin(numer_pinu_sda),freq=400_000)
```
A potem utworzyć obiekt odpowiedzialny za komunikację z sensorem:
```
from sht30 import SHT30
sht31  = SHT30(i2c,i2c_address=68)
```
i czytać wartości:
```
t, rh = sht.measure()
print(f"Temperatura: {t}°C, wilgotność: {rh}%Rh")
```
Ten sensor nie jest zamontowany aktualnie w "ptaśku".


# Biblioteka do obsługi czasu rzeczywistego (kalendarza i godziny)

--> [DS3231](DS3231/)
Zamontowany zegar to DS3231.

Znowu, potrzeba najpierw zainicjować szynę I2C:
```
from machine import Pin,I2C
i2c = I2C(0,scl=Pin(numer_pinu_scl), sda=Pin(numer_pinu_sda),freq=400_000)
```
A potem utworzyć obiekt odpowiedzialny za komunikację z zegarem

```
from ds3231_gen import DS3231
rtc = DS3231(i2c)
```
Teraz można po prostu odczytać aktualny czas:
```
rok,miesiac,dzien,godzina,minuta,sekunda,dzien_tygodnia,_ = rtc.get_time()
```


# Biblioteka do obsługi czujnika temperatury i wilgotności AHT21 / AHT10 (na zapas)

--> [ahtx0](ahtx0/)

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
Ten sensor nie jest zamontowany aktualnie w "ptaśku".


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
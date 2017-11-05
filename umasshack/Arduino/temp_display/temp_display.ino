//code write by Moz for YouTube changel LogMaker360, 26-10-2015
//code belongs to this video: https://www.youtube.com/watch?v=sBIXxS4xTao

#include <OneWire.h>
#include <LiquidCrystal.h>
#include <SoftwareSerial.h>

LiquidCrystal lcd(7, 8, 9, 10, 11 , 12);
 int Fahrenheit;
 int Celsius;
// DS18S20 Temperature chip i/o
OneWire ds(13);  // on pin 10

void setup(void) {
  // initialize inputs/outputs
  // start serial port
  lcd.begin(16, 2);
  lcd.setCursor(0,0);
  lcd.clear();
  Serial.begin(9600);
}

void loop(void) {

  //For conversion of raw data to C
  int HighByte, LowByte, TReading, SignBit, Tc_100, Whole, Fract;

  byte i;
  byte present = 0;
  byte data[12];
  byte addr[8];

  ds.reset();
  ds.select(addr);
  ds.write(0x44,1);         // start conversion, with parasite power on at the end

  // we might do a ds.depower() here, but the reset will take care of it.

  present = ds.reset();
  ds.select(addr);
  ds.write(0xBE);         // Read Scratchpad

  //Serial.print("P=");
  //Serial.print(present,HEX);
  //Serial.print(" ");
  for ( i = 0; i < 9; i++) {           // we need 9 bytes
    data[i] = ds.read();
  //  Serial.print(data[i], HEX);
   // Serial.print(" ");
  }
 // Serial.print(" CRC=");
  //Serial.print( OneWire::crc8( data, 8), HEX);

  // Serial.println();

  //Conversion of raw data to C
  LowByte = data[0];
  HighByte = data[1];
  TReading = (HighByte << 8) + LowByte;
  SignBit = TReading & 0x8000;  // test most sig bit
  if (SignBit) // negative
  {
    TReading = (TReading ^ 0xffff) + 1; // 2's comp
  }
  Tc_100 = (6 * TReading) + TReading / 4;    // multiply by (100 * 0.0625) or 6.25

  Whole = Tc_100 / 100;  // separate off the whole and fractional portions
  Fract = Tc_100 % 100;

  Celsius = Whole;
  Fahrenheit = (Celsius * 1.8) + 32;
  lcd.clear();
  lcd.write("Temp = ");
  lcd.print(Fahrenheit, DEC);
  lcd.write(" F");

  Serial.print("Temperature: ");
  Serial.print(Fahrenheit);
  Serial.print("\n");

  delay(1000);
}

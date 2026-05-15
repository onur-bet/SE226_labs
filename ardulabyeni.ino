int LED1pin = 43;
int LED2pin = 44;
int LED3pin = 45;
int LED4pin = 46;
int button1pin = 38;
int button2pin = 39;
int button2pin = 40;
int button2pin = 31;



bool systemON       = false;
bool prevBtn1       = false;
bool prevBtn2       = false;

int  currentMode    = 1;

unsigned long lastStepTime  = 0;
unsigned long lastBlinkTime = 0;
int           animStep      = 0;
bool          blinkState    = false;


void allOff() {
  digitalWrite(LED1pin, LOW);
  digitalWrite(LED2pin, LOW);
  digitalWrite(LED3pin, LOW);
  digitalWrite(LED4pin, LOW);
}

int ledPin(int index) {
  int pins[4] = {LED1pin, LED2pin, LED3pin, LED4pin};
  return pins[index];
}

void setup() {
  pinMode(LED1pin,    OUTPUT);
  pinMode(LED2pin,    OUTPUT);
  pinMode(LED3pin,    OUTPUT);
  pinMode(LED4pin,    OUTPUT);
  pinMode(button1pin, INPUT);
  pinMode(button2pin, INPUT);
}

void loop() {
  bool btn1 = digitalRead(button1pin);
  bool btn2 = digitalRead(button2pin);


  if (btn1 && !prevBtn1) {
    systemON = !systemON;
    if (!systemON) allOff();
    animStep = 0;
  }

  
  if (btn2 && !prevBtn2) {
    currentMode  = (currentMode % 3) + 1;
    animStep     = 0;
    lastStepTime = millis();
  }

  prevBtn1 = btn1;
  prevBtn2 = btn2;

  if (systemON) {
    unsigned long now = millis();

    if (currentMode == 1) {
     
      if (now - lastBlinkTime >= 1000) {
        lastBlinkTime = now;
        blinkState = !blinkState;
        digitalWrite(LED1pin, blinkState);
        digitalWrite(LED2pin, blinkState);
        digitalWrite(LED3pin, blinkState);
        digitalWrite(LED4pin, blinkState);
      }

    } else if (currentMode == 2) {
    
      if (now - lastStepTime >= 1000) {
        lastStepTime = now;
        allOff();
        digitalWrite(ledPin(animStep), HIGH);
        animStep = (animStep + 1) % 4;
      }

    } else if (currentMode == 3) {
    
      if (now - lastStepTime >= 1000) {
        lastStepTime = now;
        allOff();
        digitalWrite(ledPin(3 - animStep), HIGH);
        animStep = (animStep + 1) % 4;
      }
    }
  }
}
Sensor Data Logger / Sensor-Daten-Logger (IR-Receiver)


EN: A Python-based utility designed to capture and log object transitions (e.g., on a conveyor belt or light barrier) via a serial interface (Arduino). 
    The application processes real-time sensor data and exports it into Excel-friendly CSV files.
DE: Ein Python-basiertes Tool zum Erfassen und Protokollieren von Objektdurchläufen an einem Fließband oder einer Lichtschranke via serieller Schnittstelle (Arduino). 
    Die Daten werden automatisch in Excel-geeignete CSV-Dateien exportiert.   
    
    Features:
    
      - Real-time Logging: Captures start time, end time, and total duration for every detected object.
      - Intelligent Debouncing: Filters out signal noise and false positives using adjustable threshold counters.
      - Signal Tolerance: Prevents recording gaps by tolerating short signal interruptions (adjustable buffer).
      - Auto-Save: Periodically saves data (default: every 10 seconds) to prevent data loss in case of power failure.
      - Excel Optimized: Exports CSV files using ; delimiters and localized number formats (commas for decimals) for seamless integration with Excel.
      - Portable EXE: Includes a standalone executable that runs on Windows without requiring a Python installation.

      Prerequisites
      
      Hardware
      - KY-005 IR-Transmitter
      - KY-022 IR-Receiver
      - Atmega328p Board/Arduino Uno R3
      Software
      - Arduino IDE
      - Python-compatible IDE + dependencies (pyserial)

      Setup

      1. Connect your Arduino/Microcontroller to your PC. Start the Sketch combined.ino.
      2. Ensure your firmware sends the string OBJECT DETECTED! via the serial monitor when the sensor is triggered.
      3. Verify your COM port in the Windows Device Manager (Default: COM3).
      4. Close serial monitor and launch SensorLogger.exe (or run python DataIn.py).
      5. Once an object is detected, the console will display the status.
      6. CSV files are generated in the same directory as the application. Files are named using the current timestamp.

      Configuration
      The following parameters can be adjusted in the DataIn.py source code:
      PORT: The COM port of your device.
      TOLERANCE_LIMIT: The number of missing signal cycles allowed before a recording is finalized.
      SAVE_INTERVAL_SEC: Frequency of automatic file exports.

      To create your own standalone version, use PyInstaller
      

      

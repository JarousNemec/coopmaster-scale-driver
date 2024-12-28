import serial
import logging
import time as atime
import datetime

WEIGHT_COM_PORT = "COM4"
# WEIGHT_COM_PORT = "/dev/ttyUSB0"  # linux Ubuntu wth weight Arduino
WEIGHT_INTERVAL_SEC = 0.5


def get_weight_number(d):  # nacteni vahy z dat
    try:
        weight_string = str(d.replace("\r\n", ""))
        return float(weight_string)
    except ValueError:
        logging.error("cant convert weight to number - str '%s'", weight_string)
        return -1


if __name__ == '__main__':
    f = None
    logging.info("weighting spying start")
    try:
        # otevreni logu
        f = open("arduino_weight.log", "a")
        time_to_log = datetime.datetime.now().strftime("%H:%M:%S")
        str_to_write = time_to_log + ";0; weight check started;\n"
        f.write(str_to_write)

        arduino = serial.Serial(port=WEIGHT_COM_PORT,baudrate=9600, timeout=1)
        if arduino:
            while True:
                try:
                    # 30 vterin pauza pro cteni vahy
                    atime.sleep(WEIGHT_INTERVAL_SEC)
                    # cmd 'w' zadam arduino po seriovem portu o poslani aktualni vahy
                    written_lenght = arduino.write('w'.encode('ascii'))
                    #if written_lenght != 1:
                    #    logging.error("cmd w arduino - error bad received len %d", written_lenght)

                    # ctu aktualni vahu z arduina po seriovem portu
                    str_read_weight = arduino.readline().decode('ascii')
                    incomming_weight = get_weight_number(str_read_weight)

                    time_to_log = datetime.datetime.now().strftime("%H:%M:%S")
                    #time_to_log = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    # zaloguj ji
                    str_to_write = time_to_log + ";" + str(incomming_weight) + ";\n"
                    print(str_to_write)
                    f.write(str_to_write)

                except Exception as ex:
                    logging.exception(ex)

    except Exception as ex:
        logging.exception(ex)

    # if arduino:
    #     arduino.close()

    if f:
        f.close()
    logging.info("weighting spying end")
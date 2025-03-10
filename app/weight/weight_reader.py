import threading
import time
import serial
import logging
import time as atime
import datetime

from app import configuration

weight_data = ""


def get_weight_number(d):  # nacteni vahy z dat
    try:
        weight_string = str(d.replace("\r\n", ""))
        return float(weight_string)
    except ValueError:
        logging.error("cant convert weight to number - str '%s'", weight_string)
        return -1


def get_weight():
    global weight_data
    return weight_data


def run_gobbler():
    global weight_data
    f = None
    logging.info("weighting spying start")
    try:
        # otevreni logu
        f = open("arduino_weight.log", "a")
        time_to_log = datetime.datetime.now().strftime("%H:%M:%S")
        str_to_write = time_to_log + ";0; weight check started;\n"
        f.write(str_to_write)


        arduino = serial.Serial(
            port=configuration.config.WEIGHT_COM_PORT,
            baudrate=9600,
            timeout=1
        )
        if arduino:
            while True:
                try:
                    # 30 vterin pauza pro cteni vahy
                    atime.sleep(configuration.config.WEIGHT_INTERVAL_SEC)

                    # cmd 'w' zadam arduino po seriovem portu o poslani aktualni vahy
                    written_lenght = arduino.write('w'.encode('ascii'))
                    #if written_lenght != 1:
                    #    logging.error("cmd w arduino - error bad received len %d", written_lenght)

                    # ctu aktualni vahu z arduina po seriovem portu
                    str_read_weight = arduino.readline().decode('ascii')
                    incomming_weight = get_weight_number(str_read_weight)

                    # todo: fix time zone
                    time_to_log = datetime.datetime.now().strftime("%H:%M:%S")
                    #time_to_log = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    # zaloguj ji
                    str_to_write = time_to_log + ";" + str(incomming_weight) + ";\n"
                    print(str_to_write)
                    f.write(str_to_write)
                    weight_data = str_to_write
                except Exception as ex:
                    logging.exception(ex)

    except Exception as ex:
        # if permission denied occurred, try
        # "sudo usermod -a -G tty yourname"

        logging.exception(ex)


def start_weight_gobbler():
    stream_thread = threading.Thread(target=run_gobbler)
    stream_thread.start()

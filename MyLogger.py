import logging

class MyLogger:
    logger = logging.getLogger()

    @staticmethod
    def Initialize():
        # Устанавливаем уровень логирования
        MyLogger.logger.setLevel(logging.INFO)  # DEBUG, INFO, WARNING, ERROR, CRITICAL

        # Создаем обработчик для записи в файл
        file_handler = logging.FileHandler("game.log")
        file_handler.setLevel(logging.INFO)

        # Создаем обработчик для вывода в консоль
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Создаем форматтер для сообщений логгера
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

        # Добавляем форматтер к обоим обработчикам
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Добавляем оба обработчика к логгеру
        MyLogger.logger.addHandler(file_handler)
        MyLogger.logger.addHandler(console_handler)
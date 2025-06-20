from pathlib import Path

import yaml

from tgpy.utils import CONFIG_FILENAME, JSON, UNDEFINED, dot_get


class Config:
    __data: dict
    __config_filename: str

    def __init__(self, config_filename: Path = CONFIG_FILENAME):
        self.__data = {}
        self.__config_filename = config_filename

    def get(self, key: str | None, default: JSON = UNDEFINED) -> JSON:
        return dot_get(
            self.__data,
            key or '',
            default if default is not UNDEFINED else None,
            create=default is not UNDEFINED,
        )

    def set(self, key: str | None, value: JSON):
        if not key:
            self.__data = value
            self.save()
            return
        path, _, key = key.rpartition('.')
        last_obj = dot_get(self.__data, path, create=True)
        last_obj[key] = value
        self.save()

    def unset(self, key: str):
        if not key:
            raise ValueError("Can't unset the root key")
        path, _, key = key.rpartition('.')
        try:
            last_obj = dot_get(self.__data, path, {})
        except KeyError:
            return
        if key not in last_obj:
            return
        del last_obj[key]
        self.save()

    def load(self):
        try:
            with open(self.__config_filename) as file:
                self.__data = yaml.safe_load(file)
        except FileNotFoundError:
            self.__data = {}

    def save(self):
        self.__config_filename.write_text(yaml.safe_dump(self.__data))


config = Config()

__all__ = ['config']

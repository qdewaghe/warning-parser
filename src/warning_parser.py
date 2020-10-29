from typing import List, Dict, Set
import re


class Warning:
    def __init__(self, file_path: str, line: str, column: str,
                 severity: str, message: str, category: str, tool: str) -> None:
        self.__line = line
        self.__column = column
        self.__severity = severity
        self.__tool = tool
        self.__filepath = file_path

        # gcc prints ‘’ instead of '', which can be an issue
        self.__message = message.replace('‘', '\'').replace('’', '\'')

        if category.startswith('-W'):
            self.__category = category[2:]
        else:
            self.__category = category

        self.__hash = hash((self.__filepath, self.__line,
                            self.__column, self.__category))

    def __str__(self) -> str:
        return (f'({self.__tool}) {self.__filepath}:{self.__line}:{self.__column}: '
                f'{self.__severity}: {self.__message} [{self.__category}]')

    def get_filepath(self) -> str:
        return self.__filepath

    def get_severity(self) -> str:
        return self.__severity

    def get_category(self) -> str:
        return self.__category

    def get_tool(self) -> str:
        return self.__tool

    def get_line(self) -> str:
        return int(self.__line)

    def get_column(self) -> int:
        return int(self.__column)

    def get_message(self) -> str:
        return self.__message

    def __eq__(self, other) -> bool:
        return isinstance(other, Warning) and self.__hash == other.__hash

    def __hash__(self):
        return self.__hash


def get_warnings(path: str, tool: str) -> Set[Warning]:

    regex = r'^(.*)\.([a-z+]{1,3}):(\d+):(\d+): (warning|error): (.*) \[((\w|-|=)*)\]$'
    #           ~~   ~~~~~~~~~~~~~ ~~~~~ ~~~~~  ~~~~~~~~~~~~~~~  ~~~~   ~~~~~~~~~~~
    #           |    |             |     |      |                |       |
    #           Path Extension     Line  Column Severity         Message Category
    #           1    2             3     4      5                6       7
    #
    # Severity accepts error as well as warning for clang-tidy
    # Otherwise errors won't be taken into account because of categories

    warnings = set()

    with open(path, "r") as file:
        for line in file:
            match = re.match(regex, line)

            if match != None:
                path = match.group(1)
                ext = match.group(2)
                line = match.group(3)
                column = match.group(4)
                severity = match.group(5)
                message = match.group(6)
                category = match.group(7)

                path = path + "." + ext

                w = Warning(
                    path,
                    line,
                    column,
                    severity,
                    message,
                    category,
                    tool,
                )

                warnings.add(w)

    return warnings

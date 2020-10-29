from src.warnings_parser import get_warnings


def test_gcc():
    warnings = list(get_warnings('tests/gcc.txt', 'gcc'))
    assert len(warnings) == 1
    assert warnings[0].get_category() == "unused-variable"
    assert warnings[0].get_column() == 7
    assert warnings[0].get_line() == 6
    assert warnings[0].get_severity() == "warning"
    assert warnings[0].get_tool() == "gcc"
    assert warnings[0].get_message() == "unused variable 'i'"
    assert warnings[0].get_filepath() == "./test/test.cpp"


def test_clang():
    warnings = list(get_warnings('tests/clang.txt', 'clang'))
    assert len(warnings) == 1


def test_clang_tidy():
    warnings = list(get_warnings('tests/clang-tidy.txt', 'clang-tidy'))
    assert len(warnings) == 2


def test_cppcheck():
    warnings = list(get_warnings('tests/cppcheck.txt', 'cppcheck'))
    assert len(warnings) == 1

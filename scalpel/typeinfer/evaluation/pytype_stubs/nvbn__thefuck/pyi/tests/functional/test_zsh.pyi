# (generated with --quick)

from typing import Any, Tuple

init_zshrc: str
proc: Any
pytest: Any
python_2: Tuple[str, str, str]
python_3: Tuple[str, str, str]
test_how_to_configure_alias: Any
test_refuse_with_confirmation: Any
test_select_command_with_arrows: Any
test_with_confirmation: Any
test_without_confirmation: Any

def history_changed(proc, TIMEOUT, to) -> None: ...
def history_not_changed(proc, TIMEOUT) -> None: ...
def how_to_configure(proc, TIMEOUT) -> None: ...
def refuse_with_confirmation(proc, TIMEOUT) -> None: ...
def select_command_with_arrows(proc, TIMEOUT) -> None: ...
def with_confirmation(proc, TIMEOUT) -> None: ...
def without_confirmation(proc, TIMEOUT) -> None: ...
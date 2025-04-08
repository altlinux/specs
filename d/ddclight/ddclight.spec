Name: ddclight
Version: 0.1.0
Release: alt1
License: Mit

Summary: A script for controlling monitor brightness via DDC/CI
Summary(ru_RU.UTF-8): Скрипт для управления яркостью мониторов через DDC/CI

Group: System/Configuration/Hardware

Url: https://altlinux.space/fiersik/ddclight

Source: %name-%version.tar

BuildArch: noarch

%description
A utility for controlling the brightness of external monitors with
DDC/CI support. It allows you to easily adjust brightness levels
via the command line.

%description -l ru_RU.UTF-8
Утилита для управления яркостью внешних мониторов с поддержкой DDC/CI.
Позволяет легко изменять уровень яркости через командную строку.

%prep
%setup

%install
install -pD -m0755 %name %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name

%changelog
* Tue Apr 08 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.0-alt1
- Initial build

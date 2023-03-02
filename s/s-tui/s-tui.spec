Name: s-tui
Version: 1.1.4
Release: alt1

Summary: CPU performance monitoring and testing
Summary(ru_RU.UTF-8): Мониторинг и тестирование производительности процессора
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://github.com/amanusk/s-tui

Requires: stress-ng
Requires: python3-module-psutil
Requires: python3-module-urwid

# Source-url: https://github.com/amanusk/s-tui/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildRequires(pre): rpm-build-python3

%description
Terminal-based processor load monitoring utility. The Stress-Terminal user
interface, s-tui, monitors temperature, clock speed, power consumption and
CPU usage from the terminal. Shows performance degradation caused by thermal
throttling. Does not require an X server. Built-in CPU Boot Options
(stress/stress-ng/FIRESTARTER). Electrical power readings are supported on
2nd generation and later Intel Core processors (Sandy Bridge) and AMD 17h
family processors using the amd_energy driver. s-tui tested to work on
Raspberry-Pi 4,3,2,1. All readings are taken from the sensors of your
equipment, make sure that the necessary sensors are physically present on
your devices. s-tui gives you the ability to run arbitrary shell scripts
when a certain threshold is exceeded, such as your CPU temperature. See the
documentation for more information. s-tui allows you to generate reports in
csv format with the -c option. s-tui gives a warning signal about the
decrease in the clock speed of the processor, caused by thermal throttling,
changing the color of the monitor to a flashing red indication.

%description -l ru_RU.UTF-8
Утилита мониторинга загрузки процессора на базе терминала. Пользовательский
интерфейс Stress-Terminal, s-tui, отслеживает температуру, тактовую частоту,
энергопотребление и использование ЦП с терминала. Показывает снижение
производительности, вызванное тепловым дросселированием. Не требует X-сервера.
Встроенные параметры загрузки ЦП (stress/stress-ng/FIRESTARTER). Показания
электрической мощности поддерживаются процессорами Intel Core 2-го поколения
и более поздних версий (Sandy Bridge) и процессорами семейства AMD 17h с
использованием драйвера amd_energy. s-tui протестирован для работы на
Raspberry-Pi 4,3,2,1. Все показания снимаются с датчиков вашего оборудования,
убедитесь, что необходимые датчики физически присутствуют на ваших
устройствах. s-tui дает вам возможность запускать произвольные сценарии
оболочки при превышении определенного порога, например температуры вашего
процессора. См. документацию для получения дополнительной информации. s-tui
позволяет создавать отчеты в формате csv с опцией -c. s-tui подает
предупреждающий сигнал о снижении тактовой частоты процессора, вызванном
тепловым троттлингом, изменением цвета монитора на мигающую красную индикацию.

%prep
%setup

# Replacing python with python3
find s_tui/ -name "*.py" -exec sed -i 's|#!%_bindir/env python|#%_bindir/python3|' {} ";"
find s_tui/ -name "*.py" -exec sed -i 's|#!%_bindir/python|#%_bindir/python3|' {} ";"

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%_bindir/%name
%python3_sitelibdir_noarch/s_tui
%python3_sitelibdir_noarch/s_tui-%version.dist-info

%changelog
* Thu Mar 02 2023 Evgeny Chuck <koi@altlinux.org> 1.1.4-alt1
- new version (1.1.4) with rpmgs script

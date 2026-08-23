%define _unpackaged_files_terminate_build 1
%def_with check

Name: s-tui
Version: 1.5.0
Release: alt1
Summary: Terminal-based CPU stress and monitoring utility
Summary(ru_RU.UTF-8): Терминальная утилита для стресс-тестирования и мониторинга ЦП
License: GPL-2.0-or-later
Group: System/Kernel and hardware
URL: https://amanusk.github.io/s-tui
VCS: https://github.com/amanusk/s-tui

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-psutil
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-urwid
%endif

Requires: stress-ng

%description
s-tui is a terminal user interface for monitoring CPU temperature, frequency,
power consumption and utilization. It can detect performance degradation
caused by thermal throttling and does not require an X server. The application
includes a built-in CPU stress test and can optionally use stress or stress-ng.
It can also export readings in CSV format and run custom scripts when configured
thresholds are exceeded.

%description -l ru_RU.UTF-8
s-tui — терминальный интерфейс для мониторинга температуры, частоты,
энергопотребления и загрузки процессора. Программа обнаруживает снижение
производительности из-за термического троттлинга и не требует X-сервера.
В состав входит встроенный стресс-тест процессора; дополнительно можно
использовать stress или stress-ng. Результаты измерений можно экспортировать
в формате CSV, а при превышении заданных порогов — запускать пользовательские
сценарии.

%prep
%setup

%python3_fix_shebang s_tui

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%_bindir/%name
%python3_sitelibdir_noarch/s_tui
%python3_sitelibdir_noarch/%{pyproject_distinfo %name}

%changelog
* Sun Aug 23 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.5.0-alt1
- Updated to version 1.5.0.
- Enabled the test suite during package build.
- Removed obsolete compatibility workarounds.

* Sat May 25 2024 Grigory Ustinov <grenka@altlinux.org> 1.1.4-alt1.1
- NMU: fix working with new urwid

* Thu Mar 02 2023 Evgeny Chuck <koi@altlinux.org> 1.1.4-alt1
- new version (1.1.4) with rpmgs script

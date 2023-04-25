Name: hidapitester
Version: 0.3
Release: alt1

Summary: Simple command-line program to test HIDAPI
Summary(ru_RU.UTF-8): Простой инструмент командной строки для проверки HIDAPI
License: GPL-3.0
Group: Development/Other
Url: https://github.com/todbot/hidapitester

Packager: Pavel Isopenko <pauli@altlinux.org>
Source: %name-%version.tar

# Automatically added by buildreq on Tue Apr 25 2023
# optimized out: libgpg-error pkg-config sh4
BuildRequires: libhidapi-devel libudev-devel

%description
The goal of the hidapitester program is to provide a simple,
low-dependency command-line tool to test out every API call in hidapi.
Default builds are fully-static with no requirements on a system-installed hidapi.

%description -l ru_RU.UTF-8
Цель программы hidapitester - предоставить простой, независимый инструмент командной строки
для проверки любых API вызовов hidapi.
По умолчанию сборка полностью статическая и не требует установки hidapi в системе.

%prep
%setup
%make_build

%install
install -d -m0755 %buildroot%_bindir
install -m0755 %name %buildroot%_bindir

%files
%attr(4711, root, root) %_bindir/%name
%doc docs test_hardware

%changelog
* Tue Apr 25 2023 Pavel Isopenko <pauli@altlinux.org> 0.3-alt1
- initial build for Sisyphus



Name: bmcontrol
Version: 1.1
Release: alt1

Summary: Control tool for MP707x controllers
License: GNU GPLv3
Group: System/Kernel and hardware
Url: https://code.google.com/p/bmcontrol/
# git clone https://code.google.com/p/bmcontrol/

Packager: Pavel Isopenko <pauli@altlinux.org>
Summary: Control tool for MP707x controllers
Summary(ru_RU.UTF-8): Инструмент управления для контроллеров семейства MP707x
Source: %name-%version.tar
BuildRequires: gcc-c++ libstdc++-devel libhid-devel

%description
Control tool for MP707x controllers

%description -l ru_RU.UTF-8
Программа контроля и управления управляющим устройством MP707 для Linux-систем.
Позволяет передавать основные команды, сканировать подключенные датчики температуры и получать от них данные. Программа реализована на С++ и работает из командной строки.

%prep
%setup

%build
%make_build
# %makeinstall_std

%install
install -d -m0755 %buildroot%_sbindir
install -m0755 bmcontrol %buildroot%_sbindir

%files
%attr(4711, root, root) %_sbindir/bmcontrol

%changelog
* Tue Jun 02 2015 Pavel Isopenko <pauli@altlinux.org> 1.1-alt1
 -initial build for Sisyphus



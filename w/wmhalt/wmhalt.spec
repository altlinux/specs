# spec by Kogan Konstantin<kostyalamer@yandex.ru> Vladimir Gusev<vova1971@narod.ru>

Name: wmhalt
Version: 1.3
Release: alt1

Summary: Window Maker and IceWM - Halt, Reboot and LockScreen 
Summary(ru_RU.UTF-8): программа для выключения, перезагрузки и блокировки экрана в  Window Maker и IceWM
License: GPL2
Group: Graphical desktop/Window Maker

URL: http://kostyalamer.narod.ru/wmhalt/wmhalt.html

BuildArch: noarch

Source: %name-%version.tar.gz
Source1: %name.menu

Requires: python-devel python-module-pywm python-modules-tkinter
Requires: python-modules-encodings SysVinit-usermode xscreensaver
AutoReqProv: no

%description
Window Maker and IceWM - Halt, Reboot and LockScreen.

Author: Kogan Konstantin <kostyalamer@yandex.ru>
Design: Vladimir Gusev <vova1971@narod.ru>

%description -l ru_RU.UTF-8
программа для выключения, перезагрузки и блокировки экрана в  Window Maker и IceWM.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%name/Data
cp -R Data %buildroot%_datadir/%name
install -Dp -m0755 %name.py %buildroot%_datadir/%name
install -Dp -m0755 %name %buildroot%_bindir/%name
install -Dp -m0755 icehalt.py %buildroot%_datadir/%name
install -Dp -m0755 icehalt %buildroot%_bindir/icehalt
install -Dp -m0644 another/%name-16x16.png %buildroot%_miconsdir/%name.png
install -Dp -m0644 another/%name-32x32.png %buildroot%_niconsdir/%name.png
install -Dp -m0644 another/%name-48x48.png %buildroot%_liconsdir/%name.png
install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%_bindir/*
%_menudir/*
%_miconsdir/*
%_liconsdir/*
%_niconsdir/*
%_datadir/%name



%changelog
* Sat Jan 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus


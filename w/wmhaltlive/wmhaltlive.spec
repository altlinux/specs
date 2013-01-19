# spec by Kogan Konstantin<kostyalamer@yandex.ru> Vladimir Gusev<vova1971@narod.ru>

Name: wmhaltlive
Version: 1.0
Release: alt1

Summary: Window Maker LiveCD - Halt, Reboot
Summary(ru_RU.UTF-8): программа для выключения, и перезагрузки в Live сборках Window Maker
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
Window Maker LiveCD - Halt, Reboot.

%description -l ru_RU.UTF-8
программа для выключения и перезагрузки в Live сборках с Window Maker.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%name/Data
cp -R Data %buildroot%_datadir/%name
install -Dp -m0755 %name.py %buildroot%_datadir/%name
install -Dp -m0755 %name %buildroot%_bindir/%name
install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%_bindir/*
%_menudir/*
%_datadir/%name


%changelog
* Sat Jan 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus


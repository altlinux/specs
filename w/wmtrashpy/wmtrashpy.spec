# spec by Kogan Konstantin<kostyalamer@yandex.ru>

Name: wmtrashpy
Version: 0.93
Release: alt1

Summary: Trash for Window Maker
Summary(ru_RU.UTF-8): Корзина для Window Maker
License: GPL2
Group: Graphical desktop/Window Maker

URL: http://kostyalamer.narod.ru/wmtrashpy/wmtrashpy.html

BuildArch: noarch

Source: %name-%version.tar.gz
Source1: %name.menu

#BuildRequires: rpm-build-dir
Requires: WindowMaker python-devel python-module-pywm
Requires: python-modules-tkinter python-modules-encodings
AutoReqProv: no

%description
Trash for Window Maker.

%description -l ru_RU.UTF-8
Корзина для Window Maker.

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
%_datadir/%name/Data
%_datadir/%name

%changelog
* Sat Jan 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.93-alt1
- Initial build for Sisyphus


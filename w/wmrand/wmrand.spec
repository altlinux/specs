# spec by Kogan Konstantin

Name: wmrand
Version: 1.0
Release: alt1
Summary: wmrand - programm select randomize theme for Window Maker
Summary(ru_RU.UTF-8): wmrand - программа для управления режимом случайной темы в Window Maker
License: GPL2
Group: Graphical desktop/Window Maker

BuildArch: noarch

Source: %name-%version.tar.gz
Source1: %name.menu
Requires: python-devel python-modules-tkinter python-modules-encodings
Requires: WindowMaker
AutoReqProv: no

%description
wmrand - programm select randomize theme for Window Maker.

%description -l ru_RU.UTF-8
wmrand - программа для управления режимом случайной темы в Window Maker.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%name
cp -R * %buildroot%_datadir/%name
install -Dp -m0755 %name %buildroot%_bindir/%name
install -Dp -m0755 %name.py %buildroot%_datadir/%name
install -Dp -m0755 themerand.py %buildroot%_datadir/%name
install -Dp -m0755 themerand %buildroot%_bindir/
install -Dp -m0755 themerand %buildroot%_datadir/WindowMaker/autostart.d/themerand
install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%_bindir/*
%_menudir/*
%_datadir/%name
%_datadir/WindowMaker/autostart.d/*

%changelog
* Sat Jan 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus


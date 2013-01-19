# spec by Kogan Konstantin and Ivan Kornilov

Name: wmfon
Version: 1.3
Release: alt1
Summary: wmfon - Selection and resize fon for Window Maker.
Summary(ru_RU.UTF-8): wmfon -выбирает фон и растягивает его на рабочий стол Window Maker
License: GPL2
Group: Graphical desktop/Window Maker

URL: http://kostyalamer.narod.ru/wmfon/wmfon.html
BuildArch: noarch

Source: %name-%version.tar.gz
Source1: %name.menu
Requires: python-devel python-modules-tkinter python-modules-encodings
Requires: mirage
AutoReqProv: no

%description
wmfon - Selection and resize fon for Window Maker.

%description -l ru_RU.UTF-8
wmfon - программа для выбора фона и его растяжки на весь рабочий стол Window Maker-а.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%name
cp -R * %buildroot%_datadir/%name
install -Dp -m0755 %name %buildroot%_bindir/%name
install -Dp -m0755 %name.py %buildroot%_datadir/%name
#install -Dp -m0755 mirage.py %buildroot%_datadir/%name
#install -Dp -m0755 mirage %buildroot%_datadir/%name
install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%_bindir/*
%_menudir/*
%_datadir/%name



%changelog
* Sat Jan 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus


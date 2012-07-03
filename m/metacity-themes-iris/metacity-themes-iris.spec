Name: metacity-themes-iris
Version: 1.0
Release: alt1

Summary: Metacity theme - Iris
Summary(ru_RU.UTF-8): Тема Iris для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: Iris.tar.bz2
Requires: metacity
Buildarch: noarch

%description
This package contains Iris theme for Metacity simulating the
look and feel of 4Dwm windowmanager for Irix.

%description -l ru_RU.UTF-8
Пакет содержит тему Iris для Metacity, подражающую
внешнему виду диспетчера окон 4Dwm для Irix.

%prep
%setup -q -n Iris

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/Iris/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/Iris/metacity-1 

%files
%_datadir/themes/Iris/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build

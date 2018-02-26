Name: metacity-themes-aqua
Version: 1.0
Release: alt1

Summary: Metacity theme - Aqua
Summary(ru_RU.UTF-8): Тема Aqua для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: Aqua.tar.bz2
Requires: metacity
Buildarch: noarch

%description
This package contains Aqua theme for Metacity windowmanager.

%description -l ru_RU.UTF-8
Пакет содержит тему Aqua для диспетчера окон Metacity.

%prep
%setup -q -n Aqua

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/Aqua/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/Aqua/metacity-1 

%files
%_datadir/themes/Aqua/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build

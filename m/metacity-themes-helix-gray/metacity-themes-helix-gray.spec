Name: metacity-themes-helix-gray
Version: 1.0
Release: alt1

Summary: Metacity theme - HeliX-gray
Summary(ru_RU.UTF-8): Тема HeliX-gray для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: HeliX-gray.tar.bz2
Requires: metacity
Buildarch: noarch

%description
This package contains HeliX-gray theme for Metacity windowmanager.

%description -l ru_RU.UTF-8
Пакет содержит тему HeliX-gray для диспетчера окон Metacity.

%prep
%setup -q -n HeliX-gray

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/HeliX-gray/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/HeliX-gray/metacity-1 

%files
%_datadir/themes/HeliX-gray/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build

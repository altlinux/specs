Name: metacity-themes-koynacity-blue
Version: 1
Release: alt1

Summary: Metacity theme - Koynacity-Blue
Summary(ru_RU.UTF-8): Тема Koynacity-Blue для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: Koynacity-Blue.tar.bz2
Requires: metacity
Buildarch: noarch

%description
This package contains Koynacity-Blue theme for Metacity windowmanager.

%description -l ru_RU.UTF-8
Пакет содержит тему Koynacity-Blue для диспетчера окон Metacity.

%prep
%setup -q -n Koynacity-Blue

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/Koynacity-Blue/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/Koynacity-Blue/metacity-1 

%files
%_datadir/themes/Koynacity-Blue/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1-alt1
- ALTLinux build

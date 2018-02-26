Name: metacity-themes-crux-with-icons
Version: 1.0
Release: alt1

Summary: Metacity theme - Crux
Summary(ru_RU.UTF-8): Тема "Южный крест" для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: Crux-with-icons.tar.bz2
Requires: metacity
Buildarch: noarch

%description
This package contains Crux theme for Metacity windowmanager.

%description -l ru_RU.UTF-8
Пакет содержит тему "Южный крест" для диспетчера окон Metacity.

%prep
%setup -q -n Crux-with-icons

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/Crux-with-icons/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/Crux-with-icons/metacity-1 

%files
%_datadir/themes/Crux-with-icons/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build

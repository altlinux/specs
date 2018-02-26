Name: metacity-themes-metamile-marker
Version: 1.0
Release: alt1

Summary: Metacity theme - metamile-marker
Summary(ru_RU.UTF-8): Тема metamile-marker для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: metamile-marker.tar.bz2
Requires: metacity
Buildarch: noarch

%description
This package contains metamile-marker theme for Metacity windowmanager.

%description -l ru_RU.UTF-8
Пакет содержит тему metamile-marker для диспетчера окон Metacity.

%prep
%setup -q -n metamile-marker

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/metamile-marker/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/metamile-marker/metacity-1 

%files
%_datadir/themes/metamile-marker/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build

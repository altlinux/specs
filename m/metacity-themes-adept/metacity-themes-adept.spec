Name: metacity-themes-adept
Version: 1.0
Release: alt1

Summary: Metacity theme - Adept
Summary(ru_RU.UTF-8): Тема Adept для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: Adept.tar.bz2
Requires: metacity
Buildarch: noarch

%description
This package contains Adept theme for Metacity windowmanager.

%description -l ru_RU.UTF-8
Пакет содержит тему Adept для диспетчера окон Metacity.

%prep
%setup -q -n Adept

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/Adept/metacity-1
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/Adept/metacity-1

%files
%_datadir/themes/Adept/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build

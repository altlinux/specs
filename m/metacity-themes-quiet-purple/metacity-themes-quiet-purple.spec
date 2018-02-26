Name: metacity-themes-quiet-purple
Version: 0.1
Release: alt1

Summary: Metacity theme - Quiet-purple
Summary(ru_RU.UTF-8): Тема quiet-purple для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: quiet-purple.tar.bz2
Requires: metacity
Buildarch: noarch

%description
This package contains quiet-purple theme for Metacity windowmanager.

%description -l ru_RU.UTF-8
Пакет содержит тему Quiet-purple для диспетчера окон Metacity.

%prep
%setup -q -n quiet-purple

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/quiet-purple/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/quiet-purple/metacity-1 

%files
%_datadir/themes/quiet-purple/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.1-alt1
- ALTLinux build

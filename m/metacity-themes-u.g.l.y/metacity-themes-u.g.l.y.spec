Name: metacity-themes-u.g.l.y
Version: 1.0
Release: alt1

Summary: Metacity theme - u.g.l.y
Summary(ru_RU.UTF-8): Тема u.g.l.y для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: u.g.l.y.tar.bz2
Requires: metacity
Buildarch: noarch

%description
This package contains u.g.l.y theme for Metacity windowmanager.

%description -l ru_RU.UTF-8
Пакет содержит тему u.g.l.y для диспетчера окон Metacity.

%prep
%setup -q -n u.g.l.y

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/u.g.l.y/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/u.g.l.y/metacity-1 

%files
%_datadir/themes/u.g.l.y/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build

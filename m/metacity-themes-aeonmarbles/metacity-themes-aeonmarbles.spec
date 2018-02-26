Name: metacity-themes-aeonmarbles
Version: 1.1.1
Release: alt1

Summary: Metacity theme - AEonMarbles
Summary(ru_RU.UTF-8): Тема AEonMarbles для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: AEonMarbles.tar.bz2
Requires: metacity
Buildarch: noarch

%description
This package contains AEonMarbles theme for Metacity windowmanager.

%description -l ru_RU.UTF-8
Пакет содержит тему AEonMarbles для диспетчера окон Metacity.

%prep
%setup -q -n AEonMarbles

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/AEonMarbles/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/AEonMarbles/metacity-1 

%files
%_datadir/themes/AEonMarbles/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.1.1-alt1
- ALTLinux build

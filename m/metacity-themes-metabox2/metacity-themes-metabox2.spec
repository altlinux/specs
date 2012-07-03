Name: metacity-themes-metabox2
Version: 1.0
Release: alt1

Summary: Metacity theme - Metabox 2
Summary(ru_RU.UTF-8): Тема Metabox 2 для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: Metabox.tar.bz2
Requires: metacity
Buildarch: noarch

%description
This package contains Metabox 2 theme for Metacity windowmanager.

%description -l ru_RU.UTF-8
Пакет содержит тему Metabox 2 для диспетчера окон Metacity.

%prep
%setup -q -n Metabox

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/Metabox2/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/Metabox2/metacity-1 

%files
%_datadir/themes/Metabox2/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build

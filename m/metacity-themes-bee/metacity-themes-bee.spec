Name: metacity-themes-bee
Version: 1.0
Release: alt1

Summary: Metacity theme - Bee
Summary(ru_RU.UTF-8): Тема Bee для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: Bee.tar.bz2
Requires: metacity
Buildarch: noarch

%description
Black and yellow theme for Metacity.

%description -l ru_RU.UTF-8
Чёрно-желтая тема для Metacity.

%prep
%setup -q -n Bee

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/Bee/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/Bee/metacity-1 

%files
%_datadir/themes/Bee/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build

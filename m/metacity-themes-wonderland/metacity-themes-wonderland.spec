Name: metacity-themes-wonderland
Version: 1.0
Release: alt1

Summary: Metacity theme - Wonderland (Bluecurve)
Summary(ru_RU.UTF-8): Тема "Страна чудес" (или Bluecurve) для Metacity
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source: Wonderland.tar.bz2
Requires: metacity
Buildarch: noarch

%description
Red Hat Linux default theme.

%description -l ru_RU.UTF-8
Стандартная тема RedHat Linux.

%prep
%setup -q -n Wonderland

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes/Wonderland/metacity-1 
%__install -m644 -p metacity-1/* $RPM_BUILD_ROOT%_datadir/themes/Wonderland/metacity-1 

%files
%_datadir/themes/Wonderland/metacity-1

%changelog
* Sun Feb 02 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build

Summary: Gray GTK2 theme
Name: gtk2-theme-gray
Version: 1.7
Release: alt1
License: GPL
Group: Graphical desktop/GNOME
URL: http://www.cimitan.com/pages/themes.php
Packager: Valery Inozemtsev <shrek@altlinux.ru>

BuildArch: noarch

Source0: Gray.tar.gz

%description
Gray version of the nice theme "Mint" by lokheed, with a new Metacity theme.

%prep

%install
mkdir -p %buildroot%_datadir/themes
tar -xzf %SOURCE0 -C %buildroot%_datadir/themes/
find %buildroot%_datadir/themes -type f -exec chmod -x {} \;

%files
%_datadir/themes/Gray*

%changelog
* Wed Apr 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.7-alt1
- initial build

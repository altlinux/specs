Name: gnome-icon-theme-tango
Version: 0.1
Release: alt5
Summary: Tango-style icons for GNOME desktop
License: GPL
Group: Graphical desktop/GNOME

PreReq: libgtk+2-common
Obsoletes: gnome-icon-themes-extras
BuildArch: noarch

Source0: tango.tar.bz2

%description
Tango-style icons for GNOME desktop

%prep

%install
mkdir -p %buildroot%_iconsdir
tar -xjf %SOURCE0 -C %buildroot%_iconsdir/
find %buildroot%_iconsdir/ -type f -exec chmod -x {} \;
touch %buildroot%_iconsdir/tango/icon-theme.cache

%post
gtk-update-icon-cache -f -t %_iconsdir/tango/ >/dev/null 2>&1 ||:

%files
%ghost %_iconsdir/tango/icon-theme.cache
%_iconsdir/tango

%changelog
* Sun Oct 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt5
- post: updated icon cache

* Wed Apr 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt4
- added nm-{adhoc,device-wired,device-wireless,no-connection} icons

* Sun Apr 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt3
- small updated

* Thu Mar 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt2
- added gtk-* icons

* Wed Mar 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt1
- initial release


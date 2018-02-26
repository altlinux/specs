Name: parcellite
Version: 1.0.2
Release: alt0.rc5
Summary: Lightweight GTK+ Clipboard Manager
License: GPLv3
Group: Graphical desktop/GNOME
Url: http://parcellite.sourceforge.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: intltool libgtk+2-devel

%description
Parcellite  is a lightweight GTK+ clipboard manager. This is a stripped
down, basic-features-only clipboard manager with a small  memory  foot-
print for those who like simplicity.

%prep
%setup -q
%patch -p1

%build
%autoreconf
chmod +x configure
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_sysconfdir/xdg/autostart/*.desktop
%_bindir/%name
#_desktopdir/%name.desktop
%_man1dir/%name.1*

%changelog
* Tue Mar 13 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt0.rc5
- 1.0.2 RC5

* Fri Apr 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt0.rc3
- 1.0.2 RC3

* Sat Mar 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- fixed clear not working with type-as-you-search off

* Sat Mar 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Mon Mar 07 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Wed Dec 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Sat May 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.2-alt2
- added autostart for LXDE (closes: #23429)

* Sun Jan 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Wed Dec 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt1.svn107
- SVN revision 107

* Sun May 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt1
- initial release

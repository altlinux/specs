Name: parcellite
Version: 1.2.2
Release: alt1
Summary: Lightweight GTK+ Clipboard Manager
License: GPLv3
Group: Graphical desktop/GNOME
Url: http://parcellite.sourceforge.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: xdotool

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: intltool libgtk+2-devel

%description
Parcellite  is a lightweight GTK+ clipboard manager. This is a stripped
down, basic-features-only clipboard manager with a small  memory  foot-
print for those who like simplicity.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
sed -i "s|\(.*VERSION \).*|\1\"%version\"|" config.h
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
* Thu Mar 30 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Tue Apr 28 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt2
- replace icon with edit-paste

* Mon Apr 27 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Wed Feb 06 2019 Anton Midyukov <antohami@altlinux.org> 1.1.9-alt2
- Added startup for MATE (Closes: 36000)

* Sun Oct 05 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.1.9-alt1
- 1.1.9

* Sun Jul 06 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Fri Oct 18 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Wed Aug 07 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Fri Jan 25 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Tue Jan 22 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.1.4-alt0.rc3
- 1.1.4 RC3

* Sun Jan 20 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.1.4-alt0.rc2
- 1.1.4 RC2

* Thu Jan 17 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Wed Jan 16 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt0.rc7
- 1.0.2 RC7

* Tue Jan 15 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt0.rc6
- 1.0.2 RC6

* Sun Jul 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt0.rc5.1
- Fixed build

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

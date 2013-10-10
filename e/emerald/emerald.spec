Name: emerald
Version: 0.8.99
Release: alt2

Group: Graphical desktop/Other
Summary: Themeable window decorator and compositing manager for Compiz
Url: http://www.compiz-fusion.org/
License: GPL
Packager: Motsyo Gennadi <drool@altlinux.ru>

Requires: compiz

Source: %name-%version.tar.bz2

BuildPreReq: compiz-devel

# Automatically added by buildreq on Wed Oct 31 2012 (-bi)
# optimized out: compiz elfutils fontconfig fontconfig-devel glib2-devel gtk-update-icon-cache libX11-devel libXrender-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel libstartup-notification perl-XML-Parser pkg-config python-base shared-mime-info xorg-renderproto-devel xorg-xproto-devel
BuildRequires: compiz-devel desktop-file-utils intltool libwnck-devel python-module-distribute

%description
Emerald is themeable window decorator and compositing manager for Compiz.

%package devel
Summary: Development files for emerald
Group: Development/C
Requires: %name = %version-%release

%description devel
The emerald-devel package provides development files for emerald,
the themeable window decorator for compiz.

%prep
%setup -q

%build
%autoreconf
CFLAGS='-ldl'
%configure \
	--disable-static \
	--enable-librsvg \
	--disable-mime-update
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_bindir/*
%_libdir/*.so.*
%dir %_libdir/emerald
%dir %_libdir/emerald/engines
%_libdir/emerald/engines/*.so
%_datadir/emerald
%_datadir/mime-info/*
%_datadir/mime/packages/*
%_desktopdir/*.desktop
%_pixmapsdir/*.png
%_iconsdir/hicolor/48x48/mimetypes/*.png
%_man1dir/emerald*.1*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Oct 10 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.99-alt2
- fix Requires

* Thu Oct 10 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.99-alt1
- 0.8.99 git

* Mon Sep 23 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.4-alt2
- fix build for Sisyphus

* Wed Oct 31 2012 Motsyo Gennadi <drool@altlinux.ru> 0.8.4-alt1.M60T.1
- 0.8.4 build for t6

* Sat Feb 20 2010 Motsyo Gennadi <drool@altlinux.ru> 0.8.2-alt1.M51.1
- pickup from archive, build for M51

* Tue Mar 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Sat Feb 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt3
- rebuild with compiz-0.8.0

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Tue Sep 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Wed Sep 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.7-alt1
- 0.7.7

* Sun Jun 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Fri Apr 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Fri Feb 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6.99-alt1
- 0.6.99

* Wed Oct 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Tue Aug 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.1-alt2
- fixed build dependencies

* Mon Mar 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Thu Mar 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt1
- 0.2.0 release

* Sun Feb 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt0.0rc1
- 0.2.0-RC1

* Mon Feb 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt0.0pre1
- 0.2.0pre1

* Thu Dec 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Mon Dec 11 2006 Sergey V Turchin <zerg at altlinux dot org> 0.1.3-alt1
- new version

* Tue Nov 14 2006 Sergey V Turchin <zerg at altlinux dot org> 0.1.2-alt2
- fix build requires

* Thu Nov 09 2006 Sergey V Turchin <zerg at altlinux dot org> 0.1.2-alt1
- new version

* Tue Nov 07 2006 Sergey V Turchin <zerg at altlinux dot org> 0.1.1-alt1
- intial specfile

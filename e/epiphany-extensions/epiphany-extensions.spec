%define ver_major 3.4
%define eapi_ver 3.4

Name:    epiphany-extensions
Version: %ver_major.0
Release: alt1

Summary: Extensions for Epiphany, a GNOME web browser.
Summary(ru_RU.UTF-8): Расширения для интернет-браузера Epiphany
Group: Networking/WWW
License: GPL
URL: http://www.gnome.org/projects/epiphany

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: epiphany >= 3.4.0

BuildPreReq: gnome-common intltool gnome-doc-utils
BuildPreReq: libgio-devel >= 2.28.0 libgtk+3-devel >= 2.11.6
BuildPreReq: epiphany-devel >= %ver_major libwebkitgtk3-devel
BuildPreReq: libgio-devel libxml2-devel libdbus-glib-devel
BuildRequires: gcc-c++ libOpenSP-devel

%description
Extensions for Epiphany, a GNOME web browser based on the Webkit rendering engine.
%description -l ru_RU.UTF8
Расширения для Epiphany - интернет-браузера
графической оболочки GNOME, основанного
на движке отрисовки страниц Webkit.

# This is default set exclude "certificates" extension
%define extensions actions,adblock,auto-reload,extensions-manager-ui,greasemonkey,gestures,html5tube,push-scroller,tab-key-tab-navigate,tab-states,rss

%prep
%setup -q

%build
%configure \
	--disable-static \
	--with-extensions=%extensions \
	--disable-schemas-compile \
	--disable-scrollkeeper

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome --output=%name.lang %name %name-%eapi_ver

%files -f %name.lang
%_libdir/epiphany/%eapi_ver/extensions/*.so*
%_libdir/epiphany/%eapi_ver/extensions/*.ephy-extension
%_datadir/%name
%_datadir/epiphany/icons/*/*/*/*.*
%config %_datadir/glib-2.0/schemas/org.gnome.epiphanyextensions.gschema.xml
%doc AUTHORS NEWS README TODO COPYING.*

%exclude %_libdir/epiphany/%eapi_ver/extensions/*.la

%changelog
* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sat Oct 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon Apr 11 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.92-alt2
- rebuild against epiphany-3.0

* Thu Mar 24 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.92-alt1
- 2.91.92

* Fri Oct 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt3
- rebuild against new webkit

* Wed Sep 01 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt2
- rebuild against new epiphany

* Sun Aug 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Wed May 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Thu Apr 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt3
- rebuild to move extensions in proper location according with chanages
  in last epiphany
- rss, greasemonkey and gestures extensions enabled
- another fixes of gtk deprecations from upstream

* Sun Apr 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt2
- replaced obsolete gtk symbols

* Thu Apr 01 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Feb 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Fri Jan 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Wed Dec 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 28 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt3
- relaxed dependence on epiphany

* Sat Sep 26 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- fixed linking

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Thu Sep 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Tue Aug 25 2009 Alexey Shabalin <shaba@altlinux.ru> 2.27.91-alt1
- 2.27.91

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Mar 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.91-alt1
- 2.25.91

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Tue Dec 09 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- removed obsolete {update,clean}_scrollkeeper
- requires python-module-pygtk >= 2.13.0

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Tue Sep 23 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Sat Sep 06 2008 Yuri N. Sedunov <aris@altlinux.org> 2.23.91-alt1
- new version

* Wed May 28 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Wed Apr 09 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.1-alt1
- 2.22.1

* Thu Mar 13 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Mon Jan 14 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.3-alt1
- 2.20.3

* Fri Oct 19 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.1-alt1
- 2.20.1

* Thu Sep 20 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.0-alt1
- 2.20.0

* Mon Aug 20 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.3-alt1
- 2.18.3

* Sat Jun 16 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.2-alt1
- 2.18.2

* Thu Apr 26 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.1-alt1
- 2.18.1

* Mon Mar 12 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.0-alt0.1
- 2.18.0

* Wed Mar 07 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.17.92-alt0.1
- 2.17.92 (!!!WARNING!!! this is an experimental build)

* Mon Nov 27 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.1-alt3
- Rebuild with new epiphany and firefox

* Mon Oct 09 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.1-alt1
- 2.16.1

* Thu Sep 07 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.0-alt1
- 2.16.0

* Tue Aug 15 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.1.1-alt2
- Rebuild with new epiphany and mozilla

* Thu Jun 01 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.1.1-alt1
- 2.14.1.1

* Fri Apr 14 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.1-alt1
- 2.14.1

* Tue Mar 14 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.0.1-alt2
- ChangeLog corrected

* Mon Mar 13 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.0.1-alt1
- 2.14.0.1

* Tue Mar 07 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.9.7-alt2
- Disable --as-needed flag for linker

* Wed Feb 15 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.9.7-alt1
- 1.9.7

* Fri Dec 02 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Fri Oct 28 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.8.1-alt2
- Rebuild with python support

* Mon Oct 03 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Tue Sep 13 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.8.0-alt3
- 1.8.0

* Sat Apr 23 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Sat Apr 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Fri Mar 04 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.5.8-alt1
- 1.5.8

* Fri Jan 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Thu Dec 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.4.3-alt1
- first build for Sisyphus.

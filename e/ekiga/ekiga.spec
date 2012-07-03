%define req_ptlib_ver	2.8.3
%define req_opal_ver	3.8.3

Name: ekiga
Version: 3.3.0
Release: alt2

Summary: IP phone client with full SIP and H.323 support

License: GPL
Group: Networking/Chat
Url: http://www.ekiga.org

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: gnomemeeting
Obsoletes: gnomemeeting
Requires: libpt >= %req_ptlib_ver libopal >= %req_opal_ver libpt-plugins

# Source-git: git://git.gnome.org/ekiga
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): libGConf-devel
BuildRequires: libpt-devel >= %req_ptlib_ver libopal-devel >= %req_opal_ver
BuildRequires: GConf boost-signals-devel evolution-data-server-devel gcc-c++ gnome-doc-utils intltool libXv-devel
BuildRequires: libavahi-glib-devel libdbus-glib-devel libldap-devel libnotify-devel libsasl2-devel python-modules-compiler
BuildPreReq: libgtk+2-devel

%description
Ekiga is an IP phone client with full SIP and H.323 support.

%prep
%setup -q
%patch -p1

%build
gnome-doc-prepare -f
%autoreconf
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper \
	--enable-dbus
%make_build

%install
%makeinstall_std

%find_lang %name --with-gnome

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%doc README FAQ AUTHORS TODO
%_sysconfdir/gconf/schemas/*.schemas
%_bindir/%{name}*
%dir %_libdir/%name
%dir %_libdir/%name/%version
%_libdir/%name/%version/*.so
%_libdir/%name/%version/*.la
%dir %_libdir/%name/%version/plugins
%_libdir/%name/%version/plugins/*.so
%_libdir/%name/%version/plugins/*.la
%_datadir/dbus-1/services/*
%_datadir/sounds/%name
%_desktopdir/*.desktop
%_pixmapsdir/%name
%_iconsdir/hicolor/16x16/apps/%name.png
%_iconsdir/hicolor/22x22/apps/%name.png
%_iconsdir/hicolor/24x24/apps/%name.png
%_iconsdir/hicolor/32x32/apps/%name.png
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%_iconsdir/hicolor/72x72/apps/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png
%_man1dir/*.1*

%changelog
* Fri Apr 06 2012 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt2
- cleanup spec and build to Sisyphus again

* Fri Jul 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.1
- Rebuilt with Boost 1.47.0

* Tue Mar 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Mon Oct 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.2.7-alt3
- rebuild with evolution-data-server-2.32

* Mon Jun 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.2.7-alt2
- rebuild with libedataserver-1.2.so.13

* Tue Jun 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.2.7-alt1
- 3.2.7

* Tue Sep 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.2.6-alt1
- 3.2.6

* Tue Sep 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.2.5-alt2
- rebuild with libldap2.4

* Tue Jul 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.2.5-alt1
- 3.2.5

* Wed Jun 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.2.4-alt1
- 3.2.4

* Wed May 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.2.3-alt1
- 3.2.3

* Mon May 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.2.0-alt2
- fixed build

* Sun Apr 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.2.0-alt1
- 3.2.0

* Tue Jan 13 2009 Vitaly Lipatov <lav@altlinux.ru> 3.0.2-alt1
- new version 3.0.2 (with rpmrb script)
- remove gnome/help and omf from files (already in name.lang)

* Tue Nov 18 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- new version 3.0.1 (with rpmrb script)
- update buildreq

* Wed Apr 23 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.12-alt1
- new version 2.0.12 (with rpmrb script) - close bug #15439
- update summary (fix bug #12744)

* Tue Oct 09 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.11-alt1
- new version 2.0.11 (with rpmrb script)

* Tue Sep 18 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.10-alt1
- new version 2.0.10 (with rpmrb script)

* Mon Sep 03 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.9-alt3
- rebuild with new libedataserver

* Sun Jun 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.9-alt2
- fix build: add --disable-scrollkeeper

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.9-alt1
- new version 2.0.9 (with rpmrb script)
- needed updated libpw, libopal, update buildreq

* Sun Mar 11 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.7-alt1
- new version 2.0.7
- bzip ChangeLog

* Sat Feb 17 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version (2.0.5)
- update buildreq, enable dbus support

* Fri Oct 13 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt0.1cvs20061012
- new snapshot

* Tue Aug 08 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt0.3cvs20060808
- new snapshot

* Sun Jul 23 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt0.3cvs20060723
- new snapshot

* Wed Jun 07 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt0.2cvs20060603
- new snapshot (2.0.2)

* Thu May 25 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt0.2cvs20060520
- snapshot from 20060520, build with correct libopal

* Wed May 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt0.1cvs20060521
- new snapshot

* Tue May 16 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt0.1cvs20060515
- new snapshot

* Thu Apr 13 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt0.1cvs20060413
- new snapshot
- do not require scrollkeeper

* Tue Feb 28 2006 Vitaly Lipatov <lav@altlinux.ru> 1.99.1-alt0.1cvs20060228
- new snapshot (thanks to Yuri)

* Sat Feb 25 2006 Yuri N. Sedunov <aris@altlinux.ru> 1.99.1-alt0.2
- current cvs snapshot

* Tue Feb 14 2006 Vitaly Lipatov <lav@altlinux.ru> 1.99.1-alt0.1
- new version (2.0 BETA 2)
- remove generic INSTALL

* Sat Jan 21 2006 Vitaly Lipatov <lav@altlinux.ru> 1.99.0-alt0.1
- prerelease (was gnomemeeting)

* Sat Jan 07 2006 Vitaly Lipatov <lav@altlinux.ru> 1.9.9-alt0.1cvs20060107
- new version

* Fri Sep 09 2005 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt0.1
- new version (D-BUS disabled)

* Thu Jul 28 2005 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt4
- disable dbus using (due incompatible new API in dbus)

* Fri May 27 2005 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt3
- fix dbus build requires

* Mon May 02 2005 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- fix libpw-plugins requires

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version (patches from FC3)

* Mon Feb 07 2005 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version
- disable howl (there is too old version in Sisyphus)

* Tue Jun 15 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.2-alt1.2
- NMU: remove support for old alternatives
  (this alternatives wasn't work)

* Fri Jun 11 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1.1
- rebuild with correct libopenh323
- change group to Chat

* Sat May 22 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version
- add require to needed version of libxml2
- remove COPYING from doc

* Sat Jan 03 2004 Vitaly Lipatov <lav@altlinux.ru> 0.98.5-alt1
- new version
- build with gcc3.3

* Tue Mar 25 2003 Vitaly Lipatov <lav@altlinux.ru> 0.96.1-alt1
- new version

* Wed Dec 04 2002 Vitaly Lipatov <lav@altlinux.ru> 0.94.1-alt3
- rebuild with libpw
- remove directfb requires
- add generic name to menu
- spec cleanup

* Sun Dec 01 2002 Vitaly Lipatov <lav@altlinux.ru> 0.94.1-alt2
- rebuild with libspeex

* Sun Nov 24 2002 Vitaly Lipatov <lav@altlinux.ru> 0.94.1-alt1
- new version 0.94.1
- new icons
- move to the video group
- several new fixes/adaptions (from Fri Oct 25 2002 Florin <florin@mandrakesoft.com> 0.94-0.1.1mdk)
- adapted for pwlib (libpwlib), openh323 (libopenh323)
- spec cleanup, summary and description are translated in russian
- Speex codec support exist but temporary disabled
- updated ru.po from Leon Kanter <leon@asplinux.ru>

* Tue Nov 12 2002 AEN <aen@altlinux.ru> 0.93.1-alt3
- rebuilt with new directfb

* Wed Oct 09 2002 AEN <aen@altlinux.ru> 0.93.1-alt2
- spec file cleanup

* Tue Oct 08 2002 AEN <aen@altlinux.ru> 0.93.1-alt1
- new version

* Wed Mar 13 2002 AEN <aen@logic.ru> 0.85.1-alt1
- new version

* Tue Jan 08 2002 AEN <aen@logic.ru> 0.12.2-alt1
- new version

* Wed Oct 10 2001 AEN <aen@logic.ru> 0.11-alt1
- first build for Sisyphus

* Wed Sep 19 2001 Florin <florin@mandrakesoft.com> 0.11-1mdk
- 0.11

* Mon Sep 17 2001 Stefan van der Eijk <stefan@eijk.nu> 0.11-0.PRE3.3mdk
- BuildRequires: gettext-devel
- Remove redundant BuildRequires

* Wed Sep 12 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.11-0.PRE3.2mdk
- added dynamic desktop entry

* Sun Aug 26 2001 Florin <florin@mandrakesoft.com> 0.11-0.PRE3.1mdk
- update the versions in Requires & Buildrequires sections
- use %_includedir/openh323 instead of %_includedir/oh323
- use -lh323_linux_x86_r instead if -loh323
- 0.11PRE3

* Sun Aug 26 2001 Florin <florin@mandrakesoft.com> 0.10-8mdk
- add the versions in the Require section
- fix the permissions of some doc files

* Mon Aug 20 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.10-7mdk
- Fix menu entry for applet support
- Add missing directory

* Mon Aug 20 2001 Florin <florin@mandrakesoft.com> 0.10-6mdk
- rebuild due too pwlib fixes

* Sun Aug 19 2001 Florin <florin@mandrakesoft.com> 0.10-5mdk
- update the xpm icons

* Sun Aug 19 2001 Florin <florin@mandrakesoft.com> 0.10-4mdk
- new modified sources

* Sat Aug 18 2001 Florin <florin@mandrakesoft.com> 0.10-3mdk
- slighlty modified sources
- use the new PTLIB_INCLUDE_DIR & OPENH323_INCLUDE_DIR var
- don't need the old patches anymore
- add the ptlib patch because of pwlib

* Thu Aug 16 2001 Florin <florin@mandrakesoft.com> 0.10-2mdk
- added patches (more elegant)

* Tue Aug 14 2001 Florin <florin@mandrakesoft.com> 0.10-1mdk
- first Mandrake release

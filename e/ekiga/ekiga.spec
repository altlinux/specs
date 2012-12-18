
Name: ekiga
Version: 4.0.0
Release: alt1

Summary: IP phone client with full SIP and H.323 support

License: GPL
Group: Networking/Instant messaging
Url: http://www.ekiga.org

Provides: gnomemeeting
Obsoletes: gnomemeeting
Requires: libpt libopal libpt-plugins

# Source-git: git://git.gnome.org/ekiga
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%define ptlib_ver 2.10.9
%define opal_ver 3.10.9

%def_enable gconf
%def_enable eds
%def_enable notify
%def_enable ldap
%def_enable xv
%def_enable dbus
%def_enable dbus_service
%def_enable avahi
%def_enable gstreamer
%def_enable xcap
%def_enable loudmouth
%def_enable gdu

BuildRequires: intltool gcc-c++
BuildRequires: pkgconfig(gtk+-2.0) >= 2.20.0 pkgconfig(gnome-icon-theme) >= 3.0.0
BuildRequires: pkgconfig(glib-2.0) >= 2.24.0 pkgconfig(gmodule-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0)
BuildRequires: boost-signals-devel
BuildRequires: pkgconfig(libxml-2.0)
%{?_enable_gconf:BuildRequires: pkgconfig(gconf-2.0) >= 2.6.0}
%{?_enable_eds:BuildRequires: pkgconfig(libebook-1.2)}
%{?_enable_notify:BuildRequires: pkgconfig(libnotify)}
%{?_enable_ldap:BuildRequires: libldap-devel}
BuildRequires: libsasl2-devel
%{?_enable_xv:BuildRequires: pkgconfig(xv)}
%{?_enable_dbus:BuildRequires: pkgconfig(dbus-1) >= 0.36 pkgconfig(dbus-glib-1) >= 0.36}
BuildRequires: libv4l-devel
%{?_enable_avahi:BuildRequires: pkgconfig(avahi-client) >= 0.6 pkgconfig(avahi-glib) >= 0.6}
%{?_enable_gstreamer:BuildRequires: pkgconfig(gstreamer-plugins-base-0.10) >= 0.10.21.3 pkgconfig(gstreamer-interfaces-0.10) pkgconfig(gstreamer-app-0.10)}
%{?_enable_xcap:BuildRequires: pkgconfig(libsoup-2.4)}
%{?_enable_loudmouth:BuildRequires: pkgconfig(loudmouth-1.0)}
%{?_enable_gdu:BuildRequires: /usr/bin/scrollkeeper-config gnome-doc-utils}
BuildRequires: pkgconfig(ptlib) >= %ptlib_ver
BuildRequires: pkgconfig(opal) >= %opal_ver

%description
Ekiga is an IP phone client with full SIP and H.323 support.

%package plugin-avahi
Summary: Avahi(mDNS) Support for Ekiga
Group: Networking/Instant messaging
Requires: %name = %version-%release

%description plugin-avahi
Avahi(mDNS) Support for Ekiga.

%package plugin-evolution
Summary: Evolution-data-server addressbook support for Ekiga
Group: Networking/Instant messaging
Requires: %name = %version-%release

%description plugin-evolution
Evolution-data-server addressbook support for Ekiga.

%package plugin-gstreamer
Summary: GStreamer support for Ekiga
Group: Networking/Instant messaging
Requires: %name = %version-%release

%description plugin-gstreamer
GStreamer support for Ekiga.

%package plugin-ldap
Summary: LDAP addressbook support for Ekiga
Group: Networking/Instant messaging
Requires: %name = %version-%release

%description plugin-ldap
LDAP addressbook support for Ekiga.

%package plugin-notify
Summary: Libnotify support for Ekiga
Group: Networking/Instant messaging
Requires: %name = %version-%release

%description plugin-notify
libnotify support for Ekiga.

%package plugin-xmpp
Summary: Experimental Loudmouth support for Ekiga
Group: Networking/Instant messaging
Requires: %name = %version-%release

%description plugin-xmpp
experimental Loudmouth support for Ekiga.

%package plugin-xcap
Summary: experimental XCAP support for Ekiga
Group: Networking/Instant messaging
Requires: %name = %version-%release

%description plugin-xcap
experimental XCAP support for Ekiga.

%package plugins
Summary: All plugins for Ekiga
Group: Networking/Instant messaging
%{?_enable_avahi:Requires: %name-plugin-avahi = %version-%release}
%{?_enable_eds:Requires: %name-plugin-evolution = %version-%release}
%{?_enable_gstreamer:Requires: %name-plugin-gstreamer = %version-%release}
%{?_enable_ldap:Requires: %name-plugin-ldap = %version-%release}
%{?_enable_notify:Requires: %name-plugin-notify = %version-%release}
%{?_enable_loudmouth:Requires: %name-plugin-xmpp = %version-%release}
%{?_enable_xcap:Requires: %name-plugin-xcap = %version-%release}

%description plugins
All for Ekiga.

%prep
%setup -q
%patch -p1

%build
gnome-doc-prepare -f
%autoreconf
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper \
	%{subst_enable gconf} \
	%{subst_enable eds} \
	%{subst_enable notify} \
	%{subst_enable ldap} \
	%{subst_enable xv} \
	%{subst_enable dbus} \
	%{?_enable_dbus_service:--enable-dbus-service} \
	%{subst_enable avahi} \
	%{subst_enable gstreamer} \
	%{subst_enable xcap} \
	%{subst_enable loudmouth} \
	%{subst_enable gdu}

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
%dir %_libdir/%name/%version/plugins
%_datadir/dbus-1/services/*
%_datadir/sounds/%name
%_desktopdir/*.desktop
%_pixmapsdir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/*.1*

%exclude %_libdir/%name/%version/*.la
%exclude %_libdir/%name/%version/plugins/*.la


%if_enabled avahi
%files plugin-avahi
%_libdir/%name/%version/plugins/libgmavahi.so
%endif

%if_enabled eds
%files plugin-evolution
%_libdir/%name/%version/plugins/libgmevolution.so
%endif

%if_enabled gstreamer
%files plugin-gstreamer
%_libdir/%name/%version/plugins/libgmgstreamer.so
%endif

%if_enabled ldap
%files plugin-ldap
%_libdir/%name/%version/plugins/libgmldap.so
%endif

%if_enabled notify
%files plugin-notify
%_libdir/%name/%version/plugins/libgmlibnotify.so
%endif

%if_enabled loudmouth
%files plugin-xmpp
%_libdir/%name/%version/plugins/libgmloudmouth.so
%endif

%if_enabled xcap
%files plugin-xcap
%_libdir/%name/%version/plugins/libgmresource_list.so
%_libdir/%name/%version/plugins/libgmxcap.so
%endif

%files plugins

%changelog
* Mon Dec 17 2012 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1
- 4.0.0
- move plugins to separate packages

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt2.2
- Rebuilt with Boost 1.51.0

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt2.1
- Fixed build

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

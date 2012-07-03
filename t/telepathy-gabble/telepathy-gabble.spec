%def_enable voip
%def_enable ft

Name: telepathy-gabble
Version: 0.16.0
Release: alt1

Summary: Jabber/XMPP connection manager
License: LGPL
Group: Networking/Instant messaging
Url: http://telepathy.freedesktop.org/

Source: http://telepathy.freedesktop.org/releases/telepathy-gabble/%name-%version.tar.gz

%define telepathy_glib_ver 0.18.0
%define glib_ver 2.24

Requires: ca-certificates

BuildPreReq: libtelepathy-glib-devel >= %telepathy_glib_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildRequires: libdbus-devel libdbus-glib-devel libxml2-devel libnice-devel
BuildRequires: libsoup-devel xsltproc libsqlite3-devel libgnutls-devel libgcrypt-devel gtk-doc
BuildRequires: python-module-twisted-words python-module-xmpp
# for tests
BuildRequires: /proc dbus-tools-gui python-module-dbus python-module-twisted-web python-module-twisted-core-gui

%description
Gabble is a Jabber/XMPP connection manager for the Telepathy framework,
currently supporting single user chats, multi user chats and voice/video
calls. Install this package to use Telepathy instant messaging clients
with Jabber/XMPP servers, including Google Talk.

%prep
%setup -q

%build
%autoreconf
%configure \
	--disable-static \
	%{subst_enable voip} \
	%{subst_enable ft} \
	--with-ca-certificates="%_datadir/ca-certificates/ca-bundle.crt"
%make_build

%install
%make_build DESTDIR=%buildroot install

%check
# jingle/call-codecoffer.py failed (1 of 233)
#%%make check

%files
%_bindir/telepathy-gabble-xmpp-console
%_libexecdir/telepathy-gabble
%dir %_libdir/telepathy/gabble-0/
%dir %_libdir/telepathy/gabble-0/lib/
%_libdir/telepathy/gabble-0/lib/libgabble-plugins.so
%_libdir/telepathy/gabble-0/lib/libgabble-plugins-%version.so
%_libdir/telepathy/gabble-0/lib/libwocky-telepathy-gabble-%version.so
%_libdir/telepathy/gabble-0/lib/libwocky.so
%dir %_libdir/telepathy/gabble-0/plugins
%_libdir/telepathy/gabble-0/plugins/libgateways.so
%_libdir/telepathy/gabble-0/plugins/libconsole.so
%_datadir/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.gabble.service
%_datadir/telepathy/managers/gabble.manager
%_man8dir/*
%dir %_datadir/doc/telepathy-gabble
%doc %_datadir/doc/telepathy-gabble/*.html
%doc AUTHORS NEWS README

%exclude %_libdir/telepathy/gabble-0/*/*.la

%changelog
* Tue Apr 03 2012 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Fri Mar 23 2012 Yuri N. Sedunov <aris@altlinux.org> 0.15.5-alt1
- 0.15.5

* Sun Nov 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Thu Oct 27 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.7-alt1
- 0.12.7

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.6-alt1
- 0.12.6

* Wed Aug 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- 0.12.4

* Wed Jun 29 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- 0.12.3

* Wed Jun 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.2-alt1
- 0.12.2

* Thu Jun 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Sun Mar 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.5-alt1
- 0.10.5
- updated buildreqs

* Thu Nov 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.4-alt1
- 0.10.4

* Wed Jun 09 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.14-alt1
- 0.8.14

* Wed Apr 21 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.13-alt1
- 0.8.13

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.12-alt1
- 0.8.12

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.11-alt1
- 0.8.11

* Sat Jan 30 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.10-alt1
- 0.8.10

* Thu Jan 07 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.9-alt1
- 0.8.9

* Mon Sep 14 2009 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3

* Sun May 17 2009 Yuri N. Sedunov <aris@altlinux.org> 0.7.27-alt1
- 0.7.27

* Thu Jan 29 2009 Yuri N. Sedunov <aris@altlinux.org> 0.7.19-alt1
- new version

* Sun Jan 18 2009 Yuri N. Sedunov <aris@altlinux.org> 0.7.18-alt1
- 0.7.18

* Thu Dec 18 2008 Yuri N. Sedunov <aris@altlinux.org> 0.7.17-alt1
- 0.7.17

* Tue Dec 02 2008 Yuri N. Sedunov <aris@altlinux.org> 0.7.16-alt1
- 0.7.16
- updated buildreqs

* Mon Dec 01 2008 Yuri N. Sedunov <aris@altlinux.org> 0.7.15-alt2
- updated buildreqs

* Sun Nov 09 2008 Yuri N. Sedunov <aris@altlinux.org> 0.7.15-alt1
- 0.7.15

* Wed May 14 2008 Igor Zubkov <icesik@altlinux.org> 0.7.6-alt1
- 0.7.5 -> 0.7.6

* Sat May 10 2008 Igor Zubkov <icesik@altlinux.org> 0.7.5-alt1
- 0.7.4 -> 0.7.5

* Fri May 02 2008 Igor Zubkov <icesik@altlinux.org> 0.7.4-alt1
- 0.7.3 -> 0.7.4

* Wed Apr 30 2008 Igor Zubkov <icesik@altlinux.org> 0.7.3-alt1
- 0.7.2 -> 0.7.3

* Mon Apr 28 2008 Igor Zubkov <icesik@altlinux.org> 0.7.2-alt2
- fix rebuild

* Thu Jan 24 2008 Igor Zubkov <icesik@altlinux.org> 0.7.2-alt1
- 0.7.1 -> 0.7.2

* Mon Dec 24 2007 Igor Zubkov <icesik@altlinux.org> 0.7.1-alt3
- rebuild with new dbus

* Fri Dec 07 2007 Igor Zubkov <icesik@altlinux.org> 0.7.1-alt2
- fix build on x86_64

* Wed Dec 05 2007 Igor Zubkov <icesik@altlinux.org> 0.7.1-alt1
- 0.7.0 -> 0.7.1

* Wed Dec 05 2007 Igor Zubkov <icesik@altlinux.org> 0.7.0-alt1
- 0.6.1 -> 0.7.0
- buildreq

* Wed Nov 07 2007 Igor Zubkov <icesik@altlinux.org> 0.6.1-alt1
- 0.6.0 -> 0.6.1

* Fri Sep 28 2007 Igor Zubkov <icesik@altlinux.org> 0.6.0-alt1
- 0.5.14 -> 0.6.0

* Fri Sep 07 2007 Igor Zubkov <icesik@altlinux.org> 0.5.14-alt1
- 0.5.13 -> 0.5.14

* Thu Sep 06 2007 Igor Zubkov <icesik@altlinux.org> 0.5.13-alt1
- 0.5.12 -> 0.5.13

* Fri Jun 22 2007 Igor Zubkov <icesik@altlinux.org> 0.5.12-alt1
- build for Sisyphus



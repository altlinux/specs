#%%set_verify_elf_method unresolved=relaxed

Name: telepathy-salut
Version: 0.8.0
Release: alt1

Summary: A link-local XMPP connection manager
License: LGPLv2.1+
Group: Networking/Instant messaging
Url: http://telepathy.freedesktop.org/

Source: http://telepathy.freedesktop.org/releases/%name/%name-%version.tar.gz

BuildPreReq: libtelepathy-glib-devel >= 0.17.5
BuildRequires: gtk-doc libasyncns-devel libavahi-gobject-devel libdbus-glib-devel
BuildRequires: libsasl2-devel libsoup-devel libxml2-devel python-module-PyXML valgrind
BuildRequires: libgnutls-devel libgcrypt-devel libsqlite3-devel libcheck-devel libuuid-devel

# for check
BuildRequires: /proc dbus-tools-gui python-module-twisted-web python-module-twisted-words
BuildRequires: python-module-avahi python-module-twisted-core-gui

%description
A link-local XMPP connection manager for telepathy.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%check
# avahi/file-transfer/send-file-declined.py fails in hasher
#%%make check

%install
%make_install DESTDIR=%buildroot install

rm -rf %buildroot%_docdir/%name/

%files
%_libexecdir/%name
%dir %_libdir/telepathy/salut-0
%dir %_libdir/telepathy/salut-0/lib
%_libdir/telepathy/salut-0/lib/*.so
%dir %_libdir/telepathy/salut-0/plugins
%_man8dir/*
%_datadir/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.salut.service
%_datadir/telepathy/managers/salut.manager
%doc AUTHORS NEWS docs/clique.html

%exclude %_libdir/telepathy/salut-0/lib/*.la

%changelog
* Wed Apr 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed Mar 28 2012 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Sun Mar 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Fri Sep 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.13-alt1
- 0.3.13

* Mon May 24 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.12-alt1
- 0.3.12

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.11-alt1
- 0.3.11

* Mon Apr 27 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- 0.3.9

* Sun Jan 18 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- 0.3.7

* Tue Dec 02 2008 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- 0.3.6

* Sun Nov 09 2008 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- 0.3.5

* Thu Jun 05 2008 Igor Zubkov <icesik@altlinux.org> 0.3.3-alt1
- 0.3.2 -> 0.3.3

* Thu May 22 2008 Igor Zubkov <icesik@altlinux.org> 0.3.2-alt1
- 0.2.1 -> 0.3.2

* Mon Apr 28 2008 Igor Zubkov <icesik@altlinux.org> 0.2.1-alt2
- fix rebuild

* Tue Jan 15 2008 Igor Zubkov <icesik@altlinux.org> 0.2.1-alt1
- 0.1.11 -> 0.2.1

* Mon Dec 24 2007 Igor Zubkov <icesik@altlinux.org> 0.1.11-alt2
- rebuild with new dbus

* Wed Dec 05 2007 Igor Zubkov <icesik@altlinux.org> 0.1.11-alt1
- 0.1.10 -> 0.1.11
- buildreq

* Tue Nov 27 2007 Igor Zubkov <icesik@altlinux.org> 0.1.10-alt1
- 0.1.9 -> 0.1.10

* Thu Nov 15 2007 Igor Zubkov <icesik@altlinux.org> 0.1.9-alt1
- 0.1.8 -> 0.1.9

* Wed Nov 14 2007 Igor Zubkov <icesik@altlinux.org> 0.1.8-alt1
- 0.1.7 -> 0.1.8

* Mon Nov 12 2007 Igor Zubkov <icesik@altlinux.org> 0.1.7-alt1
- 0.1.6 -> 0.1.7

* Wed Nov 07 2007 Igor Zubkov <icesik@altlinux.org> 0.1.6-alt1
- 0.1.5 -> 0.1.6

* Wed Sep 26 2007 Igor Zubkov <icesik@altlinux.org> 0.1.5-alt1
- 0.1.3 -> 0.1.5

* Thu Jul 12 2007 Igor Zubkov <icesik@altlinux.org> 0.1.3-alt1
- build for Sisyphus



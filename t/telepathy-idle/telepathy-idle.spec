Name: telepathy-idle
Version: 0.2.0
Release: alt1

Summary: A full-featured IRC connection manager
License: LGPL
Group: Networking/Instant messaging
Url: http://telepathy.freedesktop.org/

Source: http://telepathy.freedesktop.org/releases/telepathy-idle/%name-%version.tar.gz

# Automatically added by buildreq on Wed Aug 26 2009
BuildRequires: libgio-devel >= 2.32.0
BuildRequires: libtelepathy-glib-devel >= 0.22.0
BuildRequires: libdbus-glib-devel libssl-devel
BuildRequires: python-module-twisted-words python-module-xmpp xsltproc

%description
A full-featured IRC connection manager for telepathy.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libexecdir/%name
%_datadir/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.idle.service
%_datadir/telepathy/managers/idle.manager
%_man8dir/*
%doc AUTHORS NEWS

%changelog
* Thu Oct 03 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.17-alt1
- 0.1.17

* Tue May 07 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.16-alt1
- 0.1.16

* Thu Feb 28 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.14-alt1
- 0.1.14

* Sat Oct 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.12-alt1
- 0.1.12

* Sun Nov 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.11-alt1
- 0.1.11

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.10-alt1
- 0.1.10

* Mon Mar 14 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt1
- 0.1.8

* Sat Dec 11 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt2
- updated buildreqs

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Wed Aug 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- 0.1.4

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.1.2-alt2.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Mon Apr 28 2008 Igor Zubkov <icesik@altlinux.org> 0.1.2-alt2
- fix rebuild

* Sat Sep 29 2007 Igor Zubkov <icesik@altlinux.org> 0.1.2-alt1
- 0.1.1 -> 0.1.2

* Wed Jul 11 2007 Igor Zubkov <icesik@altlinux.org> 0.1.1-alt1
- build for Sisyphus


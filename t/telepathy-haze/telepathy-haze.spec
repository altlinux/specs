Name: telepathy-haze
Version: 0.6.0
Release: alt1

Summary: a connection manager built around libpurple
License: GPL v2 or later
Group: Networking/Instant messaging
Url: http://developer.pidgin.im/wiki/TelepathyHaze

Source: http://telepathy.freedesktop.org/releases/%name/%name-%version.tar.gz

BuildPreReq: glib2-devel >= 2.22 libgio-devel libdbus-glib-devel >= 0.73
BuildRequires: libpurple-devel >= 2.7.0 libtelepathy-glib-devel >= 0.13.9
# for check:
BuildRequires: python-module-twisted-words python-module-twisted-core-gui

%description
telepathy-haze is a connection manager built around libpurple, the
core of Pidgin (formerly Gaim), as a Summer of Code project under the
Pidgin umbrella.  Ultimately, any protocol supported by libpurple will
be supported by telepathy-haze; for now, XMPP, MSN and AIM are known to
work acceptably, and others will probably work too.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%check
%make check

%files
%doc AUTHORS NEWS
%_libexecdir/%name
%_man8dir/*
%_datadir/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.haze.service

%changelog
* Thu Apr 05 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Wed Aug 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt2
- fixed freedesktop.org bugs ##30475, 30594
- %%check section temporarily disabled

* Fri Sep 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Sun Aug 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- 0.3.6

* Sun Aug 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt2
- python-module-twisted-core-gui added to buldreqs

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- 0.3.5

* Fri Mar 05 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4

* Thu Jan 28 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Thu Jan 07 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Mon Apr 27 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Sun Nov 09 2008 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Mon Jul 14 2008 Igor Zubkov <icesik@altlinux.org> 0.2.0.1-alt3
- fix build on x86_64

* Mon May 26 2008 Igor Zubkov <icesik@altlinux.org> 0.2.0.1-alt2
- fix build

* Thu May 01 2008 Igor Zubkov <icesik@altlinux.org> 0.2.0.1-alt1
- 0.2.0 -> 0.2.0.1

* Sat Feb 23 2008 Igor Zubkov <icesik@altlinux.org> 0.2.0-alt1
- 0.1.4 -> 0.2.0

* Sat Nov 24 2007 Igor Zubkov <icesik@altlinux.org> 0.1.4-alt1
- 0.1.3 -> 0.1.4

* Fri Nov 16 2007 Igor Zubkov <icesik@altlinux.org> 0.1.3-alt1
- 0.1.2 -> 0.1.3

* Mon Sep 17 2007 Igor Zubkov <icesik@altlinux.org> 0.1.2-alt1
- 0.1.1 -> 0.1.2

* Fri Aug 24 2007 Igor Zubkov <icesik@altlinux.org> 0.1.1-alt2
- fix file conflict with empathy

* Sat Aug 18 2007 Igor Zubkov <icesik@altlinux.org> 0.1.1-alt1
- build for Sisyphus


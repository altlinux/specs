Name: tclock
Version: 1.0.2
Release: alt1

Summary: Simple transparent X11 analog clock
Group: Monitoring
License: BSD

Source: %name-%version.tar

Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: imake libX11-devel libXext-devel xorg-cf-files

%description
Simple transparent X11 analog clock showing no numbers but 12 stones.
Stones and arrow geometry is configurable.

%prep
%setup

%build
xmkmf
%make

%install
%make_install install install.man DESTDIR="$RPM_BUILD_ROOT"

%files
%_x11bindir/%name
%_x11mandir/man?/%name.*

%changelog
* Wed Jun 17 2026 Fr. Br. George <george@altlinux.org> 1.0.2-alt1
- Incorporate patches.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.1-alt5.qa1
- NMU: rebuilt for debuginfo.

* Tue Dec 02 2008 Fr. Br. George <george@altlinux.ru> 1.0.1-alt5
- libXext-devel added

* Fri Nov 17 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt4
- sigsuspend() is used instead of sigpause()

* Mon Oct 09 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt3
- GEAR adatped
- Moved from /usr/X11R6

* Fri Jan 23 2004 Fr. Br. George <george@altlinux.ru> 1.0.1-alt2
- Automatical generated libX* dependencies removed

* Fri Oct 31 2003 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- ALT Linux port


Name: tclock
Version: 1.0.1
Release: alt5

Summary: Simple transparent X11 analog clock
Group: Monitoring
License: BSD

Source: ftp://ftp.uni-potsdam.de/pub/X11/tools/clocks/%name-%version.tar.Z

Patch0: %name.FreeBSD.patch
Patch1: %name.sigsuspend.patch

Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: imake libX11-devel libXext-devel xorg-cf-files

%description
Simple transparent X11 analog clock showing no numbers but 12 stones.
Stones and arrow geometry is configurable.

%prep
%setup -cq
%patch0 -p0
%patch1 -p1

%build
# Can't build both 2.0.x/2.1.x memstat modules
xmkmf
%make

%install
%make_install install install.man DESTDIR="$RPM_BUILD_ROOT"

%files
%_x11bindir/%name
%_x11mandir/man?/%name.*

%changelog
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


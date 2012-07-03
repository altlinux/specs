Name: xman
Version: 1.1.2
Release: alt1
Summary: Manual page display program for the X Window System
Group: System/X11
Source: %name-%version.tar.bz2
# Fix xman to work with bzipped pages
License: MIT
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel pkg-config xorg-xproto-devel
BuildRequires: libXaw-devel

BuildRequires: libXaw-devel xorg-util-macros

%description
Xman is a manual page display program for the X Window System.

%prep
%setup -n %name-%version

%build
%autoreconf
%configure --disable-xprint
%make

%install
%make install DESTDIR=%buildroot

%files
%_bindir/xman
%_datadir/X11/xman.help
%_x11appconfdir/Xman
%_mandir/man1/xman.1.gz

%changelog
* Fri Jul 01 2011 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1.1
- Recalculate buildreq

* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Thu Sep 23 2010 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Autobuild version bump to 1.1.0

* Tue Aug 25 2009 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Version up

* Sat Nov 29 2008 Fr. Br. George <george@altlinux.ru> 1.0.2-alt3
- Sync with upstream up to aw7 downgrade patch

* Sat Oct 21 2006 Fr. Br. George <george@altlinux.ru> 1.0.2-alt2
- __autoreconf added to correct manpage extension

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Initial build from MDV

* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 21:09:36 (59517)
- rebuild to fix libXaw.so.8 dependency

* Tue Jun 06 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-06-06 19:37:48 (36717)
- added patch: support man pages compressed using bzip2

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 22:34:52 (31402)
- fill in more missing descriptions

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

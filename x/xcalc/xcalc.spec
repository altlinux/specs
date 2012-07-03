Name: xcalc
Version: 1.0.4.1
Release: alt1.1
Summary: Scientific calculator for X
Group: System/X11
Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
License: MIT
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel pkg-config xorg-xproto-devel
BuildRequires: libXaw-devel

BuildRequires: libXaw-devel libXt-devel xorg-util-macros

%description
Xcalc is a scientific calculator desktop accessory that can emulate a TI-30
or an HP-10C.

%prep
%setup -q -n %name-%version

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc README
%_bindir/xcalc
%_x11appconfdir/*
%_mandir/man1/xcalc.*

%changelog
* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.0.4.1-alt1.1
- Recalculate buildreq

* Wed Dec 08 2010 Fr. Br. George <george@altlinux.ru> 1.0.4.1-alt1
- Autobuild version bump to 1.0.4.1

* Sun Sep 26 2010 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Fri Nov 21 2008 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Version up
- sync with upstream up to aw7 downgrade patch

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV

* Fri Sep 01 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-09-01 19:22:17 (59409)
- rebuild for libXaw

* Thu Jun 01 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-06-01 20:13:15 (31864)
- fill in missing description & summaries

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 20:32:41 (31747)
- rebuild against new libXaw package

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

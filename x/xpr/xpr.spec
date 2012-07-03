Name: xpr
Version: 1.0.4
Release: alt1
Summary: Dump an X window directly to a printer
Group: System/X11
Source: %name-%version.tar.bz2
Url: http://xorg.freedesktop.org/releases/individual/app/
License: MIT
Packager: Fr. Br. George <george@altlinux.ru>

BuildRequires: libX11-devel
BuildRequires: libXmu-devel
BuildRequires: xorg-util-macros

%description
Xpr takes as input a window dump file produced by xwd(1) and formats it for
output on PostScript printers, the Digital LN03 or LA100, the IBM PP3812 page
printer, the HP LaserJet (or other PCL printers), or the HP PaintJet.

%prep
%setup -n %name-%version

%build
%configure
%make

%install
%make install DESTDIR=%buildroot

%files
%_bindir/*
%_man1dir/*

%changelog
* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Tue Apr 26 2011 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2.1
- Fixed build

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:09:04 (31709)
- fill in a few more missing descriptions

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

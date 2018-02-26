Name: showfont
Version: 1.0.3
Release: alt1.1
Summary: Font dumper for X font server
Group: System/X11
Url: http://cgit.freedesktop.org/xorg/app/showfont
Source: %name-%version.tar.bz2
License: MIT
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Tue May 18 2010
BuildRequires: libFS-devel

BuildRequires: xorg-util-macros

%description
Showfont  displays  data  about  a font that matches the given pattern.
The information shown includes font information, font properties, character
metrics, and character bitmaps.

%prep
%setup -q -n %name-%version

%build
%autoreconf
%configure
%make

%install
%make install DESTDIR=%buildroot

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1.1
- Recalculate buildreq

* Fri Nov 05 2010 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue May 18 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Version up

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Wed May 17 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-17 00:18:30 (27489)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

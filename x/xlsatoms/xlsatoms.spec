Name: xlsatoms
Version: 1.1.1
Release: alt1
Summary: List interned atoms defined on server
Group: System/X11
Source: %name-%version.tar.bz2
License: MIT
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Tue May 18 2010
BuildRequires: libxcb-devel

BuildRequires: xorg-util-macros

%description
Xlsatoms lists the interned atoms.  By default, all atoms starting from 1 (the lowest atom value defined by  the  protocol)  are  listed  until unknown  atom  is  found.  If an explicit range is given, xlsatoms will try all atoms in the range, regardless of whether or not any are  undefined.

%prep
%setup -n %name-%version

%build
%autoreconf
%configure
%make

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*

%changelog
* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1.1
- Recalculate buildreq

* Fri Jun 04 2010 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Version up

* Tue May 18 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- New version

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

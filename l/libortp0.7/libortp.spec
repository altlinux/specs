%define rname ortp
%define libname lib%rname
%define sffx 0.7

Name:		%libname%sffx
Version:	0.7.1
Release:	alt3.1

Group:		Networking/Other
Summary:	oRTP - a Real-time Transport Protocol stack
License:	LGPL

Provides: %libname = %version-%release

Source:		ortp-%version.tar.gz
Patch: libortp0.7-0.7.1-alt-DSO.patch

BuildRequires: gcc-c++ glibc-devel-static pkg-config glib2-devel

%description
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

%package devel
Summary: Headers, libraries and docs for the oRTP library
Group: Development/C
Requires: %name = %version-%release
Requires: glibc-devel
Conflicts: %libname-devel

%description devel
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

This package contains header files and development libraries needed to
develop programs using the oRTP library.

%package devel-static
Summary: Static library build for the oRTP
Group: Development/C
Requires: %name-devel = %version-%release
Conflicts: %libname-devel-static
Requires: glibc-devel-static

%description devel-static
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

This package contains static library build for the oRTP.

%prep
%setup -n %rname-%version
%patch -p2
%autoreconf

%build
%configure \
    --includedir=%_includedir/%rname%sffx \
    --disable-glibtest
%make_build

%install
%make DESTDIR=%buildroot install
rm -rf %buildroot/usr/share/gtk-doc

%files
%_libdir/*.so.*
%doc AUTHORS COPYING NEWS README TODO ChangeLog

%files devel
%_libdir/*.so
%_includedir/*
%doc docs/html
%_libdir/pkgconfig/*.pc

%files devel-static
%_libdir/*.a

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt3.1
- Fixed build

* Tue Dec 07 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt3
- rebuilt

* Fri Aug 31 2007 Sergey V Turchin <zerg at altlinux dot org> 0.7.1-alt2
- rename package
- built with glib2

* Sun Jul 16 2006 Mikhail Yakshin <greycat@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus


Name: libunibreak
Version: 3.0
Release: alt2

Summary: Unicode line-breaking library
License: zlib
Group: System/Libraries
URL: http://vimgadgets.sourceforge.net/libunibreak
Packager: Mikhail Kolchin <mvk@altlinux.org>

Source: %name-%version.tar.gz

# Automatically added by buildreq on Mon Sep 29 2014
BuildRequires: glibc-devel-static

%description
Libunibreak is the successor of liblinebreak, an implementation of the line
breaking algorithm as described in Unicode 6.0.0 Standard Annex 14, Revision
26, available at http://www.unicode.org/reports/tr14/tr14-26.html

It is designed to be used in a generic text renderer. FBReader is one
real-world example, and you may also check some simple sample code, like
showbreak and breaktext.

%package devel
Summary: Development files for libunibreak
Group: Development/C

%description devel
The libunibreak-devel package contains libraries and header files for
developing applications that use libunibreak.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

rm -f %buildroot/%_includedir/*
rm -f %buildroot/%_libdir/*.so
rm -f %buildroot/%_libdir/pkgconfig/%name.pc

%files
%doc AUTHORS ChangeLog LICENCE NEWS README.md
%_libdir/*.so.*

%changelog
* Wed Nov 08 2023 Sergey V Turchin <zerg@altlinux.org> 3.0-alt2
- don't package devel files

* Tue Jul 28 2015 Mikhail Kolchin <mvk@altlinux.org> 3.0-alt1
- new version

* Mon Sep 29 2014 Mikhail Kolchin <mvk@altlinux.org> 1.1-alt1
- initial build for ALT Linux Sisyphus

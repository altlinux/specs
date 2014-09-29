Name: libunibreak
Version: 1.1
Release: alt1

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
%autoreconf
%configure \
   --disable-static

%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog LICENCE NEWS README.md
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/libunibreak.pc

%changelog
* Mon Sep 29 2014 Mikhail Kolchin <mvk@altlinux.org> 1.1-alt1
- initial build for ALT Linux Sisyphus

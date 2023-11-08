%define rname libunibreak
%define sover 5
%define libunibreak %rname%sover
Name: %libunibreak
Version: 5.1
Release: alt1

Group: System/Libraries
Summary: Unicode line-breaking library
Url: http://vimgadgets.sourceforge.net/libunibreak
License: Zlib

Source: %rname-%version.tar

BuildRequires: glibc-devel

%description
Libunibreak is the successor of liblinebreak, an implementation of the line
breaking algorithm as described in Unicode 6.0.0 Standard Annex 14, Revision
26, available at http://www.unicode.org/reports/tr14/tr14-26.html

It is designed to be used in a generic text renderer. FBReader is one
real-world example, and you may also check some simple sample code, like
showbreak and breaktext.

%package devel
Group: Development/C
Summary: Development files for libunibreak
Provides: libunibreak-devel = %version
Obsoletes: libunibreak-devel <  %version-%release
%description devel
The libunibreak-devel package contains libraries and header files for
developing applications that use libunibreak.

%prep
%setup -n %rname-%version

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS LICENCE NEWS README.md
%_libdir/libunibreak.so.%sover
%_libdir/libunibreak.so.%sover.*

%files devel
%doc doc/html
%_includedir/*
%_libdir/lib*.so
%_libdir/pkgconfig/%rname.pc

%changelog
* Wed Nov 08 2023 Sergey V Turchin <zerg@altlinux.org> 5.1-alt1
- initial build

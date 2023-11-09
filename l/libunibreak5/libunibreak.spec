%define rname libunibreak
%define major 5
%define sover %major
%define libunibreak %rname%major
Name: %libunibreak
Version: 5.1
Release: alt2

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
Conflicts: libunibreak-devel
Conflicts: libunibreak3-devel
Requires(post,preun): alternatives >= 0.2
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

#install alternative
mv %buildroot/%_libdir/pkgconfig/%rname{,-%major}.pc
install -d %buildroot/%_sysconfdir/alternatives/packages.d/
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name-devel <<__EOF__
%_libdir/pkgconfig/%rname.pc %_libdir/pkgconfig/%rname-%major.pc %version
__EOF__

%files
%doc AUTHORS LICENCE NEWS README.md
%_libdir/libunibreak.so.%sover
%_libdir/libunibreak.so.%sover.*

%files devel
%doc doc/html
%config /%_sysconfdir/alternatives/packages.d/%name-devel
%_includedir/*
%_libdir/lib*.so
%_libdir/pkgconfig/%rname-%major.pc

%changelog
* Thu Nov 09 2023 Sergey V Turchin <zerg@altlinux.org> 5.1-alt2
- add alternatives support for pc-file

* Wed Nov 08 2023 Sergey V Turchin <zerg@altlinux.org> 5.1-alt1
- initial build

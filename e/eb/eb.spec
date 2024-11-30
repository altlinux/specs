Name: eb
Version: 4.4.3
Release: alt2
Summary: Library for accessing Japanese CD-ROM electronic books

Group: System/Libraries
License: BSD
Url: https://www.mistys-internet.website/eb/index-en.html
VCS: https://github.com/mistydemeo/eb/
Source0: %name-%version.tar
Patch1: eb-aclocal-conf-libdir.patch
Patch2: eb-gcc14.patch

BuildRequires: zlib-devel

%description
EB Library is a C library for accessing CD-ROM books.
EB Library supports to access CD-ROM books of
EB, EBG, EBXA, EBXA-C, S-EBXA and EPWING formats.

%package devel
Summary: Development files for eb
Group: Development/C
Requires: eb = %EVR
Requires: zlib-devel

%description devel
This package contains development files needs to use eb in programs.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure --disable-static --sysconfdir=%_libdir
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING NEWS README
%_bindir/*
%_libdir/libeb.so.*
%_datadir/eb

%files devel
%_includedir/eb
%_libdir/eb.conf
%_libdir/libeb.so
%_datadir/aclocal/*

%changelog
* Sat Nov 30 2024 Anton Farygin <rider@altlinux.ru> 4.4.3-alt2
- fixed build with gcc 14
- updated homepage

* Tue Nov 27 2018 Anton Farygin <rider@altlinux.ru> 4.4.3-alt1
- first build for ALT


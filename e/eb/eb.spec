Name: eb
Version: 4.4.3
Release: alt1
Summary: Library for accessing Japanese CD-ROM electronic books

Group: System/Libraries
License: BSD
Url: http://www.sra.co.jp/people/m-kasahr/eb/
# ftp://ftp.sra.co.jp/pub/misc/eb/
Source0: %name-%version.tar
Patch1: eb-aclocal-conf-libdir.patch

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
* Tue Nov 27 2018 Anton Farygin <rider@altlinux.ru> 4.4.3-alt1
- first build for ALT


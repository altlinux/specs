Name: libmspack
Version: 0.0.20060920alpha
Release: alt3

Summary: Compressors and decompressors for Microsoft compression formats

License: LGPL
Group: Development/C
Url: http://www.cabextract.org.uk/libmspack/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.cabextract.org.uk/libmspack/%name-%version.tar.bz2

BuildRequires: gcc

%package devel
Summary: Development files for libmspack
Group: Development/C

%description
The purpose of libmspack is to provide compressors and decompressors,
archivers and dearchivers for Microsoft compression formats: CAB, CHM,
HLP, KWAJ, LIT and SZDD. It is also designed to be easily embeddable,
stable, robust and resource-efficient.

The library is not intended as a generalised "any archiver" interface.
Users of the library must explicitly choose the format they intend to work
with.

%description devel
This package contains development files required
in development of the %name-based applications.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc README
%_libdir/*.so.*

%files devel
%doc doc/*
%_includedir/mspack.h
%_libdir/*.so

%changelog
* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.0.20060920alpha-alt3
- fix Url

* Sun Jan 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.0.20060920alpha-alt2
- cleanup spec, enable SMP build

* Wed Jun 27 2007 Vitaly Lipatov <lav@altlinux.ru> 0.0.20060920alpha-alt1
- initial build for ALT Linux Sisyphus


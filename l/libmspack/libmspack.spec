Name: libmspack
Version: 0.5
Release: alt1

Summary: Compressors and decompressors for Microsoft compression formats

License: LGPL
Group: Development/C
Url: http://www.cabextract.org.uk/libmspack/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/kyz/libmspack/archive/v%{version}alpha.tar.gz
Source: %name-%version.tar

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
mkdir m4
%autoreconf
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
%_pkgconfigdir/*.pc

%changelog
* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- new version 0.5 (with rpmrb script)

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- new version 1.5 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- update to 0.4-alpha

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.0.20060920alpha-alt3.qa1
- NMU: rebuilt for debuginfo.

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.0.20060920alpha-alt3
- fix Url

* Sun Jan 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.0.20060920alpha-alt2
- cleanup spec, enable SMP build

* Wed Jun 27 2007 Vitaly Lipatov <lav@altlinux.ru> 0.0.20060920alpha-alt1
- initial build for ALT Linux Sisyphus


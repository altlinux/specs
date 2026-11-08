%define oname sndio
%define sover 7
%define libname libsndio%sover

Name: lib%oname%sover
Version: 1.10.0
Release: alt2

Summary: A sound library (legacy)

Group: System/Legacy libraries
License: ISC
Url: http://www.sndio.org

# Source0-url: http://www.sndio.org/%oname-%version.tar.gz
Source0: %oname-%version.tar

BuildRequires: pkgconfig(alsa)

%description
Legacy sndio library with the ABI 7 interface.

%package -n %libname-devel
Summary: The development files for %oname
Group: Development/C
Requires: %libname = %EVR

%description -n %libname-devel
This package contains the development files for %oname.
%prep
%setup -n %oname-%version

%build
./configure \
--prefix=%prefix \
--libdir=%_libdir \
--mandir=%_mandir \
--pkgconfdir=%_pkgconfigdir \
--privsep-user=_sndio

%make_build

%install
%makeinstall_std

# Retain only the versioned ABI 7 library.
rm -v %buildroot%_bindir/{aucat,midicat,sndiod,sndioctl}
rm -v %buildroot%_mandir/man*/*
rm -v %buildroot%_includedir/%oname.h
rm -v %buildroot%_libdir/libsndio.so
rm -v %buildroot%_pkgconfigdir/sndio.pc

%files
%_libdir/libsndio.so.%{sover}*

%changelog
* Fri Nov 06 2026 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt2
- build legacy ABI 7 library as a separate source package.

* Tue Mar 18 2025 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt1
- new version 1.10.0 (with rpmrb script)

* Mon Mar 17 2025 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- initial build for ALT Sisyphus


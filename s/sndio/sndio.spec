%define sover 9
%define libname libsndio%sover

Name: sndio
Version: 1.11.0
Release: alt1

Summary: A sound library

Group: Sound
License: ISC
Url: http://www.sndio.org

# Source0-url: http://www.sndio.org/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: %name.sysusers.conf
Patch0: configure-version.patch

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libbsd)

Requires: %libname = %EVR

%description
Sndio is a small audio and MIDI framework. It provides a lightweight audio &
MIDI server and a fully documented user-space API to access either the server
or directly the hardware in a uniform way. Reliability through simplicity are
part of the project goals.


%package -n %libname
Summary: Libraries for %name
Group: System/Libraries

%description -n %libname
This package contains the libraries for %name.


%package -n libsndio-devel
Summary: The development files for %name
Group: Development/C
Requires: %libname = %EVR
Provides: libsndio7-devel = %EVR
Obsoletes: libsndio7-devel < %EVR

%description -n libsndio-devel
This package contains the development files for %name.
%prep
%setup
%patch0 -p1

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

# Install sndiod systemd service file
install -Dm 644 contrib/sndiod.service %buildroot%_unitdir/sndiod.service
install -Dm 644 contrib/default.sndiod %buildroot%_sysconfdir/default/sndiod
install -Dm 644 %SOURCE1 %buildroot%_sysusersdir/%name.conf


%pre
%sysusers_create_package %name %SOURCE1

%post
%post_systemd sndiod.service

%preun
%preun_systemd sndiod.service

%files
%_bindir/aucat
%_bindir/midicat
%_bindir/sndiod
%_bindir/sndioctl
%_mandir/man*/*
%_unitdir/sndiod.service
%config(noreplace) %_sysconfdir/default/sndiod
%_sysusersdir/%name.conf

%files -n %libname
%_libdir/libsndio.so.%{sover}
%_libdir/libsndio.so.%{sover}.0

%files -n libsndio-devel
%_includedir/%name.h
%_libdir/libsndio.so
%_pkgconfigdir/sndio.pc
%changelog
* Thu Nov 05 2026 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt1
- new version 1.11.0.
- rename libsndio7-devel to libsndio-devel (closes: #61345).
- added BuildRequires: pkgconfig(libbsd) for 1.11.0.
- fixed pkg-config version to 1.11.0.
- use sysusers.d for the _sndio user.
- mark /etc/default/sndiod as %%config(noreplace).
- added systemd scriptlets for sndiod.service.

* Tue Mar 18 2025 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt1
- new version 1.10.0 (with rpmrb script)

* Mon Mar 17 2025 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- initial build for ALT Sisyphus


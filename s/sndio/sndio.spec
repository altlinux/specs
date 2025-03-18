%define sover 7
%define libname libsndio%sover

Name: sndio
Version: 1.10.0
Release: alt1

Summary: A sound library

Group: Sound
License: ISC
Url: http://www.sndio.org

# Source0-url: http://www.sndio.org/%name-%version.tar.gz
Source0: %name-%version.tar

BuildRequires: pkgconfig(alsa)

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


%package -n %libname-devel
Summary: The development files for %name
Group: Development/C
Requires: %libname = %EVR

%description -n %libname-devel
This package contains the development files for %name.
%prep
%setup

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
install -Dm 755 contrib/sndiod.service %buildroot%_unitdir/sndiod.service
install -Dm 644 contrib/default.sndiod %buildroot%_sysconfdir/default/sndiod


%pre
%_sbindir/useradd -r -n -g audio -d /var/empty -s /bin/false -c "sndio pseudo user" _sndio >/dev/null 2>&1 ||:

%files
%_bindir/aucat
%_bindir/midicat
%_bindir/sndiod
%_bindir/sndioctl
%_mandir/man*/*
%_unitdir/sndiod.service
%_sysconfdir/default/sndiod

%files -n %libname
%_libdir/libsndio.so.%{sover}*

%files -n %libname-devel
%_includedir/%name.h
%_libdir/libsndio.so
%_pkgconfigdir/sndio.pc
%changelog
* Tue Mar 18 2025 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt1
- new version 1.10.0 (with rpmrb script)

* Mon Mar 17 2025 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- initial build for ALT Sisyphus


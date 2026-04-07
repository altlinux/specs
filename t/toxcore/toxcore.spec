%define _unpackaged_files_terminate_build 1

%define abiversion 2

Name: toxcore
Version: 0.2.22
Release: alt1

Summary: Peer to peer (serverless) instant messenger
License: GPL-3.0-or-later
Group: System/Libraries
Url: https://github.com/TokTok/c-toxcore
VCS: https://github.com/TokTok/c-toxcore.git

Source: %name-%version.tar
Source1: %name-%version-third_party-cmp.tar

BuildRequires: libcheck-devel
BuildRequires: libconfig-devel
BuildRequires: libopus-devel
BuildRequires: libsodium-devel
BuildRequires: libvpx-devel

%description
Tox is a peer to peer (serverless) instant messenger aimed at making security
and privacy easy to obtain for regular users. It uses libsodium (based on NaCl)
for its encryption and authentication.

%package -n libtoxav%abiversion
Summary: Library for Tox protocol that provides audio/video functionality
Group: System/Libraries

%description -n libtoxav%abiversion
The `libtoxav1` library provides the necessary functionality for handling audio
vand video calls in the Tox protocol. It relies on external libraries like
`libopus` for audio encoding/decoding and `libvpx` for video processing. This
library is essential for Tox clients that support multimedia communication.

%package -n libtoxcore%abiversion
Summary: Library for Tox protocol that provides the messenger functionality
Group: System/Libraries

%description -n libtoxcore%abiversion
The `libtoxcore1` library is the core implementation of the Tox protocol. It
provides functionalities such as messaging, file transfer, and connection
management. This library is the foundation for all Tox clients and services.

%package -n libtoxencryptsave%abiversion
Summary: Library for Tox protocol that provides encryption of Tox profiles
Group: System/Libraries

%description -n libtoxencryptsave%abiversion
The `libtoxencryptsave1` library provides functionality for encrypting and
saving Tox profile data, such as private keys and settings. It ensures that
sensitive information is securely stored on disk.

%package bootstrapd
Summary: Highly configurable DHT bootstrap node daemon based on Tox protocol
Group: System/Libraries

%description bootstrapd
The `toxcore-bootstrapd` package provides a daemon for running a Tox bootstrap
node. Bootstrap nodes help new clients connect to the Tox network by providing
initial peer information. This package is essential for maintaining the
distributed nature of the Tox network.

%package devel
Summary: Development files for %name
Group: System/Libraries

%description devel
The `toxcore-devel` package provides header files and static libraries
necessary for developing applications that use the Toxcore libraries. It is
required for compiling and linking against `libtoxcore`, `libtoxav`, and
`libtoxencryptsave`.

%prep
%setup -a1
%autopatch -p1

%build
%autoreconf
%configure \
  --enable-daemon \
  --enable-static=no \
  #

%make_build

%install
%makeinstall
rm -f %buildroot%_bindir/DHT_bootstrap
install -d -m700 %buildroot/var/lib/tox-bootstrapd/
install -D -m644 other/bootstrap_daemon/tox-bootstrapd.conf \
  %buildroot/etc/tox-bootstrapd.conf
install -D -m644 other/bootstrap_daemon/tox-bootstrapd.service \
  %buildroot%_unitdir/tox-bootstrapd.service
sed -i "s|/usr/local/bin|%_bindir|g" %buildroot%_unitdir/tox-bootstrapd.service

%pre bootstrapd
/usr/sbin/groupadd -r -f tox-bootstrapd
/usr/sbin/useradd -r \
  -d /var/lib/tox-bootstrapd -s /dev/null \
  -c 'TOX DHT bootstrap daemon' \
  -g tox-bootstrapd tox-bootstrapd >/dev/null 2>&1 ||:

%files -n libtoxav%abiversion
%_libdir/libtoxav.so.%{abiversion}*

%files -n libtoxcore%abiversion
%_libdir/libtoxcore.so.%{abiversion}*

%files -n libtoxencryptsave%abiversion
%_libdir/libtoxencryptsave.so.%{abiversion}*

%files bootstrapd
%doc other/bootstrap_daemon/README.md
%dir %attr(700,tox-bootstrapd,tox-bootstrapd) /var/lib/tox-bootstrapd
%_bindir/tox-bootstrapd
%_datadir/bash-completion/completions/tox-bootstrapd
%_sysconfdir/tox-bootstrapd.conf
%_unitdir/tox-bootstrapd.service

%files devel
%_includedir/tox
%_libdir/libtoxav.so
%_libdir/libtoxcore.so
%_libdir/libtoxencryptsave.so
%_pkgconfigdir/libtoxav.pc
%_pkgconfigdir/libtoxcore.pc

%changelog
* Tue Apr 07 2026 Anton Farygin <rider@altlinux.org> 0.2.22-alt1
- 0.2.21 -> 0.2.22

* Wed Nov 12 2025 Constantin Sunzow <protvin@altlinux.org> 0.2.21-alt2
- Fix FTBFS (qTox): add to packaging lost header tox_log_level.h.

* Tue Aug 05 2025 Constantin Sunzow <protvin@altlinux.org> 0.2.21-alt1
- New version.

* Tue Feb 25 2025 Constantin Sunzow <protvin@altlinux.org> 0.2.20-alt1
- Disable build static package.
- New version.

* Mon Oct 18 2021 Anton Farygin <rider@altlinux.ru> 0.1.11-alt3
- NMU: fixed build with LTO

* Sun Feb 11 2018 Denis Smirnov <mithraen@altlinux.ru> 0.1.11-alt2
- rebuild with new libsodium

* Sun Feb 11 2018 Denis Smirnov <mithraen@altlinux.ru> 0.1.11-alt1
- update from upstream git

* Wed Jun 14 2017 Denis Smirnov <mithraen@altlinux.ru> 0.1.9-alt1
- update from upstream git (ALT #33283)

* Mon Mar 27 2017 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt2.20170327
- update from upstream git

* Mon Jul 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt2.20160725
- build tox-bootstrapd subpackage

* Mon Jul 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1.20160725
- update from upstream git (ALT #32105)

* Tue Jun 16 2015 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20150616
- update from upstream git (ALT #31056)

* Tue Dec 16 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20141216
- update from upstream git

* Tue Nov 04 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20141104
- update from upstream git

* Wed Oct 22 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20141022
- update from upstream git

* Tue Oct 14 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20141014
- update from upstream git (ALT #30394)

* Mon Aug 25 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20140717.1
- rebuild with new libsodium

* Thu Jul 17 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20140717
- update from upstream git

* Thu Jul 17 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20140628.1
- package tox/tox.h (ALT #30195)

* Sat Jun 28 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20140628
- update from upstream git

* Thu Jun 26 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1.20140626
- update from upstream git

* Thu Jun 26 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus


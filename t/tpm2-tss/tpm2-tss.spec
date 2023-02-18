%define udevrules_prefix 60-
%define soname 0
%define _localstatedir /var
%def_disable check

Name: tpm2-tss
Version: 4.0.1
Release: alt1
Summary: TPM2.0 Software Stack
# The entire source code is under BSD except implementation.h and tpmb.h which
# is under TCGL(Trusted Computing Group License).
License: BSD-2-Clause
Url: https://github.com/tpm2-software/tpm2-tss
Source0: %name-%version.tar
Source1: %name.watch
Patch: %name-%version-%release.patch
Group: System/Configuration/Hardware
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: autoconf-archive
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: libsystemd-devel
BuildRequires: libgcrypt-devel
BuildRequires: openssl-devel
BuildRequires: libjson-c-devel
BuildRequires: libcurl-devel
BuildRequires: libuuid-devel
%if_enabled check
BuildRequires: libuthash-devel
BuildRequires: procps
BuildRequires: libcmocka-devel
%endif

%description
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

%package -n lib%name%soname
Summary: TPM2.0 Software Stack
Group: System/Configuration/Hardware
Requires: lib%name-common = %EVR

%description -n lib%name%soname
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

%package -n lib%name-common
Summary: Common files for TPM2.0 Software Stack
Group: System/Configuration/Hardware

%description -n lib%name-common
This package contains common files required to work witj libtpm2-tss.

%package -n lib%name-devel
Summary: Headers and libraries for building apps that use tpm2-tss
Group: Development/C
Requires: lib%name%soname = %EVR

%description -n lib%name-devel
This package contains headers and libraries required to build applications that
use tpm2-tss.

%prep
%setup
%patch -p1
echo "%version" > VERSION

%build
./bootstrap
%autoreconf
# Use built-in tpm-udev.rules, with specified installation path and prefix.
%configure \
    --disable-static \
    --disable-silent-rules \
    --with-udevrulesdir=%_udevrulesdir \
    --with-udevrulesprefix=%udevrules_prefix \
    --with-runstatedir=/run \
    --with-sysusersdir=/lib/sysusers.d \
    --with-tmpfilesdir=%_tmpfilesdir \
%if_enabled check
    --enable-unit \
%endif
    %nil

%make_build

%check
%make_build check

%install
%makeinstall_std
mkdir -p %buildroot%_sharedstatedir/%name/system/keystore

%pre -n lib%name-common
groupadd -r -f tss >/dev/null 2>&1 ||:
useradd -g tss -c 'TPM2 Software Stack User' \
    -d /var/empty -s /dev/null -r -l -M tss >/dev/null 2>&1 ||:

%files -n lib%name%soname
%_libdir/*.so.*

%files -n lib%name-common
%doc README.md CHANGELOG.md LICENSE
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_udevrulesdir/%{udevrules_prefix}tpm-udev.rules
%_tmpfilesdir/*
%_man5dir/*
/lib/sysusers.d/*
%dir %_sharedstatedir/%name
%dir %_sharedstatedir/%name/system
%attr(2775,tss,tss) %dir %_sharedstatedir/%name/system/keystore

%files -n lib%name-devel
%_includedir/tss2
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*
%_man7dir/*

%changelog
* Sat Feb 18 2023 Alexey Shabalin <shaba@altlinux.org> 4.0.1-alt1
- 4.0.1 (Fixes: CVE-2023-22745)

* Thu Mar 24 2022 Alexey Shabalin <shaba@altlinux.org> 3.2.0-alt1
- new version 3.2.0

* Tue Jul 06 2021 Alexey Shabalin <shaba@altlinux.org> 3.1.0-alt1
- new version 3.1.0 (Fixes: CVE-2020-24455)
- Revert "Added dependency from systemd-stateless"
- Drop execute adduser, groupadd and other root utils in Makefile
- Disable check (fail 1 from 41)

* Fri Jan 22 2021 Danil Shein <dshein@altlinux.org> 3.0.3-alt1
- 3.0.3

* Tue Dec 01 2020 Danil Shein <dshein@altlinux.org> 3.0.2-alt1
- update version to 3.0.2
- enable unit tests

* Thu Oct 08 2020 Anton Farygin <rider@altlinux.ru> 2.4.3-alt1
- 2.4.3 (fixes: CVE-2020-24455)

* Thu Aug 20 2020 Anton Farygin <rider@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Wed Jul 15 2020 Anton Farygin <rider@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Wed Mar 25 2020 Alexey Shabalin <shaba@altlinux.org> 2.4.0-alt1
- 2.4.0

* Thu Mar 12 2020 Anton Farygin <rider@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Fri Jan 10 2020 Anton Farygin <rider@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Tue Nov 05 2019 Alexey Shabalin <shaba@altlinux.org> 2.3.1-alt2
- add tss user and group (ALT #37279)

* Mon Sep 16 2019 Anton Farygin <rider@altlinux.ru> 2.3.1-alt1
- first build for ALT, based on specfile from Fedora


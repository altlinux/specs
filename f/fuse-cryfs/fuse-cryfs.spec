%define oname cryfs
%def_without system_spdlog
Name: fuse-cryfs
Version: 0.9.10
Release: alt2

Summary: Cryptographic filesystem for the cloud

License: LGPL
Group: System/Kernel and hardware
Url: https://www.cryfs.org/

Requires: fuse

# Source-url: https://github.com/cryfs/cryfs/archive/%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires: rpm-macros-cmake cmake
BuildRequires: boost-devel boost-devel-headers boost-filesystem-devel boost-program_options-devel
#BuildRequires: boost-devel-static
BuildRequires: libcryptopp-devel
BuildRequires: libcurl-devel
BuildRequires: libfuse-devel
BuildRequires: libssl-devel

BuildRequires: gcc-c++

# TODO: check when will req spdlog >= 1.1
%if_with system_spdlog
# instead builtin
BuildRequires: libspdlog-devel = 0.12.0
%endif

BuildRequires: python-modules-json

%description
CryFS encrypts your files, so you can safely store them anywhere.
It works well together with cloud services
like Dropbox, iCloud, OneDrive and others.
See https://www.cryfs.org.

%prep
%setup

# conflicts with CHAR_WIDTH macro
%__subst "s|CHAR_WIDTH|SPDLOG_CHAR_WIDTH|g" vendor/spdlog/spdlog/fmt/bundled/format.h
%if_with system_spdlog
# replaced with libspdlog-devel
rm -rf vendor/spdlog/
%__subst "s|.*spdlog.*||" vendor/CMakeLists.txt
%__subst "s|spdlog||" src/cpp-utils/CMakeLists.txt
%endif

# explicitly set python-2
find . -type f | xargs sed -i \
	-e '1s:^#!/usr/bin/env python$:#!/usr/bin/python%__python_version:' \
	%nil

%build
%cmake -DBUILD_TESTING=off -DBoost_INCLUDE_DIRS=%_includedir/boost -DBoost_USE_STATIC_LIBS=off -DCMAKE_BUILD_TYPE=RELEASE
%make_build -C BUILD

%install
%makeinstall_std -C BUILD

%files
%_bindir/cryfs
%_man1dir/*

%changelog
* Mon Dec 16 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.10-alt2
- Rebuilt with boost-1.71.0.

* Tue Feb 12 2019 Vitaly Lipatov <lav@altlinux.ru> 0.9.10-alt1
- new version 0.9.10 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt2.1
- NMU: autorebuild with libcryptopp.so.7

* Mon Sep 03 2018 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt2
- disable build with external stdlog

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt1
- new version 0.9.9 (with rpmrb script), rebuild with libcryptopp-6.1.0
- enable dynamic boost build

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt2.1
- NMU: autorebuild with libcryptopp-5.6.5

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt2
- fix build, build with external spdlog

* Wed Mar 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- initial build for ALT Linux Sisyphus

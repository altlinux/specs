%define oname cryfs
Name: fuse-cryfs
Version: 0.9.7
Release: alt2.1

Summary: Cryptographic filesystem for the cloud

License: LGPL
Group: System/Kernel and hardware
Url: https://www.cryfs.org/

Requires: fuse

# Source-url: https://github.com/cryfs/cryfs/archive/%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: boost-devel
BuildRequires: boost-devel-static
BuildRequires: libcryptopp-devel
BuildRequires: libcurl-devel
BuildRequires: libfuse-devel
BuildRequires: libssl-devel

# instead builtin
BuildRequires: libspdlog-devel

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
# replaced with libspdlog-devel
rm -rf vendor/spdlog/
%__subst "s|.*spdlog.*||" vendor/CMakeLists.txt
%__subst "s|spdlog||" src/cpp-utils/CMakeLists.txt

%build
%cmake -DBUILD_TESTING=off -DCMAKE_BUILD_TYPE=RELEASE
%make_build -C BUILD

%install
%makeinstall_std -C BUILD

%files
%_bindir/cryfs

%changelog
* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt2.1
- NMU: autorebuild with libcryptopp-5.6.5

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt2
- fix build, build with external spdlog

* Wed Mar 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- initial build for ALT Linux Sisyphus

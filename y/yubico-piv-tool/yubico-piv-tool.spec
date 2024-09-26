%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

Name: yubico-piv-tool
Version: 2.6.1
Release: alt1

Summary: Command line tool for the YubiKey PIV application
License: BSD-2-Clause
Group: System/Configuration/Hardware
Url: https://developers.yubico.com/yubico-piv-tool/
Vcs: https://github.com/Yubico/yubico-piv-tool

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

Requires: pcsc-lite-ccid

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: libcheck-devel
BuildRequires: libpcsclite-devel
BuildRequires: zlib-devel
BuildRequires: gengetopt
BuildRequires: help2man
BuildRequires: ctest

%description
The Yubico PIV tool is used for interacting with the Personal Identity
Verification (PIV) application on a YubiKey.

With it you may generate keys on the device, importing keys and certificates,
and create ceritficate requests, and other operations. A shared library and
a command-line tools is included.

%package devel
Summary: Development files for yubico-piv-tool
Group: Development/Other

%description devel
%summary.

%prep
%setup
%autopatch -p1

%build
%cmake -DBUILD_STATIC_LIB=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc COPYING NEWS README
%_bindir/%name
%_libdir/libykpiv.so.*
%_libdir/libykcs11.so.*
%_man1dir/%name.*

%files devel
%doc COPYING NEWS README
%_includedir/ykpiv/
%_libdir/libykpiv.so
%_libdir/libykcs11.so
%_pkgconfigdir/ykpiv.pc
%_pkgconfigdir/ykcs11.pc

%changelog
* Thu Sep 26 2024 Anton Zhukharev <ancieg@altlinux.org> 2.6.1-alt1
- Updated to 2.6.1.

* Thu May 16 2024 Anton Zhukharev <ancieg@altlinux.org> 2.5.2-alt1
- Updated to 2.5.2.

* Wed Feb 14 2024 Anton Zhukharev <ancieg@altlinux.org> 2.5.1-alt1
- Updated to 2.5.1.

* Fri Feb 09 2024 Anton Zhukharev <ancieg@altlinux.org> 2.5.0-alt1
- Updated to 2.5.0.

* Mon Dec 11 2023 Anton Zhukharev <ancieg@altlinux.org> 2.4.2-alt1
- Updated to 2.4.2.

* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 2.3.1-alt1
- New version.
- Set strict ELF verification.
- Follow SharedLib policy.

* Sat Aug 27 2022 Anton Zhukharev <ancieg@altlinux.org> 2.3.0-alt1.gitd9d05fcc
- fix tests

* Tue Aug 02 2022 Anton Zhukharev <ancieg@altlinux.org> 2.3.0-alt1
- initial build for Sisyphus


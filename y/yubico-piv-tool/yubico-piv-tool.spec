%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

%define abiversion 2

Name: yubico-piv-tool
Version: 2.7.3
Release: alt1

Summary: Command line tool for the YubiKey PIV application
License: BSD-2-Clause
Group: System/Configuration/Hardware
Url: https://developers.yubico.com/yubico-piv-tool/
Vcs: https://github.com/Yubico/yubico-piv-tool

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

Requires: pcsc-lite-ccid
Requires: libykpiv%abiversion = %EVR

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

%package -n libykpiv%abiversion
Summary: Library to interact with the PIV application on a Yubikey
Group: System/Libraries

%description -n libykpiv%abiversion
Shared library to interact with the Personal Identity Verification (PIV)
application on a YubiKey.

%package -n libykpiv-devel
Summary: Development files for libykpiv
Group: Development/C++
Requires: libykpiv%abiversion = %EVR

%description -n libykpiv-devel
Provides development files for libykpiv.

%package -n ykcs11
Summary: PKCS#11 module for a YubiKey
Group: System/Libraries
Requires: libykpiv%abiversion = %EVR

%description -n ykcs11
PKCS#11 module that allows external applications to communicate with
the PIV application running on a YubiKey.

%prep
%setup
%autopatch -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_STATIC_LIB=OFF
%cmake_build

%install
%cmake_install

# I don't think PKCS#11 module needs that almost empty pkg-config file.
rm %buildroot%_pkgconfigdir/ykcs11.pc

%check
%ctest

%files
%doc COPYING NEWS README
%_bindir/%name
%_man1dir/%name.*

%files -n libykpiv%abiversion
%doc COPYING NEWS README
%_libdir/libykpiv.so.%abiversion
%_libdir/libykpiv.so.%version

%files -n libykpiv-devel
%doc COPYING NEWS README
%_libdir/libykpiv.so
%_includedir/ykpiv/
%_pkgconfigdir/ykpiv.pc

%files -n ykcs11
%_libdir/libykcs11.so
%_libdir/libykcs11.so.%abiversion
%_libdir/libykcs11.so.%version

%changelog
* Fri Jan 23 2026 Anton Zhukharev <ancieg@altlinux.org> 2.7.3-alt1
- Updated to 2.7.3.
- Separated libykpiv shared library and ykcs11 module.

* Fri Aug 15 2025 Anton Zhukharev <ancieg@altlinux.org> 2.7.2-alt1
- Updated to 2.7.2.

* Wed Feb 26 2025 Anton Zhukharev <ancieg@altlinux.org> 2.7.1-alt1
- Updated to 2.7.1.

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


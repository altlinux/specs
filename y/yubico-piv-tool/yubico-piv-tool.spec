%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

Name: yubico-piv-tool
Version: 2.3.1
Release: alt1

Summary: Command line tool for the YubiKey PIV application
License: BSD-2-Clause
Group: System/Configuration/Hardware
Url: https://github.com/Yubico/yubico-piv-tool

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: libssl-devel
BuildRequires: libcheck-devel
BuildRequires: libpcsclite-devel
BuildRequires: pkg-config
BuildRequires: gengetopt
BuildRequires: help2man
BuildRequires: ctest

Requires: pcsc-lite-ccid

%description
The Yubico PIV tool is used for interacting with the Personal Identity
Verification (PIV) application on a YubiKey.

With it you may generate keys on the device, importing keys and certificates,
and create ceritficate requests, and other operations. A shared library and
a command-line tools is included.

%package devel
Summary: Development files for yubico-piv-tool
Group: Development/Other

Requires: %name = %EVR

%description devel
%summary

%prep
%setup

%build
%cmake_insource -DBUILD_STATIC_LIB=OFF
%cmake_build

%install
%cmake_install

%check
%make_build test 

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
%_libdir/pkgconfig/ykpiv.pc
%_libdir/pkgconfig/ykcs11.pc

%changelog
* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 2.3.1-alt1
- New version.
- Set strict ELF verification.
- Follow SharedLib policy.

* Sat Aug 27 2022 Anton Zhukharev <ancieg@altlinux.org> 2.3.0-alt1.gitd9d05fcc
- fix tests

* Tue Aug 02 2022 Anton Zhukharev <ancieg@altlinux.org> 2.3.0-alt1
- initial build for Sisyphus


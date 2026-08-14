Name:     procdump
Version:  3.5.2
Release:  alt2

Summary:  A Linux version of the ProcDump Sysinternals tool

License:  MIT

ExclusiveArch: x86_64 aarch64
Group:    Other
Url:      https://github.com/Microsoft/ProcDump-for-Linux

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Microsoft/ProcDump-for-Linux/archive/%version.tar.gz
Source:   %name-%version.tar

Patch1: procdump-system-libbpf.patch
Patch2: procdump-no-werror.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: clang
BuildRequires: libstdc++-devel
BuildRequires: libelf-devel
BuildRequires: libbpf-devel
BuildRequires: bpftool
BuildRequires: zlib-devel

Requires: gdb >= 7.7.1

%description
ProcDump is a Linux reimagining of the classic ProcDump tool from the Sysinternals suite of tools for Windows.
ProcDump provides a convenient way for Linux developers to create core dumps of their application based on performance triggers.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
export PATH=/usr/sbin:$PATH
export CC=clang
export CXX=clang++
# corex is a static archive; LTO bitcode in .a breaks ld's archive index
%add_optflags -fno-lto
VERSION=%version %cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
install -D -m 0755 %_cmake__builddir/procdump %buildroot%_bindir/procdump
install -D -m 0644 %_cmake__builddir/procdump.1.gz %buildroot%_man1dir/procdump.1.gz

%files
%_bindir/procdump
%_man1dir/*
%doc CONTRIBUTING.md README.md

%changelog
* Thu Aug 13 2026 Vitaly Lipatov <lav@altlinux.ru> 3.5.2-alt2
- escape RPM macros in changelog

* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 3.5.2-alt1
- new version 3.5.2
- switch to cmake build, use system libbpf
- use %%cmake/%%cmake_build macros (BR(pre): rpm-macros-cmake)
- drop upstream -Werror (unused-symbol warnings fail under %%cmake's -Wall)
- disable LTO (corex static archive; LTO bitcode breaks ld's archive index)

* Sun Mar 08 2026 Vitaly Lipatov <lav@altlinux.ru> 3.5.0-alt1
- new version 3.5.0

* Fri Feb 26 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- fix build (thanks, Fedora!)

* Mon May 11 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Mon Jan 27 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- new version 1.1 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Tue Dec 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus

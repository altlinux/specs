%define cargo_prep %nil
%define cargo_build %rust_build
%define cargo_install %rust_install

Name:     procdump
Version:  3.5.3
Release:  alt1

Summary:  A Linux version of the ProcDump Sysinternals tool

License:  MIT

# upstream eBPF program and .NET profiler support only x86_64 and aarch64
ExclusiveArch: x86_64 aarch64
Group:    Other
Url:      https://github.com/Microsoft/ProcDump-for-Linux

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Microsoft/ProcDump-for-Linux/archive/%version.tar.gz
Source:   %name-%version.tar
Source1:  %name-development-%version.tar
Source2:  config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: clang
BuildRequires: libstdc++-devel
BuildRequires: pkgconfig(libbpf)
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(zlib)

Requires: gdb >= 7.7.1

%description
ProcDump is a Linux reimagining of the classic ProcDump tool from the Sysinternals suite of tools for Windows.
ProcDump provides a convenient way for Linux developers to create core dumps of their application based on performance triggers.

%prep
%setup -a1
%cargo_prep
install -vD %SOURCE2 .cargo/config.toml
# link the system libbpf instead of building the copy bundled in libbpf-sys
sed -i -e 's/^\(libbpf-\(rs\|cargo\) = {.*optional = true\)/\1, default-features = false/' \
    crates/procdump/Cargo.toml
grep -q 'libbpf-rs = .*default-features = false' crates/procdump/Cargo.toml
grep -q 'libbpf-cargo = .*default-features = false' crates/procdump/Cargo.toml

%build
export PROCDUMP_VERSION=%version
export CC=clang
export CXX=clang++
# keep symbols for debuginfo (upstream release profile strips them)
export CARGO_PROFILE_RELEASE_STRIP=false
%cargo_build -p procdump-cli

%install
%cargo_install
install -D -m 0644 procdump.1 %buildroot%_man1dir/procdump.1

%check
export PROCDUMP_VERSION=%version
export CC=clang
export CXX=clang++
export CARGO_PROFILE_RELEASE_STRIP=false
%rust_test --offline -p procdump-cli -p procdump

%files
%_bindir/procdump
%_man1dir/procdump.1*
%doc CONTRIBUTING.md README.md

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 3.5.3-alt1
- new version 3.5.3 (rewritten in Rust upstream)
- build with cargo, vendor crates via .gear/predownloaded-development
- build eBPF program from source with clang, link system libbpf
- drop CMake-era patches
- run upstream unit tests in %%check

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

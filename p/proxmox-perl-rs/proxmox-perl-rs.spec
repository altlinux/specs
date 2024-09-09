%global _unpackaged_files_terminate_build 1
%def_without check

Name: proxmox-perl-rs
Version: 0.3.4
Release: alt1
Summary: PVE and PMG common parts which have been ported to Rust
License: AGPL-3.0+
Group: Development/Other
URL: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/proxmox-perl-rs.git
Source: %name-%version.tar
Patch: %name-%version.patch
Patch1: 0001-ALT-set-correct-context-not-None.patch
Source1: genpackage.pl

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust clang-devel perl-devel
BuildRequires: libssl-devel libacl-devel libuuid-devel
BuildRequires: cargo-vendor-checksum
BuildRequires: /proc
%set_perl_req_method relaxed

%description
Contains the perl side of modules provided by the libraries of both
libpve-rs-perl and libpmg-rs-perl, loading whichever is available.

%package -n libproxmox-rs-perl
Summary: PVE/PMG common parts which have been ported to Rust
Version: 0.3.4
Group: Development/Other
Provides: proxmox-perl-rs = %EVR
Provides: proxmox-rs-perl = %EVR

%description -n libproxmox-rs-perl
%summary

%package -n libpve-rs-perl
Summary: PVE parts which have been ported to Rust
Version: 0.8.10
Group: Development/Other
Provides: pve-perl-rs = %EVR
Provides: pve-rs-perl = %EVR

%description -n libpve-rs-perl
%summary

%package -n libpmg-rs-perl
Summary: Components of Proxmox Mail Gateway which have been ported to Rust
Version: 0.7.6
Group: Development/Other
Provides: pmg-perl-rs = %EVR
Provides: pmg-rs-perl = %EVR

%description -n libpmg-rs-perl
%summary

%prep
%setup
%patch -p1
%patch1 -p1
pushd pve-rs
sed -i 's/PL_use_safe_putenv = on ? TRUE : FALSE;//' vendor/perlmod/src/glue.c
cargo-vendor-checksum --vendor vendor -f perlmod/src/glue.c
%ifarch aarch64
sed -i 's/mut i8/mut u8/' vendor/proxmox-sys/src/fs/dir.rs
# Checksum update for patched files
cargo-vendor-checksum --vendor vendor -f proxmox-sys/src/fs/dir.rs
%endif
cargo-vendor-checksum --vendor vendor -f proxmox-notify/src/context/mod.rs
popd

%build
export BUILD_MODE=release
export PERLMOD_WRITE_PACKAGES=1
export BUILD_TARGET=pve
export RUSTFLAGS="-L/usr/lib64/perl5/CORE -lperl"

cp %SOURCE1 common/pkg/
cp %SOURCE1 pmg-rs/
cp %SOURCE1 pve-rs/
sed -i 's|/usr/lib/perlmod/genpackage.pl|./genpackage.pl|'  common/pkg/Makefile pmg-rs/Makefile pve-rs/Makefile

# Build only in pve-rs:
pushd pve-rs
%make
popd
pushd common/pkg
%make
popd

%install
pushd pve-rs
install -pD -m0644 target/release/libpve_rs.so %buildroot%perl_vendor_autolib/libpve_rs.so
mkdir -p %buildroot%perl_vendor_privlib/{PVE/RS/ResourceScheduling,Proxmox/Lib,Proxmox/RS}
install -m0644 PVE/RS/*.pm %buildroot%perl_vendor_privlib/PVE/RS/
install -m0644 PVE/RS/ResourceScheduling/*.pm %buildroot%perl_vendor_privlib/PVE/RS/ResourceScheduling/
install -m0644 common/pkg/PVE/RS/*.pm %buildroot%perl_vendor_privlib/PVE/RS/
install -m0644 Proxmox/RS/*.pm %buildroot%perl_vendor_privlib/Proxmox/RS/
install -m0644 common/pkg/Proxmox/Lib/Common.pm Proxmox/Lib/PVE.pm %buildroot%perl_vendor_privlib/Proxmox/Lib/

%check
pushd pve-rs
LD_LIBRARY_PATH='$LD_LIBRARY_PATH:../target/release' make check

%files -n libpve-rs-perl
%perl_vendor_autolib/libpve_rs.so
%dir %perl_vendor_privlib/PVE/RS
%dir %perl_vendor_privlib/PVE/RS/ResourceScheduling
%perl_vendor_privlib/PVE/RS/*.pm
%perl_vendor_privlib/PVE/RS/ResourceScheduling/*.pm

%files -n libproxmox-rs-perl
%dir %perl_vendor_privlib/Proxmox/RS
%perl_vendor_privlib/Proxmox/RS/*
%dir %perl_vendor_privlib/Proxmox/Lib
%perl_vendor_privlib/Proxmox/Lib/*


%changelog
* Mon Sep 09 2024 Alexander Burmatov <thatman@altlinux.org> 0.3.4-alt1
- Update:
  + libproxmox-rs-perl 0.3.4
  + libpve-rs-perl 0.8.10

* Fri Sep 06 2024 Alexander Burmatov <thatman@altlinux.org> 0.3.3-alt3
- some notifications fixes (thx andy@)
- Update:
  + libpve-rs-perl 0.8.9

* Wed Apr 03 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.3.3-alt2
- update cargo vendor

* Thu Feb 22 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.3.3-alt1
- Update:
  + libproxmox-rs-perl 0.3.3
  + libpve-rs-perl 0.8.8
- new building scheme

* Tue Nov 07 2023 Andrew A. Vasilyev <andy@altlinux.org> 0.2.1-alt3
- libpve-rs-perl: add linking with libperl (Closes: #48330)

* Fri Mar 17 2023 Alexey Shabalin <shaba@altlinux.org> 0.2.1-alt2
- Update libpve-rs-perl 0.7.3

* Mon Oct 03 2022 Alexey Shabalin <shaba@altlinux.org> 0.2.1-alt1
- Update:
  + libproxmox-rs-perl 0.2.1
  + libpve-rs-perl 0.7.2

* Fri May 06 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.1.0-alt1.2
- add %%set_perl_req_method relaxed

* Fri May 06 2022 Alexey Shabalin <shaba@altlinux.org> 0.1.0-alt1.1
- Update libpve-rs-perl.

* Sun Mar 06 2022 Alexey Shabalin <shaba@altlinux.org> 0.1.0-alt1
- initial build.


Name: libpve-rs-perl
Version: 0.4.4
Release: alt1
Summary: PVE parts which have been ported to Rust
License: GPLv3
Group: System/Libraries
URL: https://git.proxmox.com/git/proxmox-perl-rs.git

Source1: perlmod.tar.xz
Source2: proxmox-openid-rs.tar.xz
Source3: proxmox.tar.xz
Source4: pve-rs-cargo.tar.xz
Source0: pve-rs.tar.xz

Patch1: pve-rs.patch
Patch2: proxmox-openid-rs.patch

ExclusiveArch: x86_64 aarch64
BuildRequires: /proc clang-devel rust-cargo perl-devel libssl-devel libacl-devel libuuid-devel

%description
This package contains the source for the Rust pve-rs crate

%prep
%setup -q -c -n %name -a1 -a2 -a3 -a4
%patch1 -p0 -b .alt
%patch2 -p0 -b .alt
find -name config -delete

%build
export CARGO_HOME=%_builddir/%name/cargo
make -C pve-rs pve BUILD_MODE=release

%install
install -pD -m0644 pve-rs/target/release/libpve_rs.so %buildroot%perl_vendor_autolib/libpve_rs.so
mkdir -p %buildroot%perl_vendor_privlib/PVE/RS
install -m0644 pve-rs/PVE/RS/*.pm %buildroot%perl_vendor_privlib/PVE/RS/

%files
%perl_vendor_autolib/libpve_rs.so
%dir %perl_vendor_privlib/PVE
%dir %perl_vendor_privlib/PVE/RS
%perl_vendor_privlib/PVE/RS/*.pm

%changelog
* Tue Dec 07 2021 Valery Inozemtsev <shrek@altlinux.ru> 0.4.4-alt1
- initial release


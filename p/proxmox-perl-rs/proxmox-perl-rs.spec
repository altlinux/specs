%global _unpackaged_files_terminate_build 1

Name: proxmox-perl-rs
Version: 0.1.0
Release: alt1.2
Summary: PVE and PMG common parts which have been ported to Rust
License: AGPL-3.0+
Group: Development/Other
URL: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/proxmox-perl-rs.git
Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust clang-devel perl-devel
BuildRequires: libssl-devel libacl-devel libuuid-devel
BuildRequires: /proc
%set_perl_req_method relaxed

%description
Contains the perl side of modules provided by the libraries of both
libpve-rs-perl and libpmg-rs-perl, loading whichever is available.

%package -n libproxmox-rs-perl
Summary: PVE/PMG common parts which have been ported to Rust
Version: 0.1.0
Group: Development/Other
Provides: proxmox-perl-rs = %EVR
Provides: proxmox-rs-perl = %EVR

%description -n libproxmox-rs-perl
%summary

%package -n libpve-rs-perl
Summary: PVE parts which have been ported to Rust
Version: 0.6.1
Group: Development/Other
Provides: pve-perl-rs = %EVR
Provides: pve-rs-perl = %EVR

%description -n libpve-rs-perl
%summary

%package -n libpmg-rs-perl
Summary: Components of Proxmox Mail Gateway which have been ported to Rust
Version: 0.5.1
Group: Development/Other
Provides: pmg-perl-rs = %EVR
Provides: pmg-rs-perl = %EVR

%description -n libpmg-rs-perl
%summary

%prep
%setup
%patch -p1

%build
export BUILD_MODE=release
export PERLMOD_WRITE_PACKAGES=1
#%make pve
#%make pmg
#%make build
%make gen
%make pve

%install
install -pD -m0644 target/release/libpve_rs.so %buildroot%perl_vendor_autolib/libpve_rs.so
mkdir -p %buildroot%perl_vendor_privlib/{PVE/RS,Proxmox/Lib,Proxmox/RS}
install -m0644 PVE/RS/*.pm %buildroot%perl_vendor_privlib/PVE/RS/
install -m0644 common/pkg/PVE/RS/*.pm %buildroot%perl_vendor_privlib/PVE/RS/
install -m0644 Proxmox/RS/*.pm %buildroot%perl_vendor_privlib/Proxmox/RS/
install -m0644 Proxmox/Lib/{Common,PVE}.pm %buildroot%perl_vendor_privlib/Proxmox/Lib/

%files -n libpve-rs-perl
%perl_vendor_autolib/libpve_rs.so
%dir %perl_vendor_privlib/PVE/RS
%perl_vendor_privlib/PVE/RS/*.pm

%files -n libproxmox-rs-perl
%dir %perl_vendor_privlib/Proxmox/RS
%perl_vendor_privlib/Proxmox/RS/*
%dir %perl_vendor_privlib/Proxmox/Lib
%perl_vendor_privlib/Proxmox/Lib/*


%changelog
* Fri May 06 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.1.0-alt1.2
- add %%set_perl_req_method relaxed

* Fri May 06 2022 Alexey Shabalin <shaba@altlinux.org> 0.1.0-alt1.1
- Update libpve-rs-perl.

* Sun Mar 06 2022 Alexey Shabalin <shaba@altlinux.org> 0.1.0-alt1
- initial build.


%define _unpackaged_files_terminate_build 1

Name: proxmox-backup-qemu
Summary: Proxmox Backup Server client library for QEMU
Version: 2.0.2
Release: alt1
License: AGPL-3.0+
Group: Archiving/Backup
Url: https://git.proxmox.com/?p=proxmox-backup-qemu.git
Vcs: git://git.proxmox.com/git/proxmox-backup-qemu.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64 ppc64le riscv64 loongarch64

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust clang-devel
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(openssl)
BuildRequires: libfuse3-devel libacl-devel libuuid-devel libsystemd-devel
BuildRequires: /proc

%description
PVE Backup Server client library for QEMU
This library contains the library to access the Proxmox Backup server from
within QEMU.

%package -n lib%name
Summary: Proxmox Backup Server client library for QEMU
Group: System/Libraries
Provides: libproxmox-backup-qemu0 = %EVR
Provides: libpve-backup-qemu = %EVR
Obsoletes: libpve-backup-qemu < %EVR

%description -n lib%name
PVE Backup Server client library for QEMU
This library contains the library to access the Proxmox Backup server from
within QEMU.

%package -n lib%name-devel
Summary: Proxmox Backup Server client library for QEMU development files
Group: Development/Other
Requires: lib%name = %EVR
Provides: libpve-backup-qemu-devel = %EVR
Obsoletes: libpve-backup-qemu-devel < %EVR

%description -n lib%name-devel
PVE Backup Server development environment.
This library contains the library to access the Proxmox Backup server from
within QEMU.

%prep
# Vendoring:
# rm -rf Cargo.lock vendor/*
# cargo vendor
# find vendor -name *.a -delete
# git add -f vendor Cargo.lock ...
%setup

# PATCH: libexecdir for 'file-restore'
sed -i -e 's|/usr/lib/x86_64-linux-gnu/proxmox-backup/file-restore|/usr/libexec/proxmox-backup/file-restore|' vendor/pbs-buildcfg/src/lib.rs

# allow patching vendored rust code
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
	vendor/pbs-buildcfg/.cargo-checksum.json

%build
export REPOID=alt
%rust_build

%install
install -pD -m644 proxmox-backup-qemu.h %buildroot%_includedir/proxmox-backup-qemu.h
install -pD -m644 target/release/libproxmox_backup_qemu.so %buildroot%_libdir/libproxmox_backup_qemu.so.0
ln -s libproxmox_backup_qemu.so.0 %buildroot%_libdir/libproxmox_backup_qemu.so
#%%rust_install

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed May 06 2026 Sergey Konev <darisishe@altlinux.org> 2.0.2-alt1
- 2.0.2

* Mon Aug 18 2025 Sergey Konev <darisishe@altlinux.org> 2.0.1-alt1
- 2.0.1

* Fri Jul 11 2025 Ivan A. Melnikov <iv@altlinux.org> 1.5.1-alt2
- NMU: build on loongarch64

* Fri Mar 07 2025 Sergey Konev <darisishe@altlinux.org> 1.5.1-alt1
- 1.5.1

* Wed Apr 03 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.4.1-alt2
- update cargo vendor

* Mon Dec 04 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.4.1-alt1
- 1.4.1

* Sat May 14 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.3.1-alt1
- 1.3.1-1

* Sun Jan 23 2022 Alexey Shabalin <shaba@altlinux.org> 1.2.1-alt1
- Build as separate package.


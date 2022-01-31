%define _unpackaged_files_terminate_build 1

Name: proxmox-backup-qemu
Summary: Proxmox Backup Server client library for QEMU
Version: 1.2.1
Release: alt1
License: AGPL-3.0+
Group: Archiving/Backup
Url: https://git.proxmox.com/?p=proxmox-backup-qemu.git
Vcs: git://git.proxmox.com/git/proxmox-backup-qemu.git
Source: %name-%version.tar
Patch: %name-%version.patch
Patch0001: 0001-ALT-use-libexedir-for-file-restore.patch

ExclusiveArch: x86_64 aarch64 ppc64le riscv64
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust clang-devel
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(openssl)
BuildRequires: libfuse3-devel libacl-devel libuuid-devel
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
%setup
%patch -p1
%patch0001 -p1

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
* Sun Jan 23 2022 Alexey Shabalin <shaba@altlinux.org> 1.2.1-alt1
- Build as separate package.


Name: bcachefs-tools
Version: 1.4.1
Release: alt2

Summary: Userspace tools and docs for bcachefs
License: GPLv2
Group: System/Kernel and hardware

Url: https://bcachefs.org/
Source: %name-%version-%release.tar

BuildRequires: pkgconfig(blkid)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(liburcu)
BuildRequires: pkgconfig(libsodium)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libkeyutils)
BuildRequires: pkgconfig(systemd)
BuildRequires: libaio-devel

%description
Userspace tools and docs for bcachefs.
Bcachefs is an advanced new filesystem for Linux, with an emphasis
on reliability and robustness and the complete set of features
one would expect from a modern filesystem.

%prep
%setup
sed -ri '/^VERSION/ s,v0.1-nogit,v%version,'  Makefile

%build
%make_build NO_RUST=please EXTRA_CFLAGS='%optflags'

%install
%make_install NO_RUST=please PREFIX=%_prefix ROOT_SBINDIR=%_sbindir DESTDIR=%buildroot install
install -pm0755 mount.bcachefs.sh %buildroot%_sbindir/mount.bcachefs

%define _udevdir %(pkg-config --variable=udevdir udev)
%define _systemunitdir %(pkg-config --variable systemdsystemunitdir systemd)

%files
%doc COPYING README*

%_udevdir/rules.d/*.rules

%_systemunitdir/bcachefsck@.service
%_systemunitdir/system-bcachefsck.slice

%_sbindir/bcachefs
%_sbindir/fsck.bcachefs
%_sbindir/mkfs.bcachefs
%_sbindir/mount.bcachefs

%_man8dir/bcachefs.8*

%changelog
* Fri May 24 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.1-alt2
- rebuilt with usrmerged paths

* Thu Feb 08 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1
- 1.4.1 released

* Thu Nov 16 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.3-alt1
- initial

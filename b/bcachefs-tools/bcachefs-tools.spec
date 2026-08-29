Name: bcachefs-tools
Version: 1.39.2
Release: alt1

Summary: Userspace tools and docs for bcachefs
License: GPLv2
Group: System/Kernel and hardware
URL: https://bcachefs.org/
VCS: http://evilpiepirate.org/git/bcachefs-tools.git

ExclusiveArch: aarch64 x86_64

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: clang-devel
BuildRequires: rust-bindgen rust-cargo /proc
BuildRequires: pkgconfig(blkid)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(liburcu)
BuildRequires: pkgconfig(libsodium)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libkeyutils)
BuildRequires: pkgconfig(libunwind)
BuildRequires: pkgconfig(systemd)
BuildRequires: libaio-devel

%description
Userspace tools and docs for bcachefs.
Bcachefs is an advanced new filesystem for Linux, with an emphasis
on reliability and robustness and the complete set of features
one would expect from a modern filesystem.

%prep
%setup -a1
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 .cargo vendor
%endif
echo %version > .version

%build
%make_build PREFIX=%_prefix ROOT_SBINDIR=%_sbindir

%install
%make_install PREFIX=%_prefix ROOT_SBINDIR=%_sbindir DESTDIR=%buildroot install
rm -f  %buildroot%_sbindir/*.fuse.bcachefs
rm -rf %buildroot%_datadir/initramfs-tools
rm -rf %buildroot%_usrsrc/bcachefs-%version

%files
%doc COPYING README*
%_udevrulesdir/*.rules
%_unitdir/bcachefs-wait-devices@.service
%_sbindir/bcachefs
%_sbindir/fsck.bcachefs
%_sbindir/mkfs.bcachefs
%_sbindir/mount.bcachefs
%_datadir/bash-completion/completions/bcachefs
%_man8dir/bcachefs.8*

%changelog
* Sat Aug 29 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.39.2-alt1
- 1.39.2 released

* Mon Aug 10 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.39.1-alt1
- 1.39.1 released

* Tue Aug 04 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.39.0-alt1
- 1.39.0 released

* Sat Jul 25 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.38.8-alt1
- 1.38.8 released

* Mon Jul 20 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.38.6-alt1
- 1.38.6 released

* Thu Sep 04 2025 Michael Shigorin <mike@altlinux.org> 1.4.1-alt4
- E2K: lcc 1.29 ftbfs workaround (ilyakurdyukov@; mcst#9685)

* Tue Mar 18 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.1-alt3
- fixed FTBFS found after libuserspace-rcu update to 0.15

* Fri May 24 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.1-alt2
- rebuilt with usrmerged paths

* Thu Feb 08 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1
- 1.4.1 released

* Thu Nov 16 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.3-alt1
- initial

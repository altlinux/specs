Name:		mdevctl
Version:	1.1.0
Release:	alt2.22
Summary:	Mediated device management and persistence utility

Group:		System/Configuration/Hardware
License:	LGPLv2
URL:		https://github.com/mdevctl/mdevctl

Source0:	%name-%version.tar
Patch0:		%name-%version.patch

BuildRequires: pkgconfig(udev)
BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: python3-module-docutils

Requires: udev

%description
mdevctl is a utility for managing and persisting devices in the
mediated device device framework of the Linux kernel.  Mediated
devices are sub-devices of a parent device (ex. a vGPU) which
can be dynamically created and potentially used by drivers like
vfio-mdev for assignment to virtual machines.

%prep
%setup
%patch0 -p1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export RST2MAN=rst2man.py
cargo build --offline --release

%install
%makeinstall_std

%check
export RUST_BACKTRACE=1
export RST2MAN=rst2man.py
cargo check
cargo test --release --no-fail-fast

%files
%doc COPYING README.md
%_sbindir/mdevctl
%_sbindir/lsmdev
%_udevrulesdir/60-mdevctl.rules
%_sysconfdir/mdevctl.d
%_man8dir/mdevctl.8*
%_man8dir/lsmdev.8*
%_datadir/bash-completion/completions/*

%changelog
* Fri Mar 18 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.1.0-alt2.22
- update to upstream, fix for rst2man
- package mdevctl.d directory

* Mon Jan 24 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.1.0-alt2.20
- update to recent upstream

* Fri Sep 10 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.1.0-alt1
- new version 1.1.0
- enable %%check

* Sat Jul 10 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Fri Jun 25 2021 Alexey Shabalin <shaba@altlinux.org> 0.81-alt1
- new version 0.81

* Tue Dec 15 2020 Alexey Shabalin <shaba@altlinux.org> 0.78-alt1
- new version 0.78

* Tue Sep 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.69-alt1
- 0.69

* Fri Jul 10 2020 Alexey Shabalin <shaba@altlinux.org> 0.61-alt1
- Initial build


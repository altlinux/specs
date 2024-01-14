Name:		mdevctl
Version:	1.3.0
Release:	alt3
Summary:	Mediated device management and persistence utility

Group:		System/Configuration/Hardware
License:	LGPLv2
URL:		https://github.com/mdevctl/mdevctl

Source0:	%name-%version.tar
Patch0:		%name-%version.patch
Patch3500:	%name-1.3.0-alt-nix-loongarch64.patch

BuildRequires: pkgconfig(udev)
BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: python3-module-docutils
BuildRequires: systemd
BuildRequires: cargo-vendor-checksum diffstat

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
# patch vendored nix crate
%patch3500 -p1
# update checksums
diffstat -p1 -l %PATCH3500 | sed -re 's@vendor/@@' | xargs cargo-vendor-checksum -f

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export RST2MAN=rst2man
cargo build --offline --release

%install
%makeinstall_std

%check
export RUST_BACKTRACE=1
export RST2MAN=rst2man
cargo check
cargo test --release --no-fail-fast

%files
%doc COPYING README.md
%_sbindir/mdevctl
%_sbindir/lsmdev
%_udevrulesdir/60-mdevctl.rules
%_sysconfdir/mdevctl.d
/usr/lib/%name
%_man8dir/mdevctl.8*
%_man8dir/lsmdev.8*
%_datadir/bash-completion/completions/*

%changelog
* Sun Jan 14 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.3.0-alt3
- add scripts.d subdirs (Closes: #49068)

* Thu Jan 11 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.3.0-alt2
- NMU: fixed FTBFS on LoongArch

* Tue Jan 09 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.3.0-alt1
- new version 1.3.0

* Sat Aug 06 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sat Apr 16 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.1.0-alt3.22
- spec: fix build with rst2man

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


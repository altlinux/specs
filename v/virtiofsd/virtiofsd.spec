%global _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec

Name: virtiofsd
Version: 1.8.0
Release: alt1
Summary: Virtio-fs vhost-user device daemon (Rust version)
Group: Emulators
License: Apache-2.0 AND BSD-3-Clause
Url: https://gitlab.com/virtio-fs/virtiofsd
Source: %name-%version.tar
Patch: %name-%version.patch

ExcludeArch: %arm %ix86 %mips32

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libcap-ng-devel
BuildRequires: libseccomp-devel
BuildRequires: /proc

Requires: qemu-common
Provides: vhostuser-backend(fs)
Conflicts: qemu-virtiofsd

%description
%summary.

%prep
%setup
%patch -p1
mkdir -p .cargo
cat >.cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install -t %_libexecdir
install -D -p -m 0644 50-qemu-virtiofsd.json %buildroot%_datadir/qemu/vhost-user/50-qemu-virtiofsd.json

%files
%doc README.md
%_libexecdir/virtiofsd
%_datadir/qemu/vhost-user/50-qemu-virtiofsd.json

%changelog
* Mon Oct 23 2023 Alexey Shabalin <shaba@altlinux.org> 1.8.0-alt1
- New version 1.8.0.

* Tue Jul 04 2023 Alexey Shabalin <shaba@altlinux.org> 1.6.1-alt1
- New version 1.6.1.

* Wed Apr 26 2023 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- Initial package.



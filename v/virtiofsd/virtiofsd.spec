%global _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec

Name: virtiofsd
Version: 1.11.1
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

Provides: vhostuser-backend(fs)
Conflicts: qemu-virtiofsd
Conflicts: pve-qemu-system < 8.1.5

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

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
%rust_build

%install
%rust_install -t %_libexecdir
install -D -p -m 0644 50-virtiofsd.json %buildroot%_datadir/qemu/vhost-user/50-virtiofsd.json

%files
%doc README.md
%_libexecdir/virtiofsd
%_datadir/qemu/vhost-user/50-virtiofsd.json

%changelog
* Thu Jul 18 2024 Alexey Shabalin <shaba@altlinux.org> 1.11.1-alt1
- New version 1.11.1.

* Mon Jun 24 2024 Alexey Shabalin <shaba@altlinux.org> 1.11.0-alt1
- New version 1.11.0.

* Tue Apr 16 2024 Alexey Shabalin <shaba@altlinux.org> 1.10.1-alt1
- 1.10.1
- Allow install with pve-qemu (drop R: qemu-common) (ALT#50017).

* Mon Jan 15 2024 Alexey Shabalin <shaba@altlinux.org> 1.9.0-alt1
- New version 1.9.0.

* Mon Oct 23 2023 Alexey Shabalin <shaba@altlinux.org> 1.8.0-alt1
- New version 1.8.0.

* Tue Jul 04 2023 Alexey Shabalin <shaba@altlinux.org> 1.6.1-alt1
- New version 1.6.1.

* Wed Apr 26 2023 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- Initial package.



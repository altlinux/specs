%define _unpackaged_files_terminate_build 1

Name:    oci-registry
Version: 0.4.5
Release: alt1

Summary: An implementation of the OCI Registry spec
License: MIT
Group:   Other
Url:     https://github.com/mcronce/oci-registry

Source: %name-%version.tar
Source2: %name.service
Source3: %name.sysconfig
Patch: %name-%version-%release.patch
#upstream supports x86_64 and aarch64
ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: pkgconfig(libzstd)

Requires: containers-common

%description
oci-registry is an implementation of the OCI Registry spec with
filesystem and S3 storage back-ends. Features: pull-through cache
for any registry, not just docker.io; filesystem and S3 storage
back-ends; small footprint; helm charts.

%prep
%setup
%patch -p1

mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/mcronce/dkregistry-rs.git"]
git = "https://github.com/mcronce/dkregistry-rs.git"
replace-with = "vendored-sources"

[source."git+https://github.com/mcronce/rusoto.git?branch=enable-http1"]
git = "https://github.com/mcronce/rusoto.git"
branch = "enable-http1"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[env]
ZSTD_SYS_USE_PKG_CONFIG = "1"

[profile.release]
strip = false
EOF

%build
%rust_build

%install
%rust_install
install -Dm 0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -Dm 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
mkdir -p %buildroot%_localstatedir/%name/data
install -Dm 0640 example.yaml %buildroot%_sysconfdir/%name/config.yaml

%check
%rust_test

%pre
groupadd -r -f %name 2>/dev/null ||:
useradd -r -g %name -c 'Oci-registry daemon' \
         -s /bin/bash  -d %_localstatedir/%name %name 2>/dev/null ||:

%files
%doc README.md
%_bindir/%name
%dir %_sysconfdir/%name
%config(noreplace) %attr(0640,root,%name) %_sysconfdir/%name/config.yaml
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %attr(0750,%name,%name) %_localstatedir/%name
%dir %attr(0750,%name,%name) %_localstatedir/%name/data
%_unitdir/%name.service

%changelog
* Thu Dec 19 2024 Nadezhda Fedorova <fedor@altlinux.org> 0.4.5-alt1
- Initial build for ALTLinux.

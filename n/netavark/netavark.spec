%global _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec

Name: netavark
Version: 1.4.0
Release: alt1
License: Apache-2.0
Summary: OCI network stack
Group: Development/Other
Url: https://github.com/containers/%name
Vcs: https://github.com/containers/%name
Source: %name-%version.tar
Patch: %name-%version.patch

#Recommends: aardvark-dns >= 1.0.3
Provides: container-network-stack = 2

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: go-md2man
BuildRequires: /proc

%description
%summary.

Netavark is a rust based network stack for containers. It is being
designed to work with Podman but is also applicable for other OCI
container management applications.

Netavark is a tool for configuring networking for Linux containers.
Its features include:
* Configuration of container networks via JSON configuration file
* Creation and management of required network interfaces,
    including MACVLAN networks
* All required firewall configuration to perform NAT and port
    forwarding as required for containers
* Support for iptables and firewalld at present, with support
    for nftables planned in a future release
* Support for rootless containers
* Support for IPv4 and IPv6
* Support for container DNS resolution via aardvark-dns.

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
%make_build

cd docs
go-md2man -in %name.1.md -out %name.1

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc README.md
%_libexecdir/podman/%name
%_man1dir/%name.1*

%changelog
* Wed Jan 11 2023 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- new version 1.4.0

* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sun Jul 31 2022 Alexey Shabalin <shaba@altlinux.org> 1.1.0-alt1
- Initial build.


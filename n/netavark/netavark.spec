%global _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec
# nftables or iptables
%define default_fw nftables

Name: netavark
Version: 1.12.2
Release: alt1
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT
Summary: OCI network stack
Group: Development/Other
Url: https://github.com/containers/%name
Vcs: https://github.com/containers/%name
Source: %name-%version.tar
Patch: %name-%version.patch
Patch1: vendored-nix-loongarch64-support.patch
ExcludeArch: %arm %ix86

# Minimum X.Y dep for aardvark-dns
%define major_minor %((v=%version; echo ${v%.*}))
Requires: aardvark-dns >= %major_minor
Provides: container-network-stack = 2
%if "%default_fw" == "nftables"
Requires: nftables
%else
Requires: iptables
%endif
BuildRequires(pre): rpm-macros-rust rpm-macros-systemd
BuildRequires: rpm-build-rust rpm-build-systemd
BuildRequires: go-md2man
BuildRequires: /usr/bin/protoc
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

[source."https://github.com/containers/netavark-dhcp-proxy"]
git = "https://github.com/containers/netavark-dhcp-proxy"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false
EOF

%patch1 -p1
# allow patching vendored rust code
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    ./vendor/nix-0.26.4/.cargo-checksum.json

%build
NETAVARK_DEFAULT_FW=%{default_fw} %make_build

pushd docs
go-md2man -in %name.1.md -out %name.1
popd

%install
%makeinstall_std PREFIX=%_prefix SYSTEMDDIR=%_unitdir LIBEXECDIR=%_libexecdir

%post
%post_systemd_postponed %name-dhcp-proxy.service
%post_systemd_postponed %name-firewalld-reload.service

%preun
%preun_systemd %name-dhcp-proxy.service
%preun_systemd %name-firewalld-reload.service

%files
%doc README.md
%_libexecdir/podman/%name
%_man1dir/%name.1*
%_unitdir/*

%changelog
* Thu Aug 22 2024 Alexey Shabalin <shaba@altlinux.org> 1.12.2-alt1
- New version 1.12.2.

* Fri May 31 2024 Alexey Shabalin <shaba@altlinux.org> 1.11.0-alt1
- New version 1.11.0.
- Switch default firewall to nftables.

* Sat Mar 23 2024 Ivan A. Melnikov <iv@altlinux.org> 1.10.3-alt1.1
- Fix FTBFS on loongarch64.

* Fri Mar 22 2024 Alexey Shabalin <shaba@altlinux.org> 1.10.3-alt1
- New version 1.10.3.

* Mon Dec 11 2023 Alexey Shabalin <shaba@altlinux.org> 1.9.0-alt1
- New version 1.9.0.

* Fri Oct 06 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.8.0-alt2
- NMU: fixed FTBFS on LoongArch.

* Fri Oct 06 2023 Alexey Shabalin <shaba@altlinux.org> 1.8.0-alt1
- New version 1.8.0.

* Tue May 02 2023 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- New version 1.6.0.

* Mon Feb 27 2023 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt1
- new version 1.5.0

* Wed Jan 11 2023 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- new version 1.4.0

* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sun Jul 31 2022 Alexey Shabalin <shaba@altlinux.org> 1.1.0-alt1
- Initial build.


%define _unpackaged_files_terminate_build 1

Name: yggdrasil
Version: 0.4.3
Release: alt1

Summary: End-to-end encrypted IPv6 networking
License: LGPLv3
Group: Security/Networking
Url: https://yggdrasil-network.github.io

Source: %name-%version.tar
Patch0: go_mod_vendor.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
Yggdrasil is an overlay network implementation of a new routing scheme for mesh
networks. It is designed to be a future-proof decentralised alternative to the
structured routing protocols commonly used today on the Internet and other
networks.

The current implementation of Yggdrasil is a lightweight userspace software
router which is easy to configure and supported on a wide range of platforms.
It provides end-to-end encrypted IPv6 routing between all network participants.
Peerings between nodes can be configured using TCP/TLS connections over local
area networks, point-to-point links or the Internet. Even though the Yggdrasil
Network provides IPv6 routing between nodes, peering connections can be set up
over either IPv4 or IPv6.

%prep
%setup
%patch0 -p1

%build
%gobuild -o %_builddir/ ./cmd/*
cp -r LICENSE README.md CHANGELOG.md contrib/systemd/* %_builddir/

%install
mkdir -p %buildroot

cd %_builddir

sed -i yggdrasil-default-config.service -e 's/\/usr\/bin\/chmod/\/bin\/chmod/g'

install -pD yggdrasil %buildroot%_bindir/yggdrasil
install -pD yggdrasilctl %buildroot%_bindir/yggdrasilctl
install -pD yggdrasil.service %buildroot%_unitdir/yggdrasil.service
install -pD yggdrasil-default-config.service %buildroot%_unitdir/yggdrasil-default-config.service

%files
%doc LICENSE README.md CHANGELOG.md
%attr(0755,root,root) %_bindir/*
%attr(0644,root,root) %_unitdir/*

%pre
/usr/sbin/groupadd -r -f yggdrasil

%changelog
* Mon May 30 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.3-alt1
- initial build for Sisyphus

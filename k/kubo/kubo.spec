Name: kubo
Version: 0.23.0
Release: alt1

Summary: IPFS implementation in Go

License: MIT
Group: File tools
Url: https://github.com/ipfs/kubo

# Source-url: https://github.com/ipfs/kubo/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
# systemd macro
BuildRequires(pre): rpm-build-compat


ExclusiveArch: %go_arches

BuildRequires: git-core
BuildRequires: golang

#Requires: fuse
#Requires: nss-myhostname
#Requires: udev-rules
Obsoletes: go-ipfs
Provides: go-ipfs = %version

%description
IPFS is a global, versioned, peer-to-peer filesystem. It combines good ideas
from Git, BitTorrent, Kademlia, SFS, and the Web. It is like a single bittorrent
swarm, exchanging git objects. kubo (previously go-ipfs) provides an interface
as simple as the HTTP web, but with permanence built in. You can also mount the
world at /ipfs.

%prep
%setup -a1

%build
export GOTAGS=openssl
go build -mod=vendor -buildmode=pie -o ./cmd/ipfs/ipfs ./cmd/ipfs

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_userunitdir
mkdir -p %buildroot%_unitdir

cp cmd/ipfs/ipfs %buildroot%_bindir
cat << EOF >>  %buildroot%_userunitdir/ipfs.service
[Unit]
Description=InterPlanetary File System (IPFS) daemon

[Service]
ExecStart=%_bindir/ipfs daemon
Restart=on-failure

[Install]
WantedBy=default.target
EOF
cat << EOF >> %buildroot%_unitdir/ipfs@.service
[Unit]
Description=InterPlanetary File System (IPFS) daemon

[Service]
User=%%i
ExecStart=%_bindir/ipfs daemon
Restart=on-failure

[Install]
WantedBy=default.target
EOF

%files
%_bindir/ipfs
%_userunitdir/ipfs.service
%_unitdir/ipfs@.service
%doc LICENSE*
%doc docs/*

%changelog
* Sun Nov 05 2023 Vitaly Lipatov <lav@altlinux.ru> 0.23.0-alt1
- new version 0.23.0 (with rpmrb script)

* Sat Aug 12 2023 Vitaly Lipatov <lav@altlinux.ru> 0.22.0-alt1
- new version 0.22.0 (with rpmrb script)

* Fri Aug 04 2023 Vitaly Lipatov <lav@altlinux.ru> 0.21.0-alt1
- new version 0.21.0 (with rpmrb script)

* Wed Apr 19 2023 Vitaly Lipatov <lav@altlinux.ru> 0.19.1-alt1
- new version 0.19.1 (with rpmrb script)

* Wed Apr 19 2023 Vitaly Lipatov <lav@altlinux.ru> 0.18.1-alt1
- initial build for ALT Sisyphus (thanks, Mageia!)

# TODO: build from source

Name: go-ipfs
Version: 0.4.13
Release: alt1

Summary: IPFS implementation in Go

License: MIT
Group: File tools
Url: https://github.com/ipfs/go-ipfs

Packager: Vitaly Lipatov <lav@altlinux.ru>

# TODO:
## Source-url: https://dist.ipfs.io/go-ipfs/v%version/go-ipfs_v%{version}_linux-386.tar.gz
#Source: %name-x86-%version.tar

# Source-url: https://dist.ipfs.io/go-ipfs/v%version/go-ipfs_v%{version}_linux-amd64.tar.gz
#Source: %name-x86_64-%version.tar

# Source-url: https://dist.ipfs.io/go-ipfs/v%version/go-ipfs_v%{version}_linux-amd64.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64

%description
TODO: build from source

IPFS is a global, versioned, peer-to-peer filesystem. It combines good ideas from
Git, BitTorrent, Kademlia, SFS, and the Web. It is like a single bittorrent swarm,
exchanging git objects. IPFS provides an interface as simple as the HTTP web, but
with permanence built in. You can also mount the world at /ipfs.

For more info see: https://github.com/ipfs/ipfs.

%prep
%setup

%install
install -m755 -D ipfs %buildroot%_bindir/ipfs

%files
%doc LICENSE README.md
%_bindir/ipfs

%changelog
* Fri Dec 29 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.13-alt1
- new version 0.4.13 (with rpmrb script)

* Mon Oct 02 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.11-alt1
- new version 0.4.11 (with rpmrb script)

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.10-alt1
- new version 0.4.10 (with rpmrb script)

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.9-alt1
- new version 0.4.9 (with rpmrb script)

* Wed Mar 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.7-alt1
- new version 0.4.7 (with rpmrb script)

* Mon Mar 06 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.6-alt1
- initial build for ALT Linux Sisyphus

# TODO: build from source

Name: go-ipfs
Version: 0.4.6
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
* Mon Mar 06 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.6-alt1
- initial build for ALT Linux Sisyphus

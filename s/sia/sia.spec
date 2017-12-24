# TODO: build from source

Name: sia
Version: 1.3.1
Release: alt1

Summary: Blockchain-based marketplace for file storage

License: MIT
Group: File tools
Url: https://sia.tech

Packager: Vitaly Lipatov <lav@altlinux.ru>

# TODO:
## Source-url: https://dist.ipfs.io/go-ipfs/v%version/go-ipfs_v%{version}_linux-386.tar.gz
#Source: %name-x86-%version.tar

# Source-url: https://dist.ipfs.io/go-ipfs/v%version/go-ipfs_v%{version}_linux-amd64.tar.gz
#Source: %name-x86_64-%version.tar

# Source-url: https://github.com/NebulousLabs/Sia/releases/download/v%version/Sia-v%version-linux-amd64.zip
Source: %name-%version.tar

ExclusiveArch: x86_64

%description
TODO: build from source

Sia is a new decentralized cloud storage platform that radically alters the landscape of cloud storage.
By leveraging smart contracts, client-side encryption, and sophisticated redundancy (via Reed-Solomon codes),
Sia allows users to safely store their data with hosts that they do not know or trust.
The result is a cloud storage marketplace where hosts compete to offer the best service at the lowest price.
And since there is no barrier to entry for hosts,
anyone with spare storage capacity can join the network and start making money.

%prep
%setup

%install
install -m755 -D siad %buildroot%_bindir/siad
install -m755 -D siac %buildroot%_bindir/siac

%files
%doc doc/* README.md
%_bindir/siad
%_bindir/siac

%changelog
* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Fri Oct 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- initial build for ALT Sisyphus

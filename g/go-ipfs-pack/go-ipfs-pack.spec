# TODO: build from source

Name: go-ipfs-pack
Version: 0.6.0
Release: alt1

Summary: ipfs-pack filesystem packing tool

License: MIT
Group: File tools
Url: https://github.com/ipfs/ipfs-pack

Packager: Vitaly Lipatov <lav@altlinux.ru>

# TODO:
## Source-url: https://dist.ipfs.io/go-ipfs/v%version/go-ipfs_v%{version}_linux-386.tar.gz
#Source: %name-x86-%version.tar

# Source-url: https://dist.ipfs.io/go-ipfs/v%version/go-ipfs_v%{version}_linux-amd64.tar.gz
#Source: %name-x86_64-%version.tar

# Source-url: https://dist.ipfs.io/ipfs-pack/v%version/ipfs-pack_v%{version}_linux-amd64.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64

%description
TODO: build from source

ipfs-pack is a tool and library to work with ipfs and large collections of data in UNIX/POSIX filesystems.

* It identifies singular collections or bundles of data (the pack).
* It creates a light-weight cryptographically secure manifest that
  preserves the integrity of the collection over time, and travels with the data (PackManifest).
* It helps use ipfs in a mode that references the filesystem files directly and avoids duplicating data (filestore).
* It carries a standard dataset metadata file to capture and present information about the dataset (data-package.json).
* It helps verify the authenticity of data through a file carrying cryptographic signatures (PackAuth).

%prep
%setup

%install
install -m755 -D ipfs-pack %buildroot%_bindir/ipfs-pack

%files
%_bindir/ipfs-pack

%changelog
* Fri Dec 29 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Sisyphus

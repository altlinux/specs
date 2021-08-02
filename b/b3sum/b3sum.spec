Name:     b3sum
Version:  1.0.0
Release:  alt1

Summary:  A command line utility for calculating BLAKE3 hashes
License:  Apache-2.0
Group:    Development/Tools
Url:      https://github.com/sharkdp/hyperfine

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
A command line utility for calculating BLAKE3 hashes, similar to Coreutils
tools like b2sum or md5sum.

%prep
%setup
%patch -p1

%build
cd b3sum
%rust_build

%install
cd b3sum
%rust_install

%check
cd b3sum
%rust_test

%files
%_bindir/*
%doc *.md

%changelog
* Mon Aug 02 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

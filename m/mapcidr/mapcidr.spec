Name: mapcidr
Version: 1.1.97
Release: alt1

Summary: Utility to perform multiple operations for a given subnet/CIDR ranges

License: MIT
Group: Networking/Other
URL: https://github.com/projectdiscovery/mapcidr

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/projectdiscovery/mapcidr/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: golang

%description
mapcidr is developed to ease load distribution for mass scanning operations,
it can be used both as a library and as independent CLI tool.

It provides utility to perform multiple operations for a given subnet/CIDR
ranges including CIDR expansion, slicing, aggregation, IP filtering/matching,
format conversion and host counting.

%prep
%setup -a1

%build
go build -mod=vendor -buildmode=pie -o mapcidr ./cmd/mapcidr

%install
install -Dp -m 0755 mapcidr %buildroot%_bindir/mapcidr

%files
%_bindir/mapcidr
%doc README.md

%changelog
* Wed Apr 01 2026 Vitaly Lipatov <lav@altlinux.ru> 1.1.97-alt1
- initial build for ALT Sisyphus


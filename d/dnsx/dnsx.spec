%define gobuild go build

Name: dnsx
Version: 1.2.3
Release: alt1

Summary: A fast and multi-purpose DNS toolkit

License: MIT
Group: Networking/DNS
URL: https://github.com/projectdiscovery/dnsx
# Source-url: https://github.com/projectdiscovery/dnsx.git
Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
ExclusiveArch: %go_arches

BuildRequires: golang >= 1.21

%description
dnsx is a fast and multi-purpose DNS toolkit designed for running various
probes through the retryabledns library. It supports multiple DNS queries,
user supplied resolvers, DNS wildcard filtering and more.

%prep
%setup -a1

%build
export GOFLAGS="-mod=vendor"
%gobuild -o dnsx github.com/projectdiscovery/dnsx/cmd/dnsx

%install
install -Dpm 0755 dnsx %buildroot%_bindir/dnsx

%files
%doc README.md LICENSE.md
%_bindir/dnsx

%changelog
* Thu Apr 02 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt1
- initial build for ALT Sisyphus

Name: puredns
Version: 2.1.1
Release: alt1

Summary: Fast domain resolver and subdomain bruteforcing tool

License: GPL-3.0-or-later
Group: Networking/Other
URL: https://github.com/d3mondev/puredns
# Source-url: https://github.com/d3mondev/puredns.git
Source: %name-%version.tar
Source1: %name-development-%version.tar

ExclusiveArch: %go_arches
ExcludeArch: %ix86

Requires: /usr/bin/massdns

BuildRequires(pre): rpm-macros-golang
BuildRequires: golang

%description
puredns is a fast domain resolver and subdomain bruteforcing tool that can
accurately filter out wildcard subdomains and DNS poisoned entries.

It uses massdns, a powerful stub DNS resolver, to perform bulk lookups.
With puredns, you can resolve a list of domains, bruteforce subdomains
using a wordlist, and filter out wildcard subdomains and DNS poisoned
entries.

%prep
%setup -a1

%build
export GOFLAGS="-mod=vendor"
go build -v -buildmode=pie -o %name .

%install
install -Dp -m 755 %name %buildroot%_bindir/%name

%files
%_bindir/%name
%doc README.md

%changelog
* Thu Apr 02 2026 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- initial build for ALT Sisyphus

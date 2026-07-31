%define _unpackaged_files_terminate_build 1

Name: subfinder
Version: 2.14.0
Release: alt1

Summary: Fast passive subdomain enumeration tool
License: MIT
Group: Security/Networking
Url: https://projectdiscovery.io
Vcs: https://github.com/projectdiscovery/subfinder

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
subfinder is a subdomain discovery tool that returns valid subdomains
for websites, using passive online sources. It has a simple, modular
architecture and is optimized for speed. subfinder is built for doing
one thing only - passive subdomain enumeration, and it does that very well.
We have made it to comply with all the used passive source licenses and
usage restrictions. The passive model guarantees speed and stealthiness
that can be leveraged by both penetration testers and bug bounty hunters alike.

%prep
%setup -a1

%build
export LDFLAGS='-s -w'
%gobuild -mod=vendor -o "subfinder" cmd/subfinder/main.go

%install
install -Dm0755 %name %buildroot%_bindir/%name

%files
%doc *.md
%_bindir/%name


%changelog
* Thu Jul 23 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 2.14.0-alt1
- Initial build for Sisyphus.


%define _unpackaged_files_terminate_build 1

Name: gost
Version: 3.3.0
Release: alt1

Summary: Simple tunnel written in Go

License: MIT
Group: Networking/Other
Url: https://gost.run
Vcs: https://github.com/go-gost/gost

# Source-url: https://github.com/go-gost/gost/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.26.3

%description
GOST is a secure tunnel written in Go. It supports multi-level proxy chains,
port forwarding, reverse proxying, multiple proxy and tunnel protocols,
load balancing, routing controls, access controls, and traffic limiting.

%prep
%setup -a1

%build
%gobuild -mod=vendor -o gost ./cmd/gost

%install
install -Dm0755 gost %buildroot%_bindir/gost

%check
./gost -V

%files
%_bindir/gost
%doc README.md README_en.md LICENSE

%changelog
* Sun Sep 20 2026 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- Initial build for ALT Sisyphus.

Name: wireguard-go
Version: 0.0.20230223
Release: alt1

Summary: Go Implementation of WireGuard
License: MIT
Group: System/Servers

Url: https://www.wiregurard.com/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://git.zx2c4.com/%name/snapshot/%name-%version.tar.xz
Source0: %name-%version.tar
# go mod vendor
Source1: vendor.tar

BuildRequires: golang
BuildRequires: python3

%description
This is an implementation of WireGuard in Go.

%prep
%setup -a 1

%build
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_bindir/%name

%changelog
* Sun Aug 18 2024 Nazarov Denis <nenderus@altlinux.org> 0.0.20230223-alt1
- Initial build for ALT Linux


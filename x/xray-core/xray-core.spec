Name: xray-core
Version: 24.9.7
Release: alt1

Summary: Project X
License: MPL-2.0
Group: System/Servers

Url: https://xtls.github.io/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/XTLS/Xray-core/archive/v%version/Xray-core-%version.tar.gz
Source0: Xray-core-%version.tar
# go mod vendor
Source1: vendor.tar

Source2: xray.service
Source3: xray@.service

BuildRequires: golang
BuildRequires: python3

%description
Project X originates from XTLS protocol, providing a set of network tools such as Xray-core and REALITY.

%prep
%setup -n Xray-core-%version -a 1

%build
%make_build

%install
%__mkdir_p %buildroot{%_bindir,%_unitdir}
%__install -Dp -m0755 xray %buildroot%_bindir/
%__install -Dp -m0644 %SOURCE2 %buildroot%_unitdir/
%__install -Dp -m0644 %SOURCE3 %buildroot%_unitdir/

%preun
%preun_systemd xray

%files
%doc CODE_OF_CONDUCT.md README.md
%_bindir/xray
%_unitdir/xray.service
%_unitdir/xray@.service

%changelog
* Sat Sep 07 2024 Nazarov Denis <nenderus@altlinux.org> 24.9.7-alt1
- New version 24.9.7.

* Fri Aug 30 2024 Nazarov Denis <nenderus@altlinux.org> 1.8.24-alt1
- New version 1.8.24.

* Wed Aug 21 2024 Nazarov Denis <nenderus@altlinux.org> 1.8.23-alt1
- Initial build for ALT Linux


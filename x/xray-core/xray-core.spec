%define git_version v1.260327.0

Name: xray-core
Version: 26.3.27
Release: alt1

Summary: Project X
License: MPL-2.0
Group: System/Servers

Url: https://xtls.github.io/
Vcs: https://github.com/XTLS/Xray-core
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
go build -o xray -trimpath -ldflags "-X github.com/xtls/xray-core/core.build=%git_version -s -w -buildid=" -v ./main

%install
%__mkdir_p %buildroot{%_bindir,%_unitdir}
%__install -Dp -m0755 xray %buildroot%_bindir/
%__install -Dp -m0644 %SOURCE2 %buildroot%_unitdir/
%__install -Dp -m0644 %SOURCE3 %buildroot%_unitdir/

%post
%post_systemd_postponed xray

%preun
%systemd_preun xray

%files
%doc CODE_OF_CONDUCT.md README.md
%_bindir/xray
%_unitdir/xray.service
%_unitdir/xray@.service

%changelog
* Tue Apr 14 2026 Nazarov Denis <nenderus@altlinux.org> 26.3.27-alt1
- New version 26.3.27. (ALT #58696)

* Sat Jan 24 2026 Nazarov Denis <nenderus@altlinux.org> 26.1.23-alt1
- New version 26.1.23.

* Thu Dec 25 2025 Nazarov Denis <nenderus@altlinux.org> 25.12.8-alt1
- New version 25.12.8.

* Sun Aug 03 2025 Nazarov Denis <nenderus@altlinux.org> 25.8.3-alt1
- New version 25.8.3.

* Sat Jul 26 2025 Nazarov Denis <nenderus@altlinux.org> 25.7.26-alt1
- New version 25.7.26.

* Fri Jul 25 2025 Nazarov Denis <nenderus@altlinux.org> 25.7.25-alt1
- New version 25.7.25.

* Thu Jul 24 2025 Nazarov Denis <nenderus@altlinux.org> 25.6.8-alt1
- New version 25.6.8.

* Mon Sep 30 2024 Nazarov Denis <nenderus@altlinux.org> 24.9.30-alt1
- New version 24.9.30.

* Fri Sep 20 2024 Nazarov Denis <nenderus@altlinux.org> 24.9.19-alt1
- New version 24.9.19.

* Sat Sep 07 2024 Nazarov Denis <nenderus@altlinux.org> 24.9.7-alt1
- New version 24.9.7.

* Fri Aug 30 2024 Nazarov Denis <nenderus@altlinux.org> 1.8.24-alt1
- New version 1.8.24.

* Wed Aug 21 2024 Nazarov Denis <nenderus@altlinux.org> 1.8.23-alt1
- Initial build for ALT Linux


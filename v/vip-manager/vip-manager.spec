%global import_path github.com/cybertec-postgresql/vip-manager
Name:     vip-manager
Version:  4.2.0
Release:  alt1

Summary:  Manages a virtual IP based on state kept in etcd or Consul
License:  BSD-2-Clause
Group:    Other
Url:      https://github.com/cybertec-postgresql/vip-manager

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

Source1: vip-manager@.service
Source2: vip.in

Patch1:   debian-disable_windows_build.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup
%patch1 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -pDm 0644 %SOURCE1 %buildroot%_unitdir/vip-manager@.service
install -pDm 0644 vip-manager.service %buildroot%_unitdir/vip-manager.service
install -pDm 0644 vipconfig/vip-manager.yml %buildroot%_sysconfdir/default/vip-manager.yml
install -pDm 0644 %SOURCE2 %buildroot%_sysconfdir/patroni/vip.in

%files
%_bindir/*
%_unitdir/vip-manager@.service
%_unitdir/vip-manager.service
%config(noreplace) %_sysconfdir/patroni/vip.in
%config(noreplace) %_sysconfdir/default/vip-manager.yml
%doc *.md

%changelog
* Mon Jun 01 2026 Nikolay Burykin <bne@altlinux.org> 4.2.0-alt1
- 4.2.0

* Wed May 31 2023 Nikolay Burykin <bne@altlinux.org> 1.0.2-alt2
- Backported fix VIP address lookup in IP address list from 2.1.0

* Wed May 31 2023 Nikolay Burykin <bne@altlinux.org> 1.0.2-alt1
- 1.0.2

* Wed Mar 09 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

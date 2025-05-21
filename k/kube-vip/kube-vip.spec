%define _unpackaged_files_terminate_build 1
%define import_path github.com/kube-vip/kube-vip

Name: kube-vip
Version: 0.9.1
Release: alt1

Summary: Lightweight Virtual IP and Load Balancer for Kubernetes High-Availability
Summary(ru_RU.UTF-8): Легковесный виртуальный IP и балансировщик нагрузки Kubernetes
License: Apache-2.0
Group: Networking/Other
Url: https://kube-vip.io
Vcs: https://github.com/kube-vip/kube-vip

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang
%if_with check
BuildRequires: golang
%endif

%description
kube-vip provides a lightweight and efficient virtual IP (VIP)
solution along with load balancing capabilities for Kubernetes
clusters. Written in Go, it supports ARP, BGP, and IPVS modes,
enabling highly available control planes and LoadBalancer-type
Services, especially suitable for bare-metal environments.

%description -l ru_RU.UTF-8
kube-vip предоставляет легковесное и эффективное решение для
управления виртуальными IP-адресами (VIP) и балансировки нагрузки
в Kubernetes-кластерах. Написан на языке Go и поддерживает режимы
работы через ARP, BGP и IPVS. Используется для обеспечения высокой
доступности control-plane и реализации Service типа LoadBalancer,
особенно востребованных в инфраструктуре bare-metal.

%prep
%setup
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="$BUILDDIR:%import_path"
export GOPATH="%go_path"
%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%check
go test -v ./...

%files
%doc README.md LICENSE
%_bindir/kube-vip

%changelog
* Tue May 20 2025 Denis Sergeev <zeff@altlinux.org> 0.9.1-alt1
- 0.6.3 -> 0.9.1.

* Fri Nov 24 2023 Egor Ignatov <egori@altlinux.org> 0.6.3-alt1
- 0.6.3

* Sun May 28 2023 Egor Ignatov <egori@altlinux.org> 0.6.0-alt1
- 0.6.0

* Wed Apr 12 2023 Oleg Obidin <nofex@altlinux.org> 0.5.11-alt1
- 0.5.11

* Thu Nov 24 2022 Egor Ignatov <egori@altlinux.org> 0.5.6-alt1
- 0.5.6

* Sun Oct 23 2022 Egor Ignatov <egori@altlinux.org> 0.5.5-alt1
- First build for ALT

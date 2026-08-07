%define _unpackaged_files_terminate_build 1

%ifarch riscv64
# On riscv64, pie buildmode requires cgo, which is disabled in this package
%define golang_buildmode_pie %nil
%endif

Name: calico
Version: 3.32.1
Release: alt2

Summary: Cloud native networking and network security
License: Apache-2.0 AND GPL-2.0-or-later
Group: System/Configuration/Networking
Url: https://projectcalico.org
Vcs: https://github.com/projectcalico/calico

Source0: %name-%version.tar
Source1: vendor.tar

# Calico uses runit internally, but we don't need /etc/rc.local in ALT Linux
%filter_from_requires /\/etc\/rc\.local/d

Requires: iproute2
Requires: iptables
Requires: kmod
Requires: runit
Requires: bird2

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: make
BuildRequires: iproute2-devel
BuildRequires: /proc
BuildRequires: git
BuildRequires: bsdcat

ExcludeArch: i586

%description
Calico is an open source networking and network security solution for containers,
virtual machines, and native host-based workloads. It provides network policy
enforcement, IP assignment, and routing for Kubernetes and other orchestrators.

%package kube-controllers
Summary: Calico kube-controllers
Group: System/Configuration/Networking

%description kube-controllers
Calico kube-controllers.

%package ctl
Summary: Tool to manage calico network parameters
Group: System/Configuration/Networking

%description ctl
Tool to manage calico network parameters.

%package cni
Summary: Calico CNI plugin
Group: System/Configuration/Networking
Requires: iproute2

%description cni
Calico CNI plugin.

%prep
%setup -a1

%build
export GOPATH="%_libexecdir/golang"
export CGO_ENABLED=0
export DATE=$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)
export HASH_COMMIT=$(bsdcat "%SOURCE0" | git get-tar-commit-id)
export CALICO_LDFLAGS="-s -w \
-X github.com/projectcalico/calico/pkg/buildinfo.Version=v%version \
-X github.com/projectcalico/calico/pkg/buildinfo.BuildDate=$DATE \
-X github.com/projectcalico/calico/pkg/buildinfo.GitRevision=$HASH_COMMIT"

%global golang_verbose 1
mkdir -p bin

%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" -o bin/calico-node ./node/cmd/calico-node
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" -o bin/calico-ipam ./node/cmd/calico-ipam
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" -o bin/mountns ./node/cmd/mountns
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" -o bin/calicoctl ./calicoctl/calicoctl
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" -o bin/calico-typha ./typha/cmd/calico-typha
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" -o bin/csidriver ./pod2daemon/csidriver
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" -o bin/flexvol ./pod2daemon/flexvol
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" -o bin/calico-kube-controllers ./kube-controllers/cmd/kube-controllers
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" -o bin/calico-wrapper ./kube-controllers/cmd/wrapper
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" -o bin/calico-check-status ./kube-controllers/cmd/check-status
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" -o bin/calico-apiserver ./apiserver/cmd/apiserver
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" -o bin/calico ./cni-plugin/cmd/calico
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" -o bin/calico-cni-install ./cni-plugin/cmd/install

%install
install -D -m 755 bin/calicoctl %buildroot%_bindir/calicoctl
install -D -m 755 bin/calico-typha %buildroot%_bindir/calico-typha
install -D -m 755 bin/calico-node %buildroot%_bindir/calico-node
install -D -m 755 bin/calico-ipam %buildroot%_bindir/calico-ipam
install -D -m 755 bin/mountns %buildroot%_bindir/calico-mountns
install -D -m 755 bin/csidriver %buildroot%_bindir/calico-csidriver
install -D -m 755 bin/flexvol %buildroot%_bindir/flexvol
install -D -m 755 bin/calico-kube-controllers %buildroot%_bindir/calico-kube-controllers
install -D -m 755 bin/calico-wrapper %buildroot%_bindir/calico-wrapper
install -D -m 755 bin/calico-check-status %buildroot%_bindir/calico-check-status
install -D -m 755 bin/calico-apiserver %buildroot%_bindir/calico-apiserver
install -D -m 755 bin/calico %buildroot%_bindir/calico
install -D -m 755 bin/calico-cni-install %buildroot%_bindir/calico-cni-install

install -d %buildroot%_sbindir
install -m 755 ./node/filesystem/sbin/* %buildroot%_sbindir/

install -d %buildroot%_sysconfdir
cp -r ./node/filesystem/etc/* %buildroot%_sysconfdir/

# Remove legacy and unused files
rm -f %buildroot%_sysconfdir/rc.local
rm -f %buildroot%_sysconfdir/nsswitch.conf

# Install confd configs
mkdir -p %buildroot%_sysconfdir/%name/confd/conf.d
cp -r ./confd/etc/calico/confd/conf.d/bird* %buildroot%_sysconfdir/%name/confd/conf.d/
mkdir -p %buildroot%_sysconfdir/%name/confd/templates
cp -r ./confd/etc/calico/confd/templates/bird* %buildroot%_sysconfdir/%name/confd/templates/

%files
%_bindir/calico-typha
%_bindir/calico-node
%_bindir/calico-mountns
%_bindir/calico-csidriver
%_bindir/flexvol
%_bindir/calico-apiserver
%_sbindir/restart-calico-confd
%_sbindir/start_runit
%_sbindir/versions
%config(noreplace) %_sysconfdir/%name
%_sysconfdir/service
%doc LICENSE.md README.md

%files kube-controllers
%_bindir/calico-kube-controllers
%_bindir/calico-wrapper
%_bindir/calico-check-status

%files ctl
%_bindir/calicoctl
%doc LICENSE.md README.md

%files cni
%_bindir/calico
%_bindir/calico-cni-install
%_bindir/calico-ipam
%doc LICENSE.md README.md

%changelog
* Fri Aug 07 2026 Ivan A. Melnikov <iv@altlinux.org> 3.32.1-alt2
- NMU: Fix building on riscv64.

* Tue Jul 21 2026 Timofei Fedotov <sovtouch@altlinux.org> 3.32.1-alt1
- Packaging fixes for ALT Linux RPM build.
- Updated to 3.32.1.

* Tue May 5 2026 Timofei Fedotov <sovtouch@altlinux.org> 3.32.0-alt1
- Updated to 3.32.0.

* Tue Apr 21 2026 Timofei Fedotov <sovtouch@altlinux.org> 3.31.5-alt1
- Updated to 3.31.5.

* Tue Feb 10 2026 Timofei Fedotov <sovtouch@altlinux.org> 3.31.3-alt1
- Updated to 3.31.3 for ALT Sisyphus.
- Fixed errors with version mismatch (Closes: #56531).

* Wed Nov 26 2025 Timofei Fedotov <sovtouch@altlinux.org> 3.31.2-alt1
- Updated to 3.31.2 for ALT Sisyphus.
- Fixed errors with version mismatch (Closes: #56531).

* Thu Jul 22 2025 Timofei Fedotov <sovtouch@altlinux.org> 3.30.2-alt1
- Initial build for ALT Sisyphus.

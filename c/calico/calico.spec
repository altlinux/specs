%define _unpackaged_files_terminate_build 1

%ifarch riscv64
# On riscv64, pie buildmode requires cgo, which is disabled in this package
%define golang_buildmode_pie %nil
%endif

Name: calico
Version: 3.33.0
Release: alt1

Summary: Cloud native networking and network security
License: Apache-2.0 AND GPL-2.0-or-later
Group: System/Configuration/Networking
Url: https://projectcalico.org
Vcs: https://github.com/projectcalico/calico

Source0: %name-%version.tar
Source1: vendor.tar

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
Requires: %name = %EVR

%description kube-controllers
Calico kube-controllers.

%package ctl
Summary: Tool to manage Calico network parameters
Group: System/Configuration/Networking

%description ctl
Tool to manage Calico network parameters.

%package cni
Summary: Calico CNI plugin
Group: System/Configuration/Networking
Requires: %name = %EVR
Requires: iproute2

%description cni
Calico CNI plugin.

%prep
%setup -a1

%build
# Use a private GOPATH; /usr/lib/golang is GOROOT on ALT Linux.
export GOPATH="$PWD/.gopath"
export CGO_ENABLED=0
export DATE=$(date -d "@$SOURCE_DATE_EPOCH" -u --rfc-3339=d)
export HASH_COMMIT=$(bsdcat "%SOURCE0" | git get-tar-commit-id)
export CALICO_LDFLAGS="-s -w \
-X github.com/projectcalico/calico/pkg/buildinfo.Version=v%version \
-X github.com/projectcalico/calico/pkg/buildinfo.BuildDate=$DATE \
-X github.com/projectcalico/calico/pkg/buildinfo.GitRevision=$HASH_COMMIT"

%global golang_verbose 1
mkdir -p bin

# Calico 3.33.0 uses one executable for Node, Typha, controllers, API server,
# CSI, FlexVolume, and CNI. Its main package is cmd/calico.
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" \
    -o bin/calico ./cmd/calico

# calicoctl remains available as a standalone executable.
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" \
    -o bin/calicoctl ./calicoctl/calicoctl/calicoctl.go

# The legacy status checker is still a separate executable in this release.
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" \
    -o bin/calico-check-status ./kube-controllers/cmd/check-status

# mountns is explicitly gated on the cgo build tag.
export CGO_ENABLED=1
%gobuild -mod=vendor -ldflags "$CALICO_LDFLAGS" \
    -o bin/mountns ./node/cmd/mountns

%install
install -Dm755 bin/calico %buildroot%_bindir/calico
install -Dm755 bin/calicoctl %buildroot%_bindir/calicoctl
install -Dm755 bin/calico-check-status %buildroot%_bindir/calico-check-status
install -Dm755 bin/mountns %buildroot%_bindir/calico-mountns

# The combined executable dispatches calico-ipam by argv[0].
ln -s calico %buildroot%_bindir/calico-ipam

# Retain familiar component executable names as compatibility entry points.
make_calico_wrapper() {
    name="$1"
    component="$2"
    printf '#!/bin/sh\nexec %%s component %%s "$@"\n' \
        '%_bindir/calico' "$component" > "%buildroot%_bindir/$name"
    chmod 0755 "%buildroot%_bindir/$name"
}
make_calico_wrapper calico-typha typha
make_calico_wrapper calico-kube-controllers kube-controllers
make_calico_wrapper calico-apiserver apiserver
make_calico_wrapper calico-csidriver csi
make_calico_wrapper flexvol flexvol

printf '#!/bin/sh\nexec %%s component cni install "$@"\n' \
    '%_bindir/calico' > %buildroot%_bindir/calico-cni-install
chmod 0755 %buildroot%_bindir/calico-cni-install

# The node filesystem contains runit services that call 'calico component'.
install -d %buildroot%_sbindir
install -m755 ./node/filesystem/sbin/* %buildroot%_sbindir/

install -d %buildroot%_sysconfdir
cp -r ./node/filesystem/etc/* %buildroot%_sysconfdir/

# Do not install /etc/rc.local: keep Calico's node startup private and
# make start_runit execute it explicitly with /bin/sh (the upstream file
# does not have a shebang).
install -Dm644 ./node/filesystem/etc/rc.local \
    %buildroot%_libexecdir/calico/node-startup.sh
sed -i 's|/etc/rc.local|/bin/sh %_libexecdir/calico/node-startup.sh|' \
    %buildroot%_sbindir/start_runit
rm -f %buildroot%_sysconfdir/rc.local
rm -f %buildroot%_sysconfdir/nsswitch.conf

# Install confd configs.
install -d %buildroot%_sysconfdir/%name/confd/conf.d
cp -r ./confd/etc/calico/confd/conf.d/bird* \
    %buildroot%_sysconfdir/%name/confd/conf.d/
install -d %buildroot%_sysconfdir/%name/confd/templates
cp -r ./confd/etc/calico/confd/templates/bird* \
    %buildroot%_sysconfdir/%name/confd/templates/

%files
%_bindir/calico
%_bindir/calico-typha
%_bindir/calico-mountns
%_bindir/calico-csidriver
%_bindir/flexvol
%_bindir/calico-apiserver
%_sbindir/restart-calico-confd
%_sbindir/start_runit
%_sbindir/versions
%_libexecdir/calico/node-startup.sh
%config(noreplace) %_sysconfdir/%name
%_sysconfdir/service
%doc LICENSE.md README.md

%files kube-controllers
%_bindir/calico-kube-controllers
%_bindir/calico-check-status

%files ctl
%_bindir/calicoctl
%doc LICENSE.md README.md

%files cni
%_bindir/calico-cni-install
%_bindir/calico-ipam
%doc LICENSE.md README.md

%changelog
* Tue Nov 10 2026 Timofei Fedotov <sovtouch@altlinux.org> 3.33.0-alt1
- Updated to 3.33.0.

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

%define _unpackaged_files_terminate_build 1

Name: calico
Version: 3.31.5
Release: alt1
Summary: Cloud native networking and network security
License: Apache-2.0
Group: System/Configuration/Networking
Url: https://docs.tigera.io
Vcs: https://github.com/projectcalico/calico

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: libpcap-devel
BuildRequires: libbpf-devel
BuildRequires: elfutils-devel
BuildRequires: zlib-devel
BuildRequires: golang
BuildRequires: /proc
BuildRequires: git
BuildRequires: bsdcat

Requires: iproute2
Requires: iptables
Requires: kmod
Requires: runit

ExcludeArch: i586

%description
Calico is the main Calico CNI plugin binary used to configure container
networking on Kubernetes nodes. It is invoked by the kubelet and
integrates container network namespaces with Calico's networking
fabric. This binary handles IP assignment,network policy enforcement,
and virtual interfaces setup for pods.

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

%description cni
Calico CNI plugin.

%prep
%setup -a1

%build
export GOPATH="%_libexecdir/golang"
export CGO_CFLAGS="-I%_includedir/bpf -I/usr/include"
export CGO_LDFLAGS="-L/%_libdir -lpcap -lelf -lz -lbpf"
export CGO_ENABLED=0
export DATE=$(date -u '+%%Y-%%m-%%d')
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

mkdir -p %buildroot/%_sbindir
mkdir -p %buildroot/%_sysconfdir
install -D -m 755 ./node/filesystem/sbin/* %buildroot/%_sbindir/
cp -r ./node/filesystem/etc/* %buildroot/%_sysconfdir/
mv %buildroot/%_sysconfdir/nsswitch.conf %buildroot/%_sysconfdir/calico-nsswitch.conf

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
%_sysconfdir/calico/
%_sysconfdir/service/
%_sysconfdir/calico-nsswitch.conf
%_sysconfdir/rc.local
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

%define _unpackaged_files_terminate_build 1
%define import_path github.com/projectcalico/calico

Name: calico
Version: 3.31.2
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
BuildRequires: make
BuildRequires: /proc

Requires: iproute2
Requires: iptables
Requires: kmod
Requires: runit

ExcludeArch: i586

%description
Calico is the main Calico CNI plugin binary used to configure container networking
on Kubernetes nodes. It is invoked by the kubelet and integrates container network
namespaces with Calico's networking fabric. This binary handles IP assignment,
network policy enforcement, and virtual interfaces setup for pods.

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
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_CFLAGS="-I%_includedir/bpf -I/usr/include"
export CGO_LDFLAGS="-L/%_libdir -lpcap -lelf -lz -lbpf"
export CGO_ENABLED=0

%global golang_verbose 1

%golang_prepare
%golang_build $BUILDDIR/src/%import_path/node/cmd/calico-node
%golang_build $BUILDDIR/src/%import_path/node/cmd/calico-ipam
%golang_build $BUILDDIR/src/%import_path/node/cmd/mountns
%golang_build $BUILDDIR/src/%import_path/calicoctl/calicoctl
%golang_build $BUILDDIR/src/%import_path/typha/cmd/calico-typha
%golang_build $BUILDDIR/src/%import_path/pod2daemon/csidriver
%golang_build $BUILDDIR/src/%import_path/pod2daemon/flexvol
%golang_build $BUILDDIR/src/%import_path/kube-controllers/cmd/kube-controllers
%golang_build $BUILDDIR/src/%import_path/kube-controllers/cmd/wrapper
%golang_build $BUILDDIR/src/%import_path/kube-controllers/cmd/check-status
%golang_build $BUILDDIR/src/%import_path/apiserver/cmd/apiserver
%golang_build $BUILDDIR/src/%import_path/cni-plugin/cmd/calico
%golang_build $BUILDDIR/src/%import_path/cni-plugin/cmd/install

%install
export BUILDDIR="$PWD/.build"
install -D -m 755 $BUILDDIR/bin/calicoctl %buildroot%_bindir/calicoctl
install -D -m 755 $BUILDDIR/bin/calico-typha %buildroot%_bindir/calico-typha
install -D -m 755 $BUILDDIR/bin/calico-node %buildroot%_bindir/calico-node
install -D -m 755 $BUILDDIR/bin/calico-ipam %buildroot%_bindir/calico-ipam
install -D -m 755 $BUILDDIR/bin/mountns %buildroot%_bindir/calico-mountns
install -D -m 755 $BUILDDIR/bin/csidriver %buildroot%_bindir/calico-csidriver
install -D -m 755 $BUILDDIR/bin/flexvol %buildroot%_bindir/flexvol
install -D -m 755 $BUILDDIR/bin/kube-controllers %buildroot%_bindir/calico-kube-controllers
install -D -m 755 $BUILDDIR/bin/wrapper %buildroot%_bindir/calico-wrapper
install -D -m 755 $BUILDDIR/bin/check-status %buildroot%_bindir/calico-check-status
install -D -m 755 $BUILDDIR/bin/apiserver %buildroot%_bindir/calico-apiserver
install -D -m 755 $BUILDDIR/bin/calico %buildroot%_bindir/calico
install -D -m 755 $BUILDDIR/bin/install %buildroot%_bindir/calico-cni-install

mkdir -p %buildroot/%_sbindir
mkdir -p %buildroot/%_sysconfdir
install -D -m 755 $BUILDDIR/src/%import_path/node/filesystem/sbin/* %buildroot/%_sbindir/
cp -r $BUILDDIR/src/%import_path/node/filesystem/etc/* %buildroot/%_sysconfdir/
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
* Wed Nov 26 2025 Timofei Fedotov <sovtouch@altlinux.org> 3.31.2-alt1
- Updated to 3.31.2 for ALT Sisyphus.
- Fixed errors with version mismatch (Closes: #56531).

* Thu Jul 22 2025 Timofei Fedotov <sovtouch@altlinux.org> 3.30.2-alt1
- Initial build for ALT Sisyphus.

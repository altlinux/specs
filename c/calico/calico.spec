%define _unpackaged_files_terminate_build 1
%define import_path github.com/projectcalico/calico

Name: calico
Version: 3.30.2
Release: alt1
Summary: Cloud native networking and network security
License: Apache-2.0
Group: System/Configuration/Networking
Url: https://docs.tigera.io
Vcs: https://github.com/projectcalico/calico

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre):  rpm-build-golang
BuildRequires: libpcap-devel
BuildRequires: libbpf-devel
BuildRequires: elfutils-devel
BuildRequires: zlib-devel

ExcludeArch: i586

%description
Calico is the main Calico CNI plugin binary used to configure container networking
on Kubernetes nodes. It is invoked by the kubelet and integrates container network
namespaces with Calico's networking fabric. This binary handles IP assignment,
network policy enforcement, and virtual interfaces setup for pods.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_CFLAGS="-I%_includedir/bpf -I/usr/include"
export CGO_LDFLAGS="-L/%_libdir -lpcap -lelf -lz -lbpf"

%golang_prepare
%golang_build $BUILDDIR/src/%import_path/node/cmd/calico-node
%golang_build $BUILDDIR/src/%import_path/calicoctl/calicoctl
%golang_build $BUILDDIR/src/%import_path/typha/cmd/calico-typha
%golang_build $BUILDDIR/src/%import_path/pod2daemon/csidriver
%golang_build $BUILDDIR/src/%import_path/pod2daemon/flexvol
%golang_build $BUILDDIR/src/%import_path/kube-controllers/cmd/kube-controllers
%golang_build $BUILDDIR/src/%import_path/apiserver/cmd/apiserver

%install
export BUILDDIR="$PWD/.build"
install -D -m 755 $BUILDDIR/bin/calicoctl %buildroot%_bindir/calicoctl
install -D -m 755 $BUILDDIR/bin/calico-typha %buildroot%_bindir/calico-typha
install -D -m 755 $BUILDDIR/bin/calico-node %buildroot%_bindir/calico-node
install -D -m 755 $BUILDDIR/bin/csidriver %buildroot%_bindir/csidriver
install -D -m 755 $BUILDDIR/bin/flexvol %buildroot%_bindir/flexvol
install -D -m 755 $BUILDDIR/bin/kube-controllers %buildroot%_bindir/kube-controllers
install -D -m 755 $BUILDDIR/bin/apiserver %buildroot%_bindir/apiserver

%files
%_bindir/calicoctl
%_bindir/calico-typha
%_bindir/calico-node
%_bindir/csidriver
%_bindir/flexvol
%_bindir/kube-controllers
%_bindir/apiserver
%doc LICENSE.md README.md

%changelog
* Thu Jul 22 2025 Timofei Fedotov <sovtouch@altlinux.org> 3.30.2-alt1
- Initial build for ALT Sisyphus.

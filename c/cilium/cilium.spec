%global import_path github.com/cilium/cilium
%global _unpackaged_files_terminate_build 1

%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch sisyphus
%endif

Name:    cilium
Version: 1.19.6
Release: alt1

Summary: Cloud native networking, security and observability based on eBPF
License: Apache-2.0
Group:   System/Configuration/Networking
Url:     https://github.com/cilium/cilium

ExclusiveArch: x86_64 aarch64 ppc64le loongarch64
Source: %name-%version.tar

#add skip require, it's present within the project
%add_python3_req_skip pkt_defs

BuildRequires: rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: rpm-build-python3
BuildRequires: golang >= 1.25
BuildRequires: /proc
BuildRequires: buf, protobuf-go, gcc, binutils, glibc-devel, coreutils

Requires: ipset, iproute2, iptables, libipset-devel, net-tools
Requires: conntrack-tools, cni-plugins
Requires: bpftool, libbpf
Requires: mount, delve, jq, kmod
%if "%altbranch" == "sisyphus" || "%altbranch" == "p11"
Requires: clang21.1
%else
Requires: clang20.1
%endif
Requires: ca-certificates

%description
Cilium is a networking, security, and observability platform for
containerized and cloud-native environments, built on eBPF - Linux
kernel technology that runs sandboxed programs in the kernel to inspect
and control traffic with very low overhead. It connects and load-balances
workloads at high performance and can operate as a CNI plugin for
container orchestrators such as Kubernetes or standalone.

Cilium network policy provides identity-aware enforcement across L3-L7.
Typical container firewalls filter traffic by IP and port, requiring
updates on every node whenever a container starts. Cilium instead
assigns a shared identity to workloads with the same security policy,
so policy enforcement no longer depends on IP addresses and can be
applied up to the application layer (L7), e.g. HTTP methods, paths,
or gRPC calls.

Cilium is used mainly by platform and infrastructure engineers who run
Kubernetes clusters and need a fast, secure, and observable network layer
for their workloads.

%package 	operator
Summary:        Operator component for cilium
Group:		System/Configuration/Networking

%description	operator
%summary

%package        hubble-relay
Summary:        Hubble-relay component for cilium
Group:          System/Configuration/Networking
Requires: 	ca-certificates, gops

%description    hubble-relay
%summary

%package        clustermesh-apiserver
Summary:        Clustermesh-apiserver component for cilium
Group:          System/Configuration/Networking
Requires:       gops

%description    clustermesh-apiserver
%summary

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export GOFLAGS="-mod=vendor -buildmode=pie"
export GOBIN="$BUILDDIR/bin"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X github.com/cilium/cilium/pkg/version.ciliumVersion=%version"
export CGO_ENABLED=0

%golang_prepare
# cilium
SUBDIRS_CILIUM_CONTAINER="cilium-dbg \
	daemon \
	cilium-health \
	cilium-health/responder \
	bugtool \
	hubble \
	tools/mount \
	tools/sysctlfix \
	plugins/cilium-cni"

for sub in $SUBDIRS_CILIUM_CONTAINER
do
   %golang_build $sub
done

# operator
TAGS="ipam_provider_operator" %golang_build operator

# hubble-relay
%golang_build hubble-relay

# clustermesh-apiserver 
%golang_build clustermesh-apiserver

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

# cilium
mkdir -p %buildroot%_bindir
install -p -m 0755 $BUILDDIR/bin/cilium-dbg %buildroot%_bindir/cilium-dbg
install -p -m 0755 $BUILDDIR/bin/daemon %buildroot%_bindir/%name-agent
install -p -m 0755 $BUILDDIR/bin/cilium-health %buildroot%_bindir/cilium-health
install -p -m 0755 $BUILDDIR/bin/responder %buildroot%_bindir/cilium-health-responder
install -p -m 0755 $BUILDDIR/bin/bugtool %buildroot%_bindir/%name-bugtool
install -p -m 0755 $BUILDDIR/bin/hubble %buildroot%_bindir/%name-hubble
install -p -m 0755 $BUILDDIR/bin/mount %buildroot%_bindir/%name-mount
install -p -m 0755 $BUILDDIR/bin/sysctlfix %buildroot%_bindir/%name-sysctlfix
install -p -m 0755 $BUILDDIR/bin/cilium-cni %buildroot%_bindir/cilium-cni

mkdir -p %buildroot%_localstatedir/%name/bpf
mkdir -p %buildroot%_localstatedir/%name/scripts
cp -r $BUILDDIR/src/%import_path/bpf/* %buildroot%_localstatedir/%name/bpf/
install -p -m 0644 $BUILDDIR/src/%import_path/plugins/cilium-cni/install-plugin.sh %buildroot%_localstatedir/%name/scripts/
install -p -m 0644 $BUILDDIR/src/%import_path/plugins/cilium-cni/cni-uninstall.sh %buildroot%_localstatedir/%name/scripts/
install -p -m 0644 $BUILDDIR/src/%import_path/images/cilium/init-container.sh %buildroot%_localstatedir/%name/scripts/

# operator
install -p -m 0755 $BUILDDIR/bin/operator %buildroot%_bindir/%name-operator

# hubble-relay
install -p -m 0755 $BUILDDIR/bin/hubble-relay %buildroot%_bindir/%name-hubble-relay

# clustermesh-apiserver
install -p -m 0755 $BUILDDIR/bin/clustermesh-apiserver %buildroot%_bindir/%name-clustermesh-apiserver
cp $BUILDDIR/src/%import_path/clustermesh-apiserver/etcd-config.yaml %buildroot%_localstatedir/%name/

%files
%doc *.md
%_bindir/cilium-dbg
%_bindir/%name-agent
%_bindir/cilium-health*
%_bindir/%name-bugtool
%_bindir/%name-hubble
%_bindir/%name-mount
%_bindir/%name-sysctlfix
%_bindir/cilium-cni
%dir %_localstatedir/%name/bpf
%dir %_localstatedir/%name/scripts
%_localstatedir/%name/bpf/*
%_localstatedir/%name/scripts/*

%files operator
%_bindir/%name-operator

%files hubble-relay
%_bindir/%name-hubble-relay

%files clustermesh-apiserver
%_bindir/%name-clustermesh-apiserver
%dir %_localstatedir/%name
%_localstatedir/%name/etcd-config.yaml

%changelog
* Mon Aug 03 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.19.6-alt1
- 1.19.3 -> 1.19.6

* Tue Jul 14 2026 Aleksandr Gamzin <gamzin@altlinux.org> 1.19.3-alt3
- Require compatible clang version for BPF alignchecker
- Transition from dynamic to static linking.

* Wed May 20 2026 Ivan A. Melnikov <iv@altlinux.org> 1.19.3-alt2
- NMU: Build on loongarch64.

* Thu Apr 23 2026 Nadezhda Fedorova <fedor@altlinux.org> 1.19.3-alt1
- 1.18.2 -> 1.19.3

* Fri Jan 23 2026 Alexander Stepchenko <geochip@altlinux.org> 1.18.2-alt2
- Build using latest available gcc instead of gcc14.

* Tue Oct 21 2025 Nadezhda Fedorova <fedor@altlinux.org> 1.18.2-alt1
- Initial build for ALTLinux.

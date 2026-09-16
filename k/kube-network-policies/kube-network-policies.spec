%define _unpackaged_files_terminate_build 1

Name: kube-network-policies
Version: 1.1.1
Release: alt1
Summary: Kubernetes network policies reference implementation
License: Apache-2.0
Group: System/Configuration/Networking
URL: https://kube-network-policies.sigs.k8s.io
VCS: https://github.com/kubernetes-sigs/kube-network-policies
ExclusiveArch: %go_arches
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.26

%description
A high-performance controller that enforces standard Kubernetes Network
Policies, Admin Network Policies (ANP), and Baseline Admin Network Policies
(BANP) using NFQUEUE and packet interception in userspace.

This is the default flavor. It runs an in-cluster agent on every node that
watches the Kubernetes API for standard namespace-scoped NetworkPolicy
objects, Pods, and Namespaces.

%package npa-v1alpha1
Summary: kube-network-policies with AdminNetworkPolicy v1alpha1 support
Group: System/Configuration/Networking

%description npa-v1alpha1
Extends the standard agent to add support for the AdminNetworkPolicy and
BaselineAdminNetworkPolicy APIs of the network-policy-api v1alpha1 spec.

%package npa-v1alpha2
Summary: kube-network-policies with ClusterNetworkPolicy v1alpha2 support
Group: System/Configuration/Networking

%description npa-v1alpha2
Extends the standard agent to add support for the newer Kubernetes
ClusterNetworkPolicy APIs (v1alpha2 spec). It evaluates Admin Network
Policies and Baseline Admin Network Policies using a userspace pipeline.
It also runs a built-in DNS/Domain cache to resolve egress domain-name
rules. It intercepts all traffic, because baseline policies can apply
globally across the cluster.

%package iptracker
Summary: kube-network-policies with the iptracker plugin
Group: System/Configuration/Networking

%description iptracker
Optimized for large-scale clusters. Instead of having every node run heavy
API informers for all pods, namespaces, and nodes, it connects over gRPC to
a centralized helper daemon (kube-ip-tracker) to retrieve IP-to-pod
mappings. Keeps a very low memory footprint per node.

%package -n kube-ip-tracker
Summary: Cluster-wide pod IP address tracker
Group: System/Configuration/Networking

%description -n kube-ip-tracker
A standalone control-plane helper daemon that runs centrally in the
cluster. It watches pods, namespaces, and nodes, aggregates their labels,
and runs an embedded etcd store to serve IP-to-PodInfo mappings to the node
agents running in iptracker mode.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
%ifarch x86_64 aarch64 ppc64le loongarch64
export GOFLAGS="-buildmode=pie"
%endif

%golang_build \
    ./cmd/%name/standard \
    ./cmd/%name/npa-v1alpha1 \
    ./cmd/%name/npa-v1alpha2 \
    ./cmd/%name/iptracker

# go install names binaries after their directory, and two command
# directories are named "standard". Rename before building kube-ip-tracker.
for n in standard npa-v1alpha1 npa-v1alpha2 iptracker; do
    mv "$BUILDDIR/bin/$n" "$BUILDDIR/bin/%name-$n"
done

%golang_build ./cmd/kube-ip-tracker/standard
mv "$BUILDDIR/bin/standard" "$BUILDDIR/bin/kube-ip-tracker-standard"

%install
export BUILDDIR="$PWD/.build"

%golang_install

%files
%doc README.md docs/json-logging.md
%_bindir/%name-standard

%files npa-v1alpha1
%_bindir/%name-npa-v1alpha1

%files npa-v1alpha2
%_bindir/%name-npa-v1alpha2

%files iptracker
%_bindir/%name-iptracker

%files -n kube-ip-tracker
%_bindir/kube-ip-tracker-standard

%changelog
* Mon Sep 14 2026 Vladislav Tsarev <tyaplyapych@altlinux.org> 1.1.1-alt1
- initial build

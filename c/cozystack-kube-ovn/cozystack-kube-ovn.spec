%global _unpackaged_files_terminate_build 1
%global import_path github.com/kubeovn/kube-ovn

# git rev-parse --short v1.15.26^{commit}
%global rev_commit 1671f9740

Name:    cozystack-kube-ovn
Version: 1.15.26
Release: alt1

Summary: A Bridge between SDN and Cloud Native (Cozystack-customized)
License: Apache-2.0
Group:   System/Configuration/Networking
Url:     https://www.kube-ovn.io
Vcs:     https://github.com/kubeovn/kube-ovn

Source:  %name-%version.tar
Source1: vendor.tar
# Cozystack test for the patch below
Source2: kubevirt_migration_test.go

Patch1: fix-vmim-target-pod-retry.diff

ExcludeArch: %ix86

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.26.8

%description
Kube-OVN, a CNCF Sandbox Project, integrates OVN-based Network
Virtualization with Kubernetes. It provides enhanced support
for KubeVirt and unique Multi-Tenancy capabilities.

%prep
%setup -a 1
%patch1 -p1
# store Cozystack test
cp %SOURCE2 pkg/controller/

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH:-$(date +%%s)}" +%%Y-%%m-%%d_%%H:%%M:%%S)
export LDFLAGS="-X %import_path/versions.COMMIT=git-%rev_commit \
                -X %import_path/versions.VERSION=v%version \
                -X %import_path/versions.BUILDDATE=$BUILD_DATE"
%golang_prepare
# install-cni.sh copies the CNI binary into the host /opt/cni/bin, where the
# host runtime execs it, so like upstream it is built without PIE: a Go PIE
# needs the host dynamic loader, which Talos does not have.
GOFLAGS= %golang_build ./cmd/cni
GOFLAGS="-buildmode=pie" %golang_build \
                ./cmd \
                ./cmd/bfdd_supervisor \
                ./cmd/daemon \
                ./cmd/controller

_BBDIR="$BUILDDIR"/bin
mv "$_BBDIR"/cmd             "$_BBDIR"/kube-ovn-cmd
mv "$_BBDIR"/cni             "$_BBDIR"/kube-ovn
mv "$_BBDIR"/bfdd_supervisor "$_BBDIR"/kube-ovn-bfdd-supervisor
mv "$_BBDIR"/daemon          "$_BBDIR"/kube-ovn-daemon
mv "$_BBDIR"/controller      "$_BBDIR"/kube-ovn-controller

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
export CGO_ENABLED=0
# Cozystack test
%gotest ./pkg/controller

%files
%doc README.md LICENSE
%_bindir/kube-ovn
%_bindir/kube-ovn-*

%changelog
* Thu Oct 15 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.15.26-alt1
- Initial build for ALT.

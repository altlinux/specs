%global import_path gopkg.in/k8snetworkplumbingwg/multus-cni.v4
%define _unpackaged_files_terminate_build 1
%define cni_dir %prefix/libexec/cni

%define git_commit db30741512795c258b3ba383a571a66850e8baac

Name:       cozystack-multus-cni
Version:    4.3.0
Release:    alt1

Summary:    Multus CNI meta-plugin for multiple Kubernetes pod networks (Cozystack-customized)
License:    Apache-2.0
Group:      System/Configuration/Networking
Url:        https://github.com/k8snetworkplumbingwg/multus-cni
Vcs:        https://github.com/k8snetworkplumbingwg/multus-cni.git

Source:     %name-%version.tar
Patch1:     fix-del-without-cache.diff

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.25
BuildRequires: /proc

%description
Multus CNI is a container network interface plugin for Kubernetes that
enables attaching multiple network interfaces to pods. It acts as a
meta-plugin that calls other CNI plugins, as configured by
NetworkAttachmentDefinition custom resources.

This build carries the Cozystack patches and ships the thick plugin
(multus-daemon with the multus-shim CNI binary), the thin plugin and the
helper tools used by the Multus DaemonSet.

%prep
%setup
%patch1 -p1
# replace default cni dir path to ALT's
sed -i 's|/usr/src/multus-cni/bin|%cni_dir|g' \
	cmd/install_multus/main.go cmd/thin_entrypoint/main.go
# check replace (if changes in new release)
if grep -rq --include='*.go' '/usr/src/multus-cni' cmd pkg; then exit 1; fi

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-w \
	-X %import_path/pkg/multus.version=v%version \
	-X %import_path/pkg/multus.commit=%git_commit \
	-X %import_path/pkg/multus.gitTreeState=cozystack-patched \
	-X %import_path/pkg/multus.releaseStatus=,released"

%golang_prepare
%golang_build \
    cmd/multus \
    cmd/multus-daemon \
    cmd/multus-shim \
    cmd/install_multus \
    cmd/thin_entrypoint \
    cmd/kubeconfig_generator \
    cmd/cert-approver \
    cmd/passthru-cni

_BBDIR="$BUILDDIR"/bin
mv "$_BBDIR"/install_multus         "$_BBDIR"/multus-install
mv "$_BBDIR"/thin_entrypoint        "$_BBDIR"/multus-thin-entrypoint
mv "$_BBDIR"/kubeconfig_generator   "$_BBDIR"/multus-kubeconfig-generator
mv "$_BBDIR"/cert-approver          "$_BBDIR"/multus-cert-approver

# store CNI binaries to special directory
_CNIDIR="$BUILDDIR"/cni
mkdir -p "$_CNIDIR"
mv "$_BBDIR"/multus         "$_CNIDIR"/multus
mv "$_BBDIR"/multus-shim    "$_CNIDIR"/multus-shim
mv "$_BBDIR"/passthru-cni   "$_CNIDIR"/passthru

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
BINDIR="$BUILDDIR"/cni RPM_BINDIR=%cni_dir %golang_install

%check
export CGO_ENABLED=0
%gotest ./pkg/checkpoint ./pkg/cmdutils ./pkg/k8sclient ./pkg/logging

%files
%doc LICENSE NOTICE README.md
%_bindir/multus-daemon
%_bindir/multus-install
%_bindir/multus-thin-entrypoint
%_bindir/multus-kubeconfig-generator
%_bindir/multus-cert-approver
%cni_dir/multus
%cni_dir/multus-shim
%cni_dir/passthru

%changelog
* Thu Oct 15 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 4.3.0-alt1
- Initial build for ALT.

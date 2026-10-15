%global import_path github.com/cilium/cilium
%define _unpackaged_files_terminate_build 1

%define bname cilium-operator

Name:    cozystack-cilium-operator
Version: 1.20.2
Release: alt1

Summary: Operator component for Cilium (Cozystack-customized)
License: Apache-2.0
Group:   System/Configuration/Networking
Url:     https://github.com/cilium/cilium
Vcs:     https://github.com/cilium/cilium

ExclusiveArch: x86_64 aarch64 ppc64le loongarch64

Source: %name-%version.tar
Patch1: conflict-https-and-tls-passthrough-unless-passthrough-is-narrower.diff
Patch2: merge-https-and-tls-passthrough-sharing-a-port.diff

Conflicts: cilium-operator

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang >= 1.26
BuildRequires: /proc

%description
Cilium operator is responsible for managing duties in the cluster which
should logically be handled once for the entire cluster, rather than once
for each node in the cluster: IPAM, garbage collection of identities and
endpoints, Gateway API and Ingress translation, and others.

This build carries Cozystack patches to the Gateway API translation that
allow HTTPS and TLS passthrough listeners to share a port.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
export BUILDDIR="$PWD/.build"
export GOFLAGS="-mod=vendor"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0
export LDFLAGS="-X '%import_path/pkg/version.ciliumVersion=%version cozystack-patched $(date -u -d @$(stat -c %%Y VERSION) +%%Y-%%m-%%dT%%H:%%M:%%SZ)'"

%golang_prepare
TAGS="osusergo,ipam_provider_operator" %golang_build operator

%install
export BUILDDIR="$PWD/.build"
install -Dpm 0755 $BUILDDIR/bin/operator %buildroot%_bindir/%bname

%check
export CGO_ENABLED=0
# Cozystack test after patch
%gotest -tags "osusergo,ipam_provider_operator" \
    ./operator/pkg/gateway-api/ \
    ./operator/pkg/model/translation/

%files
%doc README.rst LICENSE
%_bindir/%bname

%changelog
* Thu Oct 15 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.20.2-alt1
- Initial build for ALT.

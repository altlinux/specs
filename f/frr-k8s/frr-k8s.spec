%global _unpackaged_files_terminate_build 1
%global import_path github.com/metallb/frr-k8s

# git rev-parse --short v0.0.26^{commit}
%global commit 91642ae

Name: frr-k8s
Version: 0.0.26
Release: alt1

Summary: A kubernetes-based FRR daemon to be used by metallb or standalone
License: Apache-2.0
Group:   Networking/Other
Url:     https://github.com/metallb/frr-k8s
Vcs:     https://github.com/metallb/frr-k8s

ExcludeArch: %ix86

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang

%description
A k8s based daemonset that exposes a subset of the FRR API in a k8s manner.

%prep
%setup -a 1

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-trimpath"
export LDFLAGS="-X %import_path/internal/version.gitCommit=$commit \
                -X %import_path/internal/version.gitBranch=v%version \
                -buildid="

%golang_prepare
%golang_build \
	./cmd/frr-k8s-controller \
	./cmd/metrics \
	./cmd/status \
	./cmd/statuscleaner

_BBDIR="$BUILDDIR"/bin
mv "$_BBDIR"/frr-k8s-controller "$_BBDIR"/%name
mv "$_BBDIR"/metrics            "$_BBDIR"/frr-metrics
mv "$_BBDIR"/status             "$_BBDIR"/frr-status

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
install -Dm 755 cmd/reloader/frr-reloader.sh %buildroot%_bindir/frr-reloader.sh

%check
# skip envtests
%gotest -v $(go list ./... | grep -Ev '^%import_path/(internal/controller|cmd/status/controller|internal/frr)$')

%files
%doc README.md LICENSE
%_bindir/%name
%_bindir/frr-metrics
%_bindir/frr-status
%_bindir/statuscleaner
%_bindir/frr-reloader.sh

%changelog
* Tue Aug 25 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.0.26-alt1
- Initial build for ALT.


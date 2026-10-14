%define prog_name helm-controller
%global import_path github.com/fluxcd/%prog_name

Name:       flux2-%prog_name
Version:    1.5.0
Release:    alt1
Summary:    Flux controller for declarative management of Helm chart releases
Group:      System/Configuration/Other
License:    Apache-2.0
Url:        https://github.com/fluxcd/helm-controller

Source0:    %name-%version.tar
Source1:    vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang >= 1.26
BuildRequires: /proc

%description
The helm-controller is a Kubernetes operator,
allowing one to declaratively manage Helm chart releases.
It is part of a composable GitOps toolkit and depends on source-controller
to acquire the Helm charts from Helm repositories.

%prep
%setup -a 1

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
export TAGS="netgo,osusergo"
LDFLAGS="-w" %golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
export CGO_ENABLED=0
# Skip tests that need envtest (kube-apiserver and etcd binaries):
# - internal/controller, internal/controller_test and internal/reconcile
#   start it in TestMain
# - TestDiff and TestApplyDiff in internal/action start it per test
%gotest -tags "netgo,osusergo" -skip "^(TestDiff|TestApplyDiff)$" \
    $(go list -tags "netgo,osusergo" ./... | grep -vE '/internal/(controller|controller_test|reconcile)$')

%files
%_bindir/%prog_name
%doc README.md CHANGELOG.md LICENSE
%doc docs/spec/v2

%changelog
* Wed Oct 14 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.5.0-alt1
- New version 1.5.0.
- Set CGO_ENABLED=0.
- Enable tests.
- Fix import_path.

* Wed Feb 18 2026 Aleksandr Gamzin <gamzin@altlinux.org> 1.4.5-alt1
- 1.4.5.

* Sat Nov 02 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.1-alt1
- Initial build.

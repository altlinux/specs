%define prog_name source-watcher
%global import_path github.com/fluxcd/%prog_name/v2

Name:       flux2-%prog_name
Version:    2.1.0
Release:    alt1
Summary:    Flux controller for source composition and decomposition
Group:      System/Configuration/Other
License:    Apache-2.0
Url:        https://github.com/fluxcd/source-watcher

Source0:    %name-%version.tar
Source1:    vendor.tar

Patch0: fix-TestBuild_GarbageCollection.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang >= 1.26
BuildRequires: /proc

%description
The source-watcher is a GitOps toolkit controller that extends
Flux with advanced source composition and decomposition patterns.

%prep
%setup -a 1
%patch0 -p1

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
# The main package lives in cmd/, so %%golang_build would name the binary "cmd"
pushd "$BUILDDIR/src/%import_path"
go build -mod=vendor -tags "netgo,osusergo" -ldflags "-w" -v -o %prog_name ./cmd
popd

%install
export BUILDDIR="$PWD/.build"
install -Dm 0755 "$BUILDDIR/src/%import_path/%prog_name" %buildroot%_bindir/%prog_name

%check
export CGO_ENABLED=0
# Skip packages that need envtest (kube-apiserver and etcd binaries)
%gotest -tags "netgo,osusergo" \
    $(go list -tags "netgo,osusergo" ./... | grep -vE '/internal/(controller|controller_test)$')

%files
%_bindir/%prog_name
%doc README.md CHANGELOG.md LICENSE
%doc docs/spec/v1beta1

%changelog
* Wed Oct 14 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 2.1.0-alt1
- New version 2.1.0.
- Set CGO_ENABLED=0.
- Enable tests.

* Fri Feb 20 2026 Aleksandr Gamzin <gamzin@altlinux.org> 2.0.3-alt1
- Initial build for Sisyphus.

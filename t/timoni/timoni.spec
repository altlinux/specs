%global import_path github.com/stefanprodan/timoni
%define _unpackaged_files_terminate_build 1

Name:    timoni
Version: 0.32.0
Release: alt1

Summary: Package manager for Kubernetes, powered by CUE and inspired by Helm
License: Apache-2.0
Group:   Development/Tools
Url:     https://timoni.sh
Vcs:     https://github.com/stefanprodan/timoni.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.26
# Test requires
BuildRequires: git

%description
%summary.

Instead of mingling Go templates with YAML like Helm, or layering YAML on top
of each-other like Kustomize, Timoni relies on cuelang's type safety,
code generation, and data validation features to offer a better experience
of creating, packaging, and delivering apps to Kubernetes.

%prep
%setup -a 1

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X main.VERSION=%version -buildid="
export GOFLAGS="-trimpath"

%golang_prepare

%golang_build ./cmd/timoni

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%check
# skip envtest (require network)
%gotest -v $(go list ./... | grep -v '^%import_path/cmd/timoni$')

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Thu Aug 20 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.32.0-alt1
- Initial build for ALT.


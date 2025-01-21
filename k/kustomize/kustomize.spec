%global commit f309dfc54a4143225dd8af693a11703cc9e7d959
%global import_path github.com/kubernetes-sigs/kustomize

Name: kustomize
Version: 5.4.2
Release: alt1
Summary: Container cluster management

Group: System/Configuration/Other
License: Apache-2.0

Url: https://github.com/kubernetes-sigs/kustomize
Source0: %name-%version.tar

Patch0: add-commit-to-GitConfig.patch

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang > 1.21
BuildRequires: /proc

%description
kustomize lets you customize raw,
template-free YAML files for multiple purposes,
leaving the original YAML untouched and usable as is.
kustomize targets kubernetes;
it understands and can patch kubernetes style API objects.
It's like make, in that what it does is declared in a file,
and it's like sed, in that it emits edited text.

%prep
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
%setup
%golang_prepare
%patch0 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
export buildDate=$(date -u +'%%Y-%%m-%%dT%%H:%%M:%%SZ')
GOWORK=off  LDFLAGS="-w \
	-X sigs.k8s.io/kustomize/api/provenance.gitCommit=%commit \
	-X sigs.k8s.io/kustomize/api/provenance.buildDate=${buildDate} \
	-X sigs.k8s.io/kustomize/api/provenance.version=v%version"\
	%golang_build kustomize

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/kustomize
%doc *.md
%doc site/content/en/docs/*

%changelog
* Sun Nov 10 2024 Alexey Kostarev <kaf@altlinux.org> 5.4.2-alt1
- Initial build.

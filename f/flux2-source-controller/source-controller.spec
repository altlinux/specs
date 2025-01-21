%define prog_name source-controller
%global import_path github.com/fluxcd/%prog_name

Name: flux2-%prog_name
Version: 1.3.0
Release: alt1
Summary: Container cluster management

Group: System/Configuration/Other
License: Apache-2.0

Url: https://github.com/fluxcd/source-controller
Source0: %name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang > 1.21
BuildRequires: /proc

%description
The source-controller is a Kubernetes operator, specialised in artifacts
acquisition from external sources such as Git, OCI,
Helm repositories and S3-compatible buckets.
The source-controller implements the source.toolkit.fluxcd.io API and
is a core component of the GitOps toolkit.

%prep
%setup

%build
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

%files
%_bindir/%prog_name
%doc *.md
%doc docs/*

%changelog
* Thu Oct 31 2024 Alexey Kostarev <kaf@altlinux.org> 1.3.0-alt1
- Initial build.

%global import_path github.com/quay/clair
Name:     clair
Version:  2.1.2
Release:  alt1

Summary:  Vulnerability Static Analysis for Containers
License:  Apache-2.0
Group:    Other
Url:      https://github.com/quay/clair

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Clair is an open source project for the static analysis of vulnerabilities in
application containers.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/clair

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md

%changelog
* Fri Feb 28 2020 Mikhail Gordeev <obirvalger@altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus

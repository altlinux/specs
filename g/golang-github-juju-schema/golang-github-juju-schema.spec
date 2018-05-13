%global import_path     github.com/juju/schema

%global commit e4f08199aa80d3194008c0bd2e14ef5edc0e6be6
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-github-juju-schema
Version: 0
Release: alt1.git%abbrev
Summary: Helpers for coercing dynamically typed data structures into known forms.
License: LGPL v.3
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
This package provides helpers for coercing dynamically typed data structures into known forms.

%package devel
Summary: Helpers for coercing dynamically typed data structures into known forms.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
This package provides helpers for coercing dynamically typed data structures into known forms.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"

%golang_prepare

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

%files devel
%doc README.md LICENSE
%go_path/src/*

%changelog
* Sun May 13 2018 Denis Pynkin <dans@altlinux.org> 0-alt1.gite4f08199
- Initial package


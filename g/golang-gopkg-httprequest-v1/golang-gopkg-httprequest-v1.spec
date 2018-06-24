%global import_path gopkg.in/httprequest.v1

#global commit 7f1609ff1f3fcf3519ed62ccaaa9e609ea287838
#global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-gopkg-httprequest-v1
Version: 1.1.1
Release: alt1
Summary: This package provides functionality for unmarshaling HTTP request parameters into a struct type.
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
Package httprequest provides functionality for unmarshaling HTTP request
parameters into a struct type.

%package devel
Summary: This package provides functionality for unmarshaling HTTP request parameters into a struct type.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
Package httprequest provides functionality for unmarshaling HTTP request
parameters into a struct type.

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
* Sun May 13 2018 Denis Pynkin <dans@altlinux.org> 1.1.1-alt1
- Initial package

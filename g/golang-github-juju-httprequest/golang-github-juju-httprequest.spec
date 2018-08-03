%global import_path     github.com/juju/httprequest

%global commit 77d36ac4b71a6095506c0617d5881846478558cb
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-github-juju-httprequest
Version: 0
Release: alt0.git%abbrev
Summary: JSON-oriented HTTP server and client helpers
License: LGPL v.3
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
Package httprequest provides functionality for unmarshaling HTTP request
parameters into a struct type.

Please note that the API is not considered stable at this point
and may be changed in a backwardly incompatible manner at any time.

%package devel
Summary: JSON-oriented HTTP server and client helpers
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
Package httprequest provides functionality for unmarshaling HTTP request
parameters into a struct type.

Please note that the API is not considered stable at this point
and may be changed in a backwardly incompatible manner at any time.

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
* Wed Jul 25 2018 Lenar Shakirov <snejok@altlinux.ru> 0-alt0.git77d36ac4
- Initial build for ALT


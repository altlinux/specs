%global import_path     gopkg.in/juju/names.v2

%global commit fd59336b4621bc2a70bf96d9e2f49954115ad19b
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-gopkg-juju-names-v2
Version: 2.0
Release: alt0.git%shortcommit
Summary: This package provides helpers for handling Juju entity names.
License: LGPL v3
Group: Development/Other
Url: https://gopkg.in/juju/names.v2
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
%summary

%package devel
Summary: This package provides helpers for handling Juju entity names.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

# Auto-detected requirements
Requires:	golang(github.com/juju/errors)
Requires:	golang(github.com/juju/utils)

%description devel
%summary

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
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 2.0-alt0.gitfd59336b
- Initial package

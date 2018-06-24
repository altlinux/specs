%global import_path     github.com/juju/go4

%global commit 40d72ab9641a2a8c36a9c46a51e28367115c8e59
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-github-juju-go4
Version: 0
Release: alt1.git%abbrev
Summary: go4.org is a collection of packages for Go programmers
License: Apache v.2
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
go4.org is a collection of packages for Go programmers

%package devel
Summary: go4.org is a collection of packages for Go programmers
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
go4.org is a collection of packages for Go programmers

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
%doc AUTHORS README.md LICENSE
%go_path/src/*

%changelog
* Wed May 09 2018 Denis Pynkin <dans@altlinux.org> 0-alt1.git40d72ab9
- Initial package


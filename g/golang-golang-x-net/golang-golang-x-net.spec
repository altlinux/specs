%global import_path golang.org/x/net

%global commit a6577fac2d73be281a500b310739095313165611
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-golang-x-net
Version: 0
Release: alt2.git%abbrev
Summary: Go supplementary network libraries
License: MIT
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
Go supplementary network libraries

%package devel
Summary: golang-golang-x-net
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
Go supplementary network libraries

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
%doc AUTHORS README LICENSE PATENTS
%go_path/src/*

%changelog
* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 0-alt2.gita6577fac
- Update

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 0-alt1.git4971afdc
- Initial package


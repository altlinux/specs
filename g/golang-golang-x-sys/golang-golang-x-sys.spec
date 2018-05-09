%global import_path golang.org/x/sys

%global commit 7db1c3b1a98089d0071c84f646ff5c96aad43682
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-golang-x-sys
Version: 0
Release: alt3.git%abbrev
Summary: Go packages for low-level interaction with the operating system
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
Go packages for low-level interaction with the operating system

%package devel
Summary: golang-golang-x-sys
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
Go packages for low-level interaction with the operating system

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
%doc AUTHORS README.md LICENSE PATENTS
%go_path/src/*

%changelog
* Wed May 09 2018 Denis Pynkin <dans@altlinux.org> 0-alt3.git7db1c3b1
- Update

* Fri Feb 02 2018 Denis Pynkin <dans@altlinux.org> 0-alt2.git8f27ce8a
- Update

* Sat Jul 29 2017 Denis Pynkin <dans@altlinux.org> 0-alt1.git0f826bdd
- Initial package


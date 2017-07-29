%global import_path golang.org/x/sys

%global commit 0f826bdd13b500be0f1d4004938ad978fcc6031e
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-golang-x-sys
Version: 0
Release: alt1.git%abbrev
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
%doc AUTHORS README LICENSE PATENTS
%go_path/src/*

%changelog
* Sat Jul 29 2017 Denis Pynkin <dans@altlinux.org> 0-alt1.git0f826bdd
- Initial package


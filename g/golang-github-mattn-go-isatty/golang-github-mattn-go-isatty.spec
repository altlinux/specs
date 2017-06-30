%global import_path github.com/mattn/go-isatty

Name: golang-github-mattn-go-isatty
Version: 0.0.2
Release: alt1
Summary: isatty for golang
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
%summary

%package devel
Summary: isatty for golang
Group: Development/Other
Requires: golang
Requires:	golang(github.com/mattn/go-isatty)
Provides: golang(%import_path) = %version-%release

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
* Fri Jun 30 2017 Denis Pynkin <dans@altlinux.org> 0.0.2-alt1
- Initial package


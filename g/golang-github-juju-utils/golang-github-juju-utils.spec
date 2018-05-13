%global import_path     github.com/juju/utils

%global commit 2000ea4ff0431598aec2b7e1d11d5d49b5384d63
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-github-juju-utils
Version: 0
Release: alt1.git%abbrev
Summary: This package provides general utility packages and functions.
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
This package provides general utility packages and functions.

%package devel
Summary: This package provides general utility packages and functions.
Group: Development/Other
Requires: golang
Requires: golang(github.com/juju/loggo)
BuildRequires: golang(github.com/juju/loggo)
Provides: golang(%import_path) = %version-%release

%description devel
This package provides general utility packages and functions.

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
* Sun May 13 2018 Denis Pynkin <dans@altlinux.org> 0-alt1.git2000ea4f
- Initial package


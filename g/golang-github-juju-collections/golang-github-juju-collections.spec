%global import_path     github.com/juju/collections

%global commit 9be91dc79b7c185fa8b08e7ceceee40562055c83
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-juju-collections
Version: 0
Release: alt0.git%shortcommit
Summary: Set and deque implementations.
License: LGPLv3
Group: Development/Other
Url: https://github.com/juju/collections
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
%summary

%package devel
Summary: Set and deque implementations.
Group: Development/Other
Requires: golang
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
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 0-alt0.git9be91dc7
- Initial package

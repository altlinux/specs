%global import_path     github.com/Rican7/retry

%global commit 272ad122d6e5ce1be757544007cf8bcd1c9c9ab0
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-Rican7-retry
Version: 0.1.0
Release: alt0.git%shortcommit
Summary: simple, stateless, functional mechanism to perform actions repetitively until successful
License: MIT
Group: Development/Other
Url: https://%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
%summary

%package devel
Summary: simple, stateless, functional mechanism to perform actions repetitively until successful
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
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 0.1.0-alt0.git272ad122
- Initial package

%global import_path     github.com/pborman/uuid

%global commit cccd189d45f7ac3368a0d127efb7f4d08ae0b655
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-github-pborman-uuid
Version: 0
Release: alt1.git%abbrev
Summary: Package `pborman/uuid` implements RFC4122.
License: BSD
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
Package `pborman/uuid` implements RFC4122.

%package devel
Summary: Package `pborman/uuid` implements RFC4122.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
Package `pborman/uuid` implements RFC4122.

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
%doc CONTRIBUTORS LICENSE
%go_path/src/*

%changelog
* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt1.gitcccd189d
- Initial package


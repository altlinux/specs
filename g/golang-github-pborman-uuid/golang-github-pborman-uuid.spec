%global import_path     github.com/pborman/uuid

%global commit 1b00554d822231195d1babd97ff4a781231955c9
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-github-pborman-uuid
Version: 0
Release: alt3.git%abbrev
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
* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 0-alt3.git1b00554d
- Update

* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 0-alt2.gitc55201b0
- Update

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt1.gitcccd189d
- Initial package


%global import_path gopkg.in/tomb.v2

%global commit d5d1b5820637886def9eef33e03a27a9f166942c
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-gopkg-tomb-v2
Version: 2.0
Release: alt3.git%abbrev
Summary: The tomb package handles clean goroutine tracking and termination.
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
The tomb package handles clean goroutine tracking and termination.

%package devel
Summary: The tomb package handles clean goroutine tracking and termination.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
The tomb package handles clean goroutine tracking and termination.

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
* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 2.0-alt3.gitd5d1b582
- Update

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 2.0-alt2.git9dde9715
- Update

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 2.0-alt1.git14b3d721
- Initial package


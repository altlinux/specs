%global import_path gopkg.in/tomb.v2

%global commit 14b3d72120e8d10ea6e6b7f87f7175734b1faab8
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-gopkg-tomb-v2
Version: 2.0
Release: alt1.git%abbrev
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
* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 2.0-alt1.git14b3d721
- Initial package


%global import_path     github.com/ryanfaerman/fsm

%global commit 3dc1bc0980272fd56d81167a48a641dab8356e29
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-ryanfaerman-fsm
Version: 2.0
Release: alt0.git%shortcommit
Summary: lightweight finite state machine for Golang.
License: MIT
Group: Development/Other
Url: https://github.com/ryanfaerman/fsm
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
FSM provides a lightweight finite state machine for Golang.
It runs allows any number of transition checks you'd like the it runs them in parallel.

%package devel
Summary: lightweight finite state machine for Golang.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
FSM provides a lightweight finite state machine for Golang.
It runs allows any number of transition checks you'd like the it runs them in parallel.

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
%doc Readme.md LICENSE
%go_path/src/*

%changelog
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 2.0-alt0.git3dc1bc09
- Initial package

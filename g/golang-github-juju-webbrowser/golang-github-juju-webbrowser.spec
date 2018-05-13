%global import_path github.com/juju/webbrowser


%global commit 54b8c57083b4afb7dc75da7f13e2967b2606a507
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-github-juju-webbrowser
Version: 0
Release: alt1.git%abbrev
Summary: Go helpers for interacting with Web browsers.
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
Go helpers for interacting with Web browsers.

%package devel
Summary: Go helpers for interacting with Web browsers.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
Go helpers for interacting with Web browsers.

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
* Sun May 13 2018 Denis Pynkin <dans@altlinux.org> 0-alt1.git54b8c570
- Initial package

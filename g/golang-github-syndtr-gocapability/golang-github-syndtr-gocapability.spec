%global import_path     github.com/syndtr/gocapability

%global commit 2c00daeb6c3b45114c80ac44119e7b8801fdd852
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-github-syndtr-gocapability
Version: 0
Release: alt2.git%abbrev
Summary: Package capability provides utilities for manipulating POSIX capabilities.
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
Package capability provides utilities for manipulating POSIX capabilities.

%package devel
Summary: Package capability provides utilities for manipulating POSIX capabilities.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release
Provides: golang(%import_path/capability) = %version-%release

%description devel
Package capability provides utilities for manipulating POSIX capabilities.

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

rm -rf -- %buildroot/%go_path/src/%import_path/capability/enumgen

%files devel
%doc LICENSE
%go_path/src/*

%changelog
* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt2.git2c00daeb
- Initial package for development only

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0-alt1.git20140517
- New snapshot

* Sat Dec 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0-alt1
- Build for ALT

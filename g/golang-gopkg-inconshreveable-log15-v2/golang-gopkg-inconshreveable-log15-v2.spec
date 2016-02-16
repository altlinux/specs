%global import_path gopkg.in/inconshreveable/log15.v2

%global commit b105bd37f74e5d9dc7b6ad7806715c7a2b83fd3f
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-gopkg-inconshreveable-log15-v2
Version: 2.0
Release: alt1.git%abbrev
Summary: Simple toolkit for best-practice logging in Go
License: Apache 2.0
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
Package log15 provides an opinionated, simple toolkit for 
best-practice logging in Go (golang) that is both human and machine readable.
It is modeled after the Go standard library's `io`(http://golang.org/pkg/io/)
and `net/http`(http://golang.org/pkg/net/http/) packages and is an alternative 
to the standard library's [`log`](http://golang.org/pkg/log/) package.

%package devel
Summary: Simple toolkit for best-practice logging in Go
Group: Development/Other
Requires: golang
Requires: golang(github.com/mattn/go-colorable)

Provides: golang(%import_path) = %version-%release
Provides: golang(%import_path/ext) = %version-%release
Provides: golang(%import_path/stack) = %version-%release
Provides: golang(%import_path/term) = %version-%release

%description devel
Package log15 provides an opinionated, simple toolkit for 
best-practice logging in Go (golang) that is both human and machine readable.
It is modeled after the Go standard library's `io`(http://golang.org/pkg/io/)
and `net/http`(http://golang.org/pkg/net/http/) packages and is an alternative 
to the standard library's [`log`](http://golang.org/pkg/log/) package.

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
* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 2.0-alt1.gitb105bd37
- Initial package


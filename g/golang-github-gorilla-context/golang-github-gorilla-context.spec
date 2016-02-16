%global import_path     github.com/gorilla/context

%global commit 1c83b3eabd45b6d76072b66b746c20815fb2872d
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-github-gorilla-context
Version: 0
Release: alt3.git%abbrev
Summary: Package context stores values shared during a request lifetime.
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
Package gorilla/context stores values shared during a request lifetime.

For example, a router can set variables extracted from the URL and later
application handlers can access those values, or it can be used to store
sessions values to be saved at the end of a request. There are several
other common uses.

%package devel
Summary: %summary
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
Package gorilla/context stores values shared during a request lifetime.

For example, a router can set variables extracted from the URL and later
application handlers can access those values, or it can be used to store
sessions values to be saved at the end of a request. There are several
other common uses.

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
* Thu Feb 25 2016 Denis Pynkin <dans@altlinux.ru> 0-alt3.git1c83b3ea
- Initial build

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0-alt2.git20140604
- New snapshot

* Wed Oct 30 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0-alt2
- Update spec

* Wed Oct 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0-alt1
- Build for ALT


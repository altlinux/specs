%global import_path     github.com/gorilla/mux

%global commit acf3be1b335c8ce30b2c8d51300984666f0ceefa
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-github-gorilla-mux
Version: 0
Release: alt5.git%abbrev
Summary: Package `gorilla/mux` implements a request router and dispatcher.
License: BSD
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools
BuildRequires: golang(github.com/gorilla/context)

%description
Package `gorilla/mux` implements a request router and dispatcher.

%package devel
Summary: Package `gorilla/mux` implements a request router and dispatcher.
Group: Development/Other
Requires: golang
Requires: golang(github.com/gorilla/context)
Provides: golang(%import_path) = %version-%release

%description devel
Package `gorilla/mux` implements a request router and dispatcher.

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
* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 0-alt5.gitacf3be1b
- Version update 

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt4.git26a6070f
- Update for lxd

* Wed Jun 11 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0-alt3
- update to commit 136d54f81f (required for docker 1.0
   https://github.com/dotcloud/docker/issues/5908)

* Wed Oct 30 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0-alt2
- Update spec

* Wed Oct 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0-alt1
- Build for ALT

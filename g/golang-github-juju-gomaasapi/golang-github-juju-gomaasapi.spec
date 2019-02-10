%global import_path     github.com/juju/gomaasapi

%global commit 8a8cec793ba70659ba95f1b9a491ba807169bfc3
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-juju-gomaasapi
Version: 0
Release: alt0.git%shortcommit
Summary: MAAS API client library for Go
License: LGPL v3
Group: Development/Other
Url: https://github.com/juju/gomaasapi
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
This library serves as a minimal client for communicating with the MAAS web
API in Go programs.

%package devel
Summary: MAAS API client library for Go
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

# Auto-detected requirements
Requires:	golang(github.com/juju/collections/set)
Requires:	golang(github.com/juju/errors)
Requires:	golang(github.com/juju/loggo)
Requires:	golang(github.com/juju/schema)
Requires:	golang(github.com/juju/version)
Requires:	golang(gopkg.in/mgo.v2/bson)

%description devel
This library serves as a minimal client for communicating with the MAAS web
API in Go programs.

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
%doc README.rst LICENSE
%go_path/src/*

%changelog
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 0-alt0.git8a8cec79
- Initial package

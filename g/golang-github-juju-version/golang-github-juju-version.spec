%global import_path     github.com/juju/version

%global commit b64dbd566305c836274f0268fa59183a52906b36
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-juju-version
Version: 0
Release: alt0.git%shortcommit
Summary: version is a go package for intelligent version comparisons.
License: LGPLv3
Group: Development/Other
Url: https://github.com/juju/version
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
%summary

%package devel
Summary: version is a go package for intelligent version comparisons.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

# Auto-detected requirements
Requires:	golang(gopkg.in/mgo.v2/bson)

%description devel
%summary

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
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 0-alt0.gitb64dbd56
- Initial package

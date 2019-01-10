%global import_path     github.com/CanonicalLtd/candidclient

%global commit 8d331dd5664bea29ab3762e226b14cfc49fbe22a
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-CanonicalLtd-candidclient
Version: 1.0.0
Release: alt0.git%shortcommit
Summary: This package provides Go client code to interact with the Candid identity server.
License: LGPLv3
Group: Development/Other
Url: https://%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
%summary

%package devel
Summary: This package provides Go client code to interact with the Candid identity server.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release
Provides: golang(gopkg.in/CanonicalLtd/candidclient.v1) = %version-%release

Requires: golang(gopkg.in/juju/names.v2)

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
mkdir -p ${RPM_BUILD_ROOT}/%go_path/src/gopkg.in/CanonicalLtd
ln -s ../../%import_path ${RPM_BUILD_ROOT}/%go_path/src/gopkg.in/CanonicalLtd/candidclient.v1

%files devel
%doc README.md LICENCE
%go_path/src/*

%changelog
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 1.0.0-alt0.git8d331dd5
- Initial package

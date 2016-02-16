%global import_path     gopkg.in/flosch/pongo2.v3
# global gopath          %_datadir/gocode

Name: golang-gopkg-flosch-pongo2-v3
Version: 3.0
Release: alt1
Summary: A Django-syntax like template-engine
License: MIT
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
A Django-syntax like template-engine

%package devel
Summary: A Django-syntax like template-engine
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
A Django-syntax like template-engine

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

rm -rf -- %buildroot/%go_path/src/%import_path/template_tests


%files devel
%doc AUTHORS README.md LICENSE
%go_path/src/*

%changelog
* Mon Feb 15 2016 Denis Pynkin <dans@altlinux.ru> 3.0-alt1
- Initial package


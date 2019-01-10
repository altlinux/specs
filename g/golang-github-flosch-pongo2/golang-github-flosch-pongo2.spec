%global import_path     github.com/flosch/pongo2

%global commit 79872a7b27692599b259dc751bed8b03581dd0de
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-flosch-pongo2
Version: 3.0
Release: alt0.git%shortcommit
Summary: pongo2 is the successor of pongo, a Django-syntax like templating-language.
License: MIT
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
Summary: pongo2 is the successor of pongo, a Django-syntax like templating-language.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

# Auto-detected requirements
Requires:	golang(github.com/juju/errors)

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
%doc AUTHORS README.md LICENSE
%go_path/src/*

%changelog
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 3.0-alt0.git79872a7b
- Initial package
